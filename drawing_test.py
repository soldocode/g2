from g2 import *

#Create point for lines
l1 = Point(0,0)
l2 = Point(0,100)
l3 = Point(100,100)
l4 = Point(100,0)

#Create nodes array for lines
nodes = [l1, l2, l3, l4]

#Create chain junction, in this case with lines
chain = [0,'Line',1,'Line',2,'Line',3,'Line',0]

#Create point for the arc
a1 = Point(0,0)
a2 = Point(100,-100)
a3 = Point(200,0)

#Create arc
arc = Arc(a1, a2, a3)
arc_path = arc.discretize(10)

#Create path
lines_path = Path(nodes, chain)

#Create drawing object
drawing = Drawing()
drawing.insertPath(0, lines_path)
drawing.insertPath(1, arc_path)
drawing.toSVG()
