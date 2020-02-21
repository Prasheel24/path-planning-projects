Path Planning Project 1: 8 Puzzle

Overview:
This project explores the basic application of a Breadth First Algorithm to search the optimal way to solve the 8 Puzzle. The data structure used here is primarily a List.

Author:
Prasheel Renkuntla
-> M.Eng. Robotics Student, University of Maryland College Park. 
-> Interested in research in Planning and Controls for Autonomous Robots. 

Algorithm Overview:
The Breadth First Search (BFS) Algorithm is one of the many ways to search a tree to find a feasible optimal path. It falls under the Systematic search based algorithms. It has good application in the field of Robotics like search a maze, etc.

As Wikipedia says, this algorithm starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. There are different data structures in python that can be used to handle this problem like Lists, Sets, and Dicts. The implementation of this project is based on Lists.

There are four sets of Actions- Up(U), Left(L), Down(D), Right(R). The code depends on the order of how these actions are called. For a given combination, say U, L, R, D, and start node - [1 0 3 4 2 5 7 8 6], the code might solve the puzzle in 19 moves, whereas for combination like L, R, U, D, it solves in 22 moves. There is a tradeoff in deciding on the combination of these actions and the time taken to reach the goal state [1, 2, 3, 4, 5, 6, 7, 8, 0]. This implementation even solves the code for the hard cases where 31 moves are required to reach the Goal state. 

Dependencies:
-> Python3.5
-> Ubuntu 16.04(Preferable) / Windows 10 support exists.
-> numpy - to convert the list into an array and to have better computations than a list.
-> os - to manipulate files and store the generated data like nodes, optimal path, etc.
-> time - to calculate the time taken by the code.

Build and Run:
Open a terminal/command window in the same folder as of the project file "PuzzleSolve.py"
Run the following command-
"python3.5 PuzzleSolve.py"

You will be asked to input the number of rows and columns.
Then you will require to give the start node information as shown below (press enter after giving each number)-
1 0 3 4 2 5 7 8 6 

After the complete execution of the code, you must see a message with Goal reached!
Total moves
Optimal path states
Time to compute

References:
-> Wikipedia BFS - https://en.wikipedia.org/wiki/Breadth-first_search
-> Time Complexity of DS in python - https://medium.com/fintechexplained/time-complexities-of-python-data-structures-ddb7503790ef
-> Hardest 8 puzzle node - http://w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/