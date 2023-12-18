# Server-side programs
This directory must use on server.
Don't use on raspberry-pi (maybe not working)

# Installation
Please refer to the `requirements.txt` and execute below in this directory:
```$ pip install -r requirements.txt```

# Executation
## Step1. Start program at the raspberry pi
```$ python3 python/2.2.6_mpu6050_client.py```

## Step2. Start program at the server
```$ python3 server/receiver.py```