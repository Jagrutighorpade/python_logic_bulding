#----dict comp---
#1
"""
def main():
    l1=["ny",'fl','ca','vt']
    d1={l1[i]:l1[i+1] for i in range(len(l1)-1)}
    #={i:i for i in l1}
    print(d1)
if __name__=="__main__":
    main()"""

#2
"""
def main():
    d1={i:(i/100) for i in range(100,160,10)}
    print(d1)
if __name__=="__main__":
    main()"""

#3

def main():
    d1={"abvc":1234 , "baghs":4567, "cjhg":1876, "jggj":8764}
    d2={key:val for key ,val in d1.items() if val>2000 }
    print(d2)

if __name__=="__main__":
    main()