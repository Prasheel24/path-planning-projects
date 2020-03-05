import numpy as np

def up(x,y):
    y=y-1
    return x,y
 
def down(x,y):
    y=y+1
    return x,y
 
def left(x,y):
    x=x-1
    return x,y
  
def right(x,y):
    x=x+1
    return x,y
  
def up_left(x,y):
    x=x-1
    y=y-1
    return x,y
  
def up_right(x,y):
    x=x+1
    y=y-1
    return x,y

def down_left(x,y):
    x=x-1
    y=y-1
    return x,y

def down_right(x,y):
    x=x+1
    y=y-1
    return x,y
