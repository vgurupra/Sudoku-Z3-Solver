# Sudoku-Z3-Solver

### Installation of Z3 and verification of installation
```
- pip install z3-solver
To verify the installation:
from z3 import *
>> s = Solver ()
>> s. check ()
SAT 
This verifies the proper installation of the Z3 in the system
```

#### Mathematical Representation of the Sudoku Constraints
```
-Represent all the cells as variables (9X9 = 81 of them). 
-Set the range of these variables from 1 to 9, inclusive. 
-Assert all variables in each row as distinct. 
-Assert all variables in each column as distinct. 
-Assert that in a region each variable is not equal to others. 
-Assign some variables values from the filled-up graph.
```

#### Satisfiability Constraints in Z3
```
-A formula/constraint F is valid if F always evaluates to true for any assignment of appropriate values to its uninterpreted symbols. 
-A formula/constraint F is satisfiable if there is some assignment of appropriate values to its uninterpreted symbols under which F evaluates to true.
-The command check returns sat when Z3 finds a solution for the set of asserted constraints. We say Z3 satisfied the set of constraints. 
-We say the solution is a model for the set of asserted constraints. A model is an interpretation that makes each asserted constraint true.
```
