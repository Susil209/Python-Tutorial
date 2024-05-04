#
# # open a file
# file = open("demofile.txt", "r")
#
# # read the file contents
# contents = file.read()
# print(contents)
#
# file.close()
#
#
# using 'with' keyword
# with open("demofile.txt", "r") as file:
#     print(file.read())
#     print(file.name)
#     print(file.mode)
#
#     read only parts of the file
#     print(file.read(10))
#
#     Read Lines
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file.readlines())
#
#     using loop
#     for line in file:
#         print(line, end='')
#
#
# print(file.close())


# write into a file
with open("demofile.txt", "a") as f:
    f.write("\nNow the file has more content!")

# create a new file
with open("demofile1.txt", "w") as f:
    f.write("This is my demo file.")