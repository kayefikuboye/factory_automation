"""mobile_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:

LF_motor = robot.getDevice('front left wheel')
RF_motor = robot.getDevice('front right wheel')
LB_motor = robot.getDevice('back left wheel')
RB_motor = robot.getDevice('back right wheel')

LF_motor.setVelocity(1)
RF_motor.setVelocity(1)
LB_motor.setVelocity(1)
RB_motor.setVelocity(1)


speed=1.57

def moveForward(dist):
    LF_motor.setPosition(float('inf'))
    RF_motor.setPosition(float('inf'))
    LB_motor.setPosition(float('inf'))
    RB_motor.setPosition(float('inf'))
    
    LF_motor.setVelocity(dist)
    RF_motor.setVelocity(dist)
    LB_motor.setVelocity(dist)
    RB_motor.setVelocity(dist)

def moveBackward(dist):
    LF_motor.setPosition(float('inf'))
    RF_motor.setPosition(float('inf'))
    LB_motor.setPosition(float('inf'))
    RB_motor.setPosition(float('inf'))
    
    LF_motor.setVelocity(-dist)
    RF_motor.setVelocity(-dist)
    LB_motor.setVelocity(-dist)
    RB_motor.setVelocity(-dist)
    
def turnLeft(angle):
    LF_motor.setPosition(float('inf'))
    RF_motor.setPosition(float('inf'))
    LB_motor.setPosition(float('inf'))
    RB_motor.setPosition(float('inf'))
    
    LF_motor.setVelocity(-angle)
    RF_motor.setVelocity(angle)
    LB_motor.setVelocity(-angle)
    RB_motor.setVelocity(angle)
    
def turnRight():
    LF_motor.setPosition(float('inf'))
    RF_motor.setPosition(float('inf'))
    LB_motor.setPosition(float('inf'))
    RB_motor.setPosition(float('inf'))
    
    LF_motor.setVelocity(angle)
    RF_motor.setVelocity(-angle)
    LB_motor.setVelocity(angle)
    RB_motor.setVelocity(-angle)

def stopAll():
    LF_motor.setVelocity(0)
    RF_motor.setVelocity(0)
    LB_motor.setVelocity(0)
    RB_motor.setVelocity(0)



#current coordinate of box is
# x = 0.055
#y= 1.122
#z= 0.287

#current coordinate of robotic arm2 is
# x = 0.45
#y= 1.1
#z= 0.24

#current coordinate box wrt of base of arm is
# x = 0.45-0.055 = 0.395
#y= 1.122-1.1 = 0.022 
#z= 0.287 -0.24 = 0.047




while robot.step(timestep) != -1:
    tr = robot.getTime()
    if tr >= 25 and tr< 30:
        moveForward(0.98)
    elif tr>= 30 and tr< 35:
        turnLeft(0.85)
    elif tr>= 35 and tr< 50:
        moveForward(1.065)
    elif tr>= 50 and tr< 55:
        stopAll()
    
   
    pass

# Enter here exit cleanup code.
