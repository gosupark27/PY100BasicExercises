# Without looking at your notes or the official documentation, try to recall all values that count as falsy in Python.


falsy_values = [None, False, [], '', {}, 0, ()] # set(), range(0), 0.0, 0j
for el in falsy_values:
    print(bool(el))
