# OneBot-adapter for ChatGPT-Mirai-QQ-Bot

本项目是 [ChatGPT-Mirai-QQ-Bot](https://github.com/lss233/chatgpt-mirai-qq-bot) 的一个插件，用于将OneBot协议的消息转换为ChatGPT-Mirai-QQ-Bot的消息格式。

## 安装

```bash
pip install chatgpt-mirai-qq-bot-web-search
```

## 使用

在 chatgpt-mirai-qq-bot的web_ui中配置  
使用示例请参考 [web_search/example/roleplayWithWebSearch.yml](web_search/example/roleplayWithWebSearch.yaml)    
工作流请参考 [示例图片](web_search/example/workflow.png)

### 配置自定义搜索引擎地址

您可以在 `web_search/config.py` 中配置自定义搜索引擎地址。默认情况下，使用 Bing 作为搜索引擎。如果您希望使用其他搜索引擎，可以在 `WebSearchConfig` 类中设置 `custom_search_engine_url` 字段。例如：

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class WebSearchConfig:
    """网络搜索配置"""
    max_results: int = 3  # 最大搜索结果数
    timeout: int = 10  # 超时时间(秒)
    fetch_content: bool = True  # 是否获取详细内容
    min_sleep: float = 1.0  # 最小随机等待时间
    max_sleep: float = 3.0  # 最大随机等待时间 
    custom_search_engine_url: Optional[str] = "https://your-custom-search-engine.com/search?q="  # 自定义搜索引擎地址
```

## 开源协议

本项目基于 [ChatGPT-Mirai-QQ-Bot](https://github.com/lss233/chatgpt-mirai-qq-bot) 开发，遵循其 [开源协议](https://github.com/lss233/chatgpt-mirai-qq-bot/blob/master/LICENSE)

## 感谢

感谢 [ChatGPT-Mirai-QQ-Bot](https://github.com/lss233/chatgpt-mirai-qq-bot) 的作者 [lss233](https://github.com/lss233) 提供框架支持
