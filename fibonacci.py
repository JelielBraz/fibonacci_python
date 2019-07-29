def fibonacci():
    i = 0
    a = [0, 1]

    # b = [0,1,2,3,4,5,6,7,8,9]
    # print(b[-2])
    while i < 350:
        i = a[-2] + a[-1]
        if i > 350:
            return a
        a.append(i)
    return a


def isFibonacci(n):
    if n in fibonacci():
        return True
    else:
        return False

