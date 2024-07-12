time = input()
hour = time[0:2]
mint = time[3:]
# print(hour)
# print(mint)
rev_h = hour[::-1]
time_sleep = 0
if int(rev_h) == 32 and int(rev_h) - int(mint) < 0:
    time_sleep = 60 - int(mint)
    print(time_sleep)
    exit()
if int(rev_h) - int(mint) >= 0:
    time_sleep = int(rev_h) - int(mint)
    print(time_sleep)
else:
    time_sleep = int(rev_h) + 10 + 60 - int(mint)
    print(time_sleep)
