def add(a,b):
    try:
        return int(a)+ int(b)
    except ValueError:
        return "Enter valid Numeric value"

                    
    
def substraction(a,b):
    try:
        return int(a)- int(b)
    except ValueError:
        return "Enter valid Numeric value"
    


x= input(" enter first Number")
y= input(" enter second Number")

print(add(x,y))
