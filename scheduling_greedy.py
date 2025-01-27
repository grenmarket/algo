def init():
    with open('files/jobs.txt', 'r') as file:
        split = [line.split() for line in file][1:]
        return [[int(line[0]), int(line[1])] for line in split]

def sort(jobs):
    return sorted(jobs, key=lambda x: (x[0]/x[1], x[0]), reverse=True)

def weighted_time(schedule):
    total_time = 0
    weighted_sum = 0
    for i in range(0, len(schedule)):
        length = schedule[i][1]
        completion_time = length + total_time
        weighted_sum += completion_time*schedule[i][0]
        total_time += length
    return weighted_sum

schedule = sort(init())
print(weighted_time(schedule))
