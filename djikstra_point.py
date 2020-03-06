import numpy as np
import sys
# This try-catch is a workaround for Python3 when used with ROS; 
# it is not needed for most platforms
try:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
    pass

import time
import heapq as h
from collections import defaultdict
from queue import PriorityQueue, deque
import math
class NodeInfo:
    """
    A class to store index, cost and node information with parent child relations

    ...
    Attributes
    ----------

    cost : int 
        a cost to move from one point to another based on action
    child_node : list
        a list of elements that will contain child node information
    parent_node : list
        a list of elements that will contain parent node information

    Methods
    -------
    None
    """
    def __init__(self, child_node, cost):
        """
        Parameters
        ----------
        cost : int 
        a cost to move from one point to another based on action
        child_node : list
            a list of elements that will contain child node information
        parent_node : list
            a list of elements that will contain parent node information
        """

        self.parent_node = None
        self.child_node = child_node
        self.cost = math.inf

def inside_obstacle(node):
    """
    This function check if the point is inside an obstacle

    Args:
    node: location of a node on map

    Returns:
        True, if not inside obstacles
    
    """
    x = node[0]
    y = node[1]
    if y<=(8/5)*x+28 and y<=(-37/70)*x+(643/7) and y>=(9/5)*x-141 and y>=(-19/35)*x+(571/7): return 1

    if ((x-150)/(40))**2+((y-100)/(20))**2<=1: return 1
    
    if y<=13*x-140 and y<=185 and y<=(-7/5)*x+290 and y>=(6/5)*x+30:
        if (y<=x+100 and y<=(-6/5)*x+210):
            f=0
        else:
            return 1
    
    if y<=(3/5)*x-95 and y>=(3/5)*x-125 and y<=(-3/5)*x+175 and y>=(-3/5)*x+145: return 1
    
    if (x-225)**2+(y-150)**2<=(25)**2: return 1
    return 0

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
    else:
        return None, None
    
    

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
    else:
        return None, None        

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
    else:
        return None, None

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
    else:
        return None, None

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
    else:
        return None, None

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
    else:
        return None, None

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
    else:
        return None, None

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
    else:
        return None, None

# def actions_move(action_type,node):
#     """
#     This function defines an action set and calls corresponding actions

#     Args:
#     action_type: string type variable that will give the action input
#     node: list of elements that represent a node.

#     Returns:
#         Will return a new node location and cost
#     """
#     if action_type == "U":
#         return action_move_up(node)
#     if action_type == "D":
#         return action_move_down(node)
#     if action_type == "L":
#         return action_move_left(node)
#     if action_type == "R":
#         return action_move_right(node)
#     if action_type == "UL":
#         return action_move_up_left(node)
#     if action_type == "UR":
#         return action_move_up_right(node)
#     if action_type == "DL":
#         return action_move_down_left(node)
#     if action_type == "DR":
#         return action_move_down_right(node)
#     else:
#         return None, None

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
        return None, None

def pop_queue_element(queue):
    min_a = 0
    for elemt in range(len(queue)):
        if queue[elemt].cost < queue[min_a].cost:
            min_a = elemt
    return queue.pop(min_a)

def find_node(point, queue):
    for elem in queue:
        if elem.child_node == point:
            return queue.index(elem)
        else:
            return None 

def make_path(node, goal):
    print("Inside make path to Goal:")
    p = list()
    p.append(node.child_node)
    parent = node.parent_node
    if parent is None:
        return p
    while parent is not None:
        p.append(parent.child_node)
        parent = parent.parent_node
    p_rev = list(reversed(p))
    p_rev.append(goal)
    return p_rev

def djikstra_search(start, goal):
    """
    This is the main function that will loop over all locations

    Args:
    node: location of a point on map

    Returns:

    """
    # goal_x = goal[0]
    # goal_y = goal[1]

    start_x = start.child_node[0]
    start_y = start.child_node[1]
    start_cost = start.cost
    start_node = (start_x, start_y)

    actions_set = ['R', 'D', 'L', 'U', 'UL', 'UR', 'DL', 'DR']
    # current_heap = PriorityQueue()
    # current_heap = defaultdict(list)
    # current_heap_cost = defaultdict(list)
    # current_heap.update({0: (start_node)})
    # current_heap_cost.update({0: start_cost})


    # current_heap.update({1: (9, 9)})
    # current_heap_cost.update({0: 0})

    # current_heap.update({2: (9,10)})
    # current_heap_cost.update({0: 1})

    # current_heap.update({3: (11, 11)})
    # current_heap_cost.update({0: 2})

    # current_heap.update({4: (4, 5)})
    # current_heap_cost.update({0: 3})

    
    # print([k for k,v in current_heap.items() if v == b][0])

    # current_heap.put(start)
    # current_heap = []
    current_heap = [start]

    # current_heap = deque([start])

    # h.heapify(current_heap)
    # h.heappush(current_heap, start)

    visited_nodes = defaultdict(list)
    # visited_nodes = PriorityQueue()
    # visited_nodes = list()
    # visited_nodes = []
    # h.heapify(visited_nodes)
    # count = 0
    # visited_nodes[0] = start
    
    #     key = min(current_heap, key=current_heap.get)    
    #     print("Key is " + str(key))

    i = 0
    count = 1
    while current_heap: 
        # print(type(pop_queue_element(current_heap).child_node))
        frontier_node = pop_queue_element(current_heap) # current_heap.get()
        if frontier_node.child_node == goal:
            print("Success Dude")
            return new_node.parent_node

        # visited_nodes.append(frontier_node.child_node)
        if frontier_node.child_node not in visited_nodes.values():
            # visited_nodes.update({i : frontier_node.child_node})
            visited_nodes[i] = frontier_node.child_node

        # h.heappush(visited_nodes, frontier_node.child_node)
        if frontier_node is not None:
            for action in actions_set:
                new_node_location, running_cost = actions_move(action, frontier_node.child_node)
                # print(i)
                i += 1
                # print(new_node_location)
                if new_node_location is not None:
                    # print("Here")
                    if new_node_location == goal:
                        print("Success")
                        return new_node.parent_node

                    new_node = NodeInfo(new_node_location, running_cost)

                    new_node.parent_node = frontier_node
                    
                    # print(new_node_location in next(iter(visited_nodes.values())))
                    # new_node_location not in visited_nodes.values()
                    if new_node_location not in visited_nodes.values(): #any(new_node_location in item for item in visited_nodes.queue): #new_node_location not in list(visited_nodes.values()):
                        print(new_node_location)
                        # print(new_node_location not in visited_nodes.values())
                        # print(new_node_location in visited_nodes.values())
                        new_node.cost = running_cost + new_node.parent_node.cost
                        # visited_nodes.put(new_node_location) 
                        # visited_nodes.append(new_node_location)
                        # h.heappush(visited_nodes, new_node_location)
                        # dup_list = [i for n, i in enumerate(visited_nodes) if i not in visited_nodes[n + 1:]]
                        if new_node_location not in visited_nodes.values():
                            # visited_nodes.update({i : frontier_node.child_node})
                            visited_nodes[i] = new_node_location

                        # visited_nodes.update({i : new_node_location})

                        current_heap.append(new_node)
                    else:
                        node_exist_index = find_node(new_node_location, current_heap)
                        if node_exist_index is not None:
                            temp_node = current_heap[node_exist_index]
                            if temp_node.cost > running_cost + new_node.parent_node.cost:
                                temp_node.cost = running_cost + new_node.parent_node.cost
                                temp_node.parent = frontier
                else:
                    continue
        print(i)
        # i +=1
    return None


def main():
    tic = time.time()
    start_node = NodeInfo((10, 10), 0)
    goal_node = (25, 15)

    if goal_node > (300, 200) or start_node.child_node > (300,200):
        print("Outside map of the robot. Please try again.")
        # main()
    elif start_node.child_node < (0, 0) or goal_node <= (0, 0):
        print("Outside the map of robot. Please try again.")
        # main()
    elif inside_obstacle(goal_node):
        print("Inside goal")
        print("Please try again.")
        # main()
    else:
        # print("if")
        final_goal_parent = djikstra_search(start_node, goal_node)
        if final_goal_parent is not None:
            nodes_list = make_path(final_goal_parent, goal_node)
            print(nodes_list)

    toc = time.time() # Compute time
    print("Time to compute is " + str((toc-tic)/60) + " mins")

main()