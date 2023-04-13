import time

filename = "/log/log.txt"


def print_logs():
    with open(filename, "r") as f:
        file_content = f.read()
        f.close()
        print('Filename:', filename, '\nContent:\n', file_content)

def main():
    print_logs()


while True:
    main()
    time.sleep(3)


# import threading

# filename = "/log/log.txt"

# def print_logs():
    # with open(filename, "r") as f:
      # file_content = f.read()
      # print('Filename:', filename, '\nContent:\n', file_content)
      
# #threading.Timer(10, print_logs).start()

# def main():
    # print_logs()

# if __name__ == '__main__':
    # threading.Timer(10,main()).start()




