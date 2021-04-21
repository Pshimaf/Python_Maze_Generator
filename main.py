import sys
from random import randint

def in_matr(y_second, x_second, high_of_matr, length_of_matr):
    if y_second <= 0 or x_second <= 0 or y_second >= high_of_matr or x_second >= length_of_matr:
        return False
    else:
        return True

matr = list()
used = list()
answer = list()

def check(y, x):
    if used[y][x] or matr[y][x] == 1:
        return False
    return True

def DFS(y, x, y_final, x_final):
    used[y][x] = True
    if y == y_final and x == x_final:
        return True
    y1 = y - 1
    x1 = x
    if check(y1, x1):
        b = DFS(y1, x1, y_final, x_final)
        if b:
            answer.append([y, x])
            return True
    y1 = y + 1
    x1 = x
    if check(y1, x1):
        b = DFS(y1, x1, y_final, x_final)
        if b:
            answer.append([y, x])
            return True
    y1 = y
    x1 = x - 1
    if check(y1, x1):
        b = DFS(y1, x1, y_final, x_final)
        if b:
            answer.append([y, x])
            return True

    y1 = y
    x1 = x + 1
    if check(y1, x1):
        b = DFS(y1, x1, y_final, x_final)
        if b:
            answer.append([y, x])
            return True

    return False

high_of_maze = 0
length_of_maze = 0

print("Do you want new maze or use old one? (new/old)")
s = input()
if s == "new":
    print("Write down your maze size")
    print("High: ")
    high_of_maze = int(input())
    print("Length: ")
    length_of_maze = int(input())
    print("What you want to use? (DFS/Prim)")
    s = input()

    for i in range(0, 2 * high_of_maze + 1):
        matr.append(list())
        if i % 2 == 0:
            for j in range(0, 2 * length_of_maze + 1):
                matr[i].append(1)
        else:
            for j in range(0, 2 * length_of_maze + 1):
                if j % 2 == 0:
                    matr[i].append(1)
                else:
                    matr[i].append(0)

    if s == "DFS":
        stack = list()
        stack.append([1, 1])
        matr[1][1] = 2
        while True:
            if len(stack) == 0:
                break

            neighbour_list = []
            if in_matr(stack[-1][0] + 2, stack[-1][1] + 0, 2 * high_of_maze, 2 * length_of_maze) \
                    and matr[stack[-1][0] + 2][stack[-1][1] + 0] == 0:
                neighbour_list.append([stack[-1][0] + 2, stack[-1][1] + 0])
            if in_matr(stack[-1][0] + 0, stack[-1][1] + 2, 2 * high_of_maze, 2 * length_of_maze) \
                    and matr[stack[-1][0] + 0][stack[-1][1] + 2] == 0:
                neighbour_list.append([stack[-1][0] + 0, stack[-1][1] + 2])
            if in_matr(stack[-1][0] - 2, stack[-1][1] + 0, 2 * high_of_maze, 2 * length_of_maze) \
                    and matr[stack[-1][0] - 2][stack[-1][1] + 0] == 0:
                neighbour_list.append([stack[-1][0] - 2, stack[-1][1] + 0])
            if in_matr(stack[-1][0] + 0, stack[-1][1] - 2, 2 * high_of_maze, 2 * length_of_maze) \
                    and matr[stack[-1][0] + 0][stack[-1][1] - 2] == 0:
                neighbour_list.append([stack[-1][0] + 0, stack[-1][1] - 2])

            if len(neighbour_list) == 0:
                stack.pop()
            else:
                r = randint(0, 100)
                stack.append([neighbour_list[r % len(neighbour_list)][0], neighbour_list[r % len(neighbour_list)][1]])
                matr[stack[-1][0]][stack[-1][1]] = 2
                matr[(stack[-2][0] + stack[-1][0]) // 2][(stack[-2][1] + stack[-1][1]) // 2] = 2


    if s == "Prim":
        walls_list = []
        y_start = 2 * randint(0, high_of_maze - 1) + 1
        x_start = 2 * randint(0, length_of_maze - 1) + 1
        matr[y_start][x_start] = 2
        if in_matr(y_start + 2, x_start + 0, 2 * high_of_maze, 2 * length_of_maze) \
                and matr[y_start + 2][x_start + 0] == 0:
            walls_list.append([y_start + 1, x_start + 0])
        if in_matr(y_start + 0, x_start + 2, 2 * high_of_maze, 2 * length_of_maze) \
                and matr[y_start + 0][x_start + 2] == 0:
            walls_list.append([y_start + 0, x_start + 1])
        if in_matr(y_start - 2, x_start + 0, 2 * high_of_maze, 2 * length_of_maze) \
                and matr[y_start - 2][x_start + 0] == 0:
            walls_list.append([y_start - 1, x_start + 0])
        if in_matr(y_start + 0, x_start - 2, 2 * high_of_maze, 2 * length_of_maze) \
                and matr[y_start + 0][x_start - 2] == 0:
            walls_list.append([y_start + 0, x_start - 1])

        while True:
            if len(walls_list) == 0:
                break
            r = randint(0, len(walls_list) - 1)
            two_counter = 0
            up = False
            down = False
            left = False
            right = False
            if (matr[walls_list[r][0] + 1][walls_list[r][1]] == 2):
                up = True
                two_counter += 1
            if (matr[walls_list[r][0]][walls_list[r][1] + 1] == 2):
                right = True
                two_counter += 1
            if (matr[walls_list[r][0] - 1][walls_list[r][1]] == 2):
                down = True
                two_counter += 1
            if (matr[walls_list[r][0]][walls_list[r][1] - 1] == 2):
                left = True
                two_counter += 1

            if two_counter >= 2:
                walls_list.pop(r)
                continue

            if up:
                matr[walls_list[r][0]][walls_list[r][1]] = 2
                matr[walls_list[r][0] - 1][walls_list[r][1]] = 2
                if in_matr(walls_list[r][0] - 1 + 2, walls_list[r][1] + 0, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] - 1 + 2][walls_list[r][1] + 0] == 0:
                    walls_list.append([walls_list[r][0] - 1 + 1, walls_list[r][1] + 0])
                if in_matr(walls_list[r][0] - 1 + 0, walls_list[r][1] + 2, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] - 1 + 0][walls_list[r][1] + 2] == 0:
                    walls_list.append([walls_list[r][0] - 1 + 0, walls_list[r][1] + 1])
                if in_matr(walls_list[r][0] - 1 - 2, walls_list[r][1] + 0, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] - 1 - 2][walls_list[r][1] + 0] == 0:
                    walls_list.append([walls_list[r][0] - 1 - 1, walls_list[r][1] + 0])
                if in_matr(walls_list[r][0] - 1 + 0, walls_list[r][1] - 2, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] - 1 + 0][walls_list[r][1] - 2] == 0:
                    walls_list.append([walls_list[r][0] - 1 + 0, walls_list[r][1] - 1])
            if down:
                matr[walls_list[r][0]][walls_list[r][1]] = 2
                matr[walls_list[r][0] + 1][walls_list[r][1]] = 2
                if in_matr(walls_list[r][0] + 1 + 2, walls_list[r][1] + 0, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 1 + 2][walls_list[r][1] + 0] == 0:
                    walls_list.append([walls_list[r][0] + 1 + 1, walls_list[r][1] + 0])
                if in_matr(walls_list[r][0] + 1 + 0, walls_list[r][1] + 2, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 1 + 0][walls_list[r][1] + 2] == 0:
                    walls_list.append([walls_list[r][0] + 1 + 0, walls_list[r][1] + 1])
                if in_matr(walls_list[r][0] + 1 - 2, walls_list[r][1] + 0, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 1 - 2][walls_list[r][1] + 0] == 0:
                    walls_list.append([walls_list[r][0] + 1 - 1, walls_list[r][1] + 0])
                if in_matr(walls_list[r][0] + 1 + 0, walls_list[r][1] - 2, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 1 + 0][walls_list[r][1] - 2] == 0:
                    walls_list.append([walls_list[r][0] + 1 + 0, walls_list[r][1] - 1])
            if left:
                matr[walls_list[r][0]][walls_list[r][1]] = 2
                matr[walls_list[r][0]][walls_list[r][1] + 1] = 2
                if in_matr(walls_list[r][0] + 2, walls_list[r][1] + 1 + 0, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 2][walls_list[r][1] + 1 + 0] == 0:
                    walls_list.append([walls_list[r][0] + 1, walls_list[r][1] + 1 + 0])
                if in_matr(walls_list[r][0] + 0, walls_list[r][1] + 1 + 2, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 0][walls_list[r][1] + 1 + 2] == 0:
                    walls_list.append([walls_list[r][0] + 0, walls_list[r][1] + 1 + 1])
                if in_matr(walls_list[r][0] - 2, walls_list[r][1] + 1 + 0, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] - 2][walls_list[r][1] + 1 + 0] == 0:
                    walls_list.append([walls_list[r][0] - 1, walls_list[r][1] + 1 + 0])
                if in_matr(walls_list[r][0] + 0, walls_list[r][1] + 1 - 2, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 0][walls_list[r][1] + 1 - 2] == 0:
                    walls_list.append([walls_list[r][0] + 0, walls_list[r][1] + 1 - 1])
            if right:
                matr[walls_list[r][0]][walls_list[r][1]] = 2
                matr[walls_list[r][0]][walls_list[r][1] - 1] = 2
                if in_matr(walls_list[r][0] + 2, walls_list[r][1] - 1 + 0, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 2][walls_list[r][1] - 1 + 0] == 0:
                    walls_list.append([walls_list[r][0] + 1, walls_list[r][1] - 1 + 0])
                if in_matr(walls_list[r][0] + 0, walls_list[r][1] - 1 + 2, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 0][walls_list[r][1] - 1 + 2] == 0:
                    walls_list.append([walls_list[r][0] + 0, walls_list[r][1] - 1 + 1])
                if in_matr(walls_list[r][0] - 2, walls_list[r][1] - 1 + 0, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] - 2][walls_list[r][1] - 1 + 0] == 0:
                    walls_list.append([walls_list[r][0] - 1, walls_list[r][1] - 1 + 0])
                if in_matr(walls_list[r][0] + 0, walls_list[r][1] - 1 - 2, 2 * high_of_maze, 2 * length_of_maze) \
                        and matr[walls_list[r][0] + 0][walls_list[r][1] - 1 - 2] == 0:
                    walls_list.append([walls_list[r][0] + 0, walls_list[r][1] - 1 - 1])
if s == "old":
    print("What is the name of the file that contains the old maze?")
    s = input()
    file = open(s, 'r')
    lines_of_file = list(file.readlines())
    space_ind = 0
    length_first = len(lines_of_file[0])
    for i in range(0, length_first):
        if lines_of_file[0][i] == ' ':
            space_ind = i
    high_of_maze = int((lines_of_file[0])[0:space_ind])
    length_of_maze = int((lines_of_file[0])[space_ind + 1:-1])
    for i in range(0, 2 * high_of_maze + 1):
        matr.append((list(lines_of_file[i + 1]))[0:-1])
    for i in range(0, 2 * high_of_maze + 1):
        for j in range(0, 2 * length_of_maze + 1):
            matr[i][j] = int(matr[i][j])
    file.close()

for i in range(0, 2 * high_of_maze + 1):
    for j in range(0, 2 * length_of_maze + 1):
        if i == 1 and j == 1:
            print("\033[41m {} \033[0m".format(' '), end='')
            continue
        if i == 2 * high_of_maze - 1 and j == 2 * length_of_maze - 1:
            print("\033[42m {} \033[0m".format(' '), end='')
            continue
        if matr[i][j] == 1:
            print("\033[44m {} \033[0m".format(' '), end='')
        else:
            print("\033[47m {} \033[0m".format(' '), end='')
    print()

print("Do you want to see the answer? (yes/no)")
s = input()
if s == "yes":
    for i in range(0, 2 * high_of_maze + 1):
        used.append(list())
        for j in range(0, 2 * length_of_maze + 1):
            used[i].append(False)
    DFS(1, 1, 2 * high_of_maze - 1, 2 * length_of_maze - 1)

for i in range(0, 2 * high_of_maze + 1):
    for j in range(0, 2 * length_of_maze + 1):
        if i == 1 and j == 1:
            print("\033[41m {} \033[0m".format(' '), end='')
            continue
        if i == 2 * high_of_maze - 1 and j == 2 * length_of_maze - 1:
            print("\033[42m {} \033[0m".format(' '), end='')
            continue
        if [i, j] in answer:
            print("\033[43m {} \033[0m".format(' '), end='')
            continue
        if matr[i][j] == 1:
            print("\033[44m {} \033[0m".format(' '), end='')
        else:
            print("\033[47m {} \033[0m".format(' '), end='')
    print()

print("Do you want to save your maze? (yes/no)")
s = input()
if s == "yes":
    print("What is the name of the file in which you want to save the maze?")
    s = input()
    file = open(s, 'w')
    file.seek(0)
    file.write("{0} {1}\n".format(high_of_maze, length_of_maze))
    for i in range(0, 2 * high_of_maze + 1):
        for j in range(0, 2 * length_of_maze + 1):
            file.write(str(matr[i][j]))
        file.write('\n')
    file.close()
