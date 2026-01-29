def fuerza_bruta(time):
    suma = 0
    n = len(time)
    for i in range(n):
        for j in range(i+1, n):
            if (time[i] + time[j]) % 60  == 0:
                suma += 1 
                
    return suma

def hash_map(time):
    suma = 0
    count = {}
    for i in time:
        r = i % 60
        c = (60 - r) % 60
        if c in count:
            suma += count[c]

        count[r] = count.get(r, 0) + 1
        
    return suma

time = [30,20,150,100,40]
tiempo = [60,60,60]
print(numPairsDivisibleBy60(time))