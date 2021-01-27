mx = []
s = 0

for _ in range(10):
    x = int(input())
    if x < 0:
        s += x
        mx.append(x)

if mx:
    print(s)
    print(max(mx))
else:
    print("NO")
