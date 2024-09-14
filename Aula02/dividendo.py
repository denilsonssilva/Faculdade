def quociente (x,y):
    return x / y

x = int(input('Dividendo? '))

while true:
    y = int(input('Divisor? '))
    if y != 0: break

print(f'{x} / {y} = {quociente(x,y)}')