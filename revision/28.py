""" 28. Read Entire File i) as a string ii) line by line
    Write on a file by overwriting, write on a non existed file
"""
# Reading the entire file as a string
with open("file.txt", 'rt') as f:
    data = f.read()

# Reading the file line by line
with open("file.txt", 'rt') as f:
    for line in f:
        line.read()
text2 = '''adjflasdflaksd;nf.....'''
# Writing on a file by overwriting
with open("file.txt", "wt") as f:
    f.write("hello\n")
    f.write(text2)

# Writing only on files that doesn't exist
with open("file.txt", "xt") as f:
    f.write(text2)
