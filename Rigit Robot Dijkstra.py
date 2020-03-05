import numpy as np
import math
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.animation import FuncAnimation
from matplotlib import style


def take_input():
    print("Enter the Robot's Radius and Clearance (e.g 2 3) where 2 is Robot radius and 3 is clearance")
    R= [int(i) for i in input().split()]
    print("Enter Start followed by Goal co-ordinates x,y (e.g 5 4 230 270) where 5,4 are start points and 230,270 are goal points")
    C= [int(i) for i in input().split()]
    if (C[0]==C[2] and C[1]==C[3]): return print("Start point and Goal Point are same, Run Again to Restart")
    if not (C[0]>=0 and C[1]>=0 and C[0]<300 and C[1]<200): return print("Start point is out of bounds, Run Again to Restart")
    if not (C[2]>=0 and C[3]>=0 and C[2]<300 and C[3]<200): return print("Goal point is out of bounds, Run Again to Restart")
    elif check_if_valid(C[0],C[1],C[2],C[3],R[1]) ==1: return print("Start point lies inside an Obstacle, Run Again to Restart")
    elif check_if_valid(C[2],C[3],C[0],C[1],R[1]) == 1: return print("Goal point lies inside an Obstacle, Run Again to Restart")
    return C[0],C[1],C[2],C[3],R[0],R[1]

def draw_map():
    fig1, ax = plt.subplots()
    patches = []
    obstacle1 = mpatches.Polygon([[25,185],[75,185],[100,150],[75,120],[50,150],[20,120]], True)
    obstacle2 = mpatches.Polygon([[225,40],[250,25],[225,10],[200,25]], True)
    obstacle3 = mpatches.Polygon([[30.05,76.16],[100,38.66],[95,30],[25.05,67.5]], True)
    obstacle4 = mpatches.Circle((225, 150), 25)
    obstacle5= mpatches.Ellipse((150,100),80,40)
    patches.append(obstacle1)
    patches.append(obstacle2)
    patches.append(obstacle3)
    patches.append(obstacle4)
    patches.append(obstacle5)
    p = PatchCollection(patches, alpha=0.4)
    p.set_array(np.array([0,0,0,0,0]))
    ax.add_collection(p)
    plt.axis([0, 300, 0, 200])
    fig1.show()
    return fig1

def draw_trial_map():
    fig2, ax2 = plt.subplots()
    patches = []
    obstacle1 = mpatches.Polygon([[90,60],[110,60],[110,40],[90,40]], True)
    obstacle2 = mpatches.Circle((160, 50), 15)
    patches.append(obstacle1)
    patches.append(obstacle2)
    p = PatchCollection(patches, alpha=0.4)
    p.set_array(np.array([0,0]))
    ax2.add_collection(p)
    plt.axis([0, 200, 0, 100])
    fig2.show()

def up(x,y):
    if y<199:
        y=y+1
    return(x,y)
 
def down(x,y):
    if y>0:
        y=y-1
    return(x,y)
 
def left(x,y):
    if x>0:
        x=x-1
    return(x,y)
  
def right(x,y):
    if x<299:
        x=x+1
    return(x,y)
  
def up_left(x,y):
    if y<199 and x>0:
        x=x-1
        y=y+1
    return(x,y)
  
def up_right(x,y):
    if y<199 and x<299:
        x=x+1
        y=y+1
    return (x,y)

def down_left(x,y):
    if y>0 and x>0:
        x=x-1
        y=y-1
    return(x,y)

def down_right(x,y):
    if y>0 and x<299:
        x=x+1
        y=y-1
    return(x,y)


def dijkstra(xs,ys,xg,yg,Robot_Radius,Clearance_edge):
    # Robot Parameters
    clearance_center=Robot_Radius+Clearance_edge

    # Map
    draw_map()

    # Dijkstra Parameters
    nodes ={}
    for i in range(300):
        for j in range(200):
            nodes[i,j]=math.inf
    nodes[xs,ys]=0
    visited_nodes={}
    neighbours=deque([(xs,ys)])
    previous_node={}
    n=1



