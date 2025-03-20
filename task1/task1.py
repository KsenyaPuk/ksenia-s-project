import sys


n = int(sys.argv[1])
m = int(sys.argv[2])

position = 1 # текущая позиция

while True:
    print(position, end='')
    position = (position + m - 2) % n + 1 # сдвиг
    if position == 1:
        break