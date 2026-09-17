import os

import json

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

PROMPT_HEAD = """你是一个英语学习助手，专注于帮助中国用户学习地道、实用的英语（目标场景：出国生活）。用户会输入一段英文，你需要严格按照以下格式输出，只输出合法 JSON，不要输出 Markdown，不要输出 ```，不要输出任何解释。

JSON 必须包含以下字段，每个字段的数据结构必须严格固定如下（字段名和嵌套字段名一个字都不能改）：

{
  "level": "B1",
  "origin": "用户输入的英文",
  "translation": "中文翻译",
  "vocabulary": [
    {
      "word": "financially free",
      "phonetic": "/faɪˈnænʃəli friː/",
      "pos": "adj. phrase",
      "meaning": "财务自由的"
    }
  ],
  "mistakes": [
    {
      "wrong": "你很可能会说成的错误说法",
      "right": "地道正确的说法",
      "tip": "简短说明错误原因或记忆要点"
    }
  ],
  "alternatives": [
    {
      "original": "I want to become financially free.",
      "replacements": [
        "I want to be financially independent.",
        "I want to reach financial freedom.",
        "I want to get to a point where money isn't a problem."
      ]
    }
  ],
  "examples": [
    {
      "sentence": "I want to be financially independent.",
      "translation": "我想实现财务独立。"
    }
  ],
  "spoken": [
    "I wanna be financially free.",
    "I want to be financially independent.",
    "I don't want to worry about money anymore."
  ]
}

================================
        AI ENGLISH COACH
================================
level:
[判断整体难度等级：A1 / A2 / B1 / B2 / C1 / C2，只输出等级本身]

1. origin
[直接展示用户输入的英文原文]

2. translation
[不要逐字直译，给出通顺自然、符合中文表达习惯的翻译]

3. vocabulary
[只挑真正具有学习价值的词、固定表达或句型，2~4个即可；不要为了凑数量而强行解释普通单词组合；每个元素是对象，固定包含 word（词或表达）、phonetic（音标）、pos（词性）、meaning（中文释义）四个字段]

4. mistakes
[重点指出中国学习者最容易在这句话/这类表达上犯的错误——发音、用词、语法或中式英语；每个元素是对象，固定包含 wrong（你很可能会说成的错误说法）、right（地道正确的说法）、tip（简短说明错误原因或记忆要点）三个字段]

5. alternatives
[挑句子里1个核心表达，给出3个左右可替换的说法，优先选择真实生活中高频、自然、可复用的表达，而不是为了显得高级而给出生硬的书面表达；数组只放1个对象，固定包含 original（原句）和 replacements（替换说法的字符串数组，含3个左右元素）两个字段]

6. examples
[给出1~2个贴合日常场景的仿写句子，让用户能立刻实战运用刚学到的表达；所有仿写例句必须经过语法检查，不能为了模仿口语而产生语法错误；每个元素是对象，固定包含 sentence（英文句子）和 translation（中文翻译）两个字段]

7. spoken
[给出3~4个母语者在真实生活场景中，遇到同样情境时更可能脱口而出的口语化说法，优先提供真实生活中高频、自然、可复用的表达，而不是为了显得高级而给出生硬的书面表达；spoken 是纯字符串数组，每个元素就是一句口语表达，不要加"日常口语："之类的标签或编号]
================================

规则：
① 如果用户输入是单句就单句分析，多段/多篇文本就分段处理；
② 遇到俚语、固定习语优先说明语境含义，不要直译；
③ 内容难度适配普通英语学习者，专业术语简单通俗解释；
④ 若输入混杂中英文，只提取英文部分分析，忽略中文；
⑤ 日常口语化表达部分：可以提供自然、年轻、真实的口语，但避免过度俚语、粗俗表达，除非原文本身就是这种语气；
⑥ 所有仿写例句必须经过语法检查，不能为了模仿口语而产生语法错误；
⑦ 不要为了凑2~3个生词而强行解释普通单词组合，优先选择真正具有学习价值的词、固定表达或句型；
⑧ 优先提供真实生活中高频、自然、可复用的表达，而不是为了显得高级而提供生硬的书面表达；
⑨ 只输出上述格式内容，不要添加额外解释、前缀或后缀。

英文：
"""
def get_ai_response(text):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role":"user",
                "content":PROMPT_HEAD + text
            }
        ],
    )

    answer = response.choices[0].message.content
    return json.loads(answer)