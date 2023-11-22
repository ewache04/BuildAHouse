'''
Author name: Jeremiah E. Ochepo
last Edited: 3/3/2020 (10PM)
Description: Building A House GUI
'''
from graphics import *

def main():
    win = GraphWin('Shapes', 400, 400, autoflush=False)

    # Program Status Message
    msg = Text(Point(200.0, 20.0), 'House Information')
    msg.setFace('helvetica')
    msg.setStyle('bold')
    msg.setSize(12)
    msg.draw(win)

    color_List = ['black', 'yellow', 'red', 'blue', 'white']

    # Get Points and draw shapes
    p1 = win.getMouse().draw(win)
    p2 = win.getMouse().draw(win)

    def rectangle():
        shape = Rectangle(p1, p2)
        shape.setFill(color_List[0])
        shape.setOutline(color_List[4])
        shape.draw(win)

    rectangle()

    p3 = win.getMouse().draw(win)
    p4 = win.getMouse().draw(win)

    def triangle():
        shape = Polygon(p2, p3, p4)
        shape.setFill(color_List[2])
        shape.setOutline(color_List[4])
        shape.draw(win)

    triangle()

    p5 = win.getMouse().draw(win)
    p6 = win.getMouse().draw(win)

    def window():
        shape = Rectangle(p5, p6)
        shape.setFill(color_List[4])
        shape.setOutline(color_List[0])
        shape.draw(win)

    window()

    p7 = win.getMouse().draw(win)
    p8 = win.getMouse().draw(win)

    def front_door():
        shape = Rectangle(p7, p8)
        shape.setFill(color_List[4])
        shape.setOutline(color_List[0])
        shape.draw(win)

    front_door()

    msg.setText('Click any point to quit')
    pt = win.getMouse()
    win.close()

try:
    main()
except:
    pass
