#!/usr/bin/python3

import smbus
import math
import time
import argparse

import network.send

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def main(ip_addr,port):
    while True:
        # For sending
        dataname = []
        data = []

        time.sleep(0.1)
        gyro_xout = read_word_2c(0x43)
        gyro_yout = read_word_2c(0x45)
        gyro_zout = read_word_2c(0x47)

        print ("gyro_xout : ", gyro_xout, " scaled: ", (gyro_xout / 131))
        print ("gyro_yout : ", gyro_yout, " scaled: ", (gyro_yout / 131))
        print ("gyro_zout : ", gyro_zout, " scaled: ", (gyro_zout / 131))

        accel_xout = read_word_2c(0x3b)
        accel_yout = read_word_2c(0x3d)
        accel_zout = read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0
        
        print ("accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled)
        print ("accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled)
        print ("accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled)

        print ("x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
        print ("y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))

        ### Sending process
        dataname.extend(["x","y"])
        data.extend([str(accel_xout_scaled),str(accel_yout_scaled)])

        network.send.send_data(data,dataname,ip_addr,port,"/plot")
        time.sleep(0.5)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--ip_addr",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--port",
        type=str,
        required=True,
    )

    args = parser.parse_args()
    main(args.ip_addr,args.port)
    
