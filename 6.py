import time
import os, psutil


def z_func(s):
    z = [''] * (len(s) - 1)
    L = 0
    R = 0
    for i in range(1, len(s)):
        if i >= R:
            j = 0
            while i + j < len(s) and s[i + j] == s[j]:
                j += 1
            L = i
            R = i + j
            z[i - 1] = str(j)
        else:
            if int(z[i - L - 1]) < R - i:
                z[i - 1] = z[i - L - 1]
            else:
                j = R - i
                while i + j < len(s) and s[i + j] == s[j]:
                    j += 1
                L = i
                R = i + j
                z[i - 1] = str(j)
    return z


t_start = time.perf_counter()
process = psutil.Process(os.getpid())

f = open('input.txt')
s = f.readline().strip()

Z = z_func(s)
d = open('output.txt', 'w')
d.write(' '.join(Z))


print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")


