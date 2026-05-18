N=4
def print_board(borad):
    for i in range(N):
        for j in range(N):
            print(borad[i][j],end=" ")
        print()

def solve(board,col,rows,upperDia,lowerDia):
    if col >= N:
        return True
    
    for i in range(N):
        if (rows[i]==False and lowerDia[i+col]==False and upperDia[N-1+col-i]==False):
            board[i][col]=1
            rows[i]=True
            lowerDia[i+col]=True 
            upperDia[N-1+col-i]=True

            if solve(board,col+1,rows,upperDia,lowerDia):
                return True
            
            board[i][col]=0
            rows[i]=False 
            lowerDia[i+col]=False
            upperDia[N-1+col-i]=False
    return False

def solveNQ():
    
    board=[[0 for i in range(N)]
           for j in range(N)]
    
    rows=[False]*N
    lowerDia=[False]*(2*N-1)
    upperDia=[False]*(2*N-1)

    if solve(board,0,rows,upperDia,lowerDia)==False:
        return False
    print("Solution exist")
    print_board(board)

    return True
solveNQ()