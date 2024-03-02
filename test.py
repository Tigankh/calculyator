def is_vow(inp: list):
    lst = ['97', '101', '105', '111', '117']
    inp = str(inp)
    for i in  range(len(lst)):
        inp = inp.replace(lst[i], chr(int(lst[i])))
    inp = inp.replace(',', '').replace('[', '').replace(']', '')

    inp = inp.split()
    for i in range(len(inp)):
        if inp[i].isdigit():
            inp[i] = int(inp[i])

    return inp


print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]))