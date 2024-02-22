import utime
import cqueue

class Controller:
    def __init__(self, kp, set_point):
         self.kp = float(kp)
         self.set_point = float(set_point)
         self.measured_output = 0
         self.time_value = cqueue.IntQueue(2000)
         self.position = cqueue.IntQueue(2000)
         self.start = utime.ticks_ms()
         

    def run(self, measured_output):
         #actuation value is Kp*(theta_set - enc2.read() value
         err = self.set_point - measured_output
         actuation = self.kp*err
         print("error is")
         print(err)
         
         
         current_time = utime.ticks_ms()
         if not self.time_value.full():
             time_passed = utime.ticks_diff(current_time, self.start)
             self.time_value.put(time_passed)
             self.position.put(measured_output)
             return actuation
         else:
             return "done"
        
    def set_setpoint(self, desired_set_point):
        self.set_point = desired_set_point
        
    def set_Kp(self, desired_Kp):
        self.kp = desired_Kp
        
    def data():
        x = self.time_value.put(time_passed)
        y = self.position.put(measured_output)
        return x , y
        
    
    