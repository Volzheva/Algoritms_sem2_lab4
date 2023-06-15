f = open('input.txt')
t = f.readline()[:-1]
p = f.readline()[:-1]

res = []
for i in range(len(t) - len(p) + 1):
    if t[i] == p[0]:
        part = t[i:i+len(p)]
        if part == p:
            res.append(str(i))


d = open('output.txt', 'w')
d.write(' '.join(res))