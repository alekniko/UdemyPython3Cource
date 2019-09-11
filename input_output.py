file = open('C:\\Users\\nikomale\\Documents\\PythonTMP\\files\\input_output.txt')
file.read()
print(file.read())
file.seek(0)
print(file.readlines())
print("\n=============================\n")
file.seek(0)
print(file.read())
file.close()  # Do not forget to close files
print("\n=============================\n")

#   mode = 'r' - only read the file
#   mode = 'w' - only write in the file (it will overwrite all existing in file with new values)
#   mode = 'a' - append the file with new values
#   mode = 'r+' - read and write
#   mode = 'w+' - write and read (overwrites file or creats a new file)

with open('C:\\Users\\nikomale\\Documents\\PythonTMP\\files\\input_output.txt', mode='a', ) as file:
    file.write("\nHello")

with open('C:\\Users\\nikomale\\Documents\\PythonTMP\\files\\input_output.txt', mode='r', ) as file:
    contentOfTheFile = file.read()
    print(contentOfTheFile)

with open('C:\\Users\\nikomale\\Documents\\PythonTMP\\files\\new_file.txt', mode='w', ) as file:
    file.write("I created a new file using python script")

with open('C:\\Users\\nikomale\\Documents\\PythonTMP\\files\\new_file.txt', mode='r', ) as file:
    content = file.read()
    print(content)
