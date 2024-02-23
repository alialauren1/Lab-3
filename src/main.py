"""!
@file main.py
 
@author Alia Wolken, Eduardo Santos, Andrew Jwaideh
"""
import pyb
import utime
from motor_driver import motordriver
from encoder_reader import Encoder
from Closed_Loop_Controller import Controller


# Initialize encoder, motor driver, and controller
enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
moe = motordriver (pyb.Pin.board.PC1, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
enc2.zero()
queue_size = 100


# Paramters for the contoller
Kp = .005 #float(input("Enter the proportional gain (Kp) =  "))
setpoint = 50000 #int(input("Enter the set-point =  "))
controller_obj = Controller(Kp, setpoint, queue_size)

# Loop over a set number of iterations
for i in range(queue_size):
    reader_value = enc2.read() #Reads encoder value
    PWM = controller_obj.run(reader_value) 
    moe.set_duty_cycle(-PWM) #Ajust motor postion
    utime.sleep_ms(10) # Adds delay for stabiliy
    
    
# Retrieves time and position data from the controller object.
tup = controller_obj.data()
time = tup[0]
print(time)
pos = tup[1]

# Initalize lists to store data
time_list = []
pos_list =[]

# Store time and position data in lists
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
    
