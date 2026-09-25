def format_mistakes(data):
    result = data.get("mistakes", [])

    if not isinstance(result, list):
        result = []

    mis = []

    for i, item in enumerate(result, 1):
        if not isinstance(item, dict):
            continue

        wrong = item.get("wrong", "")
        right = item.get("right", "")
        tip = item.get("tip", "")

        mis.append(
            f"{i}. ❌ 错误：{wrong}\n"
            f"   ✅ 正确：{right}\n"
            f"   💡 说明：{tip}"
        )

    return "\n".join(mis)


def get_translation(data):
    return data.get("translation")

def get_level(data):
    return data.get("level")



def format_alternatives(data):
    alternatives = data.get("alternatives", [])

    if not isinstance(alternatives, list):
        alternatives = []

    original_sentence = ""
    replacements = []

    if alternatives:
        first_item = alternatives[0]

        if isinstance(first_item, dict):
            original_sentence = first_item.get("original", "")
            replacements = first_item.get("replacements", [])

            if not isinstance(replacements, list):
                replacements = []

    rep_lines = []

    for i, rep in enumerate(replacements, 1):
        if isinstance(rep, str):
            rep_lines.append(f"{i}. {rep}")

    output_parts = []

    if original_sentence:
        output_parts.append(f"原句：{original_sentence}")

    if rep_lines:
        output_parts.append("替换选项：")
        output_parts.extend(rep_lines)

    return "\n".join(output_parts)




def format_examples(data):
    result = data.get("examples", [])

    if not isinstance(result, list):
        result = []

    ex = []

    for i, item in enumerate(result, 1):
        if not isinstance(item, dict):
            continue

        sentence = item.get("sentence", "")
        translation = item.get("translation", "")

        ex.append(
            f"{i}. {sentence}/{translation}"
        )

    return "\n".join(ex)

def format_spoken(data):
    result = data.get("spoken", [])

    if not isinstance(result, list):
        result = []

    sp = []
    i = 0

    for word in result:
        if not isinstance(word, str):
            continue

        i += 1
        sp.append(f"{i}. {word}")

    return "\n".join(sp)

def format_vocabulary(data):
    i = 0
    result = data.get("vocabulary", [])

    if not isinstance(result, list):
        result = []

    voc = []
    for item in result:
        if not isinstance(item, dict):
            continue
        i = i + 1
        voc.append(
            f"{i}. {item.get('word', '')}/"
            f"{item.get('phonetic', '')}/"
            f"{item.get('pos', '')}/"
            f"{item.get('meaning', '')}"
        )
    return "\n".join(voc)

