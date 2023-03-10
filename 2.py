def foo(s):
    d={"upper":0, "lower":0}
    for x in s:
        if x.isupper():
           d["upper"]+=1
        elif x.islower():
           d["lower"]+=1
        else:
           pass
    print ("Mysal :", s)
    print ("Upper case : ", d["upper"])
    print ("Lower case : ", d["lower"])

foo(input())
