from aiohttp import web
import socketio

# if DEBUG = True then it will NOT send signals to the servo controller
DEBUG = True

# Servo Control
if not DEBUG:
    from PCA9685 import PCA9685


# CHANGE Channel to correct channel
xChannel = 0 
yChannel = 4

def initServoController():
    if not DEBUG:
        pwm = PCA9685(0x40)
        pwm.setPWMFreq(50)
    else:
        pwm = False
    return pwm

pwm = initServoController()
sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect')
def connect(sid, environ):
    print("connect", sid)

@sio.on('message')
async def message(sid, x, y):
    print("cordinates: ", x, " ", y)
    await sio.emit('reply', x, y)

    readAngle(xChannel, x) # x cord
    readAngle(yChannel, y) # y cord
@sio.on('disconnect')
def disconnect(sid):
    print('disconnect', sid)

#app.router.add_static('/static', 'static')
app.router.add_get('/', index)

# Servo Control
def moveServo(channel, angle, pwm):
	# servo buzzes at angles 0-5 so change to 6 
    if(angle >= 0 and angle <= 5):
	    angle = 6	
	
    pwmSignal = float(500+(angle)*(100/9)) 
	# 500  ==   0 degs
	# 1000 ==  45 degs
	# 1500 ==  90 degs
	# 2000 == 135 degs
	# 2500 == 180 degs
	# taken from wiki of servo controller
    if DEBUG:
        print("DEBUG")
        print("Moving servo...")
    else:
        print("Moving servo...")
        pwm.setServoPulse(channel, pwmSignal)
    print('done\n')

def readAngle(ch,cord):
    try:
        channel = int(ch) # x or y cord
        angle = float(cord)
        if(angle > 180 or angle < 0):
            raise Exception('angle must be between 0-180')
        if(channel < 0 or channel > 15):
            raise Exception('channel must be between 0-15')

    except Exception as e:
        print(e)
        print("please provide channel (0-15) and angle (0-180)")
    else:
        print(angle)
        print(ch)
        moveServo(channel, angle, pwm)

if __name__ == '__main__':
    if not DEBUG:
        initServoController()
    web.run_app(app)