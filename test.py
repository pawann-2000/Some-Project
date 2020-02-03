# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    for val in user1.values():
        if(val == True):
            return True
        else:
            return False


@authenticated
def message_friends(user1):
    print('message has been sent')


message_friends(user1)
