index = text9.index('sunset')
start = index
stop = index
while True:
    start -= 1
    if start >= 0 and text9[start] == '.':
        start += 1
        break
while True:
    stop += 1
    if stop < len(text9) and text9[stop] == '.':
        stop += 1
        break
print 'text9[{}:{}]: {}'.format(start, stop, text9[start:stop])
