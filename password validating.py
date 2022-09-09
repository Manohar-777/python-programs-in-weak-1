import re
p= input("Input your Username : ")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[_]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Username")
        x=False
        break

if x:
    print("Not a Valid Username")
