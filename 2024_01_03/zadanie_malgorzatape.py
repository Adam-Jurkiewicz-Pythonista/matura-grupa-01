dane = [linia.rstrip() for linia in open('przedzialy.txt')]
t = []

for linia in dane:
    pkt = linia[1:-1].split(',')
    x, y = int(pkt[0]), int(pkt[1])
    if linia[0] == '(':
        x = x + 0.5
    if linia[-1] == ')':
        y = y - 0.5
    t.append((x, y))

os = {}
os[-100.5] = 0
for i in range(-100, 101):
    os[i] = 0
    os[i + 0.5] = 0

for p in t:
    (x, y) = p
    i = x
    while i <= y:
        os[i] = 1
        i += 0.5

print(os)

# najdluzszy ciag jedynek
dl = 0
max_dl = -1
pocz = -100.5
for x in os:
    if os[x] == 1:
        if dl == 0:
            pocz = x
        dl += 1
    else:
        dl = 0
    if dl > max_dl:
        max_dl = dl
        max_pocz = pocz
        max_kon = x

print(f'Dlugosc przedziału: {max_kon - max_pocz}')
if max_pocz % 1 == 0:
    print(f'Przedział: <{max_pocz},', end='')
else:
    print(f'Przedział: ({max_pocz},', end='')
if max_kon % 1 == 0:
    print(f'{max_kon}>', end='')
else:
    print(f'({max_kon})', end='')
