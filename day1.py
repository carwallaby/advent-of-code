test_input = ['L4', 'L1', 'R4', 'R1', 'R1', 'L3', 'R5', 'L5', 'L2', 'L3',
              'R2', 'R1', 'L4', 'R5', 'R4', 'L2', 'R1', 'R3', 'L5', 'R1',
              'L3', 'L2', 'R5', 'L4', 'L5', 'R1', 'R2', 'L1', 'R5', 'L3',
              'R2', 'R2', 'L1', 'R5', 'R2', 'L1', 'L1', 'R2', 'L1', 'R1',
              'L2', 'L2', 'R4', 'R3', 'R2', 'L3', 'L188', 'L3', 'R2', 'R54',
              'R1', 'R1', 'L2', 'L4', 'L3', 'L2', 'R3', 'L1', 'L1', 'R3',
              'R5', 'L1', 'R5', 'L1', 'L1', 'R2', 'R4', 'R4', 'L5', 'L4',
              'L1', 'R2', 'R4', 'R5', 'L2', 'L3', 'R5', 'L5', 'R1', 'R5',
              'L2', 'R4', 'L2', 'L1', 'R4', 'R3', 'R4', 'L4', 'R3', 'L4',
              'R78', 'R2', 'L3', 'R188', 'R2', 'R3', 'L2', 'R2', 'R3', 'R1',
              'R5', 'R1', 'L1', 'L1', 'R4', 'R2', 'R1', 'R5', 'L1', 'R4',
              'L4', 'R2', 'R5', 'L2', 'L5', 'R4', 'L3', 'L2', 'R1', 'R1',
              'L5', 'L4', 'R1', 'L5', 'L1', 'L5', 'L1', 'L4', 'L3', 'L5',
              'R4', 'R5', 'R2', 'L5', 'R5', 'R5', 'R4', 'R2', 'L1', 'L2',
              'R3', 'R5', 'R5', 'R5', 'L2', 'L1', 'R4', 'R3', 'R1', 'L4',
              'L2', 'L3', 'R2', 'L3', 'L5', 'L2', 'L2', 'L1', 'L2', 'R5',
              'L2', 'L2', 'L3', 'L1', 'R1', 'L4', 'R2', 'L4', 'R3', 'R5',
              'R3', 'R4', 'R1', 'R5', 'L3', 'L5', 'L5', 'L3', 'L2', 'L1',
              'R3', 'L4', 'R3', 'R2', 'L1', 'R3', 'R1', 'L2', 'R4', 'L3',
              'L3', 'L3', 'L1', 'L2']

simple_case = ['R2', 'L3']


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
