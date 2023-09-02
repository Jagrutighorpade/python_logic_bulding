#1----using =
# every chnage reflect
"""
def copy1():
    l1=[10,20,[30,40]]
    l2=l1
    l1[0]=100
    print(l1)
    print(l2)

def main():
    copy1()

if __name__=="__main__":
    main()"""

#2.....shallow copy
"""
def copy1():
    l1=[10,20,[30,40]]
    import copy
    l2=copy.copy(l1)
    l3=l1.copy()
    l4=l1[:]
    l5=list(l1)

    #only l1 will change
    l2[0]=100
    print(l2)
    print(l1)
    print(l3)
    print(l4)
    print(l5)


    # every nested object /list  will change
    l2[2][0]=900
    print(l2)
    print(l1)
    print(l3)
    print(l4)
    print(l5)

def main():
    copy1()

if __name__=="__main__":
    main()"""

#--deepycopy
"""
def copy1():
    l1=[10,20,[30,40]]
    import copy
    l2=copy.deepcopy(l1)


    # change will be happend in chamngable list
    l1[0]=100
    print(" change in l1")
    print(l1)
    print(l2)

    print("\r")
    # change will be happend in chamngable list
    l2[2][0]=900
    print("change in l2")
    print(l1)
    print(l2)

def main():
    copy1()

if __name__=="__main__":
    main()"""
