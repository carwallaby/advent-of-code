def button_code(directions):
    buttons = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    _directions = {
        'L': (1, -1),
        'U': (0, -1),
        'R': (1, 1),
        'D': (0, 1)
    }

    current_coords = [0, 0]
    code = []

    for direction in directions:
        for char in direction:
            i, j = _directions[char]
            current_coords[i] += j
            if current_coords[i] < 0:
                current_coords[i] = 0
            elif current_coords[i] > 2:
                current_coords[i] = 2
        code.append(buttons[current_coords[0]][current_coords[1]])

    code = map(lambda x: str(x), code)

    return ''.join(code)


def button_code_2(directions):
    buttons = [
        [None, None, '1', None, None],
        [None, '2', '3', '4', None],
        ['5', '6', '7', '8', '9'],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ]

    _directions = {
        'L': (1, -1),
        'U': (0, -1),
        'R': (1, 1),
        'D': (0, 1)
    }

    current_coords = [2, 0]
    code = []

    for direction in directions:
        for char in direction:
            i, j = _directions[char]
            fallback_coords = [current_coords[0], current_coords[1]]
            current_coords[i] += j
            if current_coords[i] < 0:
                current_coords[i] = 0
            elif current_coords[i] > 4:
                current_coords[i] = 4
            if not buttons[current_coords[0]][current_coords[1]]:
                current_coords = fallback_coords
        code.append(buttons[current_coords[0]][current_coords[1]])

    code = map(lambda x: str(x), code)

    return ''.join(code)
