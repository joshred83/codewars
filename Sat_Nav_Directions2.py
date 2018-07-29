"""
Kata task
Your starting point is [0,0]

Simply follow the Sat Nav directions!

 When you arrive at the destination return the final coordinates.

Sat Nav directions
The device gives directions as text messages:

The first message

    Head <NORTH,EAST,SOUTH,WEST>

The en-route messages

    Take the <NEXT,2nd,3rd,4th,5th> <LEFT,RIGHT>
    Go straight on for <100,200,300,...,900>m
    Go straight on for <1.0,1.1,1.2,...,5.0>km
    Turn around!

The last message

    You have reached your destination!

NOTES

First and last messages are always present
There may be any number of en-route messages
Messages are always formatted corrrectly
A NEXT turn message means you must to proceed to the next cross-street even if you are currently at an intersection
But Turn around does not need to be done at an intersection. Just do a U-turn wherever you are!
"""
import re
import math

def proc_start(action):
    compass = {'NORTH': 1, 'EAST': 2, 'SOUTH': 3, 'WEST': 4}
    for i in compass:
        if i in action:
            return compass[i]

def proc_route(loc, ordinal, action):
    if 'Take the' in action:
        loc, ordinal = turn_action(loc, ordinal, action)

    elif 'Go straight' in action:

        distance = extract_cartesian_distance(action)
        loc = update_loc_by_cartesian_int(distance, loc, ordinal)

    elif action == 'Turn around!':
        ordinal = change_direction(-2, ordinal)

    return (loc, ordinal)


def update_loc_by_cartesian_int(distance, loc, ordinal):
    x, y = loc
    if ordinal == 1:
        y += distance
    elif ordinal == 2:
        x += distance
    elif ordinal == 3:
        y -= distance
    elif ordinal == 4:
        x -= distance

    return (x, y)


def extract_cartesian_distance(action):
    meters_re = re.compile(r'\d+m')
    kilom_re = re.compile(r'\d.\dkm')
    meters = None
    kilom = None
    if meters_re.search(action):
        meters_match = meters_re.search(action)
        meters = meters_match.group(0).rstrip('m')
    elif kilom_re.search(action):
        kilom_match = kilom_re.search(action)
        kilom = kilom_match.group(0).rstrip('km')
    if meters:
        return int(meters) / 100
    elif kilom:
        kilom = float(kilom) * 10
        return int(kilom)


def turn_action(loc, ordinal, action):
    blocks = extract_blocks(action)
    turn_direction = extract_turn(action)

    loc = update_loc_by_blocks(loc, ordinal, blocks)

    ordinal = change_direction(turn_direction, ordinal)
    return loc, ordinal


def update_loc_by_blocks(loc: tuple, ordinal: int, blocks: int) -> tuple:
    x, y = loc

    if ordinal in [3, 4]:  # if traveling south or west use negative distance
        blocks *= -1

    if ordinal == 1:
        blocks = blocks * 10 + y
        y = (blocks // 10) * 10

    elif ordinal == 2:
        blocks = blocks * 10 + x
        x = (blocks // 10) * 10

    elif ordinal == 3:
        blocks = blocks * 10 + y
        y = math.ceil(blocks / 10) * 10

    elif ordinal == 4:
        blocks = blocks * 10 + x
        x = math.ceil(blocks / 10) * 10

    return x, y


def fix_blocks(point, ordinal):
    if ordinal in [1, 2]:  # if traveling N or E, round upper block num
        point = math.ceil(point / 10) * 10

    elif ordinal in [3, 4]:  # if traveling S or W, round to lower block num
        if point % 10 != 0:
            point = math.floor(point / 10) * 10

    return point


def change_direction(turn, ordinal):
    ordinal += turn
    if ordinal > 4:
        ordinal -= 4
    if ordinal < 1:
        ordinal += 4
    return ordinal


def extract_turn(action):
    if "LEFT" in action:
        return -1
    elif "RIGHT" in action:
        return 1



def extract_blocks(action):
    try:
        blocks_re = re.compile(r'NEXT|\d+')
        blocks_m = blocks_re.search(action)
        blocks = blocks_m.group(0)
        if 'NEXT' in blocks:
            blocks = 1
        return int(blocks)
    except:
        debug('Method: extract_blocks ' + action)
        pass


def sat_nav(directions):
    x = 0
    y = 0
    loc = x, y
    ordinal = proc_start(directions.pop(0))
    for action in directions:
        loc, ordinal = proc_route(loc, ordinal, action)
    return loc