# Hongyu Tu 2020/02/03

def main():
    option = int(input('Do you have a coordinate or a label?\n0 for label\n1 for coordinate\n'))
    a = [0]
    i = 1
    j = 1
    if option == 0: # label
        label = int(input('Enter your label\n'))
        while len(a) < label:
            if a[-1] != 0:
                i, j = nextp(i, j)
            a = add(i,j,a)
        print("({},{}) has value {} and has label {}\n".format(i,j,i/j, label))

    else: # coordinate
        tarx = float(input('Enter X value\n'))
        tary = float(input('Enter Y value\n'))
        tarvalue = tarx/tary
        while tarvalue not in a:
            if a[-1] != 0:
                i, j = nextp(i, j)
            a = add(i,j,a)
        print("({},{}) has value {} and has label {}\n".format(int(tarx), int(tary), tarvalue, a.index(tarvalue)+1))
    # print(a)
    onemore = int(input('Check another one? \n0 for No \n1 for YES\n'))
    if onemore:
        print('\n')
        main()
    else:
        print('Exiting program...\n')

def nextp(x, y):
    if y == 1:
        if x < 0:
            return (1, abs(x) + abs(y))
        else:
            return (-1, x)
    elif x > 0:
        return (x + 1, y - 1)
    elif x < 0:
        return (x - 1, y - 1)

def add(x, y, dict):
    value = x / y
    # print(value)
    if value not in dict:
        dict.append(value)
    return dict

main()
