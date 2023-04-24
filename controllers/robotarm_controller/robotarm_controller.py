"""robotarm_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import ikpy
from ikpy.chain import Chain
from ikpy.link import OriginLink,URDFLink
import tempfile
# create the Robot instance.
robotarm = Robot()




# get the time step of the current world.
timestep = int(robotarm.getBasicTimeStep())

with tempfile.NamedTemporaryFile(suffix='.urdf', delete=False) as file:
    filename = file.name
    file.write(robotarm.getUrdf().encode('utf-8'))
armChain = Chain.from_urdf_file(filename, active_links_mask = [False,True,True,True,True,True,True,False, False])

joint_names = ['joint_1','joint_2','joint_3','joint_4','joint_5','joint_6','joint_base_to_jaw_1','joint_base_to_jaw_2']

initPos=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,]

robot_joints= []
vel= 0.5

for i in range(0,8):
    temp=robotarm.getDevice(joint_names[i])
    robot_joints.append(temp)
    robot_joints[i].setPosition(initPos[i])
    robot_joints[i].setVelocity(vel)
    
#Coordinates of the box with respect to origin of the world
#x= -1.0
#y = -0.13
#z= 0.316   

#Coordinates of the robot arm with respect to origin of the world
#xr= -1.0
#yr = -0.45
#zr = 0.306  

x=0
y=0.32 + 0.015
z=0.010 + 0.010 


def pickUpBox():
    ikSolution = armChain.inverse_kinematics([x,y,z])
    print(ikSolution)
    robot_joints[6].setPosition(0.01)
    robot_joints[7].setPosition(0.01)
    robot_joints[5].setPosition(0.0)
    for i in range(0,5):
        robot_joints[i].setPosition(ikSolution[i+1])

def gripperClose():
    robot_joints[6].setPosition(0.0020)
    robot_joints[7].setPosition(0.0020)
    
def homePosition(x,y,z,grip):
    ikSolution = armChain.inverse_kinematics([x,y,z])
    print(ikSolution)
    robot_joints[6].setPosition(grip)
    robot_joints[7].setPosition(grip)
    robot_joints[5].setPosition(0.0)
    robot_joints[4].setPosition(0.0)
    robot_joints[3].setPosition(0.0)
    for i in range(0,3):
        robot_joints[i].setPosition(ikSolution[i+1])



def readyToDrop():
    robot_joints[0].setPosition(-1.57)
    
    
def gripperOpen():
    robot_joints[6].setPosition(0.01)
    robot_joints[7].setPosition(0.01)
    

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robotarm.step(timestep) != -1:
    t = robotarm.getTime()
    if t>5 and t<7.5:
        pickUpBox()
    elif t >= 7.5 and t < 10:
        gripperClose()
    elif t >= 10 and t < 12.5:
        homePosition(0,0.32,0.1,0.0020)
    elif t >= 12.5 and t < 17.5:
        readyToDrop()
    elif t >= 17.5 and t < 20:
        gripperOpen()
    
    
    pass

# Enter here exit cleanup code.
