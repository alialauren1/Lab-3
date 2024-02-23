# Lab-3 Try to Control the World

## Overview
    The objective of this lab is to make a closed-loop proportional control for
    DC motors. The controller will accurately position the motor based on a
    setpoint while considering; Overshoot, response time, and accuracy.
    
## Project Setup
    
1. **Excel sheet/GUI**: Setting up the repository for this lab.
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
    different KP values.
    
## Excel Sheet
    For this lab we where supposed to set up a GUI. The GUI is supposed
    to plot multiple plot cuves, to show several curves on the same axis.

    We where not able to get to this part of the lab so we set up an exel
    sheet to plot the results we gathered from out lab. On this exel sheet
    we will plot 3 kinds of curves; underdamped (with a low KP value), 
    exessive oscillation ( with a high KP value), and finally our best
    preformance we have achived for our motor.



![image](https://github.com/alialauren1/Lab-3/assets/157066050/c7b5fdc4-4317-47af-89b1-9c502eeae2c0)
In the figure above three plots are plotted, each representing the performance of a motor under
different proportional gain (KP) values. The first plot, shown in blue, corresponds to a KP value
of 0.11. Which is the highest KP utilized in the lab. This plot illustrates that the motor's performance
is too high, implying that the proportional gain might be excessive, potentially leading to overshooting. 
The second plot, depicted in orange, corresponds to a KP value of 0.005, the lowest value tested. While
the motor operates as expected at this KP. It does not achieve optimal accuracy. Lastly, the third plot,
in green, corresponds to a KP value of 0.015, which falls between the extremes of the other two plots.
Here, the motor's performance is neither overdamped or underdamped, indicating the optimal KP vallue
for the motor's performance, providing the most amount of accuracy.

