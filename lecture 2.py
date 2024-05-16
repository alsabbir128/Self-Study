#nam1 = input("movie 1: ")
#nam2 = input("movie 2: ")
#nam3 = input("movie 3: ")

#list = [nam1,nam2,nam3]
#print(list)

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list2.copy()
copy_list1.reverse()

if(copy_list1 == list2):
    print("palindrome")
else:
    print("not palidrome")