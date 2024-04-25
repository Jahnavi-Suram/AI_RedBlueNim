import sys
max_player =  100000000
min_player = -100000000
red_value = 2
blue_value = 3
def eval(red_pile,blue_pile,version,player):
    sign=-1
    ans = red_pile*red_value+blue_pile*blue_value
    if player =="human":
        return ans
    else:
        return ans*sign

def print_answer(red_pile,blue_pile):
    print("current state",red_pile,"R ",blue_pile,"B")

def find_alpha_beta(solution,red_pile,blue_pile,version,depth,player,intmin,intmax):
    # if the current player is human consider it as minimum player and
    # the computer is considered as the max player

    if player=="computer":
        solution = max_player
    else:
        solution = min_player
    if depth == 0 or blue_pile==0 or red_pile==0:
        rests = eval(red_pile,blue_pile,version,player)
        return [rests,-1]
    current_score = 0
    current_move = -1
    for i in range(0,2):
        if (i==0 and red_pile<=0) or (i==1 and blue_pile<=0): continue
        if (i==0 and red_pile<=0) and (i==1 and blue_pile<=0): break
        if i == 0: red_pile-=1
        else: blue_pile-=1
        f = player
        if f =="human":
            f ="computer"
        else:
            f ="human"
        result,move = find_alpha_beta(solution,red_pile,blue_pile,version,depth-1,f ,intmin,intmax)
        current_score= result
        if player=="human":
            if current_score>solution:
                solution,current_move = current_score,i
            # print(current_score,solution,current_move)
            intmin = max(intmin,solution)
        else:
            if current_score<solution:
                solution,current_move = current_score,i
            intmax = min(intmax,solution)
        # print(intmin)
        if intmax<=intmin:
            break
    return current_score,current_move
def findscore(red_pile,blue_pile,length,version,player,depth):
    turn = 0
    answer = [red_pile,blue_pile]
    while(red_pile>0 and blue_pile>0):
        print_answer(red_pile,blue_pile)
        if player=="human":
            print("Choose 1 for red and 2 for blue")
            turn = int(input()) - 1
        elif player=="computer":
            result=find_alpha_beta(0,red_pile,blue_pile,version,depth,player,-100000000,100000000)
            print(result)
            if result is not None:
                turn  = result[1]
            print("computer has removed",turn+1)
        if turn == 0:
            red_pile = red_pile -1
        else:
            blue_pile = blue_pile - 1
        if player=="human":player = "computer"
        else:player = "human"
    ans = red_value*red_pile+blue_pile*blue_value
    if version=="standard":
        if player == "human":
            result="computer"
        else:
            result = "you"
    else:
        if player == "human":
            result="you"
        else:
            result = "computer"
    print(result," has won the game with a score of ",ans)


red_pile = int(sys.argv[1])
blue_pile = int(sys.argv[2])
# print(sys.argv)
version = "standard"
player = "computer"
depth = -1
if len(sys.argv)>=4:
    if len(sys.argv)==4:
        if len(sys.argv[3])==8:
            if sys.argv[3]=="standard":
                version = "standard"
            elif(len(sys.argv[3])>3):
                player = "computer"
        elif sys.argv[3] == "misere":
            version = "misere"
        elif len(sys.argv[3])>3:
            player = "human"
        else:
            depth = int(sys.argv[3])
    if len(sys.argv)==5:
        if len(sys.argv[3])==8:
            if sys.argv[3]=="standard":
                version = "standard"
            elif sys.argv[3]=="computer":
                player = "computer"
        elif sys.argv[3] == "misere":
            version = "misere"
        elif sys.argv[3] == "human":
            player = "human"
        if len(sys.argv[4])>3:
            player = sys.argv[4]
        else:
            depth = int(sys.argv[4])
    if len(sys.argv)==6:
        version = sys.argv[3]
        player = sys.argv[4]
        depth = int(sys.argv[5])
print(depth)
findscore(red_pile,blue_pile,len(sys.argv),version,player,depth)
