from typing import Dict, Any, List
import asyncio
from framework.plugin_manager.plugin import Plugin
from framework.logger import get_logger
from .config import WebSearchConfig
from .web_searcher import WebSearcher
from dataclasses import dataclass
from framework.workflow.core.block import BlockRegistry
from .blocks import WebSearchBlock
from .blocks import AppendSystemPromptBlock
from framework.ioc.inject import Inject

logger = get_logger("WebSearch")

class WebSearchPlugin(Plugin):
    def __init__(self, block_registry: BlockRegistry = Inject()):
        super().__init__()
        self.web_search_config = WebSearchConfig()
        self.searcher = None
        self.block_registry = block_registry

    def on_load(self):
        logger.info("WebSearchPlugin loading")

        # 注册Block
        try:
            self.block_registry.register("web_search", "search", WebSearchBlock)
        except Exception as e:
            logger.warning(f"WebSearchPlugin failed: {e}")
        try:
            self.block_registry.register("append_systemPrompt", "internal", AppendSystemPromptBlock)
        except Exception as e:
            logger.warning(f"WebSearchPlugin failed: {e}")

        @dataclass
        class WebSearchEvent:
            """Web搜索事件"""
            query: str

        async def handle_web_search(event: WebSearchEvent):
            """处理web搜索事件"""
            if not self.searcher:
                await self._initialize_searcher()
            return await self.searcher.search(
                event.query,
                max_results=self.web_search_config.max_results,
                timeout=self.web_search_config.timeout,
                fetch_content=self.web_search_config.fetch_content
            )
        try:
            self.event_bus.register(WebSearchEvent, handle_web_search)
        except Exception as e:
            logger.warning(f"WebSearchPlugin failed: {e}")

    def on_start(self):
        logger.info("WebSearchPlugin started")

    def on_stop(self):
        if self.searcher:
            asyncio.create_task(self.searcher.close())

        logger.info("WebSearchPlugin stopped")

    def get_actions(self) -> List[str]:
        return ["web_search"]

    def get_action_params(self, action: str) -> Dict[str, Any]:
        if action == "web_search":
            return {
                "query": "搜索关键词"
            }
        raise ValueError(f"Unknown action: {action}")

    async def execute(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if action == "web_search":
            return await self._do_search(params)
        raise ValueError(f"Unknown action: {action}")

    async def _do_search(self, params: Dict[str, Any]) -> Dict[str, Any]:
        query = params.get("query")
        if not query:
            return {
                "success": False,
                "message": "搜索关键词为空"
            }

        try:
            await self._initialize_searcher()
            results = await self.searcher.search(
                query,
                max_results=self.web_search_config.max_results,
                timeout=self.web_search_config.timeout,
                fetch_content=self.web_search_config.fetch_content
            )
            return {
                "success": True,
                "results": results
            }
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return {
                "success": False,
                "message": f"搜索失败: {str(e)}"
            }

    async def _initialize_searcher(self):
        """初始化搜索器"""
        if self.searcher is None:
            self.searcher = await WebSearcher.create()

