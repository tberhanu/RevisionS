""" 6. Sort an array of dicts based on the first_name or last_name
"""

arr_dicts = [{"fname": "John", "lname": "James", "id": 123},
            {"fname": "Mary", "lname": "Ahemsu", "id": 678},
            {"fname": "Helen", "lname": "ZGetachew", "id": 344}]

arr2 = sorted(arr_dicts, key=lambda dict: dict["fname"])
print(arr2)
print(sorted(arr_dicts, key=lambda dict: dict["lname"]))
print(sorted(arr_dicts, key=lambda dict: dict["id"]))
