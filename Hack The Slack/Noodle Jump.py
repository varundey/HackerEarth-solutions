n,k = map(int,raw_input().split())

steps = map(int,raw_input().split())

for i in range(len(steps)):
    try:
        if k + steps[i] >= steps[i+1]:
            continue
        elif k+ steps[i] < steps[i+1]:
            print steps[i]
            break
    except IndexError:
        print steps[i]
        break
