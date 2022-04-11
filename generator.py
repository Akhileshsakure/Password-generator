import random


def Generator(length, cg):
    password_char = []
    
    # for loop to make sure all the conditions are satisfied atleast once
    for set in cg:
        c = random.choice(set)
        password_char.append(c)

    # for loop for remaining characters
    for _ in range(length-len(cg)):
        group_index = random.randint(0, len(cg)-1)
        # print(group_index)
        c = random.choice(cg[group_index])
        password_char.append(c)

    # randomly shuffles the list elements
    random.shuffle(password_char)

    return ''.join(password_char)