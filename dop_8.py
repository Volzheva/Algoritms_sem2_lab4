f = open('input.txt')
s = f.readline()
d = open('output.txt', 'w')


l = len(s)
flag = False
for k in range(l-1, 0, -1):
    for i in range(l-k):
        if s[i] == s[i+k]:
            flag = True
            d.write(str(k))
            break
    if flag:
      break
if not flag:
    d.write('0')
