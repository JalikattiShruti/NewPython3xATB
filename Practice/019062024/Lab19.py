numbers = [1, 2,3,4]


def do_something(numbers):
    numbers.append(5)
   # numbers[2] = 20
    numbers[0:2] = 10,20

    return numbers
print(numbers)


# l = do_something(numbers)
# print(l)