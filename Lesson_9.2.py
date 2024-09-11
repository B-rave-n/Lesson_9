def difference(*args):
    if len(args) > 0:
        return round(max(args) - min(args), 2)
    else:
        return 0


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
assert difference(15.24, -2.2, -4.55, 0, 1.1, 0.5) == 19.79, 'Test4'
assert difference(5, 5) == 0, 'Test5'
assert difference(-3) == 0, 'Test6'
print('OK')