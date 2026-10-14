# Shelly Climate Monitor

**A Python-based environmental monitoring and automated testing project for the Shelly H&T Gen3 sensor.**

Shelly Climate Monitor is a personal Python and IoT development project focused on retrieving, processing, evaluating, and testing real-world environmental measurements.

The project began with basic HTTP requests and offline JSON testing. It gradually evolved into a functional prototype capable of communicating with a physical Shelly H&T Gen3 sensor over a local network.

The final development stage introduced automated unit testing, allowing the application's data processing and climate evaluation functions to be verified independently of the physical sensor.

The project documents the progression from fundamental Python concepts to a small, modular, hardware-connected application with automated software tests and version-controlled development.

## Project Status

**Status: Completed Learning Project**

Shelly Climate Monitor has reached its intended educational objectives.

The final prototype implements live sensor communication, temperature and humidity evaluation, basic exception handling, external device configuration, and an automated unit test suite.

**Final local test result: 11 tests passed, 0 errors, 0 failures.**

This marks the completion of the project's planned learning and development cycle.

The repository remains available as a documented, functional prototype and as a reference for future software development.

The experience and technical knowledge gained throughout this project will be carried forward into a new, independent development initiative focused on custom measurement hardware, embedded programming, and modular sensor systems.

### Implemented Features

- HTTP communication with a Shelly H&T Gen3 sensor
- Retrieval and processing of JSON sensor responses
- Extraction of temperature and relative humidity
- Measurement values returned as a Python tuple
- Independent temperature and humidity evaluation functions
- Basic network exception handling
- Automatic retry attempts
- Configurable sensor IP address
- Separation of local configuration from public source code
- Modular functions using parameters and return values
- Separation of function definitions from program execution
- Automated unit testing with Python's built-in `unittest` framework
- Eleven successfully executed unit tests
- Version-controlled development using Git and GitHub
- Documented development history and debugging process

The application operates through a Python console.

## Hardware

| Component | Description |
|---|---|
| Sensor | Shelly H&T Gen3 |
| Communication | Wi-Fi |
| Interface | Shelly HTTP RPC API |
| Host | Windows PC running Python |
| Development environment | Thonny |
| Version control | Git / GitHub |
| Testing framework | Python `unittest` |

### Physical Sensor

![Shelly H&T Gen3](assets/shelly-hnt-gen3.jpg)

*The physical Shelly H&T Gen3 sensor used during development and live communication testing.*

## Example Output

![Program execution](assets/console_output.png)

Example console output from a successful measurement:

```text
Versuche Verbindung herzustellen...
temperatur: 24.7 °C
luftfeuchtigkeit: 45.5 %
(24.7, 45.5)
zu warm
optimal
```

These example measurements were retrieved from a physical Shelly H&T Gen3 sensor.

The temperature and relative humidity values are extracted from the sensor's JSON response, returned as a tuple, and passed to independent evaluation functions.

## Installation

### Requirements

- Python 3
- Python `requests` library
- Shelly H&T Gen3 connected to the local network
- Network access to the Shelly device

### 1. Clone the Repository

```bash
git clone https://github.com/florianerler/shelly-climate-monitor.git
cd shelly-climate-monitor
```

Alternatively, download the repository directly from GitHub.

### 2. Install Dependencies

Install the required Python package using:

```bash
python -m pip install -r requirements.txt
```

The application uses the `requests` library for HTTP communication.

The automated tests use Python's built-in `unittest` framework and require no additional testing package.

### 3. Configure the Sensor

For easier configuration and separation of device-specific settings, the Shelly IP address is stored outside the main application.

Copy the provided configuration template:

`config.example`

Create a copy named:

`config.py`

Open `config.py` and configure your Shelly device:

```python
SHELLY_IP = "192.168.1.XXX"
```

Replace the placeholder with your sensor's actual local IP address.

The local `config.py` file is excluded from Git tracking through `.gitignore`.

The configuration file must exist when importing the main module, including during automated testing.

### 4. Run the Application

Execute:

```bash
python shelly_monitor.py
```

The application will attempt to contact the configured Shelly sensor and process the received measurements.

The current program repeats the request cycle approximately every 30 seconds, with additional time required for network requests.

**Important:** The battery-powered Shelly H&T Gen3 may enter sleep mode and temporarily become unavailable through HTTP.

Repeated successful requests may also return unchanged measurements.

Stop the program using `Ctrl+C` in the terminal.

## Program Architecture

The application is organized into four main functions.

| Function | Purpose |
|---|---|
| `abfrage()` | Sends an HTTP request and retrieves the response status and JSON data |
| `auswertung(wert)` | Extracts temperature and humidity values from the JSON structure |
| `komfort(wert)` | Evaluates the measured temperature |
| `feuchtigkeitsbewertung(wert)` | Evaluates relative humidity |

### Data Processing

The processing sequence follows four stages:

1. **Data acquisition:** The sensor is contacted through its local HTTP RPC interface.
2. **Data extraction:** Temperature and humidity are extracted from the JSON response.
3. **Data evaluation:** Both measurements are independently classified.
4. **Console output:** Measurements and classifications are displayed.

The extracted measurements are returned as a tuple:

```python
(temperature, humidity)
```

The tuple allows individual values to be accessed and passed to subsequent functions.

### Main Program Execution

The application's measurement loop is protected by:

```python
if __name__ == "__main__":
```

This allows functions to be imported into another Python module without automatically starting the continuous measurement loop.

This separation was introduced during the automated testing stage and represents an important improvement in the application's structure.

## Temperature Evaluation

The `komfort(wert)` function evaluates temperature using the following conditions:

| Temperature | Classification |
|---|---|
| Below 19 °C | `zu kalt` |
| 19–23 °C, inclusive | `komfort` |
| Above 23 °C | `zu warm` |

These classifications are based on developer-defined thresholds.

They are intended for programming exercises and simplified room climate evaluation rather than as universal indoor comfort standards.

## Humidity Evaluation

The `feuchtigkeitsbewertung(wert)` function evaluates relative humidity.

| Relative Humidity | Classification |
|---|---|
| Below 35% | `zu trocken` |
| 35–65%, inclusive | `optimal` |
| Above 65% | `zu feucht` |

The thresholds are preliminary and serve educational purposes.

Actual indoor climate assessment depends on additional factors, including temperature, occupancy, ventilation, and building conditions.

## Automated Unit Testing

The final development stage introduced an automated test suite using Python's standard `unittest` framework.

The purpose of the test suite is to verify that the application's evaluation and data extraction functions return the expected results for predefined inputs.

These tests operate without requiring an active connection to the physical Shelly device.

### Test File

`test_shelly_monitor.py`

The test suite contains three test classes:

- `TestKomfort`
- `TestFeuchtigkeitsbewertung`
- `TestAuswertung`

### Temperature Tests

| Test | Input | Expected Result |
|---|---|---|
| Normal temperature | 21 °C | `komfort` |
| Low temperature | 17 °C | `zu kalt` |
| High temperature | 25 °C | `zu warm` |
| Lower boundary | 19 °C | `komfort` |
| Upper boundary | 23 °C | `komfort` |

**5 temperature tests**

### Humidity Tests

| Test | Input | Expected Result |
|---|---|---|
| Normal humidity | 50% | `optimal` |
| High humidity | 80% | `zu feucht` |
| Low humidity | 20% | `zu trocken` |
| Lower boundary | 35% | `optimal` |
| Upper boundary | 65% | `optimal` |

**5 humidity tests**

### Data Extraction Test

The eleventh test verifies the `auswertung()` function using simulated Shelly sensor data.

The function receives a nested dictionary containing temperature and humidity measurements.

The test verifies that the function extracts the values correctly and returns the expected tuple.

**Input data:**

```python
{
    "temperature:0": {"tC": 20},
    "humidity:0": {"rh": 50}
}
```

**Expected return value:**

```python
(20, 50)
```

This test verifies the application's handling of nested dictionaries without requiring physical sensor communication.

**1 data extraction test**

### Running the Tests

From the project directory, execute:

```bash
python -m unittest -v
```

The `-v` argument enables verbose output, displaying the individual test results.

If Python is not available through the `python` command, use the Python interpreter associated with your development environment.

### Successful Test Execution

![Automated unit test results](assets/test_output.png)

*Terminal screenshot showing the successful execution of all eleven automated unit tests.*

Verified local test result:

```text
----------------------------------------------------------------------
Ran 11 tests in 0.003s

OK
```

All eleven tests completed successfully during the final local test run.

### Testing Scope

The automated tests currently cover:

- Temperature classifications
- Humidity classifications
- Exact evaluation boundaries
- JSON-like measurement data extraction
- Expected function return values

The following behaviors are not covered by the unit tests:

- Live HTTP communication
- Sensor sleep and wake-up behavior
- Network timeouts and connection failures
- Malformed or incomplete JSON responses
- Long-term operation and measurement reliability

The test suite verifies defined portions of the application's software logic. It does not establish that the entire system is free of defects.

## Development History

### Stage 1: HTTP and JSON Fundamentals

Development began with Python's `requests` library and a public HTTP testing service.

The initial learning objectives included:

- HTTP GET requests
- Response status codes
- JSON parsing
- Function definitions
- Return values
- Exception handling

These exercises established the foundation for communication with a physical sensor.

### Stage 2: Offline Sensor Testing

The development branch `feature/offline-sensor-testing` was created to experiment with simulated Shelly measurements.

This allowed the expected JSON structure to be studied without requiring access to physical hardware.

The exercises introduced nested dictionaries and measurement extraction.

### Stage 3: Live Sensor Integration

The project continued in `feature/shelly-live-integration`.

The application was connected to a physical Shelly H&T Gen3 through its local HTTP RPC interface.

After troubleshooting connectivity and data-processing problems, the first real temperature and relative humidity measurements were successfully retrieved.

### Stage 4: Modular Climate Evaluation

Independent evaluation functions were implemented for temperature and humidity.

Function parameters and return values were used to transfer measurements between different processing stages.

This introduced a more structured approach to software development and reduced dependencies between individual functions.

### Stage 5: Configuration Separation

The local sensor IP address was moved from the main application into a separate `config.py` file.

A public configuration template was included to make the software easier to adapt to other Shelly devices.

The local configuration file was excluded from Git tracking through `.gitignore`.

### Stage 6: Automated Unit Testing

The final development branch, `feature/automated-tests`, introduced systematic software testing using Python's `unittest` framework.

The main measurement loop was placed inside a `__main__` guard to allow individual functions to be imported independently.

Automated tests were developed incrementally, beginning with a single temperature evaluation test.

The test suite was subsequently expanded to cover:

- Temperature classifications
- Humidity classifications
- Boundary conditions
- Nested dictionary data extraction

The final local execution completed successfully with eleven passing tests.

This stage completed the project's planned educational development cycle.

## Programming Challenges and Lessons Learned

This project documents the process of learning Python through practical development, debugging, and experimentation.

**HTTP connectivity:** Incorrect device addresses, endpoint problems, and intermittent sensor availability initially prevented successful communication.

**JSON processing:** Understanding the structure of nested dictionaries was essential for correctly extracting sensor measurements.

**Python data types:** The project required distinguishing between integers, floats, strings, tuples, lists, sets, and dictionaries.

**Variable scope:** Local variables initially caused problems when accessed outside their functions. Return values and function parameters were introduced to resolve these issues.

**Function calls:** Differentiating between function references, function calls, input arguments, and returned values became an important learning objective.

**Modular programming:** Evaluation functions were redesigned to accept independent input parameters instead of relying on external variables.

**Exception handling:** Basic network-related exceptions were handled to prevent certain connection failures from immediately terminating the program.

**Git and GitHub:** Feature branches, commits, push operations, pull requests, and merge operations were used to document and organize development.

**Import behavior:** The differences between importing Python modules and executing scripts directly were explored while introducing automated tests.

**Test classes and methods:** Python classes, inheritance from `unittest.TestCase`, and test methods were introduced during the final development stage.

**Assertions:** `assertEqual()` was used to compare actual function results with expected values.

**Testing data structures:** Simulated nested dictionaries were used to verify the data extraction function independently of hardware.

**Error interpretation:** `NameError`, `TypeError`, `KeyError`, `SyntaxError`, `IndentationError`, and failed test assertions provided practical debugging experience.

These challenges were addressed incrementally and helped establish a stronger understanding of Python programming and software testing.

## Known Limitations

Although the learning project is complete, the application remains an educational prototype rather than a production-ready monitoring system.

Current limitations include:

- No permanent measurement storage
- No measurement timestamps
- No historical data visualization
- HTTP response status codes are returned but not explicitly validated
- Limited connection diagnostics
- No automated HTTP integration tests
- No automated validation of malformed JSON responses
- Repeated requests may return unchanged sensor values
- Sensor availability depends on its power supply and sleep behavior
- Simplified temperature and humidity classifications
- Fixed polling interval
- Console output remains coupled to parts of the data processing logic
- No long-term reliability testing

These limitations are documented intentionally to distinguish the project's completed learning objectives from production-level requirements.

## Future Development Perspective

**The Shelly Climate Monitor learning project is considered complete.**

No further feature development is currently planned for this prototype.

The source code, documentation, and automated tests will remain available as a reference for future work.

The next development initiative will build upon the programming knowledge acquired here while moving toward independently designed measurement hardware and embedded systems.

Areas of continued learning will include:

- Microcontroller programming
- Digital sensor communication
- I²C and other hardware interfaces
- Sensor measurement principles
- Modular hardware and software architecture
- Automated testing
- Data logging and transmission
- Measurement validation and comparative analysis
- Printed circuit board design
- Network-connected measurement systems

The next initiative will be developed as an independent project rather than as a direct extension of the Shelly Climate Monitor source code.

## Development Approach

Shelly Climate Monitor was developed as an independent educational programming project.

Its development followed an incremental approach:

1. Establish fundamental concepts.
2. Experiment with small functional components.
3. Investigate and resolve programming errors.
4. Connect the software to real hardware.
5. Improve modularity and configuration.
6. Introduce automated software testing.
7. Document the completed development process.

AI assistance was used for conceptual explanations, incremental debugging guidance, and documentation.

The programming exercises emphasized independently understanding and applying the concepts involved.

The repository preserves the progression from an elementary HTTP client to a functional, hardware-connected Python application with automated tests.

## Project Conclusion

Shelly Climate Monitor successfully achieved its intended educational objectives.

The project provided practical experience with Python, HTTP communication, JSON processing, function design, exception handling, Git-based development, and automated unit testing.

Its final development milestone consisted of eleven successfully executed unit tests covering temperature evaluation, humidity evaluation, and simulated sensor data extraction.

Although the application remains limited in scope, it established a useful technical and methodological foundation for future development.

**The learning project is now complete, and development will continue in a new, independent project focused on custom-built measurement systems.**

## License

This project is released under the MIT License.

See the `LICENSE` file for details.