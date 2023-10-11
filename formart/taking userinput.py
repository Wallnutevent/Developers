
a=int(input("Enter the value of First Number : "))
b=int(input("Enter the value of Second Number : "))
def Calculator(a,b):
    
    print("The Sum of two number  " , a , "+" ,b, "=",a+b  )
    print("The subtraction of two number  " , a , "+" ,b, "=",a-b  )
    print("The multiplication of two number  " , a , "+" ,b, "=",a*b  )
    print("The Division of two number  " , a , "+" ,b, "=",a/b  )

    if b != 0 :
        print("The Division of ", a ,"/", b , "=" ,a/b)
    else:
        print("Here bis zero so we can't proceed the division Operation")

Calculator(a,b)
















