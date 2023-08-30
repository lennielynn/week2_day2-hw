
#Given a list as a parameter,write a function that returns a list of numbers that are less than ten
#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9] 


num_list = [1,11,14,5,8,9]

# for num in num_list.copy():
#    if num < 10:
#      continue
#    else:
#      num_list.remove(num)

# print(num_list)

output = [n for n in num_list if n < 10]