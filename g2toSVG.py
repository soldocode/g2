from svgpathtools import Path, Line
import svgwrite
import g2

def g2toSVG(scene):
    count = 0
    filename = 'test.svg'
    dwg = svgwrite.Drawing(filename, profile='tiny')
    for element in scene:
        segements = []
        for geometries in element.geometries:
            if geometries[0] == 'Line':
                p1 = str(element.nodes[geometries[1]].x) + '+' + str(element.nodes[geometries[1]].y) + 'j'
                p2 = str(element.nodes[geometries[2]].x) + '+' + str(element.nodes[geometries[2]].y) + 'j'
                segements.append(Line(p1, p2))
        path = Path(*segements)
        print(path)
        svgwrite.path.Path(d=path.d(), stroke='black', fill='none')
        count+=1
    dwg.save()
    print("Saved " + filename + " with " + str(count) + " element")
