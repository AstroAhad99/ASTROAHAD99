"""

the map() function takes takes 1 iteratble and convert into another iterable but modified.

"""

friends = ['Rolf', 'Jose', 'Randy', 'Anna']

generator = filter(lambda x:x.startswith("R"), friends)
print(next(generator))
print(next(generator))

gen_comprehen = (f for f in friends if f.startswith("R"))
print(next(gen_comprehen))
print(next(gen_comprehen))


# Now here we are going to use maps

map_gen = map(lambda x:x.lower(), friends)
print(list(map_gen))

map_compre = (f.lower() for f in friends)
print(list(map_compre))