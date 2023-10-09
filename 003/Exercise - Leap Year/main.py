year = int(input())
if year % 4:
    print('Not leap year')
elif year % 400 == 0:
    print('Leap year')
elif year % 100 == 0:
    print('Not leap year')
else:
    print('Leap year')
