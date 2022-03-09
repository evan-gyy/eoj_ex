import datetime
from collections import deque
n, m, c, q = map(int, input().split())
now = datetime.datetime.strptime('8:00', '%H:%M')
end = datetime.datetime.strptime('17:00', '%H:%M')
cus = list(map(lambda x: datetime.timedelta(minutes=int(x)), input().split()))
query = list(map(int, input().split()))
seats = [[[0, 0]]*m for i in range(n)]
out = deque()
res = ['Sorry' for i in range(c)]
def get_pos(que):
    for i in range(len(que)):
        for j in range(len(que[i])):
            if que[i][j] == [0, 0]:
                return [i, j]
    return False
for i in range(len(cus)):
    r = get_pos(seats)
    if r:
        seats[r[0]][r[1]] = [i+1, cus[i]]
    else:
        out.append([i+1, cus[i]])
while now < end:
    now += datetime.timedelta(minutes=1)
    for j in range(len(seats[0])):
        s = seats[0][j]
        if s[1]:
            s[1] -= datetime.timedelta(minutes=1)
        if not s[1]:
            if s[0] != 0:
                res[s[0]-1] = datetime.datetime.strftime(now, '%H:%M')
                seats[0][j] = [0, 0]
            for mm in range(1, m):
                if seats[mm][j] != [0, 0]:
                    seats[mm-1][j] = seats[mm][j]
                    seats[mm][j] = [0, 0]
            while get_pos(seats) and out:
                rem = get_pos(seats)
                seats[rem[0]][rem[1]] = out.popleft()
for i in range(len(query)):
    print(res[query[i] - 1])


