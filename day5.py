import os
print("PROGRAM STARTED")
from openai import OpenAI

api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    raise RuntimeError(
        "未检测到 DEEPSEEK_API_KEY。请先在 PowerShell 中设置环境变量。"
    )

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)
print("ABOUT TO START LOOP")
while True:
    text = input("请输入一段英文（输入 exit 退出）：").strip()

    if text.lower() == "exit":
        break

    if not text:
        print("请输入英文内容。")
        continue

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": f"""你接下来的任务：将用户本次输入的所有英文内容作为英语学习材料进行全面分析，严格按照下面模块输出，无额外无关话术：

原文展示：直接粘贴用户输入英文
中文翻译：通顺自然的标准中文译文
核心生词 & 短语：标注音标、词性、释义，重点搭配补充
重点语法 & 句式：拆解句子结构、时态、从句、特殊句型，说明用法
易错点提示：容易写错、读错、误用的地方
同义替换：可替换的单词 / 句式，适合写作口语复用
仿写例句：2 个贴合日常场景的仿写句子

补充规则：
① 如果用户输入是单句就单句分析，多段 / 多篇文本就分段处理；
② 遇到俚语、固定习语优先说明语境含义，不要直译；
③ 内容难度适配普通英语学习者，专业术语简单通俗解释；
④ 若输入混杂中英文，只提取英文部分分析，忽略中文。

英文：{text}"""
            }
        ],
    )

    print("\n=== AI 分析结果 ===")
    print(response.choices[0].message.content)
    print()