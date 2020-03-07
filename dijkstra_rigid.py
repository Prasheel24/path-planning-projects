import numpy as np
import math
import pygame
import sys
from collections import defaultdict,deque

# Take Input form user for Robot parameters and start and goal points
def take_input():
    print("Enter the Robot's Radius and Clearance (e.g 2 3) where 2 is Robot radius and 3 is clearance")
    R= [int(i) for i in input().split()]
    if len(R) != 2: sys.exit()
    print("Enter Start followed by Goal co-ordinates x,y (e.g 5 4 230 270) where 5,4 are start points and 230,270 are goal points")
    C= [int(i) for i in input().split()]
    if len(C) != 4 : sys.exit()
    # Check if inputs are valid
    if (C[0]==C[2] and C[1]==C[3]): return print("Start point and Goal Point are same, Run Again to Restart")
    if not (C[0]>=0 and C[1]>=0 and C[0]<300 and C[1]<200): return print("Start point is out of bounds, Run Again to Restart")
    if not (C[2]>=0 and C[3]>=0 and C[2]<300 and C[3]<200): return print("Goal point is out of bounds, Run Again to Restart")
    elif check_if_valid(C[0],C[1],C[2],C[3],R[1]) ==1: return print("Start point lies inside an Obstacle, Run Again to Restart")
    elif check_if_valid(C[2],C[3],C[0],C[1],R[1]) == 1: return print("Goal point lies inside an Obstacle, Run Again to Restart")
    return C[0],C[1],C[2],C[3],R[0],R[1]

# Convert y coordinate as per pygame window
def convert(x, y):
    return (x*3,(199-y)*3)

# Draw the map with pygame
def draw_map():
    pygame.init()
    size = (300*3, 200*3)
    frame = pygame.display.set_mode((300*3, 200*3))
    frame.fill([255,255,255])
    pygame.display.set_caption("Dijsktra Animation")
    frame.fill([255,255,255])

    # Draw Obstacles
    pygame.draw.polygon(frame,[200,100,255],[convert(225,40),convert(250,25),convert(225,10),convert(200,25)])
    pygame.draw.polygon(frame,[200,100,255],[convert(25,185),convert(75,185),convert(100,150),convert(75,120),convert(50,150),convert(20,120)])
    pygame.draw.polygon(frame,[200,100,255],[convert(30,76),convert(100,39),convert(95,30),convert(25,68)])
    pygame.draw.circle(frame,[200,100,255],(225*3, (199-150)*3), 25*3)
    pygame.draw.ellipse(frame,[200,100,255],(110*3, (199-120)*3, 80*3, 40*3))

    # Refresh
    pygame.display.flip()
    return frame

################## Define Action Set####################
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
########################################################

# Check if point is inside obstacle or clearance space using half-plane equations
def check_if_valid(x,y,xg,yg,clearance_center):
    # check Conditions for half-plane equations
    if y<=(8/5)*x+28+(clearance_center/(math.sin((math.pi/2)-(math.atan(8/5))))) and y<=(-37/70)*x+(643/7)+(clearance_center/(math.sin((math.pi/2)-(math.atan(37/70))))) and y>=(9/5)*x-141-(clearance_center/(math.sin((math.pi/2)-(math.atan(9/5))))) and y>=(-19/35)*x+(571/7)-(clearance_center/(math.sin((math.pi/2)-(math.atan(19/35))))): return 1
    if ((x-150)/(40+clearance_center))**2+((y-100)/(20+clearance_center))**2<=1: return 1
    if y<=13*x-140+(clearance_center/(math.sin((math.pi/2)-(math.atan(13))))) and y<=185+clearance_center and y<=(-7/5)*x+290+(clearance_center/(math.sin((math.pi/2)-(math.atan(7/5))))) and y>=(6/5)*x+30-(clearance_center/(math.sin((math.pi/2)-(math.atan(6/5))))):
        if (y<=x+100-(clearance_center/(math.sin((math.pi/2)-(math.atan(1))))) and y<=(-6/5)*x+210-(clearance_center/(math.sin((math.pi/2)-(math.atan(6/5)))))):
            f=0
        else:
            return 1
    if y<=(3/5)*x-95+(clearance_center/(math.sin((math.pi/2)-(math.atan(3/5))))) and y>=(3/5)*x-125-(clearance_center/(math.sin((math.pi/2)-(math.atan(3/5))))) and y<=(-3/5)*x+175+(clearance_center/(math.sin((math.pi/2)-(math.atan(3/5))))) and y>=(-3/5)*x+145-(clearance_center/(math.sin((math.pi/2)-(math.atan(3/5))))): return 1
    if (x-225)**2+(y-150)**2<=(25+clearance_center)**2: return 1
    return 0

# Create new neibhours using action set
def create_node(x,y,nodes,neighbours,neighbour_costs,previous_node):
    A=up(x,y)
    B=right(x,y)
    C=down(x,y)
    D=left(x,y)
    E=up_left(x,y)
    F=up_right(x,y)
    G=down_right(x,y)
    H=down_left(x,y)
    cost=nodes[x,y]
    # update the cost if new cost is low and append node in neighbour
    if A!=(x,y) and (A not in neighbours):
        neighbours.append((A[0],A[1]))
        if nodes[A[0],A[1]]>cost+1:
            nodes[A[0],A[1]]=cost+1
            previous_node[A[0],A[1]]=(x,y)
        neighbour_costs.append(nodes[A[0],A[1]])    
    if B!=(x,y) and (B not in neighbours):
        neighbours.append((B[0],B[1]))
        if nodes[B[0],B[1]]>cost+1:
            nodes[B[0],B[1]]=cost+1
            previous_node[B[0],B[1]]=(x,y)
        neighbour_costs.append(nodes[B[0],B[1]])   
    if C!=(x,y) and (C not in neighbours):
        neighbours.append((C[0],C[1]))
        if nodes[C[0],C[1]]>cost+1:
            nodes[C[0],C[1]]=cost+1
            previous_node[C[0],C[1]]=(x,y)
        neighbour_costs.append(nodes[C[0],C[1]])    
    if D!=(x,y) and (D not in neighbours):
        neighbours.append((D[0],D[1]))
        if nodes[D[0],D[1]]>cost+1:
            nodes[D[0],D[1]]=cost+1
            previous_node[D[0],D[1]]=(x,y)
        neighbour_costs.append(nodes[D[0],D[1]])
    if E!=(x,y) and (E not in neighbours):
        neighbours.append((E[0],E[1]))
        if nodes[E[0],E[1]]>cost+math.sqrt(2):
            nodes[E[0],E[1]]=cost+math.sqrt(2)
            previous_node[E[0],E[1]]=(x,y)
        neighbour_costs.append(nodes[E[0],E[1]])
    if F!=(x,y) and (F not in neighbours):
        neighbours.append((F[0],F[1]))
        if nodes[F[0],F[1]]>cost+math.sqrt(2):
            nodes[F[0],F[1]]=cost+math.sqrt(2)
            previous_node[F[0],F[1]]=(x,y)
        neighbour_costs.append(nodes[F[0],F[1]])   
    if G!=(x,y) and (G not in neighbours):
        neighbours.append((G[0],G[1]))
        if nodes[G[0],G[1]]>cost+math.sqrt(2):
            nodes[G[0],G[1]]=cost+math.sqrt(2)
            previous_node[G[0],G[1]]=(x,y)
        neighbour_costs.append(nodes[G[0],G[1]])
    if H!=(x,y) and (H not in neighbours):
        neighbours.append((H[0],H[1]))
        if nodes[H[0],H[1]]>cost+math.sqrt(2):
            nodes[H[0],H[1]]=cost+math.sqrt(2)
            previous_node[H[0],H[1]]=(x,y)
        neighbour_costs.append(nodes[H[0],H[1]])
    return neighbours,nodes,neighbour_costs

# Dijkstra algorithm
def dijkstra(xs,ys,xg,yg,Robot_Radius,Clearance_edge):
    
    # Draw Map and start and goal points
    frame=draw_map()
    pygame.draw.rect(frame,[255,0,0],[xs*3,(199-ys)*3,3,3])
    pygame.draw.rect(frame,[0,255,0],[xg*3,(199-yg)*3,3,3])
    pygame.display.flip()
    print("Maximum Time for solving is 18 mins")
    print("Solving . . .")
    
    # Initialize Robot Parameters
    clearance_center=Robot_Radius+Clearance_edge
    
    # Initialize Dijkstra Parameters
    nodes =defaultdict(list)
    for i in range(300):
        for j in range(200):
            nodes[i,j]=math.inf
    nodes[xs,ys]=0
    visited_nodes=[]
    neighbours=deque([(xs,ys)])
    neighbour_costs=[0]
    previous_node=defaultdict(list)
    
    # Iterate the algorithm
    while True:
        pygame.event.get()

        # Sort nodes as per cost (To create a priority queue)
        neighbours = [i for _,i in sorted(zip(neighbour_costs,neighbours))]
        neighbour_costs.sort()
        x=neighbours[0][0]
        y=neighbours[0][1]

        # check if node is within obstacle or already explored
        if check_if_valid(x,y,xg,yg,clearance_center)==0 and ((x,y) not in visited_nodes):
            visited_nodes.append((x,y))
            neighbours.pop(0)
            neighbour_costs.pop(0)

            # find neighbours
            neighbours,nodes,neighbour_costs=create_node(x,y,nodes,neighbours,neighbour_costs,previous_node)
        else:
            neighbours.pop(0)
            neighbour_costs.pop(0)

        # check if no path exits
        if len(neighbours)==0:
            print("There exist no solution for the given set of parameters")
            animate_exploration(xs,ys,xg,yg,previous_node,visited_nodes,frame)
            break
        
        # check if goal reached
        if x==xg and y==yg:
            print("Total Cost to Goal",nodes[xg,yg])
            visited_nodes.append((xg,yg))
            print("Goal Reached")
            print("Done Solving!")
            animate_exploration(xs,ys,xg,yg,previous_node,visited_nodes,frame)
            break

# Animate the exploration and backtracking
def animate_exploration(xs,ys,tempx,tempy,previous_node,visited_nodes,frame):
    print("Animating....")

    # Animate Exploration
    # draw visited nodes
    for i in range(0,len(visited_nodes)):
        pygame.event.get()
        pygame.draw.rect(frame,[0,0,255],[(visited_nodes[i][0])*3,(199-visited_nodes[i][1])*3,1,1])
        pygame.time.wait(1)
        pygame.display.flip()

    # Animate Backtracking
    # draw path
    pygame.draw.rect(frame,[255,0,0],[(tempx)*3,(199-tempy)*3,3,3])
    while tempx!=xs or tempy!=ys:
        pygame.event.get()
        pygame.draw.rect(frame,[255,0,0],[(tempx)*3,(199-tempy)*3,3,3])
        (tempx,tempy)=previous_node[tempx,tempy]
        pygame.time.wait(25)
        pygame.display.flip()
    pygame.draw.rect(frame,[255,0,0],[(tempx)*3,(199-tempy)*3,3,3])
    print("Done Animating!")

    # Prevent pygame window from crashing by checking event handler
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                running=False
                break
            
# Take input from user
xs,ys,xg,yg,Robot_Radius,Clearance_edge=take_input()
# Call Dijkstra Algorithm
dijkstra(xs,ys,xg,yg,Robot_Radius,Clearance_edge)
