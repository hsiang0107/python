# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)


class RockPaperScissors:
    def __init__(self):
        self.opt1 = 'Rock'
        self.opt2 = 'Paper'
        self.opt3 = 'Scissors'
        self.A_Win = True
        self.B_Win = True

    def two_players(self, a, b):
        if (a == b):
            self.A_Win = False
            self.B_Win = False
            print('Even')
        else:
            if((a == self.opt1 and b == self.opt3) or (a == self.opt2 and b == self.opt1) or
                    (a == self.opt3 and b == self.opt2)):
                self.B_Win = False
                print('A win')
            else:
                self.A_Win = False
                print('B win')

    def test(self):
        pass


def getplayeroption():
    while 1:
        Aopt = input('Player A option: 1.Rock, 2.Paper, 3.Scissors')
        if(Aopt not in ['1', '2', '3']):
            print('Invalid input for player A, input again')
            continue
        else:
            break

    while 1:
        Bopt = input('Player B option: 1.Rock, 2.Paper, 3.Scissors')
        if(Bopt not in ['1', '2', '3']):
            print('Invalid input for player B, input again')
            continue
        else:
            break
    optlist = [Aopt, Bopt]
    # print(optlist)
    playeroption=[]
    for item in optlist:
        if(item == '1'):
            playeroption.append('Rock')
        elif(item == '2'):
            playeroption.append('Paper')
        else:
            playeroption.append('Scissors')

    return playeroption

# options = getplayeroption()
# print(options)
game1 = RockPaperScissors()
while 1:
    options = getplayeroption()
    game1.two_players(*options)
    again = input('Again ? y or n')
    if(again == 'n'):
        break
