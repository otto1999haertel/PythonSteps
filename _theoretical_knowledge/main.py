from matrix import *
from fibonachi import *
from http_error import *



print("Hello World - First Python Script")
#This is a comment
print("Hello \nNew Line")
test = "Hello World"
print(test[0])
test = "123456789"
print(test[5]) # position 5 (included)
print(test[1:5]) # postiion 5 (excluded)

squares = [1, 4, 9, 16, 25]
for square in squares:
    print(square, end=' ')
print()  # New line

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters) 
letters[2:5] = ['C', 'D', 'E'] # replace c,d,e with C,D,E
print(letters)

a,b,c = 1,2,3
print(a,b,c)

calculate_fibonacci(10)
print()

for i in range(5):
    print(i, end=' ')
print()  # New line

squares = []
for x in range(1,10):
    squares.append(x**2)
print(squares)


# List comprehension
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix)
print_matrix(matrix)
del matrix[1][1]
print_matrix(matrix)

# Tuples
t = 12345, 54321, 'hello!'
print(t)
print(t[1])
u = t, (1, 2, 3, 4, 5)
print(u)
print(u[0][2])

# Sets - unordered collection of unique elements
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # zeigt nur einzigartige Elemente
print('orange' in basket) # True

# Set operations
a = set('abracadabra')
print(a) # unique letters in the word

# Dictionaries - key-value pairs
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
print(list(tel.keys()))
print(list(tel.values()))

print(http_error(404))
print(http_error(400))