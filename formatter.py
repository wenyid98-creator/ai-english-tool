def format_mistakes(data):
    i = 0
    result = data["mistakes"]
    mis = []
    for item in result:
        i = i + 1
        mis.append( f"{i}. ❌ 错误：{item['wrong']}\n"
        f"   ✅ 正确：{item['right']}\n"
        f"   💡 说明：{item['tip']}")
    return "\n".join(mis)

def get_translation(data):
    return data["translation"]

def get_level(data):
    return data["level"]



def format_alternatives(data):
    alty_lines = []
    original_sentence = data["alternatives"][0]["original"]
    alty_lines.append(f"原句：{original_sentence}")

    i = 0
    for replace_text in data["alternatives"][0]["replacements"]:
        i = i + 1
        alty_lines.append(f"{i}. {replace_text}")

    return "\n".join(alty_lines)


def format_examples(data):
    i = 0
    result = data["examples"]
    ex = []
    for item in result:
        i = i + 1
        ex.append(f"{i}. {item['sentence']}/{item['translation']}")
    return "\n".join(ex)

def format_spoken(data):
    i = 0
    result = data["spoken"]
    sp = []
    for word in result:
        i = i + 1
        sp.append(f"{i}. {word}")
    return "\n".join(sp)

def format_vocabulary(data):
    i = 0
    result = data["vocabulary"]
    voc = []
    for item in result:
        i = i + 1
        voc.append(f"{i}. {item['word']}/{item['phonetic']}/{item['pos']}/{item['meaning']}")
    return "\n".join(voc)