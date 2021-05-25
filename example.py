import shelve

print(dir())
# print(dir(__builtins__))

print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0]!="_":
        print(obj)

help(shelve)