class Controller:
    def __init__(self, kp, set_point):
         self.kp = float(kp)
         self.set_point = float(set_point)
         
    def run(self, measured_output):
         #actuation value is Kp*(theta_set - enc2.read() value
         actuation = self.kp*(self.set_point - measured_output)
         return actuation
        
    def set_setpoint(self, desired_set_point):
        self.set_point = desired_set_point
        
    def set_Kp(self, desired_Kp):
        self.kp = desired_Kp
    