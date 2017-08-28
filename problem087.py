import primeCache as pc

bound = 50 * 10**6

bisquares = []
for m in pc.primes():
    n = m ** 4
    if n >= bound:
        break
    bisquares.append(n)

cubes = []
for m in pc.primes():
    n = m ** 3
    if n >= bound:
        break
    cubes.append(n)

squares = []
for m in pc.primes():
    n = m ** 2
    if n >= bound:
        break
    squares.append(n)

sumof34power = {}
for b in bisquares:
    for c in cubes:
        a = c + b
        if a >= bound:
            break
        sumof34power[a] = 0

sumof234power = {}
for b in sumof34power:
    for s in squares:
        a = s + b
        if a >= bound:
            break
        sumof234power[a] = 0

print len(sumof234power)
