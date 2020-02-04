floor = input('Enter the floor')

flag = 0
count = 0

for person in list(floor):
    if (person == '$'):
        count += 1
        flag = 1

    elif (person == 'G'):
        if (flag == 1 and count == 1):
            count += 1

    elif (person == 'T'):
        count += 1


if (flag == 1 and count == 2):
    print('.....Silent.....')

if (flag == 1 and count == 1):
    print('!!!!!!ALARM!!!!!!')
