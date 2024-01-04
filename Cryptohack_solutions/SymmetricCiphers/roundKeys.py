#Using code from the add_round_key.py file provided by the cryptohack course
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    flagMatrix =    [[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
    for i in range(4):
        for j in range(4):
            flagMatrix[i][j] = s[i][j]^k[i][j]
    return flagMatrix

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    summed=sum(matrix, [])
    flag = bytes(summed)
    return flag
    


print(matrix2bytes(add_round_key(state, round_key)))