#!/usr/bin/python3

def rangolify(s,c=' ',colors=[]):
    a = c.join(s[::-1] + s[1:])
    size = len(s)
    pattern = [(a[:2*i]+a[2*i::-1]).center(size*4-3,c) for i in range(size)]
    return str('\n'.join(pattern + pattern[-2::-1]))
