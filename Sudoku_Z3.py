from z3 import *

def sudoko(instance):
    X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(9) ]
    for i in range(9) ]# Defining 9x9 matrix of integer variables

    cells_c  = [ And(1 <= X[i][j], X[i][j] <= 9)
             for i in range(9) for j in range(9) ]# each cell contains a value in {1, ..., 9}

    rows_c   = [ Distinct(X[i]) for i in range(9) ]# each row contains a digit at most once

    cols_c   = [ Distinct([ X[i][j] for i in range(9) ])
             for j in range(9) ]# each column contains a digit at most once

    sq_c     = [ Distinct([ X[3*i0 + i][3*j0 + j]
    for i in range(3) for j in range(3) ])
    for i0 in range(3) for j0 in range(3) ]# each 3x3 square contains a digit at most once

    sudoku_c = cells_c + rows_c + cols_c + sq_c

    instance_c = [ If(instance[i][j] == 0,True,X[i][j] == instance[i][j])
               for i in range(9) for j in range(9) ]#check if the cell from the instance is yet to be filled


    s = Solver()

    s.add(sudoku_c + instance_c)#add the constraints

    if s.check() == sat:
        m = s.model()#if model is SAT then we can find Satisfying assignment values
        r = [ [ m.evaluate(X[i][j]) for j in range(9) ]
          for i in range(9) ]
        print_matrix(r)
    else:
        print("failed to solve")


instance = ((0,0,0,0,9,4,0,3,0),
            (0,0,0,5,1,0,0,0,7),
            (0,8,9,0,0,0,0,4,0),
            (0,0,0,0,0,0,2,0,8),
            (0,6,0,2,0,1,0,5,0),
            (1,0,2,0,0,0,0,0,0),
            (0,7,0,0,0,0,5,2,0),
            (9,0,0,0,6,5,0,0,0),
            (0,4,0,9,7,0,0,0,0))

sudoko(instance)
