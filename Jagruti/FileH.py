#----R
"""
from sys import *
def  fh():
    f=open('jag.txt','r')
    print(f.read())
fh()"""



#----A
"""
def fh():
    f=open('jag.txt','a+')
    f.write("now im working in pune")

    f=open('jag.txt','r')
    print(f.read())
    f.close()
fh()"""

#----w
"""
def fh():
    f=open('jag.txt','w')
    f.write(" jagruti mahesh ghorpade")

    f=open('jag.txt','r')
    print(f.read())
    f.close()
fh()"""

#---r+
"""
def fh():
    f=open('jag.txt','r+')
    print(f.read())
    f.write("now im working in pune")
    f.close()
fh()"""


#----W+****
"""
def fh():
    f=open('jag.txt','w+')
    f.write("now im working in pune")
    print(f.read())

    f.close()
fh()"""

#---a+--****
"""
def fh():
    f=open('jag.txt','a+')
    print(f.read())
    f.write("now im working in pune")
    f.close()
fh()"""

#---rt
"""
def fh():
    f=open('jag.txt','r+')
    print(f.read(7))
    print(f.read(7))
    print(f.read(333))
    #print(f.read(334))#sagal samplay kay print ksaru

    f.close()
fh()"""

#--for loop
"""
def fh():
    f=open("jag.txt")
    for line in f:
        print(line)
fh()"""

#---readline()
"""
def fh():
    f=open("jag.txt")
    print(f.readline())
    print(f.readline())
    print(f.readline())
fh()"""

#....readlines() in list format
"""
def fh():
    f=open("jag.txt")
    print(f.readlines())
fh()"""

#----seek()
"""
def fh():
    f=open("jag.txt")
    print(f.readline())
    f.seek(7)
    print(f.readline())
    f.seek(14)  #1st line madhun ch cut hotil
    print(f.readline())

fh()"""

#---tell ...count of data
"""
def fh():
    f=open("jag.txt")
    print(f.tell())
    print(f.readline())

    print(f.tell())
    print(f.readline())

    print(f.tell())  #1st line madhun ch cut hotil
    print(f.readline())

fh()"""

#pickling

#dumps
import pickle
def  pick():
    data=[10,20,30]
    p=pickle.dumps(data)
    print("pickling=", p)
    #unpickling
    #loads
    data = [10, 20, 30]
    q = pickle.loads(p)
    print("unpickling=", q)

pick()

