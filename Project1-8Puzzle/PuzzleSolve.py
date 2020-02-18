import numpy as np 
  
rows = int(input("Enter the number of rows:")) 
cols = int(input("Enter the number of columns:")) 
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a  
# single line separated by space 
entries = list(map(int, input().split())) 
  
# For printing the matrix 
gen_nodes = np.array(entries).reshape(rows, cols) 
# print(matrix) 

def blank_tile_location(node):
	original_node = node
	location = np.where(original_node == 0)
	for loc in zip(location[0],location[1]):
		print(loc)

blank_tile_location(gen_nodes)

