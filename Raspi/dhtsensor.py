import board
import adafruit_dht
import time

# Define the pins for DHT sensors
DHT11_PIN = board.D4
DHT22_PIN = board.D18

# Create DHT sensor objects
dht11_sensor = adafruit_dht.DHT11(DHT11_PIN)
dht22_sensor = adafruit_dht.DHT22(DHT22_PIN)

def read_sensor_data(sensor):
    try:
        temperature_c = sensor.temperature
        humidity = sensor.humidity
        return temperature_c, humidity
    except RuntimeError as e:
        print(f"Error reading sensor data: {e}")
        return None, None

def generate_report(sensor_name, temperature_c, humidity):
    if temperature_c is not None and humidity is not None:
        temperature_f = (temperature_c * 9 / 5) + 32  # Convert to Fahrenheit
        report = f"{sensor_name} Sensor Data:\n"
        report += f"Temperature: {temperature_c:.2f}°C / {temperature_f:.2f}°F\n"
        report += f"Humidity: {humidity:.2f}%\n"
        return report
    else:
        return f"Failed to read {sensor_name} sensor data."

try:
    while True:
        # Read data from DHT11 and DHT22 sensors
        dht11_temp, dht11_humidity = read_sensor_data(dht11_sensor)
        dht22_temp, dht22_humidity = read_sensor_data(dht22_sensor)

        # Generate reports for each sensor
        dht11_report = generate_report("DHT11", dht11_temp, dht11_humidity)
        dht22_report = generate_report("DHT22", dht22_temp, dht22_humidity)

        # Print the reports
        print(dht11_report)
        print(dht22_report)

        # Wait for a few seconds before reading again
        time.sleep(5)

except KeyboardInterrupt:
    print("Data acquisition stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    dht11_sensor.exit()
    dht22_sensor.exit()
