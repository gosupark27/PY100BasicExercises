# Rewrite car as a list of lists in which each nested list contains two elements that represent the corresponding key/value pairs.
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}
car = [list(element) for element in car.items()]
print(car)