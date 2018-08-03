def is_sorted(test):
    test0=[]
    for i in test:
        test0.append(i)
    test.sort()
    if test==test0:
        return True
    else:
        return False
