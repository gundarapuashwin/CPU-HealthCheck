# CPU-HealthCheck

A lightweight Windows system monitoring tool built with Python to check CPU health, usage, and overall system performance.
This project helps monitor CPU status in real-time, detect abnormal behavior, and provide useful diagnostic insights for maintaining system stability on Windows devices.

## Features

* Real-time CPU usage monitoring
* Per-core CPU utilization tracking
* CPU frequency monitoring
* RAM usage overview
* Disk usage monitoring
* System uptime tracking
* Basic health status summary
* Lightweight and fast execution
* Simple CLI-based output
* Designed specifically for Windows systems

## Tech Stack

* **Python 3**
* **psutil**
* **Windows System APIs (via Python libraries where needed)**

## Installation

Clone the repository:

```bash id="a1"}
git clone https://github.com/gundarapuashwin/CPU-HealthCheck.git
cd CPU-HealthCheck
```

Install dependencies:


```bash id="a3"}
pip install psutil
```

## Usage

Run the script:

```bash id="a4"}
python main.py
```


## Project Goal

The goal of this project is to create a simple but practical Windows diagnostics tool that helps users quickly inspect CPU and basic system health without relying on heavy third-party monitoring software.

This is especially useful for students, developers, and users troubleshooting slow systems or checking general PC performance.

## Future Improvements

* GPU health monitoring
* Battery diagnostics for laptops
* Temperature monitoring support
* Export reports to JSON/CSV
* GUI dashboard version
* Automatic health alerts for high CPU usage or overheating

## Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## License

This project is open source and available under the GNU General Public License.

## Author

Built by Ashwin Gundarapu

GitHub: https://github.com/gundarapuashwin
