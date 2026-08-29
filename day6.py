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
                "content": f"""只输出以下格式，不要添加其他内容：

translation: [这里填写中文翻译]
level: [这里填写 CEFR 等级]

英文：
{text}
英文：{text}"""
            }
        ],
    )

    print("\n=== AI 分析结果 ===")
    answer = response.choices[0].message.content
    answer1= answer.split()
    for item in answer1:
        if item == "translation:":
                position1 = answer1.index("translation:")
                translation = answer1[position1+1]
                print("AI Translation:",translation)
        if item == "level:":
         position = answer1.index("level:")
         level = answer1[position+1]
         print("AI Level:",level)
      
    print()
