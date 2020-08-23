import gates

# sum: a + !ac)b + !ab)c

simpleMode = 1
once = 0

a = 0
b = 0
c = 0

d = [1, 2, 3, 4]

d[-1]

def calc(a, b, c, simple=False):
	out = 0
	out = gates.Nand(b, c)

	print(b, c, '>', out)


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