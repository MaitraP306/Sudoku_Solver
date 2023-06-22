from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
        """Function to take input a sudoku from stdin and return
        it as a list of lists.
        Each row of sudoku is one line.
        """
        sudoku= list()
        for _ in range(9):
                row = list(map(int, input().rstrip(" ").split(" ")))
                sudoku.append(row)
        return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
        """Helper function to print sudoku to stdout
        Each row of sudoku in one line.
        """
        for i in range(9):
                for j in range(9):
                        print(sudoku[i][j], end = " ")
                print()

# You have to implement the functions below
def ceil(a):
        k = (a + ((-a)%3) )/3
        return int(k)

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
        num = 3*(ceil(pos[0]) -1) + ceil(pos[1])
        return num


def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
        n = get_block_num(sudoku , pos)
        a = ceil(n) - 1
        b = n - 3*a -1
        pos1 = [pos[0] - 3*a , pos[1] - 3*b]
        k = 3*(pos1[0]-1) + pos1[1]
        return k
def get_block(sudoku:List[List[int]], x: int) -> List[int]:
        a = ceil(x) -1
        b = x - 3*a - 1
        L = sudoku[3*a : 3*a + 3]
        l = []
        for i in range (0 , 3):
                l  += L[i][3*b : 3*b +3]
        # your code goes here
        return l

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
        L = sudoku[i-1]
        return L

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
        l = []
        for i in range (0 , 9):
                l += [sudoku[i][x-1]]
        return l

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
        for i in range (0 , 9):
                for j in range (0 , 9):
                        if(sudoku[i][j] == 0 ):
                                return((i+1 , j+1))
        return((-1,-1))

def valid_list(lst: List[int])-> bool:
        for i in range (0 , 9 ):
                for j in range (0 , i ):
                        if((lst[i] == lst[j]) and (lst[i] != 0)):
                                return False
        return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
        booleanR = True
        booleanC = True
        booleanB = True
        for i in range (1 , 10):
                if(valid_list(get_row(sudoku , i)) == False):
                        booleanR = False
                elif(valid_list(get_column(sudoku , i)) == False):
                        booleanC = False
                elif(valid_list(get_block(sudoku , i)) == False):
                        booleanB = False
        return (booleanR and booleanC and booleanB)


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
        l = []
        L = sudoku
        for i in range (1 , 10):
                L[pos[0]-1][pos[1]-1] = i
                if(valid_sudoku(L) == True):
                        l.append(i)
                L[pos[0]-1][pos[1]-1] = 0
        return l


def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
        sudoku[pos[0]-1][pos[1]-1] = num
        return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
        sudoku[pos[0] -1][pos[1]-1] = 0
        return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
        k = find_first_unassigned_position(sudoku)
        if(k != (-1 , -1)):
                l = get_candidates(sudoku,k)
                for i in range (0 , len(l)):
                        a = l[i]
                        make_move(sudoku,k,a)
                        ma = sudoku_solver(sudoku)
                        if(ma[0] == False):
                                undo_move(sudoku,k)
                        else:
                                return (True,sudoku)
        else:
                if valid_sudoku(sudoku) == True:
                     return (True,sudoku)
        return (False, sudoku)
                        
                
        


# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
        print("Testcases for In Lab evaluation")
        print("Get Block Number:")
        print(get_block_num(sudoku,(4,4)))
        print(get_block_num(sudoku,(7,2)))
        print(get_block_num(sudoku,(2,6)))
        print("Get Block:")
        print(get_block(sudoku,3))
        print(get_block(sudoku,5))
        print(get_block(sudoku,9))
        print("Get Row:")
        print(get_row(sudoku,3))
        print(get_row(sudoku,5))
        print(get_row(sudoku,9))

# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

        # Input the sudoku from stdin
        sudoku = input_sudoku()

        # Try to solve the sudoku
        possible, sudoku = sudoku_solver(sudoku)

        # The following line is for the in-lab component
        #in_lab_component(sudoku)
        # Show the result of the same to your TA to get your code evaulated

        # Check if it could be solved
        if possible:
                print("Found a valid solution for the given sudoku :)")
                print_sudoku(sudoku)

        else:
                print("The given sudoku cannot be solved :(")
                print_sudoku(sudoku)
