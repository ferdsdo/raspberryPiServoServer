# Python Server to control servo motors
* Uses PCA9685 servo controller HAT made by "Waveshare" and Raspberry pi
* Link to controller https://www.waveshare.com/servo-driver-hat.htm

# Requirements
* Python Version 3
* aiohttp
* socketio for python

# To run
### Hardware
* Attach
* Connect one servo to channel 0 and one servo to channel 4 (you can change the channel in the app.py)
* Plug in necessary power into controller

### Software
* Download repository into Raspberry pi
* `git clone 
* `pip3 install aiohttp`
* `pip3 install python-socketio`
* **Note** In 'app.py' change DEBUG to 'False' to enable control of servo control
* In 'index.html' change 'serverAddress' to the ip of the raspberry pi (example 192.168.0.23:8080). It is set to 'localhost:8080' by default
* Run with `python3 app.py`
* Connect to server via port 8080