#String formatting
# num = 12
# name = 'deez'
# print('My number is {} and my name is {}'.format(num, name))

#dictionary
d = {'key1':'value', 'key2':123}
print(d['key2'])

#lambda functions: no need for functions
def times2(num):
    return num*2

t = lambda num: num*2

#tuple unpacking:
x = [(1,2), (3,4), (5,6)]
for a,b in x:
    print(b) #prints 2, 4, 6