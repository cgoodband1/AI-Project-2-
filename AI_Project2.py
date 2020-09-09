import pygame
import math
from shapely.geometry import LineString, Polygon
#from queue import PriorityQueue
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
pygame.init()

display_width = 1000
display_height = 450

white = (255,255,255)
black = (0,0,0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(white)

#pixAr = pygame.PixelArray(gameDisplay)


pygame.draw.rect(gameDisplay, blue, (200,350,300,75), 3)

pygame.draw.polygon(gameDisplay, blue, ((275,175), (350,250), (400,25)), 3)

pygame.draw.polygon(gameDisplay, blue, ((210,300), (250,200), (300,340)), 3)

pygame.draw.polygon(gameDisplay, blue, ((150,290), (200,150), (150,50), (50,150), (75,270)),3) 

pygame.draw.polygon(gameDisplay, blue, ((550,390), (600,340), (510,250)),3) 

pygame.draw.polygon(gameDisplay, blue, ((400,225), (550,150), (475,90), (400,100)),3) 

pygame.draw.rect(gameDisplay, blue, (800,170,100,250),3)

pygame.draw.polygon(gameDisplay, blue, ((690,100), (750,70), (790,130), (600,300)),3) 

pygame.draw.polygon(gameDisplay, blue, ((680,290), (720,340), (720,390), (670,420), (640,390), (640,320)),3) 

pygame.draw.circle(gameDisplay, red, (50,240), 5)

pygame.draw.circle(gameDisplay, green, (950,370), 5)


poly2 = []
poly2.append(Polygon([(200,350),(500,350),(500,425),(200,425)]))
poly2.append(Polygon([(275,175), (350,250), (400,25)]))
poly2.append(Polygon([(210,300), (250,200), (300,340)]))
poly2.append(Polygon([(150,290), (200,150), (150,50), (50,150), (75,270)])) 
poly2.append(Polygon([(550,390), (600,340), (510,250)])) 
poly2.append(Polygon([(400,225), (550,150), (475,90), (400,100)]))
poly2.append(Polygon([(800,170),(900,170),(800,420),(900,420)]))
poly2.append(Polygon([(690,100), (750,70), (790,130), (600,300)])) 
poly2.append(Polygon([(680,290), (720,340), (720,390), (670,420), (640,390), (640,320)]))  


vertices2 = []
op2 = []
cl2 = []
o2 = []
c2 = []




class Node:
	def __init__(self, xCord, yCord):
		self.xCord = xCord
		self.yCord = yCord


vertices2.append(Node(950,370))

vertices2.append(Node(200,350))
vertices2.append(Node(500,350))
vertices2.append(Node(500,425))
vertices2.append(Node(200,425))

vertices2.append(Node(275,175))
vertices2.append(Node(350,250))
vertices2.append(Node(400,25))

vertices2.append(Node(210,300))
vertices2.append(Node(250,200))
vertices2.append(Node(300,340))

vertices2.append(Node(150,290))
vertices2.append(Node(200,150))
vertices2.append(Node(150,50))
vertices2.append(Node(50,150))
vertices2.append(Node(75,270))

vertices2.append(Node(550,390))
vertices2.append(Node(600,340))
vertices2.append(Node(510,250))

vertices2.append(Node(400,225))
vertices2.append(Node(550,150))
vertices2.append(Node(475,90))
vertices2.append(Node(400,100))

vertices2.append(Node(800,170))
vertices2.append(Node(900,170))
vertices2.append(Node(900,420))
vertices2.append(Node(800,420))

vertices2.append(Node(690,100))
vertices2.append(Node(750,70))
vertices2.append(Node(790,130))
vertices2.append(Node(600,300))

vertices2.append(Node(680,290))
vertices2.append(Node(720,340))
vertices2.append(Node(720,390))
vertices2.append(Node(670,420))
vertices2.append(Node(640,390))
vertices2.append(Node(640,320))

vertices2.append(Node(50,240))

print(len(vertices2))

def ception2(Node1):
	for x in range(len(vertices2)):
		#print(x)
		seg = LineString([(Node1.xCord,Node1.yCord), (vertices2[x].xCord, vertices2[x].yCord)])
		inter = False
		for p in poly2:

			if seg.intersects(p) == False and seg.touches(p) == True:

				inter = True
				
				
				#x = x + 1
				#o.append(vertices[x])
			elif seg.intersects(p) == True and seg.touches(p) == True:
				#print("TESSSSSSSSSSSSSSSSSSSSSSSSSSSSST")
				inter = True
				#x = x + 1
				#	print(x)
				#o.append(vertices[x])
			elif seg.intersects(p) == True and seg.touches(p) == False:
				inter = False
				break
				#o.append(vertices[x])
				#x = x + 1
		if inter:
			#print(inter)
			o2.append(vertices2[x])
			#x = x + 1

def gdistance(Node1, Node2):
	Node1 = Node1
	Node2 = Node2
	distance = math.sqrt((Node1.xCord - Node2.xCord)** 2 + (Node1.yCord - Node2.yCord) ** 2)
	return distance
	print(distance)

def hdistance2( Node1):
	Node1 = Node1
	distance = math.sqrt((Node1.xCord - vertices2[37].xCord)** 2 + (Node1.yCord - vertices2[37].yCord) ** 2)
	return distance
	print(distance)

def search2(Node1):
	for i in range(len(cl2)):
		if Node1 == cl2[i]:
			return True

def visted2():
	i = 0
	while i < len(o2):
		if search2(o2[i]) == True:
			print(o2[1])
			del o2[i]
			i = i +1
		else:
			i = i +1



c = 0
def total2(nBest, c):
	x = 0
	while x < len(o2):
		f = (gdistance(nBest, o2[x])) + (hdistance2(o2[x]))
		if f > c:
			x = x + 1
		else:
			op2.append([f,o2[x]])
			x = x + 1

def move2():
	new = op2[0]
	cl2.append(new[1])
	op2.clear()

def take_first(elem):
    return elem[0]

def drawLine(Node1,Node2):
	Node1 = Node1
	Node2 = Node2
	pygame.draw.line(gameDisplay,black,(Node1.xCord,Node1.yCord), (Node2.xCord,Node2.yCord), 5)

def printcl2():
	x = 0
	while x < (len(cl2) - 1):
		p1 = cl2[x]
		p2 = cl2[x + 1]
		drawLine(p1,p2)
		x = x + 1

#cnum = 300

#def csearch2(cnum):
#	print(len(op2))
#	x = 0
#	while x < len(op2):
#		node = op2[x]
#		current = node[0]
#		if cnum > current:
#			x = x + 1
#		else:
#			x = x + 1
c = 1000

def astar2():
	goal = vertices2[37]
	nBest = cl2[ len(cl2) - 1]
	if nBest == goal:
		print("fuck ya")
	else:
		ception2(nBest)
		visted2()
		total2(nBest,c)
		#print(op)
		op2.sort(key=take_first)
		#csearch2(cnum)
		#sort()
		x = 0
		#print("++++++++++++")
		while x < len(op2):
			next_item = op2[x]
			print(next_item)
			x = x + 1
		move2()


cl2.append(vertices2[0])
astar2()
astar2()
astar2()
print(len(o2))
astar2()
astar2()
astar2()
astar2()
astar2()
astar2()
astar2()
astar2()
astar2()
astar2()
astar2()
astar2()



printcl2()



x = 0
while x < len(op2):
	next_item = op2[x]
	print(next_item)
	x = x + 1


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	pygame.display.update()