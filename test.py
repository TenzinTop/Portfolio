n= int(input())

if (n%2)==0 and n>=2 and n<=5:
    print("Not Weird")
elif (n%2)==0 and n>=6 and n<=20:
    print("Weird")
elif (n%2)==0 and n>20:
    print("Not Weird")
elif (n%2)!=0:
    print("Weird")        


    a = int(input())
    b = int(input())
    total=0

def add():
    total=a+b
    print(total)

def diff():
    total=a-b
    print(total)

def prof():
   total= a*b
    print(total)

add()
diff()
prof()   
