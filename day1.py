def find_distance(turns):
    _direction_map = {
        'N': {
            'L': 'W',
            'R': 'E',
            'axis_direction': ('x', 1)
        },
        'E': {
            'L': 'N',
            'R': 'S',
            'axis_direction': ('y', 1)
        },
        'S': {
            'L': 'E',
            'R': 'W',
            'axis_direction': ('x', -1)
        },
        'W': {
            'L': 'S',
            'R': 'N',
            'axis_direction': ('y', -1)
        }
    }

    current_direction = 'N'
    current_coordinates = {'x': 0, 'y': 0}
    i = 0

    while i < len(turns):
        turn_dir = turns[i][0]
        blocks = int(turns[i][1:])
        current_direction = _direction_map[current_direction][turn_dir]
        axis, multiplier = _direction_map[current_direction]['axis_direction']
        current_coordinates[axis] += multiplier * blocks
        i += 1

    return abs(current_coordinates['x']) + abs(current_coordinates['y'])


def find_distance_2(turns):
    _direction_map = {
        'N': {
            'L': 'W',
            'R': 'E',
            'axis_direction': ('x', 1)
        },
        'E': {
            'L': 'N',
            'R': 'S',
            'axis_direction': ('y', 1)
        },
        'S': {
            'L': 'E',
            'R': 'W',
            'axis_direction': ('x', -1)
        },
        'W': {
            'L': 'S',
            'R': 'N',
            'axis_direction': ('y', -1)
        }
    }

    current_direction = 'N'
    current_coordinates = {'x': 0, 'y': 0}
    i = 0
    _visited = set([(0, 0)])

    while i < len(turns):
        turn_dir = turns[i][0]
        blocks = int(turns[i][1:])
        current_direction = _direction_map[current_direction][turn_dir]
        axis, multiplier = _direction_map[current_direction]['axis_direction']

        for _ in range(blocks):
            current_coordinates[axis] += multiplier * 1
            coord_visited = (current_coordinates['x'],
                             current_coordinates['y'])
            if coord_visited in _visited:
                return (abs(current_coordinates['x']) +
                        abs(current_coordinates['y']))

            _visited.add(coord_visited)

        i += 1

    return abs(current_coordinates['x']) + abs(current_coordinates['y'])
