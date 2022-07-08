from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time, sys

ANGLE = 0
FLAG_ROTATION = True
X_AXIS, Y_AXIS, Z_AXIS = 0, 0, 0
STARTTIME = time.time()

def display(clear=True):
	global ANGLE, STARTTIME
	global X_AXIS, Y_AXIS, Z_AXIS
	if clear:
		glClearColor(0.5, 0.5, 0.5, 0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	x, y, width, height = glGetDoublev(GL_VIEWPORT)
	gluPerspective(
		45,
		width/float(height or 1),
		.25,
		200,
	)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(
		0,1,20,
		0,0,0,
		0,1,0,
	)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_3(.8,.8,.3))
	glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(1,1,3,0))
	glEnable(GL_LIGHT0)
	
	glTranslatef(X_AXIS, Y_AXIS, Z_AXIS)
	if FLAG_ROTATION:
		ANGLE = rotation(current_angle=ANGLE, period=1)
	else:
		glRotatef(ANGLE, 0, 1, 0)
	STARTTIME = time.time()
	glutWireCube(10)
	glutSwapBuffers()

def rotation(current_angle, period = 30):
	global STARTTIME
	angle = ((((time.time() - STARTTIME) % period) / period) * 360 + current_angle) % 360
	glRotatef(angle, 0, 1, 0)
	return angle

def mouse_pressed(button,state,x,y):
	global FLAG_ROTATION
	if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
		FLAG_ROTATION = not FLAG_ROTATION

def key_pressed(key, x, y):
	global X_AXIS, Y_AXIS
	if key == b'w':
		Y_AXIS = Y_AXIS + 1
	elif key == b's':
		Y_AXIS = Y_AXIS - 1
	elif key == b'a':
		X_AXIS = X_AXIS - 1
	elif key == b'd':
		X_AXIS = X_AXIS + 1

if __name__ == "__main__":
	import sys
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow('Cube')

	glutDisplayFunc(display)
	glutKeyboardFunc(key_pressed)
	glutMouseFunc(mouse_pressed)
	glutIdleFunc(display)

	glEnable(GL_DEPTH_TEST)
	glutMainLoop()
