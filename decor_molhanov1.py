from datetime import datetime

#Декораторы

def timeit(arg):
    print(arg)
    def outher(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outher

@timeit('Да идите вы name')
def one(n):
    l = []
    for x in range(n):
        l.append(x)
    return l

@timeit('Идите name')
def two(n):
    l = [x for x in range(n)]
    return l

l1 = one(10000)
l2 = two(10000)

print(l1)
print(l2)
