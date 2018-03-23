from mypolygon import *

from swampy.TurtleWorld import *

def petal(t, r, angle):
    """Draws a petal using two arcs
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)



def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)


def move(t, length):
    """Moves Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down
    """
    pu(t)
    fd(t, length)
    pd(t)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)

wait_for_user()
