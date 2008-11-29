def bool2hum(b):
    if b:
        return "Si"
    else:
        return "No"

def sec2hum(s):
    return "%i minutos" % s

def set2bag(l):
    b = {}
    for e in l:
        if e in b:
            b[e] += 1
        else:
            b[e] = 1
    return b
