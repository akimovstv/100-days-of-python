print('The Love Calculator is calculating your score...')
name1 = input()  # What is your name?
name2 = input()  # What is their name?

combined = (name1 + name2).upper()
true = combined.count('T') + combined.count('R') + combined.count('U') + combined.count('E')
love = combined.count('L') + combined.count('O') + combined.count('V') + combined.count('E')
true_love = int(f'{true}{love}')
if true_love < 10 or true_love > 90:
    print(f'Your score is {true_love}, you go together like coke and mentos.')
elif 40 < true_love < 50:
    print(f'Your score is {true_love}, you are alright together.')
else:
    print(f'Your score is {true_love}.')
