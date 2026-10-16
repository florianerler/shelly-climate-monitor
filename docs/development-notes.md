# Development history and lessons learned

[Back to the project README](../README.md)

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

