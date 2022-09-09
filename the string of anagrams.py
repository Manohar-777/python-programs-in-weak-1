def check(s, t):
     
    # the sorted strings are checked
    if(sorted(s)== sorted(t)):
        print("The strings of anagrams is true.")
    else:
        print("The strings of anagrams is false.")        
         
# driver code 
s ="bobby"
t ="killer"
check(s, t)
