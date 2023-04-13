import time
import os




def print_logs():
    for filename in os.listdir('/log'):
        if filename.endswith('.txt'):
            with open('/log/' + filename, 'r') as f:
                file_content = f.read()
            print('Filename:', filename, '\nContent:\n', file_content)



def main():
    print_logs()


while True:
    main()
    time.sleep(5)






