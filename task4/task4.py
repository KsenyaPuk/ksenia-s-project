import sys

file_name = sys.argv[1]

with open(file_name, 'r') as f:
    numbers = []
    for line in f.readlines():
        numbers.append(int(line))

numbers.sort()
count = len(numbers)

index = count // 2
if count % 2 != 0: # если нечетное берем значение в отсортированном списке по середине
    median = numbers[index]
else:
    median = numbers[index - 1]

counter = 0
for num in numbers:
    counter += abs(num - median)

print(counter)