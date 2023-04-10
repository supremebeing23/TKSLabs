import time

directory = '/log'
filename = f"{directory}/log.txt"


while True:
    with open("log.txt", "a") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        time.sleep(10)
