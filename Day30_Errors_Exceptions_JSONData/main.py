#FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = { "key": "value" }
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")
except KeyError as err_msg:
    print(f"The key {err_msg} does not exist.")
else:
     content = file.read()
     print(content)
finally:
    raise KeyError

#KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

#Raise exception
# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

