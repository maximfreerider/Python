def what_list_am_i_on(actions):
    naughty_count = 0
    nice_count = 0
    for action in actions
        if naughty(action):
            naughty_count += 1
        elif nice(action):
            nice_count += 1
    return "nice" if nice_count > naughty_count else "naughty"

def naughty(action):
        return action[0] in ['b', 'f', 'k']

def nice(action):
        return action[0] in ['g', 's', 'n']