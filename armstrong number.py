num=int(input("enter any number:"))
sum = 0
t= num
while t > 0:
   digit = t % 10
   sum += digit ** 3
   t //= 10
if num == sum:
   print(num,"it is an armstrong")
else:
   print(num," is not an armstrong")
