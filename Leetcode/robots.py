def fight(robot_1, robot_2, tactics):
    if robot_1['speed'] < robot_2['speed']:
        robot_1, robot_2 = robot_2, robot_1

    attack_1 = [tactics[i] for i in robot_1['tactics']]
    health_1 = robot_1['health']

    attack_2 = [tactics[i] for i in robot_2['tactics']]
    health_2 = robot_2['health']

    x = len(attack_1)
    y = len(attack_2)
    diff = max(x, y)
    attack_1.extend([0] * (diff - x))
    attack_2.extend([0] * (diff - y))

    round = 0
    while round != len(attack_1):
        health_2 -= attack_1[round]
        if health_2 <= 0:
            return f'{robot_1["name"]} has won the fight.'
        health_1 -= attack_2[round]
        if health_1 <= 0:
            return f'{robot_2["name"]} has won the fight.'
        round += 1

    if health_1 == health_2:
        return 'The fight was a draw.'
    else:
        return f'{robot_1["name"]} has won the fight.' if health_1 > health_2 else f'{robot_2["name"]} has won the fight.'



robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile", 'punch'] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
assert fight(robot_1, robot_2, tactics) == "Missile Bob has won the fight."


robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
assert fight(robot_1, robot_2, tactics) == "Rocky has won the fight."


robot_1 = {'name': 'Missile Bob', 'health': 581, 'speed': 85, 'tactics': ['punch', 'missile', 'laser', 'punch', 'laser', 'punch', 'laser', 'laser', 'laser', 'laser']}
robot_2 = {'name': 'Rocky', 'health': 588, 'speed': 15, 'tactics': ['laser', 'laser', 'laser', 'laser', 'missile', 'punch', 'missile', 'laser', 'laser', 'punch']}
tactics = {'punch': 20, 'laser': 30, 'missile': 35}
assert fight(robot_1, robot_2, tactics) == "Rocky has won the fight."
