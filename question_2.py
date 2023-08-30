
#Write a function that takes in two lists and returns the two lists merged together and sorted.  Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]


# print(sorted(l_3))

def merge_sort(l_1, l_2):
    l_3 = l_1 + l_2
    l_3.sort()
    return l_3
print(merge_sort(l_1, l_2))
    
