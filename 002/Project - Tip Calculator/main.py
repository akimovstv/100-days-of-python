print('Welcome to the tip calculator.')
total = float(input('\nWhat was the total bill?\n$'))
tip = int(input('\nWhat percentage tip would you like to give (10, 12, or 15)?\n'))
people = int(input('\nHow many people to split the bill?\n'))
total_with_tip = total + tip / 100 * total
each_to_pay = round(total_with_tip / people, 2)
print(f'\nEach person should pay: ${each_to_pay:.2f}')
