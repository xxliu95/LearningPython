nums = [1, 2, 3, 4, 5]

# for loop
for num in nums:
    print(num)

# break
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

# continue
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

# for in for
for num in nums:
    for letter in 'abc':
        print(num, letter)

# rango
for i in range(10):
# for i in range(1, 11):
    print(i)

# while loop
x = 0
while x < 5:
    print(x)
    x += 1

# break
while True:
    if x == 5:
        break
    print(x)
    x += 1
