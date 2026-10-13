# \# Shelly Climate Monitor

# 

# A Python-based room climate monitoring project designed to retrieve, process, and eventually visualize temperature and humidity data from Shelly H\&T Gen3 sensors.

# 

# \## Project Status

# 

# **Early Development (v0.1.0)**

# 

# The project currently implements a basic HTTP client using Python's `requests` library. Communication and JSON processing are being tested using the public HTTP testing service httpbin.org.

# 

# Direct communication with the Shelly H\&T Gen3 sensor has not yet been tested successfully.

# 

# \## Current Features

# 

# \- HTTP GET requests using `requests`

# \- JSON response parsing

# \- HTTP status code retrieval

# \- Separate functions for data retrieval and processing

# \- Basic network exception handling

# \- Five-second request timeout

# \- Automatic polling every 60 seconds

# 

# \## Requirements

# 

# \- Python 3

# \- Python package: `requests`

# \- Internet access for the current test endpoint

# 

# Install the required package:

# 

# `python -m pip install requests`

# 

# \## Usage

# 

# Run the program:

# 

# `python shelly\_monitor.py`

# 

# The application currently requests data from `https://httpbin.org/get` and prints the URL returned in the JSON response.

# 

# Example output:

# 

# `Versuche Verbindung herzustellen...`

# 

# `https://httpbin.org/get`

# 

# Press Ctrl+C to stop the program.

# 

# \## Planned Features

# 

# \- \[ ] Connect to Shelly H\&T Gen3 via its local API

# \- \[ ] Extract temperature and relative humidity measurements

# \- \[ ] Monitor multiple rooms

# \- \[ ] Save historical measurements to CSV

# \- \[ ] Visualize climate data using Matplotlib

# \- \[ ] Calculate dew point and evaluate room climate

# \- \[ ] Improve error handling and connection diagnostics

# 

# \## Hardware

# 

# Target device: \*\*Shelly H\&T Gen3\*\*

# 

# Communication: Wi-Fi / HTTP API

# 

# \## About

# 

# This project is part of my journey learning Python, networking, and IoT development.

# 

# The goal is to build a modular monitoring application that combines practical programming experience with real-world environmental sensor data.

# 

# Developed as a personal learning project.

