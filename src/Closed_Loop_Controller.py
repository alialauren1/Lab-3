"""!
@file Closed_Loop_Contoller.py
This file contains code for a closed-loop control system.

    This class implements a motor driver for an ME405 kit. 
    @author Alia Wolken, Eduardo Santos, Andrew Jwaideh
"""
import utime
import cqueue

class Controller:
    """!
     This class represents a closed-loop control system.
     We implemnt a close-loop control system wirh propotional contol and data storage.
     
    """
    def __init__(self, kp, set_point, queue_size):
        """!
        Initializes the Contoller class with setpoint and proportinal gain.
        
        @param kp (float): The proportional gain paramter for the controller.
        @param set_point (float): The desired set point for the controller.
        @param queue_size (int): The maximum size of the queue.
        """

         self.kp = float(kp)
         self.set_point = float(set_point)
         #self.measured_output = 0
         self.time_value = cqueue.IntQueue(queue_size)
         self.position = cqueue.IntQueue(queue_size)
         self.start = utime.ticks_ms()
         

    def run(self, measured_output):
        """!
        Run the controller with the provided measured output.
        
        Here we run the calculations to set the value based on the current setpoint
        and measured output. It also updates internal data with measured position with
        timestamps.
        
        @param measured_output (float): The measured output values.
        
        @returns float: The actuation value computed by our controller
        """
         #actuation value is Kp*(theta_set - enc2.read() value
         self.measured_output = measured_output
         err = self.set_point - self.measured_output
         actuation = self.kp*err
         current_time = utime.ticks_ms()
         #if not self.time_value.full():
         self.time_passed = utime.ticks_diff(current_time, self.start)
         self.time_value.put(self.time_passed)
         self.position.put(self.measured_output)
         #utime.sleep_ms(10) # does this go in main or control?
         return actuation
        
    def set_setpoint(self, desired_set_point):
        """!
         Sets the desired set point for the controller.
         
         @param desired_set_point (float): The desired set point value.

        """
        self.set_point = desired_set_point
        
    def set_Kp(self, desired_Kp):
        """
        Sets the proportinal gain parameter for the controller.
        
        @param desired_Kp (float): The desired porportional gain value.
        """
        self.kp = desired_Kp
        
    def data(self):
        """
        Retrieve time and position data stored in the queues.
        
        @param tuple: A tuple containing time and position queses.
        """
         x = self.time_value
         y = self.position
         return (x, y)
        
    
  # call .get on each one of the queues  