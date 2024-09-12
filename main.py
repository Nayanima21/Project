def board(x,y):
    print(f"{'X' if x[0] else ('O' if y[0] else 0)} | {'X' if x[1] else ('O' if y[1] else 1)} | {'X' if x[2] else ('O' if y[2] else 2)} ")
    print(f"--|---|---")
    print(f"{'X' if x[3] else ('O' if y[3] else 3)} | {'X' if x[4] else ('O' if y[4] else 4)} | {'X' if x[5] else ('O' if y[5] else 5)} ")
    print(f"--|---|---")
    print(f"{'X' if x[6] else ('O' if y[6] else 6)} | {'X' if x[7] else ('O' if y[7] else 7)} | {'X' if x[8] else ('O' if y[8] else 8)}  ")

def sum(a,b,c):
    return a+b+c

def check(x,y):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in wins:
        if(sum(x[i[0]],x[i[1]],x[i[2]])==3):
            return 1
        if(sum(y[i[0]],y[i[1]],y[i[2]])==3):
            return 0
    return -1

x=[0,0,0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0,0,0]
turn=1 
c=0
print("HELLO EVERYONE!")
print("WELCOME TO TIC TAC TOE GAME")
while(True):
    board(x,y)
    if(turn==1):
        print("X's Chance")
        value=int(input("Please enter a value: "))
        x[value]=1
        turn=0
    else:
        print("O's Chance")
        value=int(input("Please enter a value: "))
        y[value]=1
        turn=1
    c+=1
    res=check(x,y)
    if(res!=-1):
        if(res==1):
            board(x,y)
            print("X Wins!")
        if(res==0):
            board(x,y)
            print("O Wins!")
        break
    if(c==9):
        board(x,y)
        print("Game over! Nobody Won")
        break

    
    

