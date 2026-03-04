# StealthTasker

**StealthTasker** is an automated, stealthy, human-like UI interaction script built with Python and PyAutoGUI. It is designed to automatically fill out tasks (such as selecting the best/worst images) across multiple iterations while mimicking organic, randomized human behavior to avoid detection by basic anti-bot mechanisms.

## Features

- **Human-Like Mouse Movements**: Uses randomized movement durations and Bézier curve easing (tweening) to simulate natural human mouse drag, instead of instantly snapping to coordinates.
- **Randomized Number Typing**: Automatically generates and types unique random numbers (between 1 and 8) with realistic, randomized typing delays between keystrokes.
- **Organic Distraction Drifts**: Naturally drifts the mouse to random intermediate "safe" areas of the screen between actions to simulate human distraction or reading.
- **Random Movement Phase (Delays)**: During the 10-second wait between loops, the mouse pointer continues to move completely randomly across the screen at varying speeds (or occasionally sits still), rather than statically waiting.
- **Graceful Kill Switch**: Implements a global `ESC` key kill switch, allowing you to stop the script instantly and safely at any moment.

## Prerequisites

- Python 3.x
- Windows/macOS/Linux

### Required Python Libraries
Install the necessary dependencies using pip:
```bash
pip install pyautogui keyboard
```

*(Note: If you want to use the included mouseinfo tool to easily grab your screen coordinates, also install `mouseinfo`)*
```bash
pip install mouseinfo
```

## Setup & Configuration

Before running the script, you must configure the exact coordinates of your target input fields and buttons.

1. **Find Your Coordinates**
   Open a terminal and run the MouseInfo tool to find the exact X and Y coordinates on your screen:
   ```bash
   python -c "import mouseinfo; mouseinfo.MouseInfoWindow()"
   ```
2. **Update the Script**
   Open `automation_script.py` and update the configuration section at the top of the file with your specific screen coordinates:
   ```python
   POS_1 = (110, 260)        # E.g., Input field 1
   POS_UNSELECT = (1058, 245) # E.g., A neutral click area
   POS_2 = (143, 345)        # E.g., Input field 2
   POS_3 = (1829, 146)       # E.g., Your final Submit button
   ```

## Usage

Simply run the script in your terminal:
```bash
python automation_script.py
```

The script will give you **3 seconds** to focus onto your target window/browser before it begins the automation loop. It will run for **50 iterations**.

## Emergency Kill Switches

Since this script takes control of your mouse and keyboard, two fail-safes are included:
1. **The ESC Key Switch**: Press and hold the `ESC` key on your keyboard at any time. The script will detect this and exit gracefully.
2. **PyAutoGUI Fail-Safe**: Quickly slam your mouse into any of the 4 extreme corners of your monitor. This will trigger PyAutoGUI's built-in fail-safe, instantly aborting the program.

## Disclaimer

This script is purely for educational purposes and personal automation. Always ensure you are complying with the Terms of Service of any application or website you interact with.
