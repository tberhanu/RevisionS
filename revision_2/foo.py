statement = "here is the example hereonennnnnn"
print(statement.index("is"))
lst = statement.split()
print(max(lst, key=len))
print(max(lst, key=lambda a: min(a)))
print(max(lst, key=min))

print(statement.index("here"))
print(statement.rindex('here'))