#Factorial of 5

def factorial(numb):
    if numb==0 or numb==1:
        return 1
    
    else:
        return numb * factorial(numb-1)
    
result=factorial(5)
print(result)   
        