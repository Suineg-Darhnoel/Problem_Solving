A = [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1]
    ]

B = [
        [0, 1],
        [0, 0]
    ]

C = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0]
    ]

# solution function
def solution(K, A):
    house_positions = []
    empty_positions = []

    # separate the locations of the houses and the empty spaces
    for i, row in enumerate(A):
        for j, elem in enumerate(row):
            if elem == 1:
                house_positions.append((i, j))
            else:
                empty_positions.append((i, j))

    # function to compute the distance from one point to another
    def distance(p_a, p_b):
        dy = abs(p_a[0] - p_b[0])
        dx = abs(p_a[1] - p_b[1])
        return dx + dy

    sol = []
    for empty_pos in empty_positions:
        if all((distance(hp, empty_pos) <= K
            for hp in house_positions)):
            sol.append(empty_pos)
    return sol

print(solution(2, A))
print(solution(1, B))
print(solution(2, C))
