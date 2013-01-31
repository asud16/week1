# This is where Exercise 5.4 goes
# Name: Aparna Sud

def is_triangle (x, y, z):
  if x > y+z or y > x+z or z > x+y: 
		print "No" 
	elif x+y == z or x+z == y or y+z == x: 
		print "Yes" 
	else: 
		print "Yes"

#is_triangle(6,10,4)

def is_triangle2 (x, y, z): 
	a= x%2 
	b= y%2 
	c= z%2 
	if a or b or c != zero:
		is_triangle (int(x), int(y), int(z))

is_triangle2 (2.5,6.5,8.5)

