def sum(x,y,z):
    return x+y+z
def board(xvalue,zvalue):
    zero="X" if xvalue[0] else('O' if zvalue[0] else 0)
    one="X" if xvalue[1] else('O' if zvalue[1] else 1)
    two="X" if xvalue[2] else('O' if zvalue[2] else 2)
    three="X" if xvalue[3] else('O' if zvalue[3] else 3)
    four="X" if xvalue[4] else('O' if zvalue[4] else 4)
    five="X" if xvalue[5] else('O' if zvalue[5] else 5)
    six="X" if xvalue[6] else('O' if zvalue[6] else 6)
    seven="X" if xvalue[7] else('O' if zvalue[7] else 7)
    eight="X" if xvalue[8] else('O' if zvalue[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    
    
def checkWin(xvalue,zvalue):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xvalue[win[0]],xvalue[win[1]],xvalue[win[2]])==3):
            print("X wins the match")
            return 1
        if(sum(zvalue[win[0]],zvalue[win[1]],zvalue[win[2]])==3):
            print("O wins the match")
            return 0
    return -1
    


if __name__=="__main__":
    xstate=[0,0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0,0]
    print("Welcome to Tic Tac Toe")
    turn=1
    while(True):
        board(xstate,zstate)
        if turn==1:
            print("X's chance")
            value=int(input("Please enter a value"))
            xstate[value]=1
        else:
            print("O's chance")
            value=int(input("Enter a value"))
            zstate[value]=1
        res=checkWin(xstate,zstate)
        if res!=-1:
            print("Match Over")
            break
        turn=1-turn