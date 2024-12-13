# Camera Sufficiency Checker

This Python program checks if a set of hardware cameras can meet the desired characteristics of a software camera based on specified distance and light level ranges. It identifies if any of the cameras provided, is suitable for the given requirements.

## Features

- Determine if any hardware camera can cover the desired subject distance range.
- Check if any camera can operate within the specified light level range.
- Returns True or False if any matching camera is found

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/clw237/cameras-sufficient.git
   cd your-repository
2. **Run Python Program**:
   ```bash
   python .\cameras-sufficient.py

### Explanation of Example Usage

- **Desired Distance Range**:  
  `desired_distance = (0.5, 5.0)` specifies that the software camera should be able to handle distances between **0.5 meters** and **5.0 meters**.

- **Desired Light Level Range**:  
  `desired_light = (100, 1000)` indicates that the software camera should operate effectively within light levels from **100 lux** to **1000 lux**.

- **Hardware Cameras Definition**:  
  The `hardware_cameras` list contains two cameras:
  
  - **Camera A**:  
    Distance limits are from **0.3 meters** to **2.0 meters**, and it operates between **50 lux** and **500 lux**.
  
  - **Camera B**:  
    Distance limits are from **1.5 meters** to **6.0 meters**, and it operates between **200 lux** and **1200 lux**.

- **Expected Result**:  
  When this code is executed, it checks if any of the listed hardware cameras can meet both the distance and light requirements specified by desired_distance and desired_light. The output will be:
  ```bash
  Is the hardware sufficient? True