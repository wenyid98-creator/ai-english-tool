# AI English Tool 📚🤖

一个基于 DeepSeek API 的英语学习辅助小工具，输入一段英文，AI 会自动帮你做全方位分析：翻译、生词短语、语法拆解、易错点提示、同义替换和仿写例句，帮助你更高效地学习英语。

项目按学习进度分阶段迭代，从最基础的单次调用（`main.py`）逐步进化到循环交互（`day5.py`），再到结构化输出解析（`day6.py`）。

---

## 📁 文件说明

### 1️⃣ `main.py` —— 基础版
最初始的版本，实现核心功能：

- 用户输入一段英文
- 调用 DeepSeek API，让 AI 按固定模板输出学习分析（原文、翻译、生词短语、语法、易错点、同义替换、仿写例句）
- 只运行一次，输出结果后程序结束

适合理解整个工具最基础的调用逻辑。

### 2️⃣ `day5.py` —— 循环交互版
在 `main.py` 的基础上做了功能升级：

- 增加 `while True` 循环，支持连续输入多段英文，无需重复运行程序
- 输入 `exit` 即可退出程序
- 增加对 `DEEPSEEK_API_KEY` 环境变量缺失的检测和友好报错提示
- 对空输入做了容错处理

### 3️⃣ `day6.py` —— 结构化输出解析版
在循环交互的基础上，尝试让 AI 按固定字段格式输出，并在代码中解析结果：

- 让 AI 只输出 `translation:` 和 `level:` 两个字段（中文翻译 + CEFR 等级）
- 使用字符串处理（`split()`）从 AI 回复中提取出对应字段的值并单独打印
- 是从"整段自由文本输出"到"结构化字段提取"的一次尝试

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install openai
```

### 2. 配置 API Key

本项目使用 [DeepSeek API](https://platform.deepseek.com/)，需要先申请 API Key，然后设置为环境变量。

**Windows (PowerShell)：**
```powershell
$env:DEEPSEEK_API_KEY="你的API密钥"
```

**macOS / Linux：**
```bash
export DEEPSEEK_API_KEY="你的API密钥"
```

### 3. 运行程序

```bash
python main.py
# 或
python day5.py
# 或
python day6.py
```

---

## 💡 使用示例

```
请输入一段英文：I have been working on this project for a while.

=== AI 分析结果 ===
原文展示：I have been working on this project for a while.
中文翻译：我已经在这个项目上工作了一段时间。
核心生词 & 短语：...
重点语法 & 句式：现在完成进行时，表示动作从过去持续到现在...
...
```

---

## 🛠 技术栈

- Python 3
- [openai](https://pypi.org/project/openai/) SDK（兼容 DeepSeek API）
- DeepSeek Chat 模型

---

## 📌 后续计划

- [ ] 优化结构化输出解析，改用 JSON 格式代替字符串 split
- [ ] 增加历史记录保存功能
- [ ] 支持批量文本分析
- [ ] 制作简单的图形界面 / Web 界面

---

## 📄 License

MIT License