from collections import namedtuple

City = namedtuple('City','name country populations coordinates')
tokio = City('Tokio','JP',36.933,(35.67899, 139.9876))

Cards = namedtuple('Card','name mast score')
card = Cards('Dama','diamonds',12)

tup = (1,2,3,4,4,5,6,7,8,9)
x = tup.__iter__()
for i in x:
    print(i)

for i in tup:
    print('cicle',i)
c = tup.__len__()
print(c)
print(len(tup))

lis1 = [1,4,3,2,4,24,6,7,8,0]
print(lis1[1:4])

DF = slice(4,50,-1)
print(DF)