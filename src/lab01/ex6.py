n = int(input("in_1: "))
m = []
c = 2
for i in range(n):
	inp = input(f"in_{c}: ").split()
	m.append(1 if inp[3] == "True" else 0)
	c += 1
s = sum(sorted(m))
print(f"out: {s} {len(m)-s}")