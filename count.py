str1 = 'abcdef'
str2 = 'abcdf'
com_str = ''.join(set(str1).intersection(str2))
print(com_str)
