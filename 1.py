import time
import os, psutil

t_start = time.perf_counter()
process = psutil.Process(os.getpid())

f = open('input.txt')
p = f.readline()[:-1]
print(p)
t = f.readline()
count = 0
res = ''
for i in range(len(t) - len(p) + 1):
    if t[i] == p[0]:
        part = t[i:i + len(p)]
        if part == p:
            count += 1
            res += str(i + 1) + ' '

d = open('output.txt', 'w')
d.write(str(count) + '\n' + str(res))

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
