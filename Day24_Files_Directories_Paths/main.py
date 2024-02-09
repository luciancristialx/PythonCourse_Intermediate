# txt_file = open("my_file.txt")
#
# file_content = txt_file.read()
# print(file_content)
#
# txt_file.close()

#Read file
# with open("my_file.txt") as txt_file:
#     file_content = txt_file.read()
#     print(file_content)

#mode = r (read), w (write), a (append)
with open("new_file.txt",mode = "w") as txt_file:
    txt_file.write("New text.")



