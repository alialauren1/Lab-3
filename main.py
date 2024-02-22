import pyb
import time
from motor_driver import motordriver
from encoder_reader import Encoder
from Closed_Loop_Controller import Controller


enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
moe = motordriver (pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
enc2.zero()


    # continues to read encoder values for testing until "Ctrl-C" is pressed
    
while True:
    try:
        # run motor and read encoder vals
        # init motor time channels init-ed in motor_driver class
        
        Kp = .5 #float(input("Enter the proportional gain (Kp) =  "))
        setpoint = 6000 #int(input("Enter the set-point =  "))
        
        reader_value = enc2.read()

        
        while True:
            
            
            controller_obj = Controller(Kp, setpoint)
            PWM = controller_obj.run(reader_value)
            actuate_motor = moe.set_duty_cycle(PWM)
            utime.sleep_ms(5)

        
    # Trying to catch the "Ctrl-C" keystroke to break out
    # of the program cleanly
    except KeyboardInterrupt:
        break
    
