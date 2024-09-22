from OpenGL.GL import glBegin, glEnd, glMatrixMode, glVertex3f, glColor3f, glClear, glFlush, GL_COLOR_BUFFER_BIT, glRotatef
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def draw():
    xrot = 45
    yrot = 45
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glutWireCube(0.7)
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Cube")
glutDisplayFunc(draw)
glutMainLoop()