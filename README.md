# Daily-English-Quote-Collection
# 🌟 Daily English Quote Collection 

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

这是一个基于 Python 的轻量级网页爬虫项目，专门从 [Quotes to Scrape](http://quotes.toscrape.com/) 网站随机抓取富有哲理的英文格言。它非常适合作为 Python 爬虫初学者的练手项目。

## ✨ 项目功能特点

- **随机抽取**：不再只是盯着第一页，支持从全站 10 页内容中随机抽取。
- **智能解析**：使用 BeautifulSoup4 精准提取格言内容及其作者。
- **环境隔离**：建议配合 Python 虚拟环境运行，保证系统整洁。

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone [https://github.com/tuyun1175/Daily-English-Quote-Collection.git](https://github.com/tuyun1175/Daily-English-Quote-Collection.git)
cd Daily-English-Quote-Collection


### 2. 安装依赖

确保你已经安装了 requests 和 beautifulsoup4 库：

Bash
pip install requests beautifulsoup4


### 3. 运行程序

Bash
python english.py


### 🛠️ 技术栈
Requests: 负责发送网络请求，获取网页 HTML。

BeautifulSoup4: 负责解析 HTML 结构，提取核心数据。

Random: 负责实现跨页面随机选取的逻辑。

### 📝 学习笔记
这个项目是我学习 Python 爬虫的第一步，我解决了以下挑战：

环境配置：学会了如何创建和管理 Python 虚拟环境。

翻页逻辑：通过观察 URL 规律，实现了跨页面抓取。

Git 操作：掌握了从本地提交代码到 GitHub 的完整流程。

⭐ 如果这个项目对你有帮助，欢迎点个 Star！
