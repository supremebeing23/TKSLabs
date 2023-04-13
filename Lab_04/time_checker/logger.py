import time

#directory = '~/log'


while True:
    #filename = /log/log.txt'
    with open("/log/log.txt", "a") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        time.sleep(10)
