def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return("There is 0 division error")


print(div(10,0))
