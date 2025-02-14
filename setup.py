from setuptools import setup, find_packages
import io
import os

version = os.environ.get('RELEASE_VERSION', '0.1.0').lstrip('v')

setup(
    name="web-search",
    version=version,
    packages=find_packages(),
    install_requires=[
        "playwright","trafilatura","lxml_html_clean",
    ],
    entry_points={
        'chatgpt_mirai.plugins': [
            'web_search = web_search:WebSearchPlugin'
        ]
    },
    author="chuanSir",
    author_email="416448943@qq.com",

    description="WebSearch adapter for lss233/chatgpt-mirai-qq-bot",
    long_description=io.open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chuanSir123/web_search",
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU Affero General Public License v3',
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/chuanSir123/web_search/issues",
        "Documentation": "https://github.com/chuanSir123/web_search/wiki",
        "Source Code": "https://github.com/chuanSir123/web_search",
    },
    python_requires=">=3.8",
)
