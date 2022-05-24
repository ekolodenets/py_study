'''
sloganMaker(["super", "hot", "guacamole"]);
//[ 'super hot guacamole',
//  'super guacamole hot',
//  'hot super guacamole',
//  'hot guacamole super',
//  'guacamole super hot',
//  'guacamole hot super' ]

sloganMaker(["cool", "pizza", "cool"]); // => [ 'cool pizza', 'pizza cool' ]
'''


import itertools

def slogan_maker(array):
    new = []
    [new.append(item) for item in array if item not in new]
    return [' '.join(i) for i in list(itertools.permutations(new))]



assert slogan_maker(["super"]) == ["super"]
assert slogan_maker(["super", "hot"]) == ["super hot", "hot super"]
assert slogan_maker(["super", "hot", "guacamole"]) == ["super hot guacamole", "super guacamole hot", "hot super guacamole", "hot guacamole super", "guacamole super hot", "guacamole hot super"]
assert slogan_maker(["super", "guacamole", "super", "super", "hot", "guacamole"]) == ["super guacamole hot", "super hot guacamole", "guacamole super hot", "guacamole hot super", "hot super guacamole", "hot guacamole super"]
assert slogan_maker(["testing", "testing", "testing"]) == ["testing"]