# ** calculator**
import random
for i in range (100):
    x=random.randrange(000,999)
    print(" your otp ", x)
    choice=eval(input(" press 1️⃣ for addition, press 2️⃣ subtraction ,press 3️⃣ for subtraction , press 4️⃣ for divison , press 5️⃣ for exit " ))
    user_otp=eval(input(" enter otp"))
    
    if user_otp==x:
        print(" verified successfully")
        if choice==1:
          print(" enter two number for addition")
          a=eval(input())
          b=eval(input())
          print(" sum  of two number = ",a+b)
        elif choice==2:
            print(" enter two number for subtraction")
            c=eval(input())
            d=eval(input())
            print(" subtraction   of two number = ",c-d)
        elif choice==3:
             print(" enter two number for multiplication")
             e=eval(input())
             f=eval(input())
             print(" multiplication of two number = ",e*f)
        elif choice==4:
            print(" enter two number for divison")
            g=eval(input())
            h=eval(input())
            if h!=0:
             print(" multiplication of two number = ",g%h)
            else:
                print(" h does not equals to zero")
        elif choice==5:
            print(" EXIT")
        else:
            print(" invalid input ❌")
    else:
        print(" invalid otp ❌")

