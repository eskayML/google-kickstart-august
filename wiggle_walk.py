def get_neighbor(r, c, i, neighbors):
    if (r, c, i) in neighbors:
        return neighbors[(r, c, i)]

    if i == 'N':
        return (r - 1, c)
    elif i == 'S':
        return (r + 1, c)
    elif i == 'E':
        return (r, c + 1)
    else:  # 'W'
        return (r, c - 1)


def link_neighbors(r, c, neighbors):
    north = get_neighbor(r, c, 'N', neighbors)
    south = get_neighbor(r, c, 'S', neighbors)
    east = get_neighbor(r, c, 'E', neighbors)
    west = get_neighbor(r, c, 'W', neighbors)

    neighbors[(*north, 'S')] = south
    neighbors[(*south, 'N')] = north
    neighbors[(*east, 'W')] = west
    neighbors[(*west, 'E')] = east


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N, R, C, r, c = map(int, input().split())
        instructions = input()  # string of N, S, E or W
        neighbors = {}

        for i in instructions:
            link_neighbors(r, c, neighbors)
            r, c = get_neighbor(r, c, i, neighbors)  # new position

        print('Case #{}: {} {}'.format(case, r, c))
