num1 = int(input("enter frist number : "))
num2 = int(input("enter second number : "))
ch = input("enter any operator(+,-,*,/): ")
result = 0
if ch == '+':
    result = num1+num2
    print("addtion is",result)
elif ch == '-':
    result = num1-num2
    print("substraction is",result)
elif ch == '*':
    result = num1*num2
    print("multiplication is",result)
elif ch == '/':
    result = num1/num2
    print("divison is",result)
else:
    print("input character is not recoquized!")

