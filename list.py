numbers=[3, 5, 7, 9, 10.5]
print(numbers)
numbers.append('Python')
print(numbers, f'Длина списка: {len(numbers)}')
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
del numbers[-1]
print(numbers)