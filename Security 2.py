floor = input('Enter the floor')

floor = list(floor)

for person in floor:

    if (person == '$'):
        x = person

    elif (person == 'G'):
        y = person

    elif (person == 'T'):
        z = person

good_condition = ['$', 'G', 'T']
nice = [x, y, z]
true = [([int(item1 == item2) for item2 in nice], [
    n for n, item2 in enumerate(nice) if item1 == item2]) for item1 in good_condition]

print(bool(true))

# if (good_condition == nice):
#     print('Silent')

# else:
#     print('ALARM!')
