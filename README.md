![IMG_20250318_203204_458](https://github.com/user-attachments/assets/9598c68b-6c5d-489e-984c-6f735327fc7a)# Pico Multimeter 📟⚡  

A **Raspberry Pi Pico-based digital multimeter** that measures **0-12V DC** using a **voltage divider**, **OLED display (SSD1306)**, and a **10kΩ potentiometer for calibration**. This project is built with **MicroPython** and optimized for **stable ADC readings, minimal noise, and smooth OLED updates**.

---
## Some Pics and Workable
![Multimeter with Pico](images/circuit_diagram.png)

---

## 📌 Features  
✅ **Measures 0-12V DC** using a safe **voltage divider circuit**  
✅ **OLED Display (SSD1306, I2C)** for real-time voltage readings  
✅ **Averaged ADC readings** to reduce fluctuations  
✅ **Calibration with a 10kΩ potentiometer** for fine-tuning accuracy  
✅ **OLED refresh optimization** to prevent flickering  
✅ **MicroPython-based for easy modification and learning**  

---

## 🛠️ Hardware Requirements  
- **Raspberry Pi Pico**  
- **SSD1306 OLED Display (I2C)**  
- **6× 470Ω resistors** (for voltage divider)  
- **10kΩ potentiometer** (for calibration)  
- **Ceramic capacitor (0.1µF - 1µF)** (for noise reduction)  
- **Jumper wires & probes**  

---

## 🔌 Circuit Diagram  
```
   +12V (Probe 1)
       |
       |   [ 470Ω ]--[ 470Ω ]--[ 470Ω ]--[ 470Ω ]--[ 470Ω ]  (~2.35kΩ total)
       |                  |
       |                  |  
       |                (Middle Pin of Pot - Wiper)  
       |                  |
       |                 (ADC0 - GP26 on Pico)
       |                  |
       |                 ===  (Ceramic Capacitor 0.1µF - 1µF)
       |                  |
       |   [ 470Ω ] (Single 470Ω to GND)  
       |                  |
       |                 GND (Probe 2)
       |
    10kΩ Potentiometer (Used for Calibration)
    ----------------------------------------
    | Left Pin  |  +12V (Probe 1 side)    |
    | Middle Pin|  ADC0 (GP26 on Pico)    |
    | Right Pin |  Ground (GND)           |
    ----------------------------------------

    Raspberry Pi Pico
  --------------------
  |                  |
  | GP26  (ADC0) <---|--- Middle of Voltage Divider
  |                  |
  | GND  <-----------|--- Ground
  |                  |
  --------------------

  OLED Display (SSD1306 - I2C)
  ----------------------------
  | OLED Pin | Pico Pin       |
  |----------|---------------|
  |   VCC    |   3.3V        |
  |   GND    |   GND         |
  |   SCL    |   GP1 (SCL)   |
  |   SDA    |   GP0 (SDA)   |
  ----------------------------
```

---

## ⚙️ How to Use  
1. **Connect probes** to an unknown voltage source (0-12V).  
2. The **OLED will display the voltage** in real-time.  
3. **Adjust the potentiometer** if calibration is needed.  
4. The **ceramic capacitor smooths out fluctuations** for stable readings.  

---

## 🔥 Future Improvements  
- ✅ **Increase voltage range to 50V DC** using a better voltage divider  
- ✅ **Add Reverse Polarity Protection** to prevent damage  
- ✅ **Add Current Measurement** using a shunt resistor  
- ✅ **Measure Resistance** using a known reference resistor
- ✅ **Make it a portable multimeter with  logging data 

---

## 📜 License  
This project is **open-source** under the **MIT License**. Feel free to **modify and improve** it! 🚀  
