# def countOfAtoms(formula):
#     data = {}
#     len_formula = len(formula)

#     for i in range(len_formula-1):
#         cur_token = formula[i]
#         next_token = formula[i+1] if i+1 <= len_formula else ''

#         if cur_token.isalpha() and cur_token.isupper():
#             if next_token.isdigit():
#                 data = if_exist_add(token_to_add=cur_token, data=data, a=next_token)

#             if next_token=='' or next_token.isalpha() and next_token.isupper() or next_token in ['(', ')']:
#                 data = if_exist_add(token_to_add=cur_token, data=data)

#             if next_token.isalpha() and next_token.islower():
#                 data = if_exist_add(token_to_add=cur_token+next_token, data=data)

#     return data

# def if_exist_add(token_to_add, data, a=1):
#     a = int(a)
#     if token_to_add in data:
#         data[token_to_add] += a
#     else:
#         data[token_to_add] = a
#     return data

def countOfAtoms(formula: str) -> str:
    # will contain hash-maps with count of elements in last meeted brackets
    n: int = len(formula)
    result_counter: dict[str, int] = {}
    parenthesis_stack: list[dict[str, int]] = []
    cur_ind = 0

    while cur_ind < n:
        cur_char: str = formula[cur_ind]

        if cur_char == "(":
            cur_ind += 1
            parenthesis_stack.append({})
            continue

        if cur_char == ")":
            mult: str = ""
            cur_ind += 1

            while cur_ind < n and formula[cur_ind].isdigit():
                mult += formula[cur_ind]
                cur_ind += 1

            last_counter: dict[str, int] = parenthesis_stack.pop()
            target: dict[str, int] = parenthesis_stack[-1] if parenthesis_stack else result_counter
            for elem, counter in last_counter.items():
                if elem not in target:
                    target[elem] = 0
                target[elem] += counter * (int(mult) if mult else 1)
            continue

        cur_elem: str = ""
        cur_counter: str = ""
        target: dict[str, int] = parenthesis_stack[-1] if parenthesis_stack else result_counter

        while cur_ind < n and cur_char not in "()":
            if cur_char.isalpha():
                if cur_char.isupper() and cur_elem != "":
                    if not cur_elem in target:
                        target[cur_elem] = 0
                    target[cur_elem] += int(cur_counter) if cur_counter else 1
                    cur_counter = ""
                    cur_elem = ""
                cur_elem += cur_char
            else:
                cur_counter += cur_char
            cur_ind += 1
            if cur_ind != n:
                cur_char = formula[cur_ind]

        target = parenthesis_stack[-1] if parenthesis_stack else result_counter
        if not cur_elem in target:
            target[cur_elem] = 0
        target[cur_elem] += int(cur_counter) if cur_counter else 1

    parts: list[str] = [
        elem + str(counter) if not counter == 1 else elem for elem, counter in result_counter.items()
    ]
    parts.sort()

    return "".join(parts)

formula = 'K4(OMg(SO3)2)2Ku'
print(countOfAtoms(formula))

