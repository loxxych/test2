def f(x):
    s = []
    x = abs(x)
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            s.append(i)
            s.append(x // i)
    if len(s) > 1:
        if s[-1] == s[-2]:
            del s[-1]
    if len(s) == 2:
        return 1
    return 0


a = [int(i) for i in open('17_9993.txt')]
res = []
pr = []
for i in range(2, 100000):
    if f(i):
        pr.append(i)
m = -1000000
for i in a:
    if str(i)[-2:] == '17':
        m = max(m, i)
for i in range(len(a) - 1):
    if (a[i] in pr and a[i + 1] not in pr) or (a[i + 1] in pr and a[i] not in pr):
        if (a[i] + a[i + 1]) % m == 0:
            res.append(a[i] * a[i + 1])
print(len(res), min(res))
