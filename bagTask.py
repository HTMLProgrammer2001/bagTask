#@param things - list of dictionaries that have properties: v(value), w(weight) and other optional
#@param maxWeight - max weight of a bag 

def bag(things: list, maxWeight: int):
    res = [{'maxVal': 0, 'using_things': []}]
    for i in range(1, maxWeight + 1):
        res += [
            max([{
                'maxVal': t['v'] + res[i - t['w']]['maxVal'],
                'using_things': res[i - t['w']]['using_things'] + [t['name']]
                }
                 if t['name'] not in res[i - t['w']]['using_things'] else {'maxVal': res[i - t['w']]['maxVal'], 'using_things': res[i - t['w']]['using_things']}
                  for t in things
		   if t['w'] <= i]
		   or [res[i - 1]],
		   key = lambda item: item['maxVal'])]
        
    return res[maxWeight]
