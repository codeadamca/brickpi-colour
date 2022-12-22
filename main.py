import os, time, brickpi3

# Initialize the EV3 Brick
BP = brickpi3.BrickPi3()

# Initialize EV3 touch sensor and motors
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)

# Without a delay reading sensor data can cause an error
time.sleep(0.5)

# Define an array to store colour names
colours = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

# Quite loop when CTRL+C is pressed
try:

    # Create a loop to react to buttons
    while True:

        # Get touch sensor status
        colour = BP.get_sensor(BP.PORT_1)
            
        print(colours[colour])

        # Loop delay
        time.sleep(0.5)

# Result of CTRL+C
except KeyboardInterrupt:
    
    # Unconfigure the sensors
    BP.reset_all() 