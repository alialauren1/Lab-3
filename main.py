import pyb
import utime
from motor_driver import motordriver
from encoder_reader import Encoder
from Closed_Loop_Controller import Controller


enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
moe = motordriver (pyb.Pin.board.PC1, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
enc2.zero()
queue_size = 100



Kp = .005 #float(input("Enter the proportional gain (Kp) =  "))
setpoint = 50000 #int(input("Enter the set-point =  "))
controller_obj = Controller(Kp, setpoint, queue_size)

for i in range(queue_size):
    reader_value = enc2.read()
    PWM = controller_obj.run(reader_value)
    moe.set_duty_cycle(-PWM)
    utime.sleep_ms(10)

tup = controller_obj.data()
time = tup[0]
print(time)
pos = tup[1]

time_list = []
pos_list =[]

for i in range(queue_size):
    time_list.append(time.get())
    
for i in range(queue_size):
    pos_list.append(pos.get())

# this is to look nice
for i in range(queue_size):
    row = f"{time_list[i]}, {pos_list[i]}"
    print(row)

# this is indep time
for i in range(queue_size):
    row = f"{time_list[i]}"
    print(row)

# this is indep pos
for i in range(queue_size):
    row = f"{pos_list[i]}"
    print(row)


    
    
    
    
    
    
    
    
    
    
    
#     
# while True:
#     try:        
#         while True:
#             reader_value = enc2.read()
#             PWM = controller_obj.run(reader_value)
#             if isinstance(PWM, str):
#                 print("done")
#                 break
#             elif PWM == 0:
#                 print("done super done")
#                 break
#             else:
#                 moe.set_duty_cycle(-PWM)
#                 print(reader_value)
                
        #print("data")
        #print(controller_obj.data())
     #   break
            
    # Trying to catch the "Ctrl-C" keystroke to break out
    # of the program cleanly
   # except KeyboardInterrupt:
   #     break
    
