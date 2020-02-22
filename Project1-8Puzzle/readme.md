### Path Planning Project 1: 8 Puzzle

## Overview:
This project explores the basic application of a Breadth First Algorithm to search the optimal way to solve the 8 Puzzle. The data structure used here is primarily a List.

## Author:
* **Prasheel Renkuntla** [GitHub](https://github.com/Prasheel24)
<br> M.Eng. Robotics Student, University of Maryland College Park. Interested in Research of Autonomous Planning and Controls for Autonomous Robots. 

## Algorithm Overview:
The Breadth First Search (BFS) Algorithm is one of the many ways to search a tree to find a feasible optimal path. It falls under the Systematic search based algorithms. It has good application in the field of Robotics like search a maze, etc.

<br>As wikipedia says, this algorithm starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. There are different data structures in python that can be used to handle this problem like Lists, Sets, and Dicts. The implementation of this project is based on Lists. There are some cases where the number of inversions in the list are odd, i.e to count the tiles preceding the another with lower number. Reference below shows a good explanation of it. If inversions in the start node are odd, then the combination is Unsolvable, like - [8, 1, 2, 0, 4, 3, 7, 6, 5].

There are four sets of Actions- Up(U), Left(L), Down(D), Right(R). The code depends on the order of how these actions are called. For a given combination, say U, L, R, D, and start node - [1 0 3 4 2 5 7 8 6], the code might solve the puzzle in 19 moves, whereas for combination like L, R, U, D, it solves in 22 moves. There is a tradeoff in deciding on the combination of these actions and the time taken to reach the goal state [1, 2, 3, 4, 5, 6, 7, 8, 0]. This implementation even solves the code for the hard cases where 31 moves are required to reach the Goal state. 

The general flow is as follows-
Consider a node, 
1 0 3 

4 2 5 

7 8 6. 

This blank tile(0) is present at the center of first row where the outer loop starts. Now from our action set sequence (U, D, L, R), the first possible node will be D, and we get a node like B-

     1 2 3   	1 0 3

B =  4 0 5,  C = 4 2 5

     7 8 6		7 8 6

Then, the algorithm will get the new location of blank tile i.e at the center of the matrix. Here, from the four actions (U, L, D, R), the inner loop will explore the 4 possible states as the blank tile will move in all directions and result in C at first. Then, the loop reiterates, and we start with parent node as B and so on.

## Functions-
* solvability_check - This function checks if the input start node is solvable or not on the basis of the inversions in the node. It returns a flag True if it is solvable.

* action_move_left - This is one of the action sets that will ove the blank tile (our case 0) to left of its position. Similar to this we will have action_move_right, action_move_up and action_move_down to move the blank tile in the right, up and down direction. It returns a new node with the new location of the tile. 

* actions_move - This is class that will is used as a wrapper over the four functions described above, which will call an action based on the input given. 

* make_path - This is the backtracking function, which will find the parent nodes of the children based on a bottom down approach. It returns the list with nodes in the optimal path.

* bfs_search - This is the main the function which runs the BFS algorithm. The BFS will search the code in a while loop on the availability of the nodes present in the parent_node list. Then, inside this loop, a for loop is applied to get the child nodes of the current parent node. After checking if the child node is not present in the explored_nodes and if the node is the goal node, the final solution along with the relatives and visited nodes is given as the output. Here, relatives are the nodes having the parent child relation for each node in the tree. 

* complete_path_file - This is the file manipulation function to write the nodes from the optimal path into nodePath.txt file.

* complete_node_file - This is a function to write the overall nodes used in the search algorithm into nodes.txt.

* complete_node_info_file - This is a function to write the node info having the parent child relationship. This is a scalable code which can be used to implement other algorithms where cost of going to each node is also considered.

* main - This is the main function that will take the input from user and start the BFS search to reach the goal node.

## Dependencies:
* Python3.5
* Ubuntu 16.04(Preferable) / Windows 10 support exists.
* numpy - to convert the list into an array and to have better computations than a list.
* os - to manipulate files and store the generated data like nodes, optimal path, etc.
* time - to calculate the time taken by the code.

## Build and Run:
Open a terminal/command window in the same folder as of the project file "PuzzleSolve.py"
Run the following command-
```
python3.5 PuzzleSolve.py
```

You will require to give the start node information as shown below (press enter after giving each number)-
1 0 3 4 2 5 7 8 6 

After the complete execution of the code, you must see a message with Goal reached!
Total moves
Optimal path states
Time to compute

## References:
* Wikipedia BFS - https://en.wikipedia.org/wiki/Breadth-first_search
* Time Complexity of DS in python - https://medium.com/fintechexplained/time-complexities-of-python-data-structures-ddb7503790ef
* Hardest 8 puzzle node - http://w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/
* Solvability Check - https://datawookie.netlify.com/blog/2019/04/sliding-puzzle-solvable/
* Inversions - https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable
