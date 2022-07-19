x = float(input('First number: '))
y = float(input('Second number: '))
znak = input('Operation: ')
result = 0
if znak == '+':
    result = x + y
elif znak == '-':
    result = x - y
elif znak == '*':
    result = x * y
elif znak == '/':
    result = x / y
else:
    print('Unsupported operation')
if result is not 0:
    print('Result:', result)
