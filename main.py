import pyb
import utime
from motor_driver import motordriver
from encoder_reader import Encoder
from Closed_Loop_Controller import Controller


enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
moe = motordriver (pyb.Pin.board.PC1, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
enc2.zero()



Kp = .1 #float(input("Enter the proportional gain (Kp) =  "))
setpoint = 50000 #int(input("Enter the set-point =  "))
controller_obj = Controller(Kp, setpoint)
    
while True:
    try:        
        while True:
            reader_value = enc2.read()
            PWM = controller_obj.run(reader_value)
            if isinstance(PWM, str):
                print("done")
                break
            else:
                moe.set_duty_cycle(-PWM)
       # print("data")
       # print(controller_obj.data())
            
    # Trying to catch the "Ctrl-C" keystroke to break out
    # of the program cleanly
    except KeyboardInterrupt:
        break
    
