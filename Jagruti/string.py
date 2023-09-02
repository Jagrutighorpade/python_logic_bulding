# ------count len of str-----
# def str1():
#     count=0
#     s= "jagruti"
#     for i in s:
#         count=count+1
#     return count
#
# def main():
#     result=str1()
#     print(result)
# if __name__=="__main__":
#     main()

# #-----len using lambda---
# from functools import reduce
# def main():
#     str1="jagruti"
#     a= reduce(lambda x,y:x+1,str1,)
#     print(a)
# if __name__=="__main__":
#     main()

# #3---using len--
# str1="jagrutimau"
# print(len(str1))

# #4-----sum---
# def str2(s):
#     #print(sum(1 for i in s))
#     ans=(sum(1 for i in s))
#     return ans
# def main():
#     str1="hello"
#     len1=str2(str1)
#     print(len1)
# if __name__=="__main__":
#     main()

######revrse----
def main():
    str1="madam"
    l1=[]
    l2=[]
    flag=0
    for i in str1:
        l1.append(i)
    print(l1)
    no=len(l1)
    for i in range(no-1,-1,-1):
        l2.append(l1[i])
    print(l2)
    for i in range(len(l1)-1):
        if l1[i]!=l2[i]:
            flag=1
            break
    if flag==0:
        print("paln yes")
    else:
        print("no")



if __name__=="__main__":
    main()



# ##1____reverse string---
# def main():
#     str1="jagruti"
#     reverse1=str1[::-1]
#     print(reverse1)
# if __name__=="__main__":
#     main()


# ##______reverse string______
# def reverse1(str1):
#     str2=""
#     for i in str1:
#         str2=i+str2
#     return str2
# def main():
#     str1= "hello jagruti ghorpade"
#     #"123456789"
#     str3= reverse1(str1)
#     print(str3)
# if __name__=="__main__":
#     main()

##------chk vowel or not----
# def chk_vowel(char1):
#     vowel=["a","e","i","o","u"]
#     for i in vowel:
#         if char1==i:
#             print("its a vowel")
#             break
#         else:
#             print("its not vowel")
#             break
# def main():
#     char1=str(input("enter single alphabate = "))
#     chk_vowel(char1)
# if __name__=="__main__":
#     main()


# ##-----2----
# def main():
#     char1=str(input("enter alphabate = "))
#     char2=char1.lower()
#     if (char2=="a" or char2=="i" or char2=="u" or char2=="e" or  char2=="o"):
#         print("its vowel")
#     else:
#         print("its consonant")
# if __name__=="__main__":
#     main



##------COUNT VOWEL IN NAME----
# def  cnt_vowel(str1):
#     count=0
#     vowel=["a","e","i","o","u"]
#     for i in vowel:
#         for j in str1:
#             if i==j:
#                 count=count+1
#     return count
# def main():
#     name=str(input("enter your name  = "))
#     str1=name.lower()
#     count1=cnt_vowel(str1)
#     print(count1)
# if __name__=="__main__":
#     main()

# ###-----WHICH VOWEL IS REAPTED----
# def cnt_vowel(name):
#     count1=0
#     count2=0
#     count3=0
#     count4=0
#     count5=0
#     for i in name:
#         if  i=="a":
#             count1=count1+1
#         elif i=="e":
#             count2=count2+1
#         elif i == "i":
#             count3 = count3 + 1
#         elif i == "o":
#             count4 = count4 + 1
#         elif i == "u":
#             count5 = count5 + 1
#     if count1>0:
#         print("a=",count1)
#     if count2>0:
#         print("e=",count2)
#     if count3>0:
#         print("i=",count3)
#     if count4>0:
#         print("o=",count4)
#     if count5>0:
#         print("u=",count5)
# def  main():
#     name1=str(input("enter your name = "))
#     name=name1.lower()
#     cnt_vowel(name)
# if __name__=="__main__":
#     main()



# #--OCCUREANCE OF GIVEN STRING CHAR---
# def cnt_str2(str1):
#     a=str1.count('a')
#     b=str1.count("b")
#     c=str1.count("c")
#     d=str1.count("d")
#     print({"a":a,"b":b,"c":c,"d":d})
# def main():
#     str1="aabbbcccddd"
#     cnt_str2(str1)
# if __name__=="__main__":
#     main()

# #-------PALINDROME(palindrome)------
# def  chk():
#     flag=0
#     x=str(input("enter string = "))
#     lis=[]
#     lis2=[]
#     for i in x:
#         lis.append(i)
#     for j in range(len(x)-1,-1,-1):
#         lis2.append(lis[j])
#     for k in range(len(x)-1):
#         if lis[k]!=lis2[k]:
#             flag=1
#             break
#     if(flag==0):
#         print("yes it is palindrome")
#     else:
#         print('no it is not palindrome')
# def main():
#     chk()
# if __name__=="__main__":
#     main()



########2palindrome-------
# def main():
#     x=str(input("Enter string = "))   #### w=" "   ----w=i+w
#     w=x[ : : -1]
#     if x==w:
#         print("y")
#     else:
#         print("n")
# if __name__=="__main__":
#     main()

# ####anagram--===
# def main():
#     no1=2013
#     no2=3012
#     c=0
#     l1=[]
#     l2=[]
#     while no1!=0:
#         reminder=no1%10
#         l1[reminder]+=1
#         no1=no1//10
#         print(l1, end=" ,")
#     while no2>0:
#         reminder=no2%10
#         no2=no2//10
# if __name__=="__main__":
#     main()

######LOWER TO UPPER#####
# def  cap(j):
#         a=(ord(j)-32)
#         print(chr(a))
# def main():
#     j=str(input("enter lower char ="))
#     cap(j)
# if __name__=="__main__":
#     main()


# #=====2====
# def cap(str1):
#     for i in str1:
#         #a=ord(i)-32
#         #a=ord(i)+32
#         print(chr(a),end="")
# def main():
#     str1=str(input("enter string="))
#     cap(str1)
# if __name__=="__main__":
#     main()




# #=====2====
# def cap(str1):
#     for i in str1:
#         A=A
#         Z=Z
#         a=a
#         z=z
#         y=ord(i)
#         if  y>=ord(A) and y<=ord(Z):  #A=65
#             x=y+32
#             print(chr(x))
#
#         elif  y>=ord(a) and y<=ord(z):  #a=97
#             m=y-32
#             print(chr(m))
#
#
#
# def main():
#     str1=str(input("enter string="))
#     cap(str1)
# if __name__=="__main__":
#     main()