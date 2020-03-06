import numpy as np
import sys
# This try-catch is a workaround for Python3 when used with ROS; 
# it is not needed for most platforms
try:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
    pass

import time
import heapq

def inside_obstacle(node):
    """
    This function check if the point is inside an obstacle

    Args:
    node: location of a node on map

    Returns:
        True, if not inside obstacles
    
    """
    return False

def action_move_left(node):
    """
    This function is an action applied on a node to move left.

    Args:
    node: location of a node on map

    Returns:
        Will return a new node location and cost
    
    """
    cost = 1
    if node[0] > 0 and not inside_obstacle(node):
        return (node[0] - 1, node[1]), cost
    
    

def action_move_right(node):
    """
    This function is an action applied on a node to move right

    Args:
    node: location of a node on map

    Returns:
        Will return a new node location and cost
    """
    cost = 1
    if node[0] < 300 and not inside_obstacle(node):
        return (node[0] + 1, node[1]), cost

def action_move_up(node):
    """
    This function is an action applied on a node to move up.

    Args:
    node: location of a node on map

    Returns:
        Will return a new node location and cost
    """
    cost = 1
    if node[1] > 0 and not inside_obstacle(node):
        return (node[0], node[1] - 1), cost

def action_move_down(node):
    """
    This function is an action applied on a node to move down.

    Args:
    node: location of a node on map

    Returns:
        Will return a new node location and cost
    """
    cost = 1
    if node[1] < 200 and not inside_obstacle(node):
        return (node[0], node[1] + 1), cost

def action_move_up_left(node):
    """
    This function is an action applied on a node to move up left.

    Args:
    node: location of a node on map

    Returns:
        Will return a new node location and cost
    """
    cost = 1.4
    if node[0] > 0 and node[1] > 0 and not inside_obstacle(node):
        return (node[0] - 1, node[1] - 1), cost

def action_move_up_right(node):
    """
    This function is an action applied on a node to move up right.

    Args:
    node: location of a node on map

    Returns:
        Will return a new node location and cost
    """
    cost = 1.4
    if node[0] < 300 and node[1] > 0 and not inside_obstacle(node):
        return (node[0] + 1, node[1] - 1), cost

def action_move_down_left(node):
    """
    This function is an action applied on a node to move down left.

    Args:
    node: location of a node on map

    Returns:
        Will return a new node location and cost
    """
    cost = 1.4
    if node[0] > 0 and node[1] < 200 and not inside_obstacle(node):
        return (node[0] - 1, node[1] + 1), cost

def action_move_down_right(node):
    """
    This function is an action applied on a node to move down right.

    Args:
    node: location of a node on map

    Returns:
        Will return a new node location and cost
    """
    cost = 1.4
    if node[0] < 300 and node[1] < 200 and not inside_obstacle(node):
        return (node[0] + 1, node[1] + 1), cost


def actions_move(action_type,node):
    """
    This function defines an action set and calls corresponding actions

    Args:
    action_type: string type variable that will give the action input
    node: list of elements that represent a node.

    Returns:
        Will return a new node location and cost
    """
    if action_type == "U":
        return action_move_up(node)
    if action_type == "D":
        return action_move_down(node)
    if action_type == "L":
        return action_move_left(node)
    if action_type == "R":
        return action_move_right(node)
    if action_type == "UL":
        return action_move_up_left(node)
    if action_type == "UR":
        return action_move_up_right(node)
    if action_type == "DL":
        return action_move_down_left(node)
    if action_type == "DR":
        return action_move_down_right(node)
    else:
        return None


def djikstra_search(location):
    goal_x = location[0]
    goal_y = location[1]

    start_x = 0
    start_y = 0

    actions_set = ['U', 'D', 'L', 'R', 'UL', 'UR', 'DL', 'DR']

    return None


def main():
    tic = time.time()
    djikstra_search((10, 10))

    toc = time.time() # Compute time
    print("Time to compute is " + str((toc-tic)/60) + " mins")

main()