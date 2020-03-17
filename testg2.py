from g2 import *

#Create point
p1 = Point(0,0)
p2 = Point(0,100)
p3 = Point(100,100)
p4 = Point(100,0)

#Create nodes array
nodes = [p1,p2,p3,p4]

#Create chain junction, in this case with lines
chain = [0,'Line',1,'Line',2,'Line',3,'Line',0]

#Create path
path = Path(nodes, chain)

#Create drawing object
drawing = Drawing()
drawing.insertPath(0, path)
drawing.toSVG()
