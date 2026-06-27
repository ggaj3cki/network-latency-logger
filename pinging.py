from subprocess import getoutput
from datetime import datetime
from time import sleep


def pinger(intervals, how_long_run):
    start_time = datetime.now()
    with open('ping_values.txt', 'a') as f:
        i = 0
        while True:
            d = getoutput('ping -n 1 8.8.8.8')
            curtime = datetime.now().strftime('%H:%M:%S')
            try:
                d = d.split('\n');d = d[2].split(' ');d=d[4].split('=');d=d[1][:-2]
                f.write(f'{curtime} : {d}ms \n')
            except IndexError:
                d = "Internet connection lost"
                f.write(f'{curtime} : {d} \n')
            i += 1
            if int(((datetime.now()-start_time).total_seconds())//60) == how_long_run:
                break
            sleep(intervals)
        f.write('\n')
            

if __name__ == '__main__':
    while True:
        try:
            inter = int(input("how often ping(in seconds): "))
            how_long = int(input("how long (in minutes): "))
            break
        except ValueError:
            print("It isn't a number, try again")

    pinger(inter, how_long)
