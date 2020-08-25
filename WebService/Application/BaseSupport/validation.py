def validation(ls):
    for each in ls:
        if type(each) == int:
            if each == None:
                return False
        elif type(each) == str:
            if each == "":
                return False
    return True

