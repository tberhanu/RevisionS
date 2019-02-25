

# with open('questions.txt', 'rt') as f:
#     all_contents = f.read()
#     print(all_contents)

# with open('questions.txt', 'r') as f:
#     i = 0
#     for line in f:
#         print(line)
#         i = i + 1
#         if i == 11:
#             break

# with open('newfile.txt', 'wt') as f:
#     f.write("This line is written by overwriting if any file exist with the same name\n")
#     f.write('overwriting: Written by Tess')


with open('non_exist_file.txt', 'xt') as f:
    f.write("This line is intended to write only in a non existed file.\n")
    f.write("If tried to run this, you will get FileExistsError\n")
    f.write("Because I already run it and the file already existed")
