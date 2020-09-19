print('hello world')
#This is comment

a = "apple"
b = 2
c = 3
d = pow(c, b)
e = d+1
#print(float(e))
#print((a[3]))

#tuple
f = (b, c, d)  #tuple-immutable
#print(type(f))
g = f[1]
#print(g)
f = range(1, 3)
g = tuple(f)
#print(g)
h = range(10, 1, -1)
#print(h)

#array
i = [3,4,7] +["5,4"] # only lists with num and str can concat together not tuples
#print(i)

#slices:sequence[start:stop:step]
j = "Hello World"
k = j[:5]
#print(k)
k = j[4:11]
#print(k)
k = j[4:-3]
#print(k)
k = j[::-1]
#print(k)

#dict
l = {"a": 1, "b": 2}
m = l["a"]
#print(m)
n = dict([["a", 1], ["b", 2]])
#print(n)

#compare
#print((1, 2) == (1, 2))
a = 'hello'
b = 'hello'
#print (a != b)

#in
#print(1 in (1, 2))
#print(range(3))
#print("hello" in "Hello World")

#conditionals
if True:
  print("here")
else:
  print("there")


#for loop
# for i in range(10):
#   print (i)

#for maintaining index count use enumerate
# for i, v in enumerate([1, 2, 3, 4, 5]):
#   print(i, v)

#list comprehension
#new_list = [express for < item > in < sequence > ]
double = [x * 3 for x in range(4)]
#this shd give [0,3,6,9]
#print(double)
upper = [c.upper() for c in "Hello"]
#print("".join(upper))

#fnx:
def add(x, y):
  return x + y
print(add(1, 3))
print(add("hello"," world"))
















