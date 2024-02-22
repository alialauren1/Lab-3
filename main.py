import pyb
import time
from motor_driver import motordriver
from encoder_reader import Encoder
from Closed_Loop_Controller import Controller


enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
moe = motordriver (pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
enc.zero()


    
    # continues to read encoder values for testing until "Ctrl-C" is pressed
while True:
    try:
        # run motor and read encoder vals
        # init motor time channels init-ed in motor_driver class
        
        Kp = float(input("Enter the proportional gain (Kp) =  "))
        setpoint = int(input("Enter the set-point =  "))
        
        controller_obj = Controller(Kp, setpoint)
        controller_obj.run(enc2.read())
        
        count = 0
        
        while: count 
        
        # Drive the motor
        moe.set_duty_cycle (50)
        
        #enc1.read()
        print('------')
        enc2.read()
        print('count',count)
        print('------------------')
        time.sleep(0.1)

        
    # Trying to catch the "Ctrl-C" keystroke to break out
    # of the program cleanly
    except KeyboardInterrupt:
        break
    
