# Server-side programs
This directory must use on server.
Don't use on raspberry-pi (maybe not working)

# Installation
Please refer to the `requirements.txt` and execute below in this directory:
```$ pip install -r requirements.txt```

# Executation
## Step1. Start program at the raspberry pi
```$ python3 python/2.2.6_mpu6050_client.py --ip_addr [Server's IP Adress] --port [Server's port number]```

## Step2. Start program at the server
```$ flask --app receiver run host="0.0.0.0"```
