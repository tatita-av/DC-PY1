from pprint import pprint

dt = []
for i in range(16):
    dt.append({'bin':bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)})

pprint(dt)