# Puppy Latin Rules:
# If a puppy name does not end in a 'y' add on a 'y' to the name
# Rufus -> Rufusy |  Spot -> Spoty
# If a puppy name does end in a 'y', replace it with 'iful' instead
# Sparky -> Sarkiful | Spoty -> Spotiful



def latinizer(name):
    last_y = 'y'
    iful = 'iful'
    if name[-1] != last_y:
        # print(name+last_y)
        return f'hi {name}, Your puppylatin name is {name+last_y}.'
    elif name[-1] != 'iful':
        # print(name[:-1]+iful)
        return f'hi {name}, Your puppylatin name is {name[:-1]+iful}.'

# latinizer('rufusy')