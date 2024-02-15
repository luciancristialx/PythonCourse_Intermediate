#Exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:
squared_numbers = [n*n for n in numbers]
# Write your code 👆 above:

#print(f"Exercise 1 result: {squared_numbers}\n")


#Exercise 2
list_of_strings = "1, 1, 2, 3, 5, 8, 13, 21, 34, 55".split(',')
# 🚨 Do  not change the code above

#Use list comprehension to convert the strings to integers 👇:
convert = [int(x) for x in list_of_strings]

#Use list comprehension to filter out the odd numbers and store the even numbers in a list called "result"

result = [n for n in convert if n%2==0]
# Write your code 👆 above:
#print(f"Exercise 2 result: {result}")

#Exercise 3
with open("file1.txt",'r') as f1:
    list1 = f1.readlines()
with open("file2.txt",'r') as f2:
    list2 = f2.readlines()

num_f1 = [int(x) for x in list1]
num_f2 = [int(x) for x in list2]

matching_numbers_result = [x for x in num_f1 if x in num_f2]
print(matching_numbers_result)
