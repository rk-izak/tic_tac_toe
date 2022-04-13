a = [' '] * 10

print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]))
a = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]

i = 0
x_win = 0
o_win = 0

while x_win == 0 or o_win == 0:
    b = input("Enter the coordinates: ")

    wrong_cord = 1
    wrong_type = 1
    wrong_occp = 1

    cord_1 = b[0]
    cord_2 = b[2]

    while wrong_cord == 1 or wrong_type == 1 or wrong_occp == 1:

        cord_1 = str(cord_1)
        cord_2 = str(cord_2)

        if cord_1.isnumeric() is False or cord_2.isnumeric() is False:
            print("You should enter numbers!")
            b = input("Enter the coordinates: ")
            cord_1 = b[0]
            cord_2 = b[2]
        else:
            wrong_type = 0

        cord_1 = int(cord_1)
        cord_2 = int(cord_2)

        if cord_1 not in range(1, 4, 1) or cord_2 not in range(1, 4, 1):
            print("Coordinates should be from 1 to 3!")
            cord_1, cord_2 = input("Enter the coordinates: ").split()
        else:
            wrong_cord = 0

        cord_1 = int(cord_1)
        cord_2 = int(cord_2)

        if a[cord_1 - 1][cord_2 - 1] == 'O' or a[cord_1 - 1][cord_2 - 1] == 'X':
            print("This cell is occupied! Choose another one!")
            cord_1, cord_2 = input("Enter the coordinates: ").split()
        else:
            wrong_occp = 0

    if i % 2 == 0:
        a[cord_1 - 1][cord_2 - 1] = 'X'
    else:
        a[cord_1 - 1][cord_2 - 1] = 'O'

    if a[0][0:3] == ['X', 'X', 'X'] or a[1][0:3] == ['X', 'X', 'X'] or a[2][0:3] == ['X', 'X', 'X'] or \
            (a[0][0] == a[1][1] == a[2][2] == 'X') or (a[0][2] == a[1][1] == a[2][0] == 'X') or \
            (a[0][0] == a[1][0] == a[2][0] == 'X') or (a[0][1] == a[1][1] == a[2][1] == 'X') or \
            (a[0][2] == a[1][2] == a[2][2] == 'X'):
        x_win = 1
        break

    if a[0][0:3] == ['O', 'O', 'O'] or a[1][0:3] == ['O', 'O', 'O'] or a[2][0:3] == ['O', 'O', 'O'] or \
            (a[0][0] == a[1][1] == a[2][2] == 'O') or (a[0][2] == a[1][1] == a[2][0] == 'O') or \
            (a[0][0] == a[1][0] == a[2][0] == 'O') or (a[0][1] == a[1][1] == a[2][1] == 'O') or \
            (a[0][2] == a[1][2] == a[2][2] == 'O'):
        o_win = 1
        break
    if i == 8:
        break

    i += 1
    print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2], a[2][0], a[2][1], a[2][2]))

print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2], a[2][0], a[2][1], a[2][2]))

if x_win == 1:
    print("X wins")
elif o_win == 1:
    print("O wins")
else:
    print("Draw")
