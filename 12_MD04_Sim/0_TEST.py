boxes = [5, 8, 6, 10, 7] # consider it as boxes

current = 7

higher = [box for box in boxes if box < current]
print(higher)

print(max(higher, key=lambda b: b))
