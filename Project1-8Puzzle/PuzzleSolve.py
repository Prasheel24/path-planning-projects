# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 2020
@author: Prasheel Renkuntla

@file:   PuzzleSolve.py
"""
# -*- coding: utf-8 -*-
import numpy as np 
import time
import os

class NodeInfo:
	"""
	A class to store index, cost and node information with parent child relations

	...
	Attributes
	----------

	cost : int 
		a cost to move from one point to another based on action
	index : int
		a unique id given to each node created
	child_node : list
		a list of elements that will contain child node information
	parent_node : list
		a list of elements that will contain parent node information

	Methods
	-------
	None
	"""
	def __init__(self, cost, index, child_node, parent_node):
		"""
		Parameters
		----------
		cost : int 
		a cost to move from one point to another based on action
		index : int
			a unique id given to each node created
		child_node : list
			a list of elements that will contain child node information
		parent_node : list
			a list of elements that will contain parent node information
		"""

		self.cost = cost
		self.index = index
		self.parent_node = parent_node
		self.child_node = child_node

def solvability_check(node):
    """
   	This is used to check the solvability of the given node.
   	It depends on the number of inversions. If odd, it is unsolvable.

    Args:
    node: list of elements that represent a node.

    Returns:
    	Will return True if there are even inversions in the code.
    """
    count = 0
    # check for inversions in the list element wise
    for i in range(8):
    	for j  in range(i+1, 9):
    		if node[j] and node[i] and node[i] > node[j]:
    			count += 1
    if count % 2 == 0:
    	return True
    else:
    	return False

def get_location(node):
    """
   	This function is used to get the location of the blank tile(0) in the given node

    Args:
    node: list of elements that represent a node.

    Returns:
    	Will return the index of 0 (type int)
    """
    new_node_loc = np.copy(node)
    # powerful where function from numpy library to find the index
    index, = np.where(node == 0)
    return int(index)

def action_move_left(node):
	"""
	This function is an action applied on a node to move the blank tile to left.

    Args:
    node: list of elements that represent a node.

    Returns:
    	Will return a list of new node with moved blank tile
    
	"""
	new_node_left = np.copy(node)
	index = get_location(new_node_left)
    # print(index)

	# Tiles on the first column of a node(matrix) cant move, and other can.
	if (index % 3 != 0): 
		new_node_left[index], new_node_left[index - 1] = new_node_left[index - 1], new_node_left[index]
	return new_node_left
	

def action_move_right(node):
	"""
   	This function is an action applied on a node to move the blank tile to the right

    Args:
    node: list of elements that represent a node.

    Returns:
    	Will return a list of new node with moved blank tile
    """
	new_node_right = np.copy(node)
	index = get_location(new_node_right)
	# print(index)

	# Tiles at index 2, 5, 8 can't move right
	if (index % 3 < 2): 
		new_node_right[index], new_node_right[index + 1] = new_node_right[index + 1], new_node_right[index]
	return new_node_right

def action_move_up(node):
	"""
   	This function is an action applied on a node to move the blank tile up.

    Args:
    node: list of elements that represent a node.

    Returns:
    	Will return a list of new node with moved blank tile
    """
	new_node_up = np.copy(node)
	index = get_location(new_node_up)
	# print(index)
	if (index != 0 and index != 1 and index != 2 ):
		new_node_up[index], new_node_up[index - 3] = new_node_up[index - 3], new_node_up[index]
	return new_node_up

def action_move_down(node):
	"""
	This function is an action applied on a node to move the blank tile down.

    Args:
    node: list of elements that represent a node.

    Returns:
    	Will return a list of new node with moved blank tile
	"""
	new_node_down = np.copy(node)
	index = get_location(new_node_down)
	# print(index)
	if (index != 6 and index != 7 and index != 8):
		new_node_down[index], new_node_down[index + 3] = new_node_down[index + 3], new_node_down[index]
	return new_node_down

def actions_move(action_type,node):
	"""
	This function defines an action set and calls corresponding actions

    Args:
    action_type: string type variable that will give the action input
    node: list of elements that represent a node.

    Returns:
    	Will return a list of new node with moved blank tile and its cost.
	"""
	if action_type == "U":
		return action_move_up(node), 0
	if action_type == "D":
		return action_move_down(node), 0
	if action_type == "L":
		return action_move_left(node), 0
	if action_type == "R":
		return action_move_right(node), 0
	else:
		return None

def make_path(node):
	"""
	This function makes a path from the start node to goal node.

    Args:
    node: list of elements that represent a node.

    Returns:
    	Will return a list of nodes that lie in the optimal path.
	"""
	path = []
	path.append(node)
	parent_node = node.parent_node
	# Iterate to find the relation between parent and child
	while parent_node is not None:
		path.append(parent_node)
		parent_node = parent_node.parent_node
	count = 0
	path_list = []
	for item in path:
		count += 1
		path_list.append(item.child_node)

	for item in list(reversed(path_list)):
		B = np.reshape(item, (-1, 3))
		print(B)

	# check  the final node in the path. 
	# final = list((path)).pop(0)
	# print(final.child_node)

	print("Optimal path states are " + str(count))
	return list(reversed(path_list))

def bfs_search(node):
	"""
	This is the main function that will loop over all nodes in the tree

    Args:
    node: list of elements that represent a node.

    Returns:
    goal_states: instance of the class with the nodes that are present in optimal path
    explored_nodes: list of all the explored nodes that have been traversed
    relative_nodes: instance of the class with all nodes in path with parent child relation
	"""
	parent_nodes = []
	parent_nodes.append(node)
	
	goal_node = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
	relative_nodes = [] # 
	explored_nodes = []
	action_set = ["U", "D", "L", "R"] # "U", "D", "L", "R"
	node_count = 0

	# Append the parent node in the explored node list
	explored_nodes.append(parent_nodes[0].child_node.tolist())

	# Loop on the parent nodes till goal state reached
	while parent_nodes:
		sol_nodes = parent_nodes.pop(0)

		# When goal node is the first node
		if sol_nodes.child_node.tolist() == goal_node.tolist():
			print("Goal Reached!")
			return sol_nodes, relative_nodes, explored_nodes # explorer, path_nodes, explored_nodes

		# Loop over the child nodes using the action set that generates all possible nodes
		for action in action_set:
			explorer_temp_node, cost = actions_move(action, sol_nodes.child_node)
			# Check if the node exists and avoid duplicates
			if any(explorer_temp_node != None) and (explorer_temp_node.tolist() != sol_nodes.child_node.tolist()):

				node_count += 1
				child_nodes = NodeInfo(cost, node_count, np.array(explorer_temp_node), sol_nodes)				
				relative_nodes.append(child_nodes)

				# check if the node has already been explored
				if not (child_nodes.child_node.tolist() in explored_nodes):
				
					parent_nodes.append(child_nodes)					
					explored_nodes.append(child_nodes.child_node.tolist())
					
					# Check if the current child node is goal.
					if child_nodes.child_node.tolist() == goal_node.tolist(): # np.array_equal(child_nodes.child_node.tolist(), goal_node.tolist()):
						print("Goal Reached!")
						print("Total explored states are " + str(len(explored_nodes)))
						return child_nodes, relative_nodes, explored_nodes # child_nodes, path_nodes, explored_nodes

	return None, None, None

def complete_path_file(path_nodes):
	"""
	This function creates/updates a file with nodes present in the optimal path

    Args:
    path_nodes: list of elements that represent a node.

    Returns:
    	Will write into a file with all nodes in the path.	
	"""
	if os.path.exists("nodePath.txt"):
		os.remove("nodePath.txt")

	file = open("nodePath.txt", "a")

	# Loop until all nodes are completed.
	for nodes in path_nodes:
		file.write(str(nodes[0]) + " " + str(nodes[3]) + " " + str(nodes[6]) + " " + str(nodes[1]) + " " + str(nodes[4]) + " " + str(nodes[7]) + " " + str(nodes[2]) + " " + str(nodes[5]) + " " + str(nodes[8]) + "\n")
	file.close()

def complete_node_file(explored):
	"""
	This function creates/updates a file with all explored nodes

    Args:
    explored: list of elements that represent a node.

    Returns:
    	Will write into a file with all explored nodes.
	"""
	if os.path.exists("Nodes.txt"):
			os.remove("Nodes.txt")

	file = open("Nodes.txt", "a")
	
	for nodes in explored:
		file.write(str(nodes[0]) + " " + str(nodes[3]) + " " + str(nodes[6]) + " " + str(nodes[1]) + " " + str(nodes[4]) + " " + str(nodes[7]) + " " + str(nodes[2]) + " " + str(nodes[5]) + " " + str(nodes[8]) + "\n")
	file.close()

def complete_node_info_file(relatives):
	"""
	This function creates/updates a file with node info

    Args:
    relatives: instance of a node that will be able to map between parent and child.

    Returns:
    	Will write into a file with child index, parent index and cost of each node traversed.
	"""
	if os.path.exists("NodesInfo.txt"):
			os.remove("NodesInfo.txt")

	file = open("NodesInfo.txt", "a")

	for nodes in relatives:
		if nodes.parent_node != None:
			if nodes.index == 0 and nodes.parent_node.index == 0: 
				file.write(str(nodes.index) + " " + str(0) + " " + str(nodes.cost) + "\n")
			if nodes.index != 1 and nodes.parent_node.index == 0:
				file.write(str(nodes.index) + " " + str(1) + " " + str(nodes.cost) + "\n")
			else:
				file.write(str(nodes.index) + " " + str(nodes.parent_node.index) + " " + str(nodes.cost) + "\n")
	file.close()

def main():
	"""
	This function takes the input, check solvability and calls BFS to reach goal state.

    Args:
    None

    Returns:
    None	
	"""
	tic = time.time() # To compute the time required.
	original_parent_node = []

	# Uncomment this for final run.
	# print("Enter the entries in a single line (separated by spaces in a row): ")
	# original_parent_node = [int(x) for x in input().split()]
	# original_parent_node = np.array(original_parent_node)

	# 1, 2, 3, 5, 6, 8, 0, 4, 7 
	# 1, 2, 3, 5, 6, 0, 4, 7, 8 
	# 0, 1, 3, 6, 2, 8, 5, 4, 7
	# 6, 3, 0, 2, 1, 8, 5, 4, 7
	# 6, 3, 8, 2, 4, 1, 5, 0, 7
	# 6, 3, 8, 2, 4, 1, 0, 5, 7
	# 6, 3, 8, 0, 4, 1, 2, 5, 7
	# 3, 0, 8, 6, 4, 1, 2, 5, 7
	# 6, 3, 8, 2, 4, 1, 0, 5, 7
	# 6, 4, 7, 8, 5, 0, 3, 2, 1 Hardest
	# 8, 6, 7, 2, 5, 4, 3, 0, 1 Hardest

	# # Comment these for final run.
	# # Hardest Case 
	original_parent_node = np.array([8, 6, 7, 2, 5, 4, 3, 0, 1])
	# original_parent_node = np.array([6, 4, 7, 8, 5, 0, 3, 2, 1])

	# # Unsolvable case	
	# original_parent_node = np.array([8, 1, 2, 0, 4, 3, 7, 6, 5])
	
	# original_parent_node = np.array([6, 3, 8, 2, 4, 1, 0, 5, 7])
	# print(original_parent_node)

	# Check solvability of the node
	if not solvability_check(original_parent_node):
		print("This case is Unsolvable!")
		print("Please Try again")
		# # Uncomment this for final run.
		# main()
	else:
		print("This case is Solvable!")
		print("The starting parent node is: " + str(original_parent_node))

		# Create an instance of the parent/start node.
		input_node = NodeInfo(0, 0, original_parent_node, None)

		goal_states, relatives, explored= bfs_search(input_node)

		# Create a path from the goal_states
		path_nodes = make_path(goal_states)

		# Write into required files
		complete_path_file(path_nodes)
		complete_node_file(explored)
		complete_node_info_file(relatives)

		toc = time.time() # Compute time
		print("Time to compute is " + str((toc-tic)/60) + " mins")

# Call the main function to start BFS search to find optimal path on 8puzzle
main()
