import gates

# sum: a + !ac)b + !ab)c

simpleMode = 0
once = 1

a = 0
b = 0
c = 1




def calc(a, b, c, simple=False):
	out = 0
	

	car_bc, sum_bc = gates.HalfAdder(b, c)
	car_l = gates.And(a, car_bc)
	car_r, sum_r = gates.HalfAdder(car_l, sum_bc)

	print(car_bc, sum_bc)
	print(car_r, sum_r)


	


def count(simple=False):
	global a
	global b
	global c

	c += 1
	if c > 1:
		c = 0
		b += 1

	if b > 1:
		b = 0
		a += 1
		if simple: return True

	if a > 1:
		return True

while True:
	calc(a, b, c, simpleMode)

	if count(simpleMode): break
	if once: break