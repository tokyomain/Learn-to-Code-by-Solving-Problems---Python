# COCI '18 Contest 2 #1 Preokret
# https://dmoj.ca/problem/coci18c2p1



# Input A : int A ( 1 <= A <= 2879) :: number of points scored by team A
# A lines As ( 1 <= As <= 2880) :: secs in which Team A was scoring points(ordered)
# Input B : int B ( 1 <= A <= 2879) :: points of Team B
# B lines Bs ( 1 <= As <= 2880) :: secs in which Team B was scoring points(ordered)

# Output 1 :  int > answer to the first question
# Output 2 : int > answer to the second question
secs_a = []
score_a = 0
secs_b = []
score_b = 0
total_score = [0,0]        # Index 0: A Index 1: B
half_time = (12*60)*2
firsthalf_points = 0
turnarounds = 0
leading = ''
leader = ''

score_a = int(input())

for n in range(score_a):
    seconds = int(input())
    secs_a.append(seconds)
    
    if seconds <= 1440:
        firsthalf_points += 1
    else:
        continue


score_b = int(input())

for m in range(score_b):
    seconds = int(input())
    secs_b.append(seconds)
    
    if seconds <= 1440:
        firsthalf_points += 1
    else:
        continue

for e in range(len(secs_a) + len(secs_b)):
    try:
        if secs_a[0] < secs_b[0]:
            total_score[0]+= 1
            secs_a.pop(0)
            
        elif secs_a[0] > secs_b[0]:
            total_score[1]+= 1
            secs_b.pop(0)
        else:
            continue

        if total_score[0] > total_score[1]:
            leading = 'A'
            if leading == leader:
                pass
            elif leader == '':
                pass
            else:
                turnarounds += 1
            leader = leading
            
        elif total_score[0] < total_score[1]:
            leading = 'B'
            if leading == leader:
                pass
            elif leader == '':
                pass
            else:
                turnarounds += 1
            leader = leading

        else:
            continue
    except:
        pass

for f in range(len(secs_a)+len(secs_b)):

    if len(secs_a)> 0:
        for n in secs_a:
            total_score[0]+= 1
    elif len(secs_b)> 0:
        total_score[1]+= 1
    else:
        continue
    if total_score[0] > total_score[1]:
            leading = 'A'
            if leading == leader:
                pass
            elif leader == '':
                pass
            else:
                turnarounds += 1
            leader = leading
            
    elif total_score[0] < total_score[1]:
        leading = 'B'
        if leading == leader:
            pass
        elif leader == '':
            pass
        else:
            turnarounds += 1
        leader = leading

    else:
        continue


print(firsthalf_points)
print(turnarounds)


