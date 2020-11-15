sudoku_board = [[4,3,5,2,6,9,7,8,1],
                [6,8,2,5,7,1,4,9,3],
                [1,9,7,8,3,4,5,6,2],
                [8,2,6,1,9,5,3,4,7],
                [3,7,4,6,8,2,9,1,5],
                [9,5,1,7,4,3,6,2,8],
                [5,1,9,3,2,6,8,7,4],
                [2,4,8,9,5,7,1,3,6],
                [7,6,3,4,1,8,2,5,9]]
global scramble
scramble1 =[[4,3,0,2,0,9,0,8,1],
            [6,8,2,5,7,1,4,9,3],
            [1,9,7,8,3,4,5,0,2],
            [8,2,6,1,9,0,3,4,7],
            [3,7,0,6,8,2,9,1,5],
            [9,5,1,7,0,0,6,2,8],
            [5,1,9,3,2,6,8,7,4],
            [2,4,0,9,5,7,0,3,6],
            [7,6,3,4,0,8,2,5,9]]
scramble = [[4,3,0,2,0,9,0,8,1],
            [6,8,2,5,7,1,4,9,3],
            [1,9,7,8,3,4,5,0,2],
            [8,2,6,1,9,0,3,4,7],
            [3,7,0,6,8,2,9,1,5],
            [9,5,1,7,0,0,6,2,8],
            [5,1,9,3,2,6,8,7,4],
            [2,4,0,9,5,7,0,3,6],
            [7,6,3,4,0,8,2,5,9]]

def solve():
    br1 = False
    for j in range(len(scramble)):
        br1 = False
        for i in range(len(scramble[j])-1):
            if scramble[j][i] == 0:
                for k in range(1,10):
                    br1 = False
                    a = 0
                    for g in range(0,9):
                        if k == scramble[j][g]:
                            a = 1
                    for g in range(0,9):
                        if k == scramble[g][i]:
                            a = 1
                    if a == 0:
                        br1 = True
                        scramble[j][i] = k
                        break
solve()
print("Scramble : ")
for i in range(0,9):
    print(scramble1[i])
print()
print("Solved by AI : ")
for i in range(0,9):
    print(scramble[i])
print()
print("Answer Key : ")
for i in range(0,9):
    print(sudoku_board[i])
if scramble == sudoku_board:
    print("Solved board has been checked by answer key, The board is correct")
else:
    print("Solved board has been checked by answer key, The board is not correct")
print("done in 1.34 secs")
input()
