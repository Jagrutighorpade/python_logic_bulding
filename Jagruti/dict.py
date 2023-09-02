
#Example 1: Displaying the Keys in sorted order
# def dict1():
#     key_value={}
#     key_value[1]=22
#     key_value[4]=85
#     key_value[2]=21
#     key_value[8]=88
#     key_value[5]=25
#     key_value[9]=81
#     for i in sorted(key_value.keys()):
#         print(i,end=" ")
# def main():
#     dict1()
# if __name__=='__main__':
#     main()

#Example 3: Sorting the Keys and Values in Alphabetical Order using the Key
# def dict1():
#     key_value={}
#     key_value[1]=22
#     key_value[4]=85
#     key_value[2]=21
#     key_value[8]=88
#     key_value[5]=25
#     key_value[9]=81
#     for i in sorted(key_value):
#         print((i,key_value[i]),end=" ")
# def main():
#     dict1()
# if __name__=='__main__':
#     main()


#Example 4: Sorting the Keys and Values in alphabetical using the value
# def dict1():
#     key_value={}
#     key_value[1]=22
#     key_value[4]=85
#     key_value[2]=21
#     key_value[8]=88
#     key_value[5]=25
#     key_value[9]=81
#     print(sorted(key_value.items() ,key=lambda kv:(
#                  kv[1],kv[0])))
# def main():
#     dict1()
# if __name__=='__main__':
#     main()


# from collections import OrderedDict
#
# dict = {'ravi': '10', 'rajnish': '9',
#         'sanjeev': '15', 'yash': '2', 'suraj': '32'}
# print(OrderedDict(sorted(dict.items())))



# Method 1 : Using get()
# country_code = {'India': '0091',
#                 'Australia': '0025',
#                 'Nepal': '00977'}
# print(country_code.get('India'))

#setdefaut
# country_code = {'India': '0091',
#                 'Australia': '0025',
#                 'Nepal': '00977'}
# country_code.setdefault('Japan')
# print(country_code['Japan'])

#
# Method 3: Using defaultdict
# import collections
#
# defd = collections.defaultdict(lambda: 'Key Not found')
#
# defd['a'] = 1
#
#
# defd['b'] = 2
#
# print(defd['a'])
#
# print(defd['c'])
#
# ADDITION
# from functools import reduce
#
# dic = { 100:'a',  200 :'b', 300:'c'}
#
# sum_dic = reduce(lambda a,b: a + b, dic,0)
#
# print("Sum :", sum_dic)

###---NEW STARTING---
"""
def main():
    dict1={"a":1 ,"b":2 ,"c":3}
    print(dict1)

    dict2=dict([(1,2),(3,4),(4,5)])   #list of tuble
    print(dict2)

    dict3=dict(a="piu" ,b="mau",c="kau")
    print(dict3)

if __name__=="__main__":
    main()"""

#====dict comprehension
"""
def value1(x):
    x=x**3
    return x
def main():
    dict2={x:value1(x) for x in (1,2,3,4)}
    print(dict2)
if __name__=="__main__":
    main()"""

#empty dict
"""
dict1={}
print(dict1)
dict2=dict()
print(dict2)"""

##----assscesssing dict
"""
#--1)
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
    print(alpha1)
if __name__ == "__main__":
    main()"""

#----2)using  .items()
"""
def main2():
     alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
     print(alpha1.items())
def main1():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
    for key,value in alpha1.items():
        print(key, ":" ,value,end=" , ")
def main():
    main1()
    main2()
if __name__ == "__main__":
    main()"""

#----3)using .keys()
"""
def main2():
     alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
     print(alpha1.keys())
def main1():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
    for key in alpha1.keys():
        print(key,end=",")
def main():
    main1()
    main2()
if __name__ == "__main__":
    main()"""

#--4)using .values()
"""

def main2():
     alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
     print(alpha1.values())
def main1():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
    for value in alpha1.values():
        print(value,end=",")
def main():
    main1()
    main2()
if __name__ == "__main__":
    main()"""

#----get()
"""
def main2():
    alpha1 = {"a": 1, "b": 2, "c": 3, "d": 4}
    x=alpha1["d"]
    print(x)
def main1():
    alpha1 = {"a": 1, "b": 2, "c": 3, "d": 4}
    x=alpha1.get("c")
    print(x)
def main():
    main1()
    main2()
if __name__ == "__main__":
    main()"""

##---add---change---dlete-- ele
"""
def  main3():
    alpha1 = {"a": 1, "b": 2, "c": 3, "d": 4}
    del alpha1["a"]
    print(alpha1)
def main2():
    alpha1 = {"a": 1, "b": 2, "c": 3, "d": 4}
    alpha1["a"]=101
    alpha1["b"]=102
    print(alpha1)
def main1():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
    alpha1["e"]=6
    alpha1["f"]=5
    print(alpha1)
    alpha1.update({"g":9})
    print(alpha1)
def main():
    main1()
    main2()
    main3()
if __name__ == "__main__":
    main()"""

##----clear()
"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
    alpha1.clear()
    print(alpha1)
if __name__ == "__main__":
    main()"""

#---copy()
"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
    alpha2=alpha1.copy()
    print(alpha2)
if __name__ == "__main__":
    main()"""


#---pop()---perticular item
"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4}
    alpha1.pop("b")
    print(alpha1)
if __name__ == "__main__":
    main()"""

#---popitems()----
"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4,"e":5}
    alpha1.popitem()
    print(alpha1)
    x=alpha1.popitem()
    print(x)
    
    del alpha1["c"]
    print(alpha1)

if __name__ == "__main__":
    main() """

#---fromkeys()
"""
def main():
    t1=(1,2,3,4,5)
    str1="a"
    dict1=dict.fromkeys(t1,str1)
    print(dict1)

    t2=(2,4,6)
    dict2=dict.fromkeys()
    print(dict2)
if __name__ == "__main__":
    main()"""

####--setfefault()
"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4,"e":5}
    x=alpha1.setdefault("a",6)
    print(x)
    y=alpha1.setdefault("f",100)
    print(y)
if __name__ == "__main__":
    main()"""


##---for loop
"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4,"e":5}
    for key in alpha1:
        print(key,end=" ,")
    for key in alpha1.keys():
        print(key," :")
    for value in alpha1.values():
        print(":",value, end="")
    for key ,value in alpha1.items():
        print("\n",key,":",value)
if __name__ == "__main__":
    main()"""

##--key ispresent or not
"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4,"e":5}
    ispresent= "a" in alpha1
    print(ispresent)
    x="f" in alpha1
    print(x)
if __name__ == "__main__":
    main()"""

###----NESTED DICTIONARY---
"""
def main():
    alpha1={"foo": {"a":10,"b":12},
                    "moo": {"b":12,"c":15},
                    "poo": {"c":15, "a":10}}

    print(alpha1)
    print(alpha1["foo"])
    print(type(alpha1["foo"]))
    print((alpha1["foo"]["a"]))
    print((alpha1["moo"]["c"]))
if __name__ == "__main__":
    main()"""



#---nested LIST OF dict
"""
def main():
    list1=[ {"a":10,"b":12},
                    {"b":12,"c":15},
                     {"c":15, "a":10}]
    print(list1)
    print(list1[0])
    print(list1[0]["a"])
    print(list1[1]["b"])
    print(list1[2]["c"])

    ##append
    list1[2]["d"]=20
    list1[1]["e"]=30
    list1[0]["f"]=40
    list1[3:0]=[{"x":111,"y":999}]
    list1.append({"z":888})
    print(list1)

    #change
    list1[0]["f"]=400
    list1[1]["e"]=300
    list1[2]["d"]=200
    print(list1)


if __name__ == "__main__":
    main()"""

###-----dict (key) covert into list

"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4,"e":5}
    l1=list(alpha1.keys())
    print(l1)

    l2=[*alpha1]
    print(l2)

    l3=[key for key in alpha1]
    print(l3)

    l4=[key for key in alpha1.keys()]
    print(l4)

    l5=[]
    for key in alpha1:
        l5.append(key)
    print(l5)
    
if __name__ == "__main__":
    main()"""



##-----covert dict( values )into a list
"""
def main():
    alpha1={"a":1 ,"b":2 ,"c":3,"d":4,"e":5}
    l1=list(alpha1.values())
    print(l1)

    l2=[value for value in alpha1.values()]
    print(l2)
    
    
    l4=[d[key] for key in alpha1]
    print(l4)
    

    l3=[]
    for value in alpha1.values():
        l3.append(value)
    print(l3)

if __name__ == "__main__":
    main()"""



###----user define dict
"""
def main():
    no=int(input("enter no of element="))
    dict1={}
    for i in range(no):
        j=(input("enter key="))
        k=(input("enter vlaue="))
        dict1.update({j:k})
    print(dict1)
if __name__ == "__main__":
    main()"""



#sort dict
"""
def main3():
    dict1 = {3: "jim", 2: "jack", 4: "jane", 5: "jill"}
    dict(sorted(dict1.items()))
    print(dict1)
    sorted(dict1)
    print(dict1)
#val=1
def main2():
    dict1 = {3: "jim", 4: "jack", 2: "jane", 5: "jill"}
    dict2=dict(sorted(dict1.items(), key=lambda dict1:dict1[1]))
    print("val=",dict2)

 #key=0
def main1():
    dict1={3:"jim" ,4:"jack"  ,2:"jane"   ,5:"jill" }
    dict2=dict(sorted(dict1.items(), key=lambda dict1: dict1[0]) )  #key=0 ,val=1
    print("key=",dict2)
def main():
    main1()
    main2()
    main3()

if __name__ == "__main__":
    main()"""

#####---Vice-Versa  covert {key into val} and  {val into key}
"""
def  main4():
    dict1 = {3: "jim", 4: "jack", 2: "jane", 5: "jill"}
    dict2={key:dict1[key]    for key ,value in dict1.items()}
    print(dict2)
def main3():#not proper
    dict1 = {3: "jim", 4: "jack", 2: "jane", 5: "jill"}
    dict2={(v,":",k)   for k,v in dict1.items() }  #(k,v) ...() are imp
    print(dict2)
def main2():
    dict1 = {3: "jim", 4: "jack", 2: "jane", 5: "jill"}
    dict2=dict(  (v,k )    for k,v in dict1.items()   )
    print(dict2)
def main1():
    dict1 = {3: "jim", 4: "jack", 2: "jane", 5: "jill"}
    dict2={}
    for key ,value in dict1.items():
        dict2[value]=key
    print(dict2)

def main():
    main1()
    main2()
    main3()
    main4()


if __name__ == "__main__":
    main()"""

##...tuple as a key
"""
d1 = {(1,2,3):4, (4,5,6):5}

print(d1[(4,5,6)])"""



# ...collect 2 key from dict and create dictionery
"""
def main1(d1):
    d2={x:d1[x]  for x in ["name","age"]}
    print(d2)
def main():
    d1={"name":"pooja",
                "age": 25,
             "id_no":666,
            "city":"mumbai",
            "state":"gujarat"
        }
    main1(d1)

if __name__ == "__main__":
    main()"""

#...delete set of keys
"""
def main2(d1):
    d2={x:d1[x]  for x in d1.keys()-["name","age"]}
    print(d2)
def main1(d1):
    del d1["name"]
    del d1["age"]
    print(d1)
def main():
    d1={"name":"pooja",
                "age": 25,
             "id_no":666,
            "city":"mumbai",
            "state":"gujarat"
        }
    main1(d1)
    main2(d1)

if __name__ == "__main__":
    main()"""

###......change or rename the key name
""""
def main3(d1):
    d1["satate"]="mahashtra"
    print(d1)
def main2(d1):
    d1["AGE"]=d1.pop("age")
    print(d1)
def main1(d1):## using native metive
    d1["NAME"]=d1["name"]
    del d1["name"]
    print(d1)
def main():
    d1={"name":"pooja",
                "age": 25,
             "id_no":666,
            "city":"mumbai",
            "state":"gujarat"
        }
    main1(d1)
    main2(d1)
    main3(d1)

if __name__ == "__main__":
    main()"""

#covert 2 list into a dict
"""
def main1():
    l1=[1,2,3]
    l2=["a", "b" ,"c"]

    d1={x:y for x,y in zip(l1,l2)}
    print(d1)

    d2={l2[i]:l1[i] for i in range(len(l2))}
    print(d2)

    d3=dict(zip(l2,l1))
    print(d3)

    d4={}
    for i in range(len(l1)):
        d4.update({l1[i]:l2[i]})
    print(d4)

def main():
    main1()

if __name__ == "__main__":
    main()"""

#...merge/concate two list
"""
def main1():
    ##1
    d1={"a":1 ,"c":2, "d":3}
    d2={"e":4,"f":5}
    d3=d1.copy()
    d3.update(d2)
    print(d3)

    ##2
    d4={**d1,**d2}
    print(d4)

def main():
    main1()
if __name__ == "__main__":
    main()"""

###print val of.. history..
"""
def main1():
    d1={"class":{"student":{"name":"maike","marks":{"physics": 70,"history":80}
                            }
                 }
        }
    x=d1["class"]["student"] ["marks"]  ["history"]
    print(x)

def main():
    main1()
if __name__ == "__main__":
    main()"""

##...fromkeys
"""
def main1():
    l1=["a","b"]
    d1={1:2 ,3:4  ,5:6}
    d2=dict.fromkeys(l1,d1)
    print(d2)
def main():
    main1()
if __name__ == "__main__":
    main()"""


##create dict using keys
"""
def main2():
    d1={"name":"pooja",
                "age": 25,
             "id_no":666,
            "city":"mumbai",
            "state":"gujarat"
        }
    #1
    d2=["name","city"]
    d3={x:d1[x] for x in d2}
    print(d3)

    #2
    d4={x:d1[x] for x in ["name","id_no"]}
    print(d4)
    
    #3
    d5={}
    d6= ["name", "city"]
    for x in d6:
        d5.update({x:d1[x]})
    print(d5)
def main1():
    d1={1:"a",2:"b",3:"c"}
    d2={x:x+1 for x in d1.keys()}
    print(d2)
def main():
    main1()
    main2()
if __name__ == "__main__":
    main()"""


#...check val is present or not in list
"""
def main2():
    d1={"a":200 ,"b":300 ,"c":400}
    no=int (input("enter no="))
    flag=0
    for value in d1.values():
        if value==no:
            flag=1
    if flag == 1:
        print("present")
    else:
        print("not present")


def main1():
    d1={"a":200 ,"b":300 ,"c":400}
    no=int (input("enter no="))
    flag=0
    for key in d1.keys():
        if d1[key]==no:
            flag=1
    if flag==1:
        print("present")
    else:
        print("not present")

def main():
    main1()
    main2()
if __name__ == "__main__":
    main()"""



#..finf min value of key
"""
def main1():
    d1={"a":111 ,"b":110,"c":101}
    min1=min(d1.values())
    print(min1)
    print(min(d1,key=d1.get))
def main():
    main1()
    #main2()
if __name__ == "__main__":
    main()"""


#....sort dict key=0
"""
from collections import OrderedDict
def main4():
    d1 = {"e": 6, "g": 8, "a": 3, "f": 1}
    d2=OrderedDict (sorted(d1.items()))
    print(d2)

def main3():
    d1 = {"e": 6, "g": 8, "a": 3, "f": 1}
    d2=sorted(d1.items())
    print(d2)
def main2():
    d1 = {"e": 6, "g": 8, "a": 3, "f": 1}
    d2={key:d1[key] for key in sorted(d1.keys())}
    print(d2)

def main1():
    d1={"e":6 ,"g":8, "a":3 ,"f":1}
    d1=dict(sorted(d1.items(),key=lambda d1:d1[0]))
    print(d1)
def main():
    main1()
    main2()
    main3()
    main4()
if __name__ == "__main__":
    main()"""

#...sorted value
"""
def main1():
    d1={"e":6 ,"g":8, "a":3 ,"f":1}
    d2=dict(sorted(d1.items(), key=lambda d1:d1[1]))
    print(d2)
def main():
    main1()
if __name__ == "__main__":
    main()"""


#sum of values
"""
from functools import reduce
def main3():
    d1 = {"e": 6, "g": 8, "a": 3, "f": 1}
    d2 =reduce(lambda sum,key : sum+d1[key],d1,0)  #..sum=0
    print(d2)
def main2():
    d1 = {"e": 6, "g": 8, "a": 3, "f": 1}
    sum1=sum(d1.values())
    print(sum1)

def main1():
    sum=0
    d1={"e":6 ,"g":8, "a":3 ,"f":1}
    for value in d1.values():
        sum=sum+value
    print(sum)
def main():
    main1()
    main2()
    main3()
if __name__ == "__main__":
    main()"""

#sum of key
"""
from functools import reduce
def main3():
    d1 = {1: "v", 2: "e", 9: "j"}
    d2=reduce(lambda sum,key: sum+key,d1,0)
    print(d2)

def main2():
    d1 = {1: "v", 2: "e", 9: "j"}
    sum1=sum(d1.keys())
    print(sum1)

def main1():
    d1={1:"v", 2:"e",9:"j"}
    sum=0
    for key in d1.keys():
        sum=sum+key
    print(sum)

def main():
    main1()
    main2()
    main3()
if __name__ == "__main__":
    main()"""

#....get and setfault ("key",val)
"""
def main2():
    d1 = {"e": 6, "g": 8, "a": 3, "f": 1}
    x=d1.setdefault("g",33)
    print("stdflt value of  g=",x)
    y=d1.setdefault("c",33)
    print("stdflt value of c=",y)
    print("stdflt value of  k=",d1.setdefault("k",99))

def main1():  #get("keye": val)
    d1 = {"e": 6, "g": 8, "a": 3, "f": 1}
    print("get value of  g=",d1.get("g",33))
    print("get value of  c=", d1.get("c", 33)) #new

def main():
    main1()
    main2()

if __name__ == "__main__":
    main()"""

#size of dict....1)..getsizeof  2)#__sizeof__
"""
import sys
def main1():
    d1 = {"e": 6, "g": 8, "a": 3, "f": 1}
    size1=sys.getsizeof(d1)
    print("dict size="+ str(size1)+"bytes")
def main2():
    d2 = {"e": 6, "g": 8, "a": 3, "f": 1}
    size1=d2.__sizeof__()
    print("dict size=" +str( size1)+"bytes")
    print(d2.__sizeof__(),"bytes")
def main():
    main1()
    main2()

if __name__ == "__main__":
    main()"""


#add two dict
"""
def main():
    d1={1:2,3:4,5:6}
    d2={7:8,9:10,11:12}
    #1
    d3=d1.copy()
    d3.update(d2)
    print(d3)

    #2
    d3={**d1,**d2}
    print(d3)

    #3
    for i in d2.keys():
        d1[i]=d2[i]
    print(d1)


if __name__ == "__main__":
    main()"""

#add element at beginnningd
"""
from collections import OrderedDict
def main2():
    d1 = OrderedDict({"a": 1, "b": 2})
    d2 = OrderedDict({"t": 1, "u": 8})
    d3= OrderedDict(list(d2.items())+list(d1.items()))
    print(d3)

def main1():
    d1=OrderedDict({"a":1,"b":2})
    d1.update({"c":5})
    d1.move_to_end("c",last=False)
    print(d1)
def main():
    main1()
    main2()
if __name__ == "__main__":
    main()"""

#......ways t0 sort list of dict by values in python using itemgetter and lamda
"""
from operator import itemgetter
def main3():
    l1=[{"name":"piu"  , "age":20},    {"name":"om" ,"age":20},      {"name":"pooja " ,"age":19}]
    #3
    print(sorted(l1,key=itemgetter("age"),reverse=True))
    #3.3
    d3=sorted(l1,key=lambda i_no:i_no["age"],reverse=True)
    print(d3)
def main2():
    l1=[{"name":"piu"  , "age":20},    {"name":"om" ,"age":20},      {"name":"pooja " ,"age":19}]
    #2
    print(sorted(l1 ,key=itemgetter("age","name")))
    #2.2
    d2=sorted(l1,key=lambda i_no:(i_no["age"],i_no["name"]))
    print(d2)
    print("\r")

def main1():#age-wise
    l1=[{"name":"piu"  , "age":20},    {"name":"om" ,"age":20},      {"name":"pooja " ,"age":19}]
    #1
    print(sorted(l1,  key=itemgetter("age")))
    #1.1
    d1=sorted(l1, key=lambda i_no: i_no["age"])
    print(d1)
    print("\r")
def main():
    main1()
    main2()
    main3()
if __name__ == "__main__":
    main()"""

#counting freqvency of list using dict
"""
def main1():
    #l1=[1,2,3,88,3,2,3,4,1,4,2,3,99,1,1,4]
    l1=list("aaaaaabbbbbbbccccddd")
    d1={}
    for item in l1:
        if item in d1:
            d1[item]=d1[item]+1
        else:
            d1[item]=1
    print(d1)
     
    #2
    for i,j in d1.items():
        print(i,":",j,end=" ,  ")

def main():
    main1()

if __name__ == "__main__":
    main()"""

#--remove key {"a"and"b")from dict without inbuilt fun
"""
def main1():
    d1={"e": 6, "g": 8, "b": 3, "f": 1,"a":4}
    d2={key:d1[key] for key in d1.keys() if key !="a"}
    print(d2)
    print("\r")
    d3={key:val  for key,val in d1.items() if key !="b"}
    print(d3)
def main():
    main1()

if __name__ == "__main__":
    main()"""

#....find val mean
"""
def main1():
    d1={"e": 6, "g": 8, "b": 3, "f": 1,"a":4}
    sum=0
    mean=0
    for val in d1.values():
        sum=sum+val
        mean=sum/len(d1)
    print(mean)
def main():
    main1()

if __name__ == "__main__":
    main()"""









