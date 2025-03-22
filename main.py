
from machine import Pin, SoftI2C, ADC
import ssd1306
import time

# OLED setup
i2c = SoftI2C(scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# ADC setup
adc = ADC(26)  # GP26 - Connected to voltage divider & potentiometer

# Constants
V_REF = 3.3
SCALING_FACTOR = 6.0  # Adjust for accuracy
CALIBRATION_OFFSET = 0.0  # Fine-tune after testing
NUM_SAMPLES = 20  # Number of ADC readings for averaging

# Function to read stable voltage
def read_voltage():
    total = 0
    for _ in range(NUM_SAMPLES):
        total += adc.read_u16()
        time.sleep_us(500)  # Short delay for better accuracy

    avg_raw = total / NUM_SAMPLES
    v_out = (avg_raw / 65535) * V_REF
    v_in = (v_out * SCALING_FACTOR) + CALIBRATION_OFFSET
    return round(v_in, 2)

# Main loop
prev_voltage = 0
while True:
    voltage = read_voltage()

    if abs(voltage - prev_voltage) > 0.02:  # Avoid unnecessary updates
        oled.fill(0)
        oled.text("Pico Multimeter", 10, 0)
        oled.text("Voltage: {:.2f}V".format(voltage), 10, 20)
        oled.text("Range: 0 - 12V DC", 10, 40)
        oled.show()
        prev_voltage = voltage

    time.sleep(0.2)  # Control update frequency
