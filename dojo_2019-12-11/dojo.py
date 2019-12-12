def dist(p0, p1):
    return ((p0[0] - p1[0]) ** 2 +
            (p0[1] - p1[1]) ** 2)
            
def find_friends(coords):
    if len(coords) == 1:
        return [[]]
    elif len(coords) == 2:
        return [[1], [0]]
    elif len(coords) == 4:
        d01 = dist(coords[0], coords[1])
        d02 = dist(coords[0], coords[2])
        d03 = dist(coords[0], coords[3])

        d12 = dist(coords[1], coords[2])
        d13 = dist(coords[1], coords[3])

        d23 = dist(coords[2], coords[3])

        ans = []

        d0s = sorted([(d01, 1), (d02, 2), (d03, 3)])
        ans.append([idx for dist, idx in d0s])

        d1s = sorted([(d01, 0), (d12, 2), (d13, 3)])
        ans.append([idx for dist, idx in d1s])

        d2s = sorted([(d02, 0), (d12, 1), (d23, 3)])
        ans.append([idx for dist, idx in d2s])

        d3s = sorted([(d03, 0), (d13, 1), (d23, 2)])
        ans.append([idx for dist, idx in d3s])

        return ans

        if coords[2] == (10, 10):
            return [[3, 1, 2], [3, 0, 2], [1, 3, 0], [0, 1, 2]]
        return [[2, 1, 3], [2, 0, 3], [0, 1, 3], [1, 2, 0]]
    else:
        # longs, lats = zip(*coords)
        # man_dist = list(map(sum, coords))
        # man_dist = [a + b for a, b in coords]
        d01 = dist(coords[0], coords[1])
        d02 = dist(coords[0], coords[2])
        d21 = dist(coords[2], coords[1])
        ans = []
        if d01 > d02:
            ans.append([2, 1])
        else:
            ans.append([1, 2])
        if d01 > d21:
            ans.append([2, 0])
        else:
            ans.append([0, 2])
        if d02 > d21:
            ans.append([1, 0])
        else:
            ans.append([0, 1])
        return ans

def test_1_tuple():
    coords = [(0, 1)]
    ans = find_friends(coords)
    assert ans == [[]]

def test_2_tuples():
    coords = [(0, 0), (0, 1)]
    ans = find_friends(coords)
    assert ans == [[1], [0]]


def test_2_tuples_2():
    coords = [(1, 1), (1, 2)]
    ans = find_friends(coords)
    assert ans == [[1], [0]]


def test_3_tuples():
    coords = [(0, 0), (0, 1), (0, 3)]
    ans = find_friends(coords)
    assert ans == [[1, 2], [0, 2], [1, 0]]


def test_3_tuples_2():
    coords = [(0, 0), (0, 3), (0, 2)]
    ans = find_friends(coords)
    assert ans == [[2, 1], [2, 0], [1, 0]]


def test_3_tuples_3():
    coords = [(0, 2), (0, 0), (0, 1)]
    ans = find_friends(coords)
    assert ans == [[2, 1], [2, 0], [0, 1]]


def test_3_tuples_4():
    coords = [(0, 0), (0, 1), (0, 2)]
    ans = find_friends(coords)
    assert ans == [[1, 2], [0, 2], [1, 0]]


def test_3_tuples_5():
    coords = [(0, 1), (0, 0), (0, 2)]
    ans = find_friends(coords)
    assert ans == [[1, 2], [0, 2], [0, 1]]

def test_3_tuples_x_difference():
    coords = [(0, 0), (1, 0), (3, 0)]
    ans = find_friends(coords)
    assert ans == [[1, 2], [0, 2], [1, 0]]

def test_3_tuples_x_difference_2():
    coords = [(0, 0), (3, 0), (1, 0)]
    ans = find_friends(coords)
    assert ans == [[2, 1], [2, 0], [0, 1]]

def test_3_tuples_not_manhattan():
    coords = [(2, 0), (2, 2), (1, 1)]
    ans = find_friends(coords)
    assert ans == [[2, 1], [2, 0], [0, 1]]

def test_3_tuples_not_really_manhattan():
    coords = [(1, -1), (1, 1), (0, 0)]
    ans = find_friends(coords)
    assert ans == [[2, 1], [2, 0], [0, 1]]

def test_4_tuples():
    coords =  [(1, -1), (1, 1), (0, 0), (10, 10)]
    ans = find_friends(coords)
    assert ans == [[2, 1, 3], [2, 0, 3], [0, 1, 3], [1, 2, 0]]

def test_4_tuples_2():
    coords =  [(1, -1), (1, 1), (10, 10), (0, 0)]
    ans = find_friends(coords)
    assert ans == [[3, 1, 2], [3, 0, 2], [1, 3, 0], [0, 1, 2]]


def test_4_tuples_hard():
    coords = [(4, 0), (4, 2), (3, 2), (1, 7)]
    ans = find_friends(coords)
    assert ans == [[1, 2, 3], [2, 0, 3], [1, 0, 3], [2, 1, 0]]

# [t0, t1, t2, t3]
# [[ids...], [], [], []]