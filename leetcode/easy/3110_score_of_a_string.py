def scoreOfString(s: str) -> int:
    fast, slow = 1,0
    sumarrize_list_tokens = []
    while fast != len(s):
        sumarrize_list_tokens.append([s[slow], s[fast]])
        fast += 1
        slow += 1
    summary = 0

    for token in sumarrize_list_tokens:
        summary += abs((int(ord(token[0]))-int(ord(token[1]))))
    return summary