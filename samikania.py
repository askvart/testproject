# Замыкания

def one():
    x = ['privet','goodbay']
    def inner():
        print(x)
        print(id(x))
    return inner

o = one()
print(o())
print(dir(o))
a = o.__closure__[0].cell_contents
print(a)
print(id(a))
a.append('Новая запись')
print(o())

