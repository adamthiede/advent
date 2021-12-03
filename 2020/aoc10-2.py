with open('aoc10-input.txt') as fd:
    data = [0] + sorted(map(int, fd))
data.append(data[-1] + 3)

def silver():
    steps = {i: 0 for i in (1,2,3)}
    prev = 0
    for num in data[1:]:
        steps[num-prev] += 1
        prev = num

    print(steps[1] * (steps[3]))

def gold():
    s = set(data)
    cache = {data[-1]: 1}

    get_steps_possible_at(data[0], data, s, cache)
    print(cache[data[0]])


def get_steps_possible_at(num, data, s, cache):
    total = sum((cache[x] if x in cache else get_steps_possible_at(x, data, s, cache)) for x in (num + i for i in range(1, 4) if num + i in s))
    cache[num] = total
    return total

silver()
gold()
