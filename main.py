from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait, StopWatch

motorspeed = 1560
angl = 90
bpm = 48 #currently set for C418 - Sweden

ev3 = EV3Brick()
MotorA = Motor(Port.A)
MotorB = Motor(Port.B)
MotorC = Motor(Port.C)
MotorD = Motor(Port.D)
try:
    Toutchsensor = TouchSensor(Port.S1)
except OSError:
    print('sensor not connected')

def startsong():
    MotorA.reset_angle(angle=0)
    MotorB.reset_angle(angle=0)
    MotorC.reset_angle(angle=0)
    MotorD.reset_angle(angle=0)

def returnAtozero():
    MotorA.run_target(motorspeed,0,then=Stop.BRAKE,wait=False)
def returnBtozero():
    MotorB.run_target(motorspeed,0,then=Stop.BRAKE,wait=False)
def returnCtozero():
    MotorC.run_target(motorspeed,0,then=Stop.BRAKE,wait=False)
def returnDtozero():
    MotorD.run_target(motorspeed,0,then=Stop.BRAKE,wait=False)

def returntostart():
    returnAtozero()
    returnBtozero()
    returnCtozero()
    returnDtozero()

analognote1 = 0
analognote2 = 0
analognote3 = 0
analognote4 = 0

def analogcontrol(setmotorAangleto,setmotorBangleto,setmotorCangleto,setmotorDangleto):
    if setmotorAangleto == 1:
        MotorA.run_target(motorspeed,angl,then=Stop.BRAKE,wait=False)
    elif setmotorAangleto == -1:
        MotorA.run_target(motorspeed,-angl,then=Stop.BRAKE,wait=False)
    elif setmotorAangleto == 0:
        MotorA.run_target(motorspeed,0,then=Stop.BRAKE,wait=False)

    if setmotorBangleto == 1:
        MotorB.run_target(motorspeed,angl,then=Stop.BRAKE,wait=False)
    elif setmotorBangleto == -1:
        MotorB.run_target(motorspeed,-angl,then=Stop.BRAKE,wait=False)
    elif setmotorBangleto == 0:
        MotorB.run_target(motorspeed,0,then=Stop.BRAKE,wait=False)

    if setmotorCangleto == 1:
        MotorC.run_target(motorspeed,angl,then=Stop.BRAKE,wait=False)
    elif setmotorCangleto == -1:
        MotorC.run_target(motorspeed,-angl,then=Stop.BRAKE,wait=False)
    elif setmotorCangleto == 0:
        MotorC.run_target(motorspeed,0,then=Stop.BRAKE,wait=False)
        
    if setmotorDangleto == 1:
        MotorD.run_target(motorspeed,angl,then=Stop.BRAKE,wait=False)
    elif setmotorDangleto == -1:
        MotorD.run_target(motorspeed,-angl,then=Stop.BRAKE,wait=False)
    elif setmotorDangleto == 0:
        MotorD.run_target(motorspeed,0,then=Stop.BRAKE,wait=False)

def songin(note1,note2,note3,note4,note5,note6,note7,note8):
    global analognote1
    global analognote2
    global analognote3
    global analognote4
    if note1 == True:
        analognote1 = 1
    if note2 == True:
        analognote1 = -1
    if note3 == True:
        analognote2 = 1
    if note4 == True:
        analognote2 = -1
    if note5 == True:
        analognote3 = 1
    if note6 == True:
        analognote3 = -1
    if note7 == True:
        analognote4 = 1
    if note8 == True:
        analognote4 = -1
    analogcontrol(setmotorAangleto=analognote1,setmotorBangleto=analognote2,setmotorCangleto=analognote3,setmotorDangleto=analognote4)
    wait(60000/bpm)

def songinrepeat(not1,not2,not3,not4,not5,not6,not7,not8,times):
    for repeattimes in range(times):
        songin(not1,not2,not3,not4,not5,not6,not7,not8)

swedenrunning = False
def sweden():
    songinrepeat(False,False,True,False,True,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,3)
    songinrepeat(False,False,True,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,2)
    songinrepeat(False,False,True,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,True,False,True,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,False,True,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(True,False,True,False,True,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,False,True,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,2)
    songinrepeat(True,False,True,False,True,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,True,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,True,False,False,False,True,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(True,False,True,False,True,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,True,False,False,2)
    songinrepeat(False,False,False,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,True,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,True,False,False,False,True,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(True,False,True,False,True,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,True,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(True,False,False,True,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(True,False,True,False,True,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,True,False,False,True,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,True,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,True,False,False,False,True,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(True,False,True,False,True,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,True,False,False,True,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,True,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,True,False,False,False,True,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(True,False,True,False,True,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,True,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,True,False,False,False,True,False,2)
    songinrepeat(False,False,False,True,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,True,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,True,False,False,1)
    songinrepeat(False,False,False,False,True,False,False,False,1)
    songinrepeat(False,True,False,True,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(True,False,False,True,False,True,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,True,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,True,False,False,True,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,True,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,2)
    songinrepeat(False,False,False,False,False,False,False,True,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(False,False,False,False,False,False,True,False,1)
    songinrepeat(False,False,False,False,False,False,False,False,1)
    songinrepeat(True,False,False,True,False,True,False,False,5)
    returntostart()
    wait(1000)

startup = True
while startup:
    if Toutchsensor.pressed() == True:
        swedenrunning = True
        startup = False

while swedenrunning:
    sweden()
    startup = True
    swedenrunning = False