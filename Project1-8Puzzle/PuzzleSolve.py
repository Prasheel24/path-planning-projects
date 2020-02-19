import numpy as np 

# # https://thispointer.com/find-the-index-of-a-value-in-numpy-array/
# def blank_tile_location(node):
# 	location = np.where(node == 0)
# 	# https://www.dotnetperls.com/zip-python
# 	for loc in zip(location[0],location[1]):
# 		print(loc)

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

def action_move_left(node):
	new_node = []
	index, = np.where(node == 0)
	print(index)
	if not (index == 0 or index == 3 or index == 6):
		node[index], node[index - 1] = node[index - 1], node[index]
	print(node)
	return node

def action_move_right(node):
	new_node = []
	index, = np.where(node == 0)
	# print(index)
	if not (index == 2 or index == 5 or index == 8):
		node[index], node[index + 1] = node[index + 1], node[index]
	# print(node)
	return node

def action_move_up(node):
	new_node = []
	index, = np.where(node == 0)
	# print(index)
	if not (index == 0 or index == 1 or index == 2):
		node[index], node[index - 3] = node[index - 3], node[index]
	# print(node)
	return node

def action_move_down(node):
	new_node = []
	index, = np.where(node == 0)
	# print(index)
	if not (index == 6 or index == 7 or index == 8):
		node[index], node[index + 3] = node[index + 3], node[index]
	# print(node)
	return node

def main():
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
	original_parent_node = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])

	# # Hardest Case 
	# original_parent_node = np.array([8, 6, 7, 2, 5, 4, 3, 0, 1])
	# original_parent_node = np.array([6, 4, 7, 8, 5, 0, 3, 2, 1])

	# # Unsolvable case	
	# original_parent_node = np.array([8, 1, 2, 0, 4, 3, 7, 6, 5])
	
	print(original_parent_node)

	if not solvability_check(original_parent_node):
		print("This case is Unsolvable!")
		print("Please Try again")

		# Uncomment this for final run.
		# main()
	else:
		print("This case is Solvable!")
		# action_move_left(original_parent_node)
		# action_move_right(original_parent_node)
		# action_move_up(original_parent_node)
		# action_move_down(original_parent_node)


main()