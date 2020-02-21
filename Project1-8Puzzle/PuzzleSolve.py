import numpy as np 
import time
import os
# import collections 
# # https://thispointer.com/find-the-index-of-a-value-in-numpy-array/
# def blank_tile_location(node):
# 	location = np.where(node == 0)
# 	# https://www.dotnetperls.com/zip-python
# 	for loc in zip(location[0],location[1]):
# 		print(loc)

class NodeInfo:
	def __init__(self, cost, index, child_node, parent_node):
		self.cost = cost
		self.index = index
		self.parent_node = parent_node
		self.child_node = child_node

def solvability_check(node):
	# 8 1 2 0 4 3 7 6 5
	# https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
	# https://datawookie.netlify.com/blog/2019/04/sliding-puzzle-solvable/
	count = 0
	for i in range(8):
		for j  in range(i+1, 9):
			if node[j] and node[i] and node[i] > node[j]:
				count += 1
	if count % 2 == 0:
		return True
	else:
		return False

def get_location(node):
	new_node_loc = np.copy(node)
	index, = np.where(node == 0)
	return int(index)

def action_move_left(node):
	new_node_left = np.copy(node)
	index = get_location(new_node_left)
	# print(index)
	if (index % 3 != 0): # not (index == 0 or index == 3 or index == 6):
		new_node_left[index], new_node_left[index - 1] = new_node_left[index - 1], new_node_left[index]
	return new_node_left
	

def action_move_right(node):
	new_node_right = np.copy(node)
	index = get_location(new_node_right)
	# print(index)
	if (index % 3 < 2): # not (index == 2 or index == 5 or index == 8):
		new_node_right[index], new_node_right[index + 1] = new_node_right[index + 1], new_node_right[index]
	# print(node)
	return new_node_right

def action_move_up(node):
	new_node_up = np.copy(node)
	index = get_location(new_node_up)
	# print(index)
	if (index != 0 and index != 1 and index != 2 ): # not (index == 0 or index == 1 or index == 2):
		new_node_up[index], new_node_up[index - 3] = new_node_up[index - 3], new_node_up[index]
	# print(node)
	return new_node_up

def action_move_down(node):
	new_node_down = np.copy(node)
	index = get_location(new_node_down)
	# print(index)
	if (index != 6 and index != 7 and index != 8): # not (index == 6 or index == 7 or index == 8):
		new_node_down[index], new_node_down[index + 3] = new_node_down[index + 3], new_node_down[index]
	# print(node)
	return new_node_down

def actions_move(action_type,node):
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
	path = []
	path.append(node)
	parent_node = node.parent_node
	while parent_node is not None:
		path.append(parent_node)
		parent_node = parent_node.parent_node
	count = 0
	# for item in range(len(path)):
	# 	# print(path[item].parent_node)
	# 	count += 1
	path_list = []
	for item in path:
		# print(item.child_node)
		count += 1
		path_list.append(item.child_node)
	# final = list((path)).pop(0)
	# print(final.child_node)
	print("Optimal path states are " + str(count))
	return list(reversed(path_list))

def bfs_search(node):
	parent_nodes = []
	parent_nodes.append(node)
	# print(node)
	# print(type(parent_nodes))
	goal_node = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0]) # np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
	relative_nodes = []
	explored_nodes = [] #set() # []
	# child_nodes = np.asarray([])
	action_set = ["U", "D", "L", "R"]
	node_count = 0
	explored_nodes.append(parent_nodes[0].child_node.tolist())
	# explored_nodes.add(str(parent_nodes[0].child_node))
	# print(explored_nodes)
	# print(parent_nodes)
	while parent_nodes:
		# print(parent_nodes[0])
		sol_nodes = parent_nodes.pop(0)
		# print("1")
		# print(explorer.child_node)
		if sol_nodes.child_node.tolist() == goal_node.tolist():
			# np.array_equal(explorer.child_node.tolist(), goal_node.tolist()):
			print("Goal Reached!")
			return sol_nodes, relative_nodes, explored_nodes # explorer, path_nodes, explored_nodes

		for action in action_set:
			# print("2")
			# print(action)
			explorer_temp_node, cost = actions_move(action, sol_nodes.child_node)
			if any(explorer_temp_node != None) and (explorer_temp_node.tolist() != sol_nodes.child_node.tolist()):
				# print("3")
				node_count += 1
				child_nodes = NodeInfo(cost, node_count, np.array(explorer_temp_node), sol_nodes)
				# print(child_nodes.child_node)
				if not (child_nodes.child_node.tolist() in explored_nodes): # (not str(child_nodes.child_node) in explored_nodes): # all(item in child_nodes.child_node for item in explored_nodes): 
				# np.any(np.array_equal(x, child_nodes.child_node) for x in path_nodes): 
				# child_nodes.child_node not in path_nodes:
					# print("4")
					# print(explored_nodes)
					# print(child_nodes.child_node)
					parent_nodes.append(child_nodes)
					# print(parent_nodes[0])
					# path_nodes = np.concatenate((path_nodes, child_nodes.child_node))
					# path_nodes = np.append(np.asarray([path_nodes]), np.array([child_nodes.child_node]), axis=0)
					
					explored_nodes.append(child_nodes.child_node.tolist())
					# explored_nodes.add(str(child_nodes.child_node))
					# array append needs to be rectified
					# path_nodes = path_nodes.astype(np.int16)
					# print(path_nodes)
					relative_nodes.append(child_nodes)
					# explored_nodes = np.append(explored_nodes, child_nodes)
					# print(node_count)
					# explored_nodes = np.append(explored_nodes, child_nodes)
					# print(explored_nodes)
					if child_nodes.child_node.tolist() == goal_node.tolist(): # np.array_equal(child_nodes.child_node.tolist(), goal_node.tolist()):
						print("Goal Reached!")
						print("Total Moves are " + str(len(explored_nodes)-1))
						return child_nodes, relative_nodes, explored_nodes # child_nodes, path_nodes, explored_nodes

	return None, None

def complete_path_file(path_nodes):
	if os.path.exists("nodePath.txt"):
		os.remove("nodePath.txt")

	file = open("nodePath.txt", "a")

	for nodes in path_nodes:
		file.write(str(nodes[0]) + " " + str(nodes[3]) + " " + str(nodes[6]) + " " + str(nodes[1]) + " " + str(nodes[4]) + " " + str(nodes[7]) + " " + str(nodes[2]) + " " + str(nodes[5]) + " " + str(nodes[8]) + "\n")
	file.close()

def complete_node_file(explored):
	if os.path.exists("Nodes.txt"):
			os.remove("Nodes.txt")

	file = open("Nodes.txt", "a")
	# print("Total states reached: " + str(len(explored)))
	for nodes in explored:
		file.write(str(nodes[0]) + " " + str(nodes[1]) + " " + str(nodes[2]) + " " + str(nodes[3]) + " " + str(nodes[4]) + " " + str(nodes[5]) + " " + str(nodes[6]) + " " + str(nodes[7]) + " " + str(nodes[8]) + "\n")
	file.close()

def complete_node_info_file(relatives):
	if os.path.exists("NodesInfo.txt"):
			os.remove("NodesInfo.txt")

	file = open("NodesInfo.txt", "a")
	# print("Total states reached: " + str(len(explored)))
	for nodes in relatives:
		if nodes.parent_node != None:
			file.write(str(nodes.index) + "\t" + str(nodes.parent_node.index) + "\t" + str(nodes.cost) + "\n")
	file.close()


	# new_node_left = np.copy(action_move_left(node))
	# new_node_right = np.copy(action_move_right(node))
	# new_node_up = np.copy(action_move_up(node))
	# new_node_down = np.copy(action_move_down(node))

	# if not np.array_equal(node, goal_node):
	# 	if not (np.array_equal(new_node_left, goal_node) or np.array_equal(new_node_left, node)):
	# 		parent_nodes = np.append([parent_nodes], [new_node_left], axis=0)	
	# 	if not (np.array_equal(new_node_right, goal_node) or np.array_equal(new_node_right, node)):
	# 		parent_nodes = np.append(parent_nodes, [new_node_right], axis=0)	
	# 	if not (np.array_equal(new_node_up, goal_node) or np.array_equal(new_node_up, node)):
	# 		parent_nodes = np.append(parent_nodes, [new_node_up], axis=0)
	# 	if not (np.array_equal(new_node_down, goal_node) or np.array_equal(new_node_down, node)):
	# 		parent_nodes = np.append(parent_nodes, [new_node_down], axis=0)
	# else:
	# 	print("We are at Goal Node!")

	# # print(parent_nodes)
	# explored_nodes = parent_nodes[0]
	# # print(explored_nodes)
	# parent_nodes = np.delete(parent_nodes, 0, 0)
	# for explorer in parent_nodes:
	# 	explored_nodes = np.append(explored_nodes, explorer)
	# 	# print(explored_nodes)
	# 	for exploring_child in explored_nodes:
	# 		child_nodes = exploring_child
	# 		print(exploring_child)
	# 		print("!!!!")
	# 		new_node_left = np.copy(action_move_left(exploring_child))
	# 		new_node_right = np.copy(action_move_right(exploring_child))
	# 		new_node_up = np.copy(action_move_up(exploring_child))
	# 		new_node_down = np.copy(action_move_down(exploring_child))
	# 		print("!")
	# 		print(new_node_left)
	# 		print("~~~~")
	# 		if new_node_left not in explored_nodes:
	# 			child_nodes = np.vstack((child_nodes, new_node_left))
	# 		if new_node_right not in explored_nodes:
	# 			child_nodes = np.vstack((child_nodes, new_node_right))
	# 		if new_node_up not in explored_nodes:
	# 			child_nodes = np.vstack((child_nodes, new_node_up))
	# 		if new_node_down not in explored_nodes:
	# 			child_nodes = np.vstack((child_nodes, new_node_down))

	# print(explored_nodes)
	# print(child_nodes)
	# # Parent node Done
	# # explored_nodes = np.copy(parent_nodes[0])
	# # # print(explored_nodes)
	# # parent_nodes = np.delete(parent_nodes, 0, 0)
	# # for i in range(len(parent_nodes)):
	# # 	print(explored_nodes)
	# # 	print(i)
	# # 	if(i < len(parent_nodes)):
	# # 		print("~")
	# # 		print(parent_nodes[0])
	# # 		explored_nodes = np.append(explored_nodes, parent_nodes[0], axis=0)
	# # 		parent_nodes = np.delete(parent_nodes, 0, 0)
	# # 	# print("~")
	# # 	# print(parent_nodes)
	# # 	# for i in explorer:
	# # 	# 	explored_nodes = explorer

	# # print(explored_nodes)

	# # print(explored_nodes)
	# # while i<9:

	# # 	new_node_left = np.copy(action_move_left(explorer))
	# # 	if not np.array_equal(new_node_left, node):

	# # 	new_node_right = np.copy(action_move_right(explorer))
	# # 	new_node_up = np.copy(action_move_up(explorer))
	# # 	new_node_down = np.copy(action_move_down(explorer))	
		
	# # 	i += 1

def main():
	tic = time.time()
	original_parent_node = []
	# # Uncomment this for final run.
	# rows = int(input("Enter the number of rows:")) 
	# cols = int(input("Enter the number of columns:")) 
	# print("Enter the entries in a single line (separated by enter/return key): ")

	# n = rows * cols
	# for i in range(0, n):
	# 	element = int(input())
	# 	original_parent_node.append(element)
	# np.asarray(original_parent_node)

	# # Comment this for final run.
	# 1, 2, 3, 5, 6, 8, 0, 4, 7 300
	# 1, 2, 3, 5, 6, 0, 4, 7, 8 600
	# 0, 1, 3, 6, 2, 8, 5, 4, 7 3.2K
	# 6, 3, 0, 2, 1, 8, 5, 4, 7 19K
	# 6, 3, 8, 2, 4, 1, 5, 0, 7 94Kb
	# 6, 3, 8, 2, 4, 1, 0, 5, 7 1.41L
	# 6, 3, 8, 0, 4, 1, 2, 5, 7
	# 3, 0, 8, 6, 4, 1, 2, 5, 7
	# 6, 3, 8, 2, 4, 1, 0, 5, 7 infinite loop
	# 6, 4, 7, 8, 5, 0, 3, 2, 1 Hardest
	original_parent_node = np.array([1, 0, 3, 4, 2, 5, 7, 8, 6])

	# # Hardest Case 
	# original_parent_node = np.array([8, 6, 7, 2, 5, 4, 3, 0, 1])
	# original_parent_node = np.array([6, 4, 7, 8, 5, 0, 3, 2, 1])

	# # Unsolvable case	
	# original_parent_node = np.array([8, 1, 2, 0, 4, 3, 7, 6, 5])
	
	# print(original_parent_node)

	if not solvability_check(original_parent_node):
		print("This case is Unsolvable!")
		print("Please Try again")

		# Uncomment this for final run.
		# main()
	else:
		print("This case is Solvable!")
		# get_location(original_parent_node)
		print("The starting parent node is: " + str(original_parent_node))
		input_node = NodeInfo(0, 0, original_parent_node, None)

		goal_states, relatives, explored= bfs_search(input_node)
		path_nodes = make_path(goal_states)
		complete_path_file(path_nodes)
		complete_node_file(explored)
		complete_node_info_file(relatives)
		toc = time.time()
		print("Time Required is: " + str((toc-tic)/60) + " mins")
main()