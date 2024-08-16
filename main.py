from langchain_community.document_loaders import JSONLoader


push_content_loader = JSONLoader(
    file_path='./data/json/makeup.json',
    jq_schema='.[].messages[].push_content',
    text_content=False)

push_content = push_content_loader.load()


def merge_push_content_by_userid(messages):
    result = {}
    for message in messages:
        userid = message["push_userid"]
        content = message["push_content"]
        if userid in result:
            result[userid].append(content)
        else:
            result[userid] = [content]
    return result

# Example usage
messages = [
    {
        "push_tag": "推",
        "push_userid": "daylilylu",
        "push_content": "啊 敗了XD",
        "push_ipdatetime": "163.25.98.111 08/19 17:23"
    },
    {
        "push_tag": "推",
        "push_userid": "ChinRB",
        "push_content": "敗了+1 XDD",
        "push_ipdatetime": "118.169.152.140 08/19 20:00"
    },
    {
        "push_tag": "推",
        "push_userid": "prankangel",
        "push_content": "謝謝分享^^",
        "push_ipdatetime": "122.254.11.22 08/19 22:41"
    },
    {
        "push_tag": "→",
        "push_userid": "mandyku",
        "push_content": "怎麼找到的沒有試用包...雖然ml數很小啦XD",
        "push_ipdatetime": "111.248.75.135 08/21 01:07"
    }
]

result = merge_push_content_by_userid(messages)
print(result)
