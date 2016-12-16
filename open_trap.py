i = 0
# find line descriptions
traps = []

for j in range(36):
    i = 0
    with open('trap.txt') as f:
        for line in f:
            if line == str(j)+'\n':
                 traps.append(i)
            i = i+1

i = 0
with open('trap.txt') as f:
    for line in f:
        if line == str(j)+'\n':
                traps.append(i)
        i = i+1
            
