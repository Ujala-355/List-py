num1 = int(input("enter"))
num2 = int(input("enter"))
a = num1
b = num2
while num2!=0:   
    temp = num2
    num2 = num1 % num2  
    num1 = temp
c= num1  
lcm = (a * b) //c
print(lcm)