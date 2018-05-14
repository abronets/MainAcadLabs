def are_balanced_brackets(expr):
    list1 = list(expr)
    if list1.count('(') == list1.count(')'):
        if '+' in list1 or '-' in list1 or '*' in list1 or '/' in list1 == True:
            return(True)
        else:
            return(False)
    else:
        return(False)
