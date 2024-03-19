import random, sys

print('ROCK, PAPER, SCISSORS')
win, loss, draw = 0, 0, 0
print('Start Play? y/n')
start = input()
if (start == 'n'):
    print("play later")
    sys.exit()
while (start == 'y'):
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    move = input()
    computermove = random.randint(1, 3)  # 1 = rock, 2 = paper , 3 = scissors
    if (move == 'q'):
        print('Play when free')
        sys.exit()
    if (move == 'r'):
        print('Rock versus ...')
    elif (move == 'p'):
        print('Paper versus ...')
    elif (move == 's'):
        print('Scissors versus ...')
    if computermove == 1:
        print('Rock')
        if move == 'r':
            draw += 1;
            print("draw")
        elif (move == 'p'):
            win = win + 1;
            print("win")
        elif (move == 's'):
            loss += 1
            print("loss")
    if computermove == 2:
        print('Paper')
        if move == 'p':
            draw += 1;
            print("draw")
        elif (move == 's'):
            win = win + 1;
            print("win")
        elif (move == 'r'):
            loss += 1
            print("loss")
    if computermove == 3:
        print('Scissor')
        if move == 's':
            draw += 1;
            print("draw")
        elif (move == 'r'):
            win = win + 1;
            print("win")
        elif (move == 'p'):
            loss += 1
            print("loss")
    print('wins' + str(win) + ', losses' + str(loss) + ', draws' + str(draw))

