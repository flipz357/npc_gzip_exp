def string2set(string, croplen=3):
    string = string.replace(".","  ")
    string = string.replace(",","  ")
    string = string.replace("?","  ")
    string = string.replace("!","  ")
    string = string.lower()
    ls = string.split()
    ls = [t for t in ls if len(t) > croplen]
    return set(ls)
