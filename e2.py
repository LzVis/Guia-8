tictactoe = [[2,2,2],
             [0,2,1],
             [0,0,1]]

def columna(matriz):
    if (matriz[0][0]==matriz[1][0]==matriz[2][0] and matriz[0][0]!=0):
        print(f"El jugador {"1" if matriz[0][0]==1 else "2"} a ganado")
    elif (matriz[0][1]==matriz[1][1]==matriz[2][1] and matriz[1][1]!=0):
        print(f"El jugador {"1" if matriz[0][1]==1 else "2"} a ganado")
    elif (matriz[0][2]==matriz[1][2]==matriz[2][2] and matriz[0][2]!=0):
        print(f"El jugador {"1" if matriz[0][2]==1 else "2"} a ganado")
        
if ( (tictactoe[0][0]==tictactoe[1][1]==tictactoe[2][2]  or tictactoe[0][2]==tictactoe[1][1]==tictactoe[2][0]) and tictactoe[1][1]!=0 ):
    print(f"El jugador {"1" if tictactoe[1][1]==1 else "2"} a ganado")
columna(tictactoe)
transpuesta = [list(fila) for fila in zip(*tictactoe)]
columna(transpuesta)