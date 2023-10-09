print('Welcome to the Enchanted Forest.')
print('Your mission is to uncover its secrets.')

choice_1 = input(
    'You find yourself at a crossroads deep in the forest. Where do you want to go? Type "left" or "right"\n'
).lower()

if choice_1 == 'left':
    choice_2 = input(
        'You come across a dark, ancient grove. There is a hidden path leading further in. '
        'Type "explore" to venture deeper. Type "continue" to stay on the main path.\n'
    ).lower()
    if choice_2 == 'explore':
        choice_3 = input(
            'As you venture deeper into the grove, you find a peculiar stone altar. It has three mysterious symbols '
            'carved into it: a sun, a moon, and a star. Which symbol do you choose to touch? \n'
        ).lower()
        if choice_3 == 'sun':
            print('You are bathed in a warm, golden light. A hidden treasure is revealed! You Win!')
        elif choice_3 == 'moon':
            print('The forest becomes shrouded in darkness, and you get lost. Game Over.')
        elif choice_3 == 'star':
            print('You hear a faint, otherworldly melody. The forest reveals its secrets to you! You Win!')
        else:
            print("You chose a symbol that doesn't exist. Game Over.")
    elif choice_2 == 'continue':
        print('You continue on the main path and encounter a mystical creature. It offers you guidance.')
        choice4 = input('The creature leads you to a magical pool. Drink from it? Type "yes" or "no"\n').lower()
        if choice4 == 'yes':
            print('You are granted the power to understand the forest\'s language. You Win!')
        else:
            print('You decline the drink and wander deeper into the forest, eventually getting lost. Game Over.')
    else:
        print('Invalid choice. Game Over.')
elif choice_1 == 'right':
    choice5 = input(
        'You decide to take the right path, which leads to a deep ravine. There is a narrow bridge across the ravine. '
        'Cross the bridge or turn back? Type "cross" or "turn back" \n'
    ).lower()
    if choice5 == 'cross':
        print(
            'You carefully cross the bridge and find a hidden glade on the other side. '
            'You discover a rare and valuable plant! You Win!'
        )
    elif choice5 == 'turn back':
        print('You decide to turn back, but while retracing your steps, you get lost in the forest. Game Over.')
    else:
        print('Invalid choice. Game Over.')
else:
    print("You chose a path that doesn't exist. Game Over.")
