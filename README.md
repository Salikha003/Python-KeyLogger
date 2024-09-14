# Simple Python Keylogger

This is a simple keylogger script written in Python using the `pynput` library that logs keystrokes to a file named `keylogger.txt`.

## Description

This script listens to keystrokes using the `pynput` library and logs them into a file. Each keystroke is recorded as follows:

- Alphabetic and numeric characters are logged as they are.
- Special keys such as `space`, `esc`, `backspace`, and others are logged by their names.
- Exceptions (such as crashes when non-character keys are pressed) are handled and logged as errors.

## Installation

### Prerequisites

- `pynput` library

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/Salikha003/Python-KeyLogger.git
   
2. **Install `pynput`**

   ```bash
   pip install pynput

# Usage

1. **Run the script using Python:**

   ```bash
   python keylogger.py

# Disclaimer

### This keylogger is intended for educational and ethical purposes only. Please ensure you have the appropriate permissions before using it :) 
