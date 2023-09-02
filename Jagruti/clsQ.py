#
# ------3------
# def main():
#     x={i:i+2 for i in range(5+1)}
#     print(x)
# if __name__=="__main__":
#     main()


# -----7----
# def main():
#     l1=[2,4,5,6,8]
#     x=[i*i for i in l1]
#     print(x)
# if __name__=="__main__":
#     main()
#
# -----14---
# def main():
#     c=0
#     no=int(input("enter no="))
#     for i in range(no):
#         c=c+i
#     print(c)
# if __name__=="__main__":
#     main()


# -----15--
# print(2**3+(6+5)**(1+1))

# -----26---
# import re
# def main():
#  stud="my name is jagruti and may contact no is 1929809820"
#  find_no=re.findall('\d',stud)
#  print(find_no)
#
# ---35----
# def main():
#     x=[1,2,3,4,5]
#     y={i:i*i for i in x}
#     print(y)
# if __name__ == "__main__":
#     main()


# --36--
# a='186,23.8'
# c=a.replace(',','.' )
# print(c)

#
# -------38=---
# def main():
#     marks=[20,40,70,30,50,90]
#     a=[x for x in marks if x<max(marks)]
#     print(max(a))
# if __name__ == "__main__":
#     main()

# --40--
# def main():
#     marks = [20, 40, 70, 30, 50, 90]
#     rev=marks[::-1]
#     print(rev)
# if __name__ == "__main__":
#     main()

# ----44--
# def main():
#     name='aaabbbccddddd'
#     counta=0
#     countb=0
#     countc=0
#     countd=0
#     for i in name:
#         if 'a'==i:
#             counta=counta+1
#         elif  'b' == i:
#             countb = countb+1
#         elif 'c' == i:
#             countc = countc + 1
#         elif 'd' == i:
#             countd = countd + 1
#     print({"a":counta ,"b":countb ,"c":countc ,"d":countd})
#
# if __name__ == "__main__":
#     main()

#
# def main():
#     for i in range(1,6):
#         for j in range(1,6):
#             if (i==1 and j<=4)or(i==2 and j<=3)or (i==3 and j<=2)or(i==4 and j==1 ):
#                 print("*",end="")
#             else:
#                 print("$",end="")
#         print()
# if __name__=="__main__":
#     main()
#


#