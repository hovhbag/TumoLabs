from time import sleep
from datetime import time

my_time = input("Insert time to count down (h:m:s)")
my_time_l = my_time.split(":")
int_time = int(my_time_l[0]) * 3600 + int(my_time_l[1])*60 + int(my_time_l[2])
while int_time > 0:
    h = int_time // 3600
    m = (int_time % 3600) // 60
    s = (int_time % 3600) % 60
    print(time(h,m,s))
    int_time -= 1
    sleep(1)
print("Time is over")