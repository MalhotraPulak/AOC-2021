import sys

def xx(x, y, val):
	if x < val:
		return (x, y)
	elif x == val:
		return None
	else:
		return (2 * val - x, y)

def yy(x, y, val):
	if y < val:
		return (x, y)
	elif y == val:
		return None
	else:
		return (x, 2* val - y)
def main():
	with open(sys.argv[1], "r") as f:
		lines = f.readlines()


	pts = []
	print(lines)
	for line in lines:
		line = line.strip()
		if line == '':
			break
		x,y = line.split(",")
		pts.append((int(x), int(y)))
                                           
	for line in lines:
		if "fold" not in line:
			continue

		last = line.split()[2]
		axis, val = last.split('=')
		val = int(val)                                           
		new_pts = set()
		for x, y in pts:
			if axis == 'x':
				pt = xx(x,y, val)
			else:
				pt = yy(x,y, val)
			if pt is not None:
				new_pts.add(pt)
		print(new_pts)
		print(len(new_pts))
		break                              


if __name__ == "__main__":
	main()
