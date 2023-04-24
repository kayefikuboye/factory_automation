"""factory__conveyor_01 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
conveyor01 = Robot()

# get the time step of the current world.
timestep = int(conveyor01.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
belt = conveyor01.getDevice('belt_motor')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
belt.setVelocity(0.1)
belt.setPosition(0.5)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while conveyor01.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
