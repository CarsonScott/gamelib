from .vectors import *
from .constants import *
import matplotlib.pyplot as plt
import numpy as np
import pygame
import math
import os

def all_equal(X):
	for i in range(1, len(X)):
		if X[i] != X[i-1]:
			return False
	return True

def clamp(x, low=0, high=1):
	return low if x < low else high if x > high else x

def cycle(x, low=0, high=1):
	if '.' in str(x):
		dec = len(str(x)) - list(str(x)).index('.') + 1
	else: dec = 0
	rng = high - low
	if x >= high:
		x = low + (x - low) % rng
	elif x < low:
		x = high - (low - x) % rng
	if dec != 0:
		m = 10 ** dec
		x = round(x * m) / m
	return x

def concatenate(*X):
	Y=[]
	for x in X:
		Y+=list(x)
	return Y

def sign(x):
	return -1 if x < 0 else 1 if x > 0 else 0

def compute_offset(A,B):
	offset=[B[i]-A[i] for i in range(len(A))]
	return offset

def compute_angle(A,B):
	dx,dy=compute_offset(B,A)
	angle=math.atan2(-dy,-dx)
	return angle

def compute_direction(A,B):
	a = compute_angle(A,B)
	return np.array([np.cos(a), np.sin(a)])

def translate_angle(a):
	if a >= math.pi:
		a = -math.pi + a % math.pi 
	elif a < -math.pi:
		a = math.pi - abs(a) % math.pi
	return a

def angle_difference(a,b):
	da = translate_angle(b-a)
	if (da + np.pi) > np.pi:
		da = (2*np.pi - (da + np.pi)) - np.pi
	return da

def compute_norm(vector):
	total=sum([vector[i]**2 for i in range(len(vector))])
	norm=math.sqrt(total)
	return norm

def compute_distance(A,B):
	offset=compute_offset(A,B)
	distance=compute_norm(offset)
	return distance

def compute_position(origin, distance, angle):
	x=origin[0]+math.cos(angle)*distance
	y=origin[1]+math.sin(angle)*distance
	position=P2Vector(x,y)
	return position

def get_mouse_position():
	return P2Vector(pygame.mouse.get_pos())

def load_image(filename, colorkey=None, rotation=None, scale=None):
	image=pygame.image.load(filename)
	if rotation!=None:image=pygame.transform.rotate(image, rotation)
	if scale!=None:image=pygame.transform.scale(image, scale)
	if colorkey!=None:image.set_colorkey(colorkey)
	return image

def parse_spritesheet(image, sprite_size):
	sprites=[]
	colorkey=image.get_colorkey()
	width,height=image.get_rect().size
	w,h=sprite_size
	for i in range(math.floor(height/h)):
		for j in range(math.floor(width/w)):
			x=j*w
			y=i*h
			sprite=image.subsurface(pygame.Rect(x,y,w,h))
			sprite.set_colorkey(colorkey)
			sprites.append(sprite)
	return sprites

def rotate_center(image, angle):
	orig_rect=image.get_rect()
	rot_image=pygame.transform.rotate(image, angle)
	rot_rect=orig_rect
	rot_rect.center=rot_image.get_rect().center
	rot_image=rot_image.subsurface(rot_rect).copy()
	return rot_image

def center_rect(bounding_rect, rect):
	width,height=bounding_rect.size
	w,h=rect.size
	x=width/2-w/2
	y=height/2-h/2
	return pygame.Rect(x,y,w,h)

def display_image(image):
	pygame.init()
	screen_size=image.get_rect().size 
	screen=pygame.display.set_mode(screen_size)
	running=True
	while running:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
		screen.fill((0,0,0))
		screen.blit(image, (0,0))
		pygame.display.flip()
	pygame.quit()

def display_animation(animation):
	pygame.init()
	max_w,max_h=(0,0)
	for image in animation.images:
		w,h=image.get_rect().size
		if w > max_w:max_w=w
		if h > max_h:max_h=h
	screen_size=(max_w,max_h)
	screen=pygame.display.set_mode(screen_size)
	clock=pygame.time.Clock()
	running=True
	while running:
		dt=clock.tick()/1000
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
		screen.fill((0,0,0))
		image=animation.update(dt)
		rect=center_rect(screen.get_rect(), image.get_rect())
		screen.blit(image, rect)
		pygame.display.flip()
	pygame.quit()

def draw_rect(target, color, rect, linewidth=0):
	size=P2Vector(rect.size)+P2Vector(linewidth,linewidth)*2
	colorkey=[255-x for x in color]
	surface=pygame.Surface(size)
	surface.set_colorkey(colorkey)
	pygame.draw.rect(surface, color, pygame.Rect(linewidth, linewidth, *rect.size), linewidth)
	position=P2Vector(rect.topleft)-P2Vector(linewidth,linewidth)
	target.blit(surface, position)

def draw_circle(target, color, position, radius, linewidth=0):
	size=P2Vector(radius,radius)*2+P2Vector(linewidth,linewidth)*2
	colorkey=[255-x for x in color]
	surface=pygame.Surface(size)
	surface.set_colorkey(colorkey)
	pygame.draw.circle(surface, color, [int(x/2) for x in size], radius, linewidth)
	position=P2Vector(position)-size/2
	target.blit(surface, position)

def get_bounding_rect(points):
	xmin,xmax,ymin,ymax=[None,None,None,None]
	for point in points:
		x,y=point
		if xmin==None:
			xmin=x
			xmax=x
			ymin=y
			ymax=y
		else:
			if x < xmin: xmin=x
			if x > xmax: xmax=x
			if y < ymin: ymin=y
			if y > ymax: ymax=y
	width=xmax-xmin
	height=ymax-ymin
	rect=pygame.Rect(xmin,ymin,width,height)
	return rect

def random_position(size):
	w,h=size
	return P2Vector(np.random.randint(w), np.random.randint(h))

def random_angle():
	return np.random.uniform(low=-math.pi, high=math.pi)

def random_string(size):
	chars='abcdefghijklmnopqrstuvwxyz0123456789'
	chars+=chars.upper()
	string=''
	for i in range(size):
		string+=np.random.choice(list(chars))
	return string

def surf_to_mat(surf):
	width,height=surf.get_rect().size
	shape=(height, width)
	mat=np.zeros(shape)
	for i in range(height):
		for j in range(width):
			mat[i][j]=surf.get_at((j,i))
	return mat

def mat_to_surf(mat):
	h, w = mat.shape
	surf = pygame.Surface((w, h))
	for y in range(h):
		for x in range(w):
			if not isinstance(mat[y][x], np.ndarray):
				color = [mat[y][x]] * 3
			else: color = mat[y][x]
			surf.set_at((x, y), color)
	return surf

def get_font_list():
	F=os.listdir(FONT_DIRECTORY)
	Y=[]
	for i in range(len(F)):
		file,ext=os.path.splitext(F[i])
		if ext=='.ttf':
			Y.append(os.path.join(FONT_DIRECTORY, F[i]))
	return Y

def load_font(filename, size):
	pygame.font.init()
	if '\\' not in filename:
		filename=os.path.join(FONT_DIRECTORY, filename)
	return pygame.font.Font(filename, size)

def render_font(string, position=[0,0], font=DEFAULT_FONT, antialias=1, color=(255,255,255)):
	if isinstance(font, str):font=load_font(font, DEFAULT_FONT_SIZE)
	surface=font.render(string, antialias, color)
	rect=surface.get_rect()
	rect.topleft=position
	return surface, rect

def print_template(screen_size=(640,480)):
	template='''
screen_size = np.array('''+str(screen_size)+''')
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

running = True
while running:
	dt = clock.tick()/1000
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

		elif event.type == pygame.KEYDOWN:
			pass

		elif event.type == pygame.MOUSEBUTTONDOWN:
			pass

	screen.fill((0,0,0))

	pygame.display.flip()

pygame.quit()
'''
	print(template)

def generate_agent_image(body_radius=64, head_radius=8, body_color=WHITE, head_color=BLUE):
	surface_size=P2Vector(2,2)*body_radius
	body_position=surface_size/2
	head_position=body_position+P2Vector(body_radius-head_radius, 0)
	surface=pygame.Surface(surface_size)
	surface.fill(MAGENTA)
	surface.set_colorkey(MAGENTA)
	pygame.draw.circle(surface, body_color, [int(x) for x in body_position], body_radius)
	pygame.draw.circle(surface, head_color, [int(x) for x in head_position], head_radius)
	return surface

def parse_spritesheet(image, rect):
	left,top,width,height=image.get_rect()
	x,y,w,h=rect
	surfaces=[]
	for x in range(0, width, w):
		for y in range(0, height, h):
			surface=image.subsurface(pygame.Rect(x,y,w,h))
			surfaces.append(surface)
	return surfaces

def key_pressed(key):
	return pygame.key.get_pressed()[key]



class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position



# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

# A* search
def astar_search(map, start, end):
 

    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
 
    def add_to_open(open, neighbor):
        for node in open:
            if (neighbor == node and neighbor.f >= node.f):
                return False
        return True
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            #path.append(start) 
            # Return reversed path
            return path[::-1]
        # Unzip the current node position
        (x, y) = current_node.position
        # Get neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)]
        # Loop neighbors
        for next in neighbors:
            # Get value from map
            if 0 <= next[0] < map.shape[0] and 0 <= next[1] < map.shape[1]:
                map_value = map[next]
                map_value = map[next]
                if(map_value == 1):
                    continue
                neighbor = Node(next, current_node)
                if(neighbor in closed):
                    continue
                neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
                neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
                neighbor.f = neighbor.g + neighbor.h
                if(add_to_open(open, neighbor) == True):
                    open.append(neighbor)
    return None