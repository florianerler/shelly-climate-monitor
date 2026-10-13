# Shelly Climate Monitor

A Python-based IoT project for monitoring and analyzing indoor temperature and humidity using Shelly H&T Gen3 sensors.

## Project Status

**Early Development | Offline Sensor Testing**

The project is currently under development as part of my Python learning journey.

Basic HTTP communication and JSON processing have been successfully tested using httpbin.org.

The latest development stage focuses on processing simulated Shelly sensor data without requiring an active network connection.

Direct communication with the physical Shelly sensor is still pending.

## Current Features

- HTTP GET requests using the `requests` library
- JSON response processing
- Separate functions for data retrieval and processing
- Basic network exception handling
- Configurable request timeout
- Offline testing with simulated sensor data
- Extraction of temperature and relative humidity values
- Formatted terminal output

## Requirements

- Python 3
- `requests` library for HTTP functionality

Install dependencies:

`python -m pip install -r requirements.txt`

## Offline Testing

The current development version uses a simulated JSON response containing temperature and humidity measurements.

Example test data:

```python
testdaten = {
    "temperature:0": {"tC": 22.4},
    "humidity:0": {"rh": 48.5}
}
```

Expected output:

```text
temperatur: 22.4 °C
luftfeuchtigkeit: 48.5 %
```

Run the current program using:

`python shelly_monitor.py`

## Planned Features

- [x] Basic HTTP communication
- [x] JSON response processing
- [x] Offline sensor data simulation
- [x] Temperature and humidity extraction
- [ ] Connect to the physical Shelly H&T Gen3
- [ ] Improve network error handling
- [ ] Support multiple sensors
- [ ] Store measurements in CSV files
- [ ] Visualize historical data with Matplotlib
- [ ] Calculate dew point
- [ ] Evaluate indoor climate conditions
- [ ] Build a graphical monitoring dashboard

## Hardware

**Target sensor:** Shelly H&T Gen3

**Communication:** Wi-Fi / HTTP API

## About

This project combines my interests in electrical engineering, environmental measurements, and Python programming.

The goal is to develop a modular monitoring application while learning practical software development, networking, and data analysis.

Developed as a personal learning project.

## License

This project is licensed under the MIT License.
