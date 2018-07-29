"""Background
It is the middle of the night.

You are jet-lagged from your long cartesian plane trip, and find yourself in a rental car
office in an unfamiliar city.

You have no idea how to get to your hotel.

Oh, and it's raining.

Could you be any more miserable?

But the friendly rental-car dude behind the desk says not to worry! He kindly pre-programs
the car Sat Nav system with your destination. He smiles and assures you that the device
works OK. What excellent service! What a nice man!

Maybe things are not so bad after all.

Then he sniggers...

City streets
The city extends as far as the eye can see in all directions, and is laid out as a giant
grid where all blocks are 1km across.

Notice that [x,y] coordinates are described with units of 100m

satnav city streets

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


def set_orientation(action: str, ordinal=None):
    compass = {'NORTH': 1, 'EAST': 2, 'SOUTH': 3, 'WEST': 4}
    turns = {'straight': 0, 'LEFT': -1, 'RIGHT': 1, 'Turn around': -2}
    if ordinal is None:
        for k, i in compass.items():
            if k in action:
                return i
    else:
        for k, i in turns.items():
            if k in action:
                ordinal += i
                if ordinal < 1:
                    ordinal += 4
                elif ordinal > 4:
                    ordinal -= 4
                return ordinal
    return ordinal


def set_distance(action):
    km_regex = re.compile(r'\d+.\d+km')
    m_regex = re.compile(r'\d+m')
    blocks = {'NEXT': 1000, '2nd': 2000, '3rd': 3000, '4th': 4000, '5th': 5000,
              '6th': 6000, '7th': 7000, '8th': 8000, '9th': 9000}

    for block in blocks:
        if block in action:
            return blocks[block]
    if km_regex.search(action):
        m = km_regex.search(action)
        return int(float(m.group(0).rstrip('km')) * 1000)
    if m_regex.search(action):
        m = m_regex.search(action)
        return int(m.group(0).rstrip('m'))


def move_car(loc, dist, direction):
    rev_compass = {1: 'NORTH', 2: 'EAST', 3: 'SOUTH', 4: 'WEST'}
    x, y = loc

    if direction in [3, 4]:
        dist *= -1

    if direction in [2, 4]:  # E ast or West
        x += dist / 100

    if direction in [1, 3]:  # North or South
        y += dist / 100

    return x, y


def sat_nav(directions):
    x, y = 0, 0
    location = x, y
    ordinal = set_orientation(directions[0])
    # rev_compass = {1: 'NORTH', 2: 'EAST', 3: 'SOUTH', 4: 'NORTH'}
    for action in directions:
        # print(action)
        distance = set_distance(action)
        if distance:
            location = move_car(location, distance, ordinal)
        # print(distance, rev_compass[ordinal], location)
        ordinal = set_orientation(action, ordinal)
    return location


directions = [
    'Head EAST',
    'Take the 2nd LEFT',
    'Take the NEXT LEFT',
    'Take the NEXT LEFT',
    'Go straight on for 1.5km',
    'Take the NEXT RIGHT',
    'Take the 2nd RIGHT',
    'Go straight on for 1.7km',
    'Turn around!',
    'Take the NEXT LEFT',
    'Go straight on for 1.0km',
    'You have reached your destination!']

print(sat_nav(directions))
directions = [
    'Head NORTH',
    'Take the 2nd LEFT',
    'Take the 2nd LEFT',
    'Take the NEXT LEFT',
    'Go straight on for 3.5km',
    'Take the NEXT RIGHT',
    'Go straight on for 2.3km',
    'Take the NEXT RIGHT',
    'Take the NEXT RIGHT',
    'Take the NEXT LEFT',
    'Take the NEXT RIGHT',
    'Go straight on for 900m',
    'You have reached your destination!'
]
sat_nav(directions)
