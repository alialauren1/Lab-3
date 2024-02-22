# Lab-3 Try to Control the World

## Overview
    The objective of this lab is to make a closed-loop proportional control for
    DC motors. The controller will accurately position the motor based on a
    setpoint while considering; Overshoot, response time, and accuracy.
    
## Project Setup
    
1. **GitHub Repository**: Setting up the repository for this lab.
2. **Motor and Encoder**: Connecting DC motor and encoder to the right pins on Nucleo and shoe
3. **Dependencies**: Add all necessary dependencies are installed
4. **Run Code**: Test the closed-loop control process and do a set response test

## Step Response Test
    We will use a step response to help the performance of the motor under
    multiple conditions. From this test, we will also include time and 
    motor position data to then be stored and see a visual using plotting
    tools.
    
## Turning the Controller
    We will control the KP (or gain) to get the desired performance while 
    considering real-world factors such as speed, overshoot, and accuracy.
    We will use the step response test to evaluate the performance at 
    different KP values
