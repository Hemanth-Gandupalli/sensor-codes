import smbus
import time

# I2C address of the MPU9250
MPU9250_ADDRESS = 0x68

# Register addresses for the accelerometer data
ACCEL_XOUT_H = 0x3B

# Initialize the I2C bus
bus = smbus.SMBus(1)  # Use bus 1 for Raspberry Pi 3, 4, or 400

# Wake up the MPU9250
bus.write_byte_data(MPU9250_ADDRESS, 0x6B, 0)

while True:
    # Read accelerometer data
    accel_data = bus.read_i2c_block_data(MPU9250_ADDRESS, ACCEL_XOUT_H, 6)

    # Combine high and low bytes for each axis
    AcX = accel_data[0] << 8 | accel_data[1]
    AcY = accel_data[2] << 8 | accel_data[3]
    AcZ = accel_data[4] << 8 | accel_data[5]

    # Print the accelerometer data
    print(f"Acceleration - X: {AcX} Y: {AcY} Z: {AcZ}")

    time.sleep(0.1)  # Delay for 100 milliseconds
