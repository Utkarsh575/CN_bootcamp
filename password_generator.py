from numpy import *
import numpy as np

def enter_word():
    for a in range(0,5):
        k=input("enter a words:- ")
        x.insert(a,k)
       
    
def pass_gen():
    l= int(input("enter the length of password:- "))
    n=""
    for k in range(0,l):
        rand_choice=random.choice(y)
        n=n+rand_choice
    print("The generated password is :- ",n)

def seperator():
    for a in range(0,len(x)):
        for ch in x[a]:
            y.append(ch)

x=[]
y=[]

while(True):
    print("""
   |\---/|
   | ,_, |          Welcome to
    \_`_/-..----.
 ___/ `   ' ,""+ \  MEOW PASSWORD GENERATOR  by:- utkarsh575
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
    """)

    print("""
    1) ENTER WORDS
    2) EXIT
    """)

    c=int(input("CHOOSE AND OPTION :-"))

    if c==1:
        enter_word()
        seperator()
        pass_gen()
        break

    elif c==2:
        print("BYE HAVE A GREAT TIME >_< ")
        break
    else:
        print("I CAN NOT COMPREHEND YOUR INVALID INPUTS TRY AGAIN ;< ")

    




        








