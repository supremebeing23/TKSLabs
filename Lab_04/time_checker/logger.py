import time
import datetime

output_dir = '/log'

while True:
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(f'{output_dir}/{current_time}.txt', 'a') as f:
        f.write(current_time + '\n')


    time.sleep(10)



# while True:
    # #filename = /log/log.txt'
    # with open("/log/log.txt", "a") as f:
        # f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        # time.sleep(10)
