#1
"""
class math:
    def add(a,b):
        add=a+b
        print(add)
def main():
    obj=math
    obj.add(20,30)
if __name__=="__main__":
    main()"""

#2
"""
class parent:
    def add(a,b):
        add=a+b
        print(add)
class chlid :
    def sub(c,d):
        sub=c-d
        print(sub)
class sub_child:
    def mul(e,f):
        mul=e*f
        print(mul)
def main():
    obj1=parent
    obj1.add(2,4)
    obj2=chlid
    obj2.sub(7,1)
    obj3=sub_child
    obj3.mul(2,3)

if __name__=="__main__":
    main()"""


#3
"""
class parent:
    x=0
    y=0
    ans=0
    def  __init__(self,a,b):
        self.x=a
        self.y=b

    def add(self):
        ans=self.x+self.y
        return (ans)
    def sub(self):
        ans=self.x-self.y
        return (ans)
    def mul(self):
        ans=self.x * self.y
        return ans

def main():
    obj=parent(20,10)
    x=obj.add()
    y=obj.sub()
    z=(obj.mul())
    print("add=",x)
    print("sub=",y)
    print("mul=",z)

if __name__=="__main__":
    main()"""

#4
"""
class Math:
    ans=0
    def __init__(self):
        self.no1=20
        self.no2=10
    def add(self):
        ans=self.no1+self.no2
        print(ans)

def main():
   obj= Math()
   obj.add()
if __name__=="__main__":
    main()"""

#5
"""
class Math:
    no1=0
    ans=0
    def __init__(self,no1):
        self.no1=no1
    def factorial(self):
        mul=1
        for i in range(1,self.no1+1):
            mul=mul*i
        print("factorial=",mul)
def main():
    no=int(input("enter no="))
    obj=Math(no)
    obj.factorial()
if __name__=="__main__":
    main()"""

#6
"""
class Math:

    def __init__(self):
        print("indide constructor")

def main():
    obj=Math()
    o2=Math()
if __name__=="__main__":
    main()"""


#7
"""
class Math:
    no1=0
    ans=0
    def __init__(self,no1):
        self.no1=no1
    def factorial(self):
        mul=1
        for i in range(1,self.no1+1):
            mul=mul*i
        print("factorial=",mul)
def main():
    no=int(input("enter no="))
    obj=Math(no)
    obj.factorial()
    
    no=int(input("enter no="))
    obj1=Math(no)
    obj1.factorial()
if __name__=="__main__":
    main()"""

#8
"""
class Math:
    def factorial(no):
        mul = 1
        for i in range(1, no + 1):
            mul = mul * i
        print("factorial=", mul)

def main():
    no=int(input("enter no="))
    obj=Math
    obj.factorial(no)
    obj.factorial(no+1)
    obj.factorial(no+2)

if __name__ == "__main__":
    main()"""

#9
"""
class Lis1:
    l1=0
    def __init__(self,size):
        self.size=size
        self.l1=[]
    def creat_lis(self):
        for i in range(self.size):
            self.l1.append(int(input("enter element=")))
        print(self.l1)
    # def  delete_ele(self):
    #     self.l1.pop(3) #index is 3
    #     print(self.l1)

    def sort_list(self):
        for i in range(0,len(self.l1)-1):
            for j in range(i+1,len(self.l1)-1):
                if self.l1[i]<self.l1[j]:
                    self.l1[i]=self.l1[j]
        print(self.l1)



def main():
    size = int(input("enter no="))
    obj=Lis1(size)
    obj.creat_lis()
    #obj.delete_ele()
    obj.sort_list()


if __name__ == "__main__":
    main()"""

#10
"""
class City:
    a=0
    b=0
    def __init__(self,a,b):
        self.A= a
        self.B= b
    def  concat(self):
        print(self.A)
        print(self.B)

class vehical:
    pass
def main():
    obj=City("nashik","pune")
    obj.concat()
    obj1=vehical
if __name__ == "__main__":
    main()"""

#11
"""
class vehical:
    pass
def main():
    obj1=vehical
if __name__ == "__main__":
    main()"""

#12
"""
class vehical:
    @classmethod
    def add(cls):
        a=20
        b=30
        ans=a+b
        print(ans)
class bus(vehical):
    pass

def main():
    obj1=bus
    obj1.add()
    obj1.multi()
if __name__ == "__main__":
    main()"""

#13#calss-instance-static
"""
class  family:
    ans=100
    #instancemethpd
    def  __init__(self):
        self.a=10
        self.b=20
    def mom(self):
        print(self.a+self.b)

    @staticmethod
    def son(m,n):
        print(m*n)

def main():
    obj=family()
    print(obj.ans)
    obj.mom()
   # family.father()
    obj.son(5,4)

if __name__ == "__main__":
    main()"""

#setter
"""
class Math:

    def __init__(self):
        self.no1=10
    def factorial(self):
        self.no1=15
        print(self.no1*2)
    def add(self):
        a=self.no1
        print(5+self.no1)
def main():
    obj=Math()
    obj.factorial()
    obj.add()

if __name__ == "__main__":
    main()"""

#default super()
"""
class base:
    a=0
    b=0
    c=50
    def __init__(self):
        self.A= "a"
        self.B= "b"
    def  concat1(self):
        print("inside the class constructor")
        print(self.B)

class derived(base):
    def __init__(self,c,d):
        super().__init__()
        self.C=c
        self.D=d
        print("this is base class c",super().c)

    def  concat2(self):
        super().concat1()
        print("inside the derived class constructor")
        print(self.D)
def main():
    obj=derived("mubai","nagar")
    obj.concat2()
if __name__ == "__main__":
    main()"""

#:parameter super()
"""
class base:
    a=0
    b=0
    c=50
    def __init__(self,a,b):
        self.A= a
        self.B= b
    def  concat1(self):
        print("inside the class constructor")
        print(self.B)

class derived(base):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.C=c
        self.D=d
        print("this is base class c",super().c)

    def  concat2(self):
        super().concat1()
        print("inside the derived class constructor")
        print(self.D)
def main():
    obj=derived("mubai","nagar","nashik","pune")
    obj.concat2()
if __name__ == "__main__":
    main()"""


#nested -inner class
#1
"""
class base:
    def __init__(self):
        self.name= "pooja"
        self.no= 12345
        self.in_obj=self.inner()   #obj of inner class
        self.in_obj.subjects()   #calling inner class method
    def student(self):
        print(self.name,"and",self.no)

    class inner:
        def __init__(self):
            self.sub = "math"
            self.marks = 100
        def subjects(self):
            print(self.sub,"and",self.marks)
def main():
    obj=base()
    obj.student()
    # obj.in_obj.subjects()
if __name__ == "__main__":
    main()"""

#2
"""
class base:
    def __init__(self):
        self.name= "pooja"
        self.no= 9876543321
        self.in_obj=self.inner()   #obj of inner class
    def student(self):
        print(self.name,"and",self.no)

    class inner:
        def __init__(self):
            self.sub = "math"
            self.marks = 100
        def subjects(self):
            print(self.sub,"and",self.marks)
def main():
    obj1=base()
   # print(obj1.name)
    obj1.student()
    # print(obj1.in_obj.sub)
    # print(obj1.in_obj.marks)
    a=obj1.in_obj
    print(a.sub)
    print(a.marks)
    # 
    # obj2=base().inner()
if __name__ == "__main__":
    main()"""

#3
"""
class base:
    def __init__(self):
        self.name= "pooja"
        self.no= 9876554321
        self.in_obj=self.inner()   #obj of inner class
    def student(self):
        print(self.name,"and",self.no)

    class inner:
        def __init__(self):
            self.sub = "math"
            self.marks = 100
        def subjects(self):
            print(self.sub,"and",self.marks)
def main():
    obj1=base()
    obj1.student()
    obj2=base().inner()
    obj2.subjects()
if __name__ == "__main__":
    main()"""




#------acessspecifier----
#public veriable
"""
class base:
    a=10
    
class derived(base):
    def add():
        print(base.a)
        
def main():
    obj=derived
    obj.add()

if __name__ == "__main__":
    main()"""

#protected  veriable(_)
"""
class base:
    _a = 1
class derived(base):
    print("nacho")

class derived1(base,derived):
    def add1():
        print(base._a)


def main():
    obj = derived1
    obj.add1()


if __name__ == "__main__":
    main()"""


#private veriable()
"""
class base:
    __a = 1
    def add():
        print(base.__a)
class sub:
    def subt():
def main():
    obj = base
    obj.add()
    
if __name__ == "__main__":
    main()"""

#protected method(_)
#can aceesss in child classes
"""
class derived():
    _name=None   ##--proted veriable
    _roll=None
    _branch=None

    def  __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch
    def _student1(self):   ###--proted method
        print(self._name)
        print(self._roll)

class derived1(derived):
    def  __init__(self,name,roll,branch):
        derived.__init__(self, name, roll, branch)
    def student2(self):
        print(self._branch)
        self._student1()   ###--calling proteced mthod

class derived2(derived1):
    def  __init__(self,name,roll,branch):
        derived.__init__(self, name, roll, branch)
    def student3(self):
        print(self._branch)
        self._student1()

def main():
    obj = derived2("puja",21,"ETC")
    obj.student3()

if __name__ == "__main__":
    main()"""

#------abstraction----
"""
from abc import ABC,abstractmethod
class game(ABC):
    @abstractmethod
    def score(self):
        pass

class cricte(game):
    def score(self):
        print("20/100")

class basketball(game):
    def score(self):
        print("25/100")

class foottball(game):
    def score(self):
        print("35/100")


def main():
    obj1=cricte()
    obj1.score()

    obj2=basketball()
    obj2.score()

    obj3=foottball()
    obj3.score()


if __name__ == "__main__":
    main()"""

#2
"""
from abc import ABC ,abstractmethod
class hospital(ABC):
    def name(self):
        print("Pravas Hospital")
    @abstractmethod
    def petiant(self):
        pass

class corona(hospital):
    def petiant(self):
        print("5 petiatnt")

class maleria(hospital):
    def petiant(self):
        print("6 petiatnt")


class dengo(hospital):
    def petiant(self):
        print("7 petiatnt")

def main():
    obj1=corona()
    obj1.name()
    obj1.petiant()

    obj2=maleria()
    obj2.petiant()

    obj3=dengo()
    obj3.petiant()


if __name__ == "__main__":
    main()"""

#polymorphism
"""
class maleria:
    def petiant(self,a,b):  #error
        print("6 petiatnt",a*a)


class dengo(maleria):
    def petiant(self,a):
        print("7 petiatnt",a+a)
        
class corona(dengo):
    def petiant(self,a):
        print("5 petiatnt=",a+a+a)
        

def main():

    obj2=corona()
    obj2.petiant(12)
    obj2.petiant(13)


if __name__ == "__main__":
    main()"""


#2
"""
class base:
    def digit1(self,no):
        print("inside base class")
        cnt=0
        while no!=0:
            r=no%10
            cnt=cnt+1
            no=no//10
        print(cnt)


class derived(base):
    def digit1(self, no):
        print("inside derived class")
        cnt = 0
        while no != 0:
            r = no % 10
            cnt = cnt + 1
            no = no // 10
        print(cnt)


def main():
    obj=derived()
    obj.digit1(12345)


if __name__ == "__main__":
    main()"""

#private
"""
class base:
    def __init__(self):
        pass
    def __digit1(self):
        print("inside base class")
    def mn(self):
        self.__digit1()

# class derived(base):
#     def __init__(self):
#         base.__init__(self)
#     def xyz(self):
#         self.mn()

def main():
    obj=base()
    obj.mn()


if __name__ == "__main__":
    main()"""


#
"""
class base:
    def __init__(self,x=10,y=204):
        self.a=x
        self.b=y
    def digit1(self):
        print("inside base class")
        print(self.a,self.b)

def main():
    obj=base()
    obj.digit1()


if __name__ == "__main__":
    main()"""
