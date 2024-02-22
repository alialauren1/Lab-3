# Lab-3 Try to Control the World

## Overview
    The objective of this lab is to make a close-loop proportinal control for
    DC motors. The controller will accurateky position the motor basesd on a
    setpoint while considering; Overshoot, response time, and accuracy.
    
## Projecet Setup
    
1. **GitHub Repository**: Setting up the repository for this lab.
2. **Motor and Encoder**: Connecting DC motor and encoder to the right pins on Nucleo and shoe
3. **Dependencies**: Add all necessary dependancies are installed
4. **Run Code: Test the closed-loop control process and doa set response test

## Step Response Test
    We will use a step response to help the preformace of the motor under
    multiple conditions. From this test we will also include time and 
    motor position data to then be stores and see a visual using plotting
    tools.
    
## Turning the Controller
    We will control the KP (or gain) to get the desired preformance while 
    considering real world factors such as speed, overshoot, and accuracy.
    We will use the step response test to evaluate the preformace at 
    diffrent KP values
