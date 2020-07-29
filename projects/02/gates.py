def Nand(a, b):
	return int(not(a and b))


def And(a, b):
	return int(a and b)

def Or(a, b):
	return int(a or b)

def HalfAdder(a, b):
	if a+b == 2:
		return 1, 0
	elif a+b == 0:
		return 0, 0
	else:
		return 0, 1

