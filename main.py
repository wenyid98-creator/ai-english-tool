
from ai import get_ai_response

from formatter import(
    format_mistakes,
    get_translation,
    get_level,
    format_alternatives,
    format_examples,
    format_spoken,
    format_vocabulary
         
)


while True:
    text = input("请输入一段英文（输入 exit 退出）：").strip()

    if text.lower() == "exit":
        print("👋 Thanks for using AI English Coach!")
        break

    if not text:
        print("请输入英文内容。")
        continue

    data = get_ai_response(text)

    

    translation = get_translation(data)
    level = get_level(data)
    vocabulary = format_vocabulary(data)
    mistakes = format_mistakes(data)
    alternatives = format_alternatives(data)
    examples = format_examples(data)
    spoken = format_spoken(data)

    print("\n=== AI ENGLISH COACH ===")
    print("\n【翻译】")
    print(translation)

    print("\n【等级】")
    print(level)

    print("\n【核心词汇】")
    print(vocabulary)

    print("\n【易错点】")
    print(mistakes)

    print("\n【同义替换】")
    print(alternatives)

    print("\n【仿写例句】")
    print(examples)

    print("\n【日常口语】")
    print(spoken)