import socket
import time
from datetime import datetime
from time import sleep

from pyModbusTCP.client import ModbusClient


# Let's create stopwatch for counting time of session
def stopWatch(sec):

    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time of session: {0} hours {1} minutes {2} secs".format(int(hours),int(mins),int(sec)))


# Starting stopwatch
start_time = time.time()

# Let's create TCP Server and ModbusTCP Client
HOST = '127.0.0.1'
PORT = 8001
c = ModbusClient(host='192.168.1.1', auto_open=True, auto_close=True, port=502)


# Set up of TCP Server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receiving TCP commands from Companion and sending via ModbusTCP to Logo
            data = conn.recv(1024)

            # Recognizing command from Companion. Command is "Q4ON", "Q3OFF" etc.

            def commandRecognize(data):

                num_q = str(data)[3]
                if str(data)[5] == 'N':
                    b_addr = int(num_q) + 8191
                    c.write_single_coil(b_addr, True)
                elif str(data)[5] == 'F':
                    b_addr = int(num_q) + 8191
                    c.write_single_coil(b_addr, False)
                elif str(data)[5] == 'O':
                    c.write_multiple_coils(8192, [False, False, False, False])
                else:
                    None
            commandRecognize(data)

            # Quit command
            if data == b'QUIT\n':
                import time
                print('Exit...')
                end_time = time.time()
                time_lapsed = end_time - start_time
                stopWatch(time_lapsed)
                sleep(3)
                c.write_multiple_coils(8192, [False, False, False, False])
                break
            conn.sendall(data)

            # Printing time
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(time, 'WIP')

            #Printing status of Relays (Qs)
            digit = c.read_coils(8192, 4)
            Qs = {'Q1': digit[0], 'Q2': digit[1], 'Q3': digit[2], 'Q4': digit[3]}
            for Q, v in Qs.items():
                if v == True:
                   print(f'{Q} is Active.')
                elif v == False:
                    print(f'{Q} is NON Active.')

            sleep(1)
            
