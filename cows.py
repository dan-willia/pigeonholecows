import typing
import random

# Constants
RADIUS = 15
HEIGHT = 600
WIDTH = 600

class Cow:
    def __init__(self, name: str, color: tuple[int, int, int], 
                 pos: tuple[int, int], dir: tuple[int, int],
                 nearest_neighbor: 'Cow' = None):
        self.name=name
        self.color=color
        self.pos=pos
        self.dir=dir
        self.nearest_neighbor = nearest_neighbor
    
    def __str__(self):
        return f"Cow(name={self.name},color={self.color},pos={self.pos},dir={self.dir},nn={self.nearest_neighbor.name})"

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

    def set_nearest_neighbor(self,nearest_neighbor: 'Cow'):
        self.nearest_neighbor = nearest_neighbor

#----non-class functions----#

def create_cows():
    # a-j represent starting coordinates
    a,b=(random.choice(range(WIDTH-RADIUS+5)),random.choice(range(WIDTH-RADIUS+5)))
    c,d=(random.choice(range(WIDTH-RADIUS+5)),random.choice(range(WIDTH-RADIUS+5)))
    e,f=(random.choice(range(WIDTH-RADIUS+5)),random.choice(range(WIDTH-RADIUS+5)))
    g,h=(random.choice(range(WIDTH-RADIUS+5)),random.choice(range(WIDTH-RADIUS+5)))
    i,j=(random.choice(range(WIDTH-RADIUS+5)),random.choice(range(WIDTH-RADIUS+5)))
    # Cow 1
    cow_1 = Cow("cow_1", (255,0,0), (a,b), 
                    (random.choice(range(-5,6)), 
                    random.choice(range(-5,6))))
    # Cow 2
    cow_2 = Cow("cow_2", (130, 224, 170), (c,d),
                    (random.choice(range(-5,6)), 
                    random.choice(range(-5,6))))
    # Cow 3
    cow_3 = Cow("cow_3", (133, 193, 233), (e,f),
                    (random.choice(range(-5,6)), 
                    random.choice(range(-5,6))))
    # Cow 4
    cow_4 = Cow("cow_4", (237, 187, 153), (g,h),
                    (random.choice(range(-5,6)), 
                    random.choice(range(-5,6))))
    # Cow 5
    cow_5 = Cow("cow_5", (165, 105, 189), (i,j),
                    (random.choice(range(-5,6)), 
                    random.choice(range(-5,6))))
    Cows = [cow_1,cow_2,cow_3,cow_4,cow_5]
    return Cows

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
                    cur_cow.nearest_neighbor = other_cow

def get_cow_from_name(name: str, loc: list[Cow]) -> Cow:
    ''' assume unique names in input list; assume cow in list'''
    for cw in loc:
        if name==cw.name:
            return cw

def find_min_distance(loc: list[Cow]) -> Cow:
    ''' returns the cow with the nearest nearest neighbor in loc'''
    min=10**6
    for cw in loc:
        cur_min = distance(cw,cw.nearest_neighbor)
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