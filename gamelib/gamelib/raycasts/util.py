from ..utilities import *

def get_slope(p1, p2):
	dx,dy = p2 - p1
	return dy / dx

def point_on_line(p, L):
	x,y = p
	p1, p2 = L
	x1,y1 = p1
	x2,y2 = p2
	X = [x1, x2]
	Y = [y1, y2]
	return min(X) <= x <= max(X) and min(Y) <= y <= max(Y)

def line_intersection(A, B):
	if A[1][0] > A[0][0]: A = [A[1], A[0]]
	if B[1][0] > B[0][0]: B = [B[1], B[0]]
	xdiff = (A[0][0] - A[1][0], B[0][0] - B[1][0])
	ydiff = (A[0][1] - A[1][1], B[0][1] - B[1][1])
	slopeA = ydiff[0] / xdiff[0]
	slopeB = ydiff[1] / xdiff[1]

	def det(a, b):	
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	point = None

	if div != 0: 
		d = (det(*A), det(*B))
		x = det(d, xdiff) / div
		y = det(d, ydiff) / div
		if point_on_line((x,y), A) and point_on_line((x,y), B):
			point = np.array((x,y))

	if point is None:			
		if ydiff[0] == 0:
			x = xdiff[0]
			y = slopeB / ydiff[1]
			if point_on_line((x,y), A) and point_on_line((x,y), B):
				point = np.array((x,y))

		elif ydiff[1] == 0:
			x = xdiff[1]
			y = slopeA / ydiff[0]
			if point_on_line((x,y), A) and point_on_line((x,y), B):
				point = np.array((x,y))
	return point

def angular_vector(a):
	return np.array((np.cos(a), np.sin(a)))

def project_point(p, a, d):
	return np.array(p) + angular_vector(a) * d

def project_line(p, a, d):
	p1 = project_point(p, a, d)
	return [np.array(p), p1]

def inverse_angle(a):
	return (a + np.pi) % (2 * np.pi)
