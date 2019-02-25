""" 15. Check if string starts/ends with certain symbols
    Replace or substitute sth in the middle of the statement

"""
string = "#starts with the hash!"
print(string.startswith("#"))
print(string.startswith("#s"))
print(string.endswith("!"))
print(string.endswith("hash!"))
print(string.endswith("@"))
print(string.startswith("###"))
print(string.startswith("hash"))

statement = "Here we go! We just ---- OLD OLD OLD ----- started the game!"
print(statement.replace("OLD", "NEW"))
