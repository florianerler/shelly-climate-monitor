# Shelly Climate Monitor

**A Python-based environmental monitoring application for the Shelly H&T Gen3 sensor.**

Shelly Climate Monitor is a personal programming and IoT development project focused on retrieving, processing and evaluating real-world environmental measurements.

The project started with basic HTTP requests and offline JSON testing. It has since evolved into a working prototype that communicates with a physical Shelly H&T Gen3 sensor through the local network.

The long-term objective is to develop a modular environmental monitoring system capable of collecting, storing, visualizing and analyzing sensor data over time.

## Current Status

**Live sensor integration: Functional prototype**

Currently implemented features:

- HTTP communication with a Shelly H&T Gen3
- Retrieval and processing of JSON sensor responses
- Extraction of temperature and relative humidity
- Returning measurement values as a Python tuple
- Independent temperature and humidity evaluation functions
- Basic connection error handling
- Automatic retry attempts
- Separation of local sensor configuration from public source code

The software currently operates through a Python console.

## Hardware

| Component | Description |
|---|---|
| Sensor | Shelly H&T Gen3 |
| Connection | Wi-Fi |
| Interface | Shelly HTTP RPC API |
| Host | Windows PC running Python |
| Development environment | Thonny |

### Physical Sensor

![Shelly H&T Gen3](assets/shelly-hnt-gen3.jpg)

*The physical Shelly H&T Gen3 sensor used during development.*

## Example Output

![Program execution](assets/console-output.png)

Example console output from a successful measurement:

    Versuche Verbindung herzustellen...
    temperatur: 24.7 °C
    luftfeuchtigkeit: 45.5 %
    (24.7, 45.5)
    zu warm
    optimal

The displayed values were retrieved from a real Shelly H&T Gen3 sensor.

## Installation

### Requirements

- Python 3
- Python `requests` library
- Shelly H&T Gen3 connected to the local network
- Network access to the Shelly device

### 1. Install Dependencies

From the project directory, execute:

`pip install -r requirements.txt`

### 2. Configure the Sensor

For privacy and easier configuration, the sensor's local IP address is not hardcoded in the main application.

Copy the provided file:

`config.example.py`

Rename the copy to:

`config.py`

Open `config.py` and enter your own Shelly IP address:

`SHELLY_IP = "192.168.1.XXX"`

Replace the placeholder with the actual IP address of your device.

The local `config.py` file is excluded from Git tracking through `.gitignore`.

### 3. Run the Application

Execute:

`python shelly_monitor.py`

The application attempts to connect to the configured sensor and processes the received measurements.

**Note:** The battery-powered Shelly H&T Gen3 may enter sleep mode and temporarily become unavailable through HTTP. Repeated requests do not necessarily represent new measurements.

## Program Architecture

The software currently uses four functions.

| Function | Purpose |
|---|---|
| `abfrage()` | Performs the HTTP request and retrieves the JSON response |
| `auswertung(wert)` | Extracts temperature and humidity values |
| `komfort(wert)` | Evaluates the measured temperature |
| `feuchtigkeitsbewertung(wert)` | Evaluates relative humidity |

The extracted measurements are returned as a tuple:

`(temperature, humidity)`

This allows further evaluation without repeating the data extraction.

### Temperature Evaluation

| Temperature | Classification |
|---|---|
| Below 18.9 °C | zu kalt |
| 18.9–23.1 °C | komfort |
| Above 23.1 °C | zu warm |

### Humidity Evaluation

| Relative Humidity | Classification |
|---|---|
| Below 34.9% | zu trocken |
| 34.9–65.1% | optimal |
| Above 65.1% | zu feucht |

These thresholds are preliminary and developer-defined. They are intended for testing and are not universal indoor climate standards.

## Development History

### Stage 1: HTTP and JSON Fundamentals

Development began with the `requests` library and a public HTTP testing service.

The initial objectives were to understand HTTP communication, response status codes, JSON parsing, function definitions and exception handling.

### Stage 2: Offline Sensor Testing

An independent branch, `feature/offline-sensor-testing`, was created for processing simulated Shelly measurement data without requiring access to physical hardware.

This allowed the JSON structure and data extraction to be tested separately from network connectivity.

### Stage 3: Live Sensor Integration

The development continued in `feature/shelly-live-integration`.

The application was connected to the physical Shelly H&T Gen3 through its HTTP RPC interface.

After resolving connectivity and data-processing errors, the first real temperature and humidity measurements were successfully retrieved.

### Stage 4: Modular Evaluation

Two independent evaluation functions were developed.

The first classifies room temperature, while the second evaluates relative humidity.

Function parameters and return values are used to transfer data between the different processing stages.

### Stage 5: Configuration Separation

The device-specific IP address was moved into a separate local configuration file.

The application now imports its sensor address from `config.py`, allowing developers to configure their own devices without modifying the main application logic.

## Programming Challenges and Lessons Learned

This project also documents the process of learning Python through practical problem-solving.

**HTTP connectivity:** Incorrect IP addresses, an invalid endpoint and intermittent sensor availability initially prevented successful communication.

**Dictionary access:** The first JSON processing attempts resulted in `KeyError` exceptions because the exact structure of the returned data had not yet been handled correctly.

**Python data types:** Returning multiple measurements required understanding the differences between tuples, sets, lists and dictionaries.

**Variable scope:** Local variables defined inside functions were initially accessed from outside their valid scope. This was resolved using return values and function parameters.

**Function calls:** Several errors were caused by confusing function references with function calls or passing unexpected argument types.

**Repeated execution:** Duplicate output revealed an unnecessary second function call.

**Modularity:** Early evaluation functions depended on variables from the main program. They were redesigned to work independently using input parameters.

**Debugging:** Reading tracebacks, inspecting return values and testing individual functions became essential parts of the development process.

Each issue was addressed incrementally, improving both the software and the developer's understanding of Python.

## Known Limitations

- No permanent measurement storage
- No measurement timestamps
- No graphical visualization
- HTTP response status codes are not yet explicitly validated
- Limited error diagnostics
- No automated test suite
- Repeated responses may contain unchanged sensor values
- Availability depends on the sensor's power and sleep behavior
- Current comfort classifications are simplified
- Polling and retry behavior require further refinement

## Planned Development

Future development may include:

- Improved error handling and HTTP status validation
- Automated offline tests
- Timestamped measurements
- CSV logging and database integration
- Historical temperature and humidity charts
- Dew point calculation
- Heating and indoor climate analysis
- MQTT communication
- Support for additional sensor devices
- Long-term monitoring through a dedicated Linux system

## Development Approach

Shelly Climate Monitor is primarily an independent learning and development project.

The software is developed incrementally, using documentation, experiments, debugging and practical testing with real hardware.

AI assistance is used for conceptual explanations, debugging hints and documentation. The programming work focuses on independently applying and understanding the concepts involved.

The repository is intended to provide a transparent record of both technical progress and the challenges encountered during development.

## License

This project is released under the MIT License.

See the `LICENSE` file for details.