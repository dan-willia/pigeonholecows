import typing
import random

# Constants
RADIUS = 15
HEIGHT = 600
WIDTH = 600

class Cow:
    def __init__(self, name: str, color: tuple[int, int, int], 
                 pos: tuple[int, int], dir: tuple[int, int],
                 nearest_neighbor: tuple[str, float] = None):
        self.name=name
        self.color=color
        self.pos=pos
        self.dir=dir
        self.nearest_neighbor = nearest_neighbor
    
    def __str__(self):
        return f"Cow(name={self.name},color={self.color},pos={self.pos},dir={self.dir},nn={self.nearest_neighbor})"

    def update_pos(self):
        x,y=self.pos
        dx,dy=self.dir
        x+=dx
        y+=dy
        self.pos=x,y

        # Bounce off wall
        if x - RADIUS <= 0 or x + RADIUS >= WIDTH:
            x,y=self.dir
            self.dir=-x,y
        if y - RADIUS <=0 or y + RADIUS >= HEIGHT:
            x,y=self.dir
            self.dir=x,-y

    def set_nearest_neighbor(self,nearest_neighbor: tuple[str, float]):
        self.nearest_neighbor = nearest_neighbor

#----non-class functions----#

def distance(cow1: Cow, cow2: Cow) -> float:
    # calculates distance between two cows
    x1,y1=cow1.pos
    x2,y2=cow2.pos

    rad = (x1-x2)**2 + (y1-y2)**2
    d = rad**(1/2)
    
    return d

def find_nearest_neighbor(loc: list[Cow]) -> None:
    '''
    calculates the nearest neighbor of each cow in the list, and updates each cow's attribute accordingly
    '''
    for cur_cow in loc:
        min = 10**5
        for other_cow in loc:
            if other_cow != cur_cow:
                d=distance(cur_cow, other_cow)
                if d<min:
                    min=d
                    cur_cow.nearest_neighbor = other_cow.name, d

def get_cow_from_name(name: str, loc: list[Cow]) -> Cow:
    ''' assume unique names in input list; assume cow in list'''
    for cw in loc:
        if name==cw.name:
            return cw

def find_min_distance(loc: list[Cow]) -> Cow:
    ''' returns the cow with the nearest nearest neighbor in loc'''
    min=10**6
    for cw in loc:
        cur_min = cw.nearest_neighbor[1]
        if cur_min<min:
            min=cur_min
            ret=cw
    return ret

def change_direction(i: int, loc: list[Cow]) -> None:
    ''' updates dx/dy of Cows based on i '''
    dx = random.choice(range(-5,6))
    dy = random.choice(range(-5,6))
    if i == 1:
        loc[0].dir = dx,dy
    elif i == 20:
        loc[1].dir = dx,dy
    elif i == 40:
        loc[2].dir = dx,dy
    elif i == 60:
        loc[3].dir = dx,dy
    elif i == 80:
        loc[4].dir = dx,dy