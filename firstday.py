import string

sum = 0
for i in range(1, 11):
    sum += i
print("The sum of the first 100 natural numbers is:", sum)

print('*' * 20)

for i in string.ascii_uppercase:
    print(i)

print('*' * 20)

for i in string.digits:
    print(i)

print('*' * 20)

for i in string.ascii_letters:
    print(i)

print('*' * 20)

for i in string.hexdigits:
    print(i)

print('*' * 20)

for i in string.punctuation:
    print(i)

print('*' * 20)

for i in string.printable:
    print(i)

print('*' * 20)

for i in range(255):
    print(i, ' : ', chr(i))

print('\n' + '*' * 20)