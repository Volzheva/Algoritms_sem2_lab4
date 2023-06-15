f = open('input.txt')
d = open('output.txt', 'w')
n = int(f.readline())
strs = {}
supr = {}
for i in range(n):
    s = f.readline().strip()
    for j in range(1, len(s)):
        if s[:j] == s[len(s)-j:]:
            if s[:j] in supr:
                supr[s[:j]] += 1
            else:
                supr[s[:j]] = 1
    if s not in strs:
        strs[s] = 1
    else:
        strs[s] += 1
m = int(f.readline())
strs1 = {}
for i in range(m):
    count = 0
    cur_s = f.readline().strip()
    if cur_s in strs:
        count += strs[cur_s]
    if cur_s in supr:
        count += supr[cur_s]
    d.write(str(count) + '\n')
