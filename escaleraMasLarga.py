import random

def descomponer(n):
    potencia = 0
    while (n%2 != 1):
        potencia += 1
        n = n/2
    return (int(n),potencia,potencia)

def componer(t):
    res = []
    for i in range(t[1], t[2]+1):
        res.append(t[0]*2**i)
    return res

def sampleList(n):
    l = random.sample(range(1, n*2), n)
    l.sort()
    return l

def escaleraMasLarga(l, verbose = False):
    ld = [descomponer(n) for n in l]
    
    # Imprime la descomposicion de cada valor
    if verbose:
        print(ld)

    es = escaleraMasLargaAux(ld, verbose)

    esc = [componer(e) for e in es if e[2] - e[1] + 1 > 1]

    maxL = 0
    maxT = ()

    for e in es:
        l = e[2] - e[1] + 1
        if l > maxL:
            maxL = l
            maxT = e

    print('Escaleras de tamaño mayor a 1: {}'.format(esc))
    print('Escalera más larga: {}'.format(componer(maxT)))
    print('Largo: {}'.format(maxL))

def escaleraMasLargaAux(ld, verbose):
    tam = len(ld)
    if tam == 1:
        return ld
    
    mitad = int(tam/2)

    izq = escaleraMasLargaAux(ld[0:mitad], verbose)
    der = escaleraMasLargaAux(ld[mitad:tam], verbose)

    res = []
    i = 0
    j = 0
    leni = len(izq)
    lend = len(der)

    while (i<leni and j<lend):
        if (izq[i][0] == der[j][0] and izq[i][2]+1 == der[j][1]):
            res.append((izq[i][0], izq[i][1], der[j][2]))
            i += 1
            j += 1
        elif (izq[i][0] == der[j][0]):
            res.append(izq[i])
            res.append(der[j])
            i += 1
            j += 1
        elif (izq[i][0] > der[j][0]):
            res.append(der[j])
            j += 1
        else:
            res.append(izq[i])
            i += 1

    while (i<leni):
        res.append(izq[i])
        i += 1

    while (j<lend):
        res.append(der[j])
        j += 1

    # Imprime los pasos recursivos
    if verbose:
        print('------------------------------------------------')
        print('in:')
        print(ld)
        print('izq:')
        print(izq)
        print('der:')
        print(der)
        print('res:')
        print(res)

    return res

## Genera una lista aleatoria de tamaño n, ordenada de menor a mayor sin repetidos
l = sampleList(n = 16)
print(l)

# Imprime todas las escaleras de tamaño mayor a uno y la escalera más larga
# Si verbose = True, muestra todos los pasos de la recursión
escaleraMasLarga(l, verbose = False)