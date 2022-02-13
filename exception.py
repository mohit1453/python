n=int(input())
for i in range(n):
    try:
        a=int(input())
        b=int(input())
        print(int(a/b))
        
    except ZeroDivisionError as ex:
        print("Error Code: integer division or modulo by zero")
    except Exception as e:
        print("Error Code:",e)
         
       
