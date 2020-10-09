#dont_get_volunteered
#To help yourself get to and from your bunk every day, write a function 
# called answer(src, dest) which takes in two parameters: the source 
# square, on which you start, and the destination square, which is where 
# you need to land to solve the puzzle.  
# The function should return an integer representing the smallest number 
# of moves it will take for you to travel from the source square to the 
# destination square using a chess knight's moves (that is, two squares 
# in any direction immediately followed by one square perpendicular to 
# that direction, or vice versa, in an "L" shape).  Both the source and 
# destination squares will be an integer between 0 and 63, inclusive, 
# and are numbered like the example chessboard below:
#---------------------------------
#| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
#---------------------------------
#| 8 | 9 |10 |11 |12 |13 |14 |15 |
#---------------------------------
#|16 |17 |18 |19 |20 |21 |22 |23 |
#---------------------------------
#|24 |25 |26 |27 |28 |29 |30 |31 |
#---------------------------------
#|32 |33 |34 |35 |36 |37 |38 |39 |
#---------------------------------
#|40 |41 |42 |43 |44 |45 |46 |47 |
#---------------------------------
#|48 |49 |50 |51 |52 |53 |54 |55 |
#---------------------------------
#|56 |57 |58 |59 |60 |61 |62 |63 |
#---------------------------------

import collections

# helper method to check that x,y are inbounds on the grid.
def is_in_range(x,y):
    return 0<=x<=7 and 0<=y<=7

# The reason the approach uses a queue is to make this a BFS, whereas
#  a stack would be DFS, because it continues off the last position it literally just made.
#  DFS is suboptimal here for a couple reasons. We want to compute the most efficient solution, but 
#  I would consider a DFS more of a brute-force approach -- it would circle around itself repeatedly and fill
#  the board almost immediately - and suboptimally. We would need a check on every subsequent step to see if 
#  our current (new) step count is greater than or less than the prior x,y position - and we would have a lot of rewriting data.
#  If we were looking to just find a solution as fast as possible (realtime), DFS would be fine here, maybe even preferred. 
#  
#  With a BFS however, we know that if a board position has been touched at all, that touch was at least 1 step prior, and we can
#  skip it and never look at it again. This saves us a lot of writes and iterations, and makes the BFS more computationally efficient.
def answer(src, dest):
    if src==dest: # obvious check
        return 0
        
    # translate src,dest into positions on 8x8 grid
    src_x, src_y, dest_x, dest_y = src // 8, src % 8, dest // 8, dest % 8

    # define all possible horsie movements:
    positions = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]

    # define empty board and empty queue q:
    board = [[None for i in range(8)] for i in range(8)] # counter to hold # steps taken per node
    board[src_x][src_y] = 0

    q = collections.deque() # for BFS to hold to-be-traversed positions
    q.append((src_x,src_y)) 

    # iterate until we have reached the destination node.
    while True:
        (x, y) = q.popleft() # dequeue

        if (x, y) == (dest_x, dest_y):
            break # ta-dah

        # check all possible horsie positions, then queue them up if they have not been visited.
        # because we are using a breadth-first approach, that's the only check that is needed.
        for dx,dy in positions:
            x1,y1 = x + dx , y + dy

            if is_in_range(x1, y1) and board[x1][y1] is None: # ensure not yet visited a node
                board[x1][y1] = board[x][y] + 1
                q.append((x1, y1))
    
    return board[dest_x][dest_y]

    
if __name__ == '__main__':
    print(answer(5,46)) #expected: 4