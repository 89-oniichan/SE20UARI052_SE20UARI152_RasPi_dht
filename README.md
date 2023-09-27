# Data Acquisition from a RasPi with Digital Sensor
## DHT11 AND DHT22

### Introduction

This report presents a comprehensive overview of data collected using DHT11 and DHT22 digital sensors on a Raspberry Pi. These sensors are widely employed in projects that involve monitoring temperature and humidity.

### Sensor Specifications

**DHT11**
- Operating Voltage: 3 to 5 volts.
- Humidity Range: 20% to 80% with an accuracy of 5%.
- Temperature Range: 0 to 50 degrees Celsius with an accuracy of ±2 degrees.
- Sampling Rate: The DHT11 can be sampled once per second.

**DHT22**
- Operating Voltage: 3 to 5 volts.
- Humidity Range: Impressive 0% to 100% with a more precise accuracy of 2-5%.
- Temperature Range: A broad range from -40 to 80 degrees Celsius with a remarkable accuracy of ±0.05 degrees.
- Sampling Rate: The DHT22 sacrifices sampling speed for accuracy and can be sampled once every two seconds.

### Sensor Use Cases

**DHT11 Use Case**
The DHT11 is suitable for scenarios where real-time temperature and humidity monitoring is required with reasonable accuracy but without the need for extreme precision. It is a cost-effective choice for applications such as:
- Home climate control systems.
- Indoor environmental monitoring in homes and offices.
- Greenhouse climate control.

**DHT22 Use Case**
The DHT22, with its impressive accuracy and extended measurement range, is ideal for applications where precision is crucial. It can be effectively used in:
- Scientific research and experiments.
- Industrial settings for process monitoring.
- Weather stations for accurate climate data collection.
- Agricultural applications in greenhouses and crop monitoring.

### Data Acquisition Code

To acquire data from the DHT11 and DHT22 sensors using a Raspberry Pi, Python code has been developed using the Adafruit CircuitPython DHT library. The code reads temperature and humidity data from both sensors and generates reports based on the collected data.

### Conclusion

The collected data from both DHT11 and DHT22 sensors reveals valuable insights into the environmental conditions being monitored. Over the course of the observations, several noteworthy trends can be observed:

- **Temperature Variation:** The temperature readings from both sensors exhibit relatively consistent fluctuations, with the DHT11 sensor recording slightly higher temperatures than the DHT22. The temperature ranges between 20.70°C (69.26°F) and 25.70°C (78.26°F) for DHT22 and 21.30°C (70.34°F) to 25.20°C (77.36°F) for DHT11. These variations can be attributed to natural climate changes or localized factors.

- **Humidity Levels:** Humidity readings showcase fluctuating humidity levels within the monitored environment. The DHT22 consistently records higher humidity percentages compared to the DHT11. The humidity ranges from 38.30% to 48.40% for DHT22 and 39.20% to 47.70% for DHT11. These variations in humidity are typical for most environments, influenced by factors such as weather conditions, ventilation, and time of day.

- **DHT22 Precision:** It's worth noting that the DHT22 demonstrates a higher level of precision in both temperature and humidity measurements. This sensor's accuracy, with an accuracy of ±0.05°C for temperature and 2-5% for humidity, makes it suitable for applications where precise data is essential.

- **DHT11 Real-Time Monitoring:** On the other hand, the DHT11 provides faster sampling rates, making it suitable for applications that require real-time monitoring, even though it sacrifices some accuracy in exchange for speed.

**Members of the Group:**

- G.V.Prashanth Reddy  SE20UARI052
- Swija Reddy Gaddam  SE20UARI152
