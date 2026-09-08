s = input("in: ")
d = ""
state = 0
start = 0
ds = 0
for i in range(len(s)):
	if state == 0:
		if 65 <= ord(s[i]) <= 90:
			d += s[i]
			start = i
			state = 1
	elif state == 1:
		if s[i] in "0123456789":
			state = 2
			ds = i - start
			break
s = s.split(".")[0][(start+ds+1)::]
for i in range(0, len(s), ds+1): d += s[i]
print(f"out: {d+"."}")