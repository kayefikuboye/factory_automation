"""factory__conveyor_01 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
conveyor02 = Robot()

# get the time step of the current world.
timestep = int(conveyor02.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
belt = conveyor02.getDevice('belt_motor')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while conveyor02.step(timestep) != -1:
    t = conveyor02.getTime()
    if t > 75 and t < 80:
        belt.setVelocity(0.1)
        belt.setPosition(0.5)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
