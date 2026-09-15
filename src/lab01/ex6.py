n = int(input("in_1: "))
c = 2
k = 0
for i in range(n):
	inp = input(f"in_{c}: ").split()
	if inp[3] == "True":
		k += 1
	c += 1
print(f"out: {k} {c-2-k}")