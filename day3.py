def is_possible_triangle(sides):
    sides = map(lambda x: int(x), sides)
    if sides[0] + sides[1] <= sides[2]:
        return False
    if sides[0] + sides[2] <= sides[1]:
        return False
    if sides[1] + sides[2] <= sides[0]:
        return False
    return True


def count_possible_triangles(triangles):
    count = 0

    for triangle in triangles:
        if is_possible_triangle(triangle):
            count += 1

    return count


def count_possible_triangles_2(triangles):
    count = 0

    for i in range(0, len(triangles), 3):
        tri_1 = [triangles[i][0], triangles[i + 1][0], triangles[i + 2][0]]
        tri_2 = [triangles[i][1], triangles[i + 1][1], triangles[i + 2][1]]
        tri_3 = [triangles[i][2], triangles[i + 1][2], triangles[i + 2][2]]

        for t in [tri_1, tri_2, tri_3]:
            if is_possible_triangle(t):
                count += 1

    return count
