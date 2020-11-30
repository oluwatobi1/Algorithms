ls = ["hello, how, are, you"]

def spliter(ls):
    words=ls[0].split(',')
    out_dict = {}
    for i in range(len(words)):
        out_dict[i] =words[i]
    return out_dict
print(spliter(ls))
