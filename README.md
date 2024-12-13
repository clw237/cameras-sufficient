# Camera Sufficiency Checker

This Python program checks if a set of hardware cameras can meet the desired characteristics of a software camera based on specified distance and light level ranges. It identifies which camera, if any, is suitable for the given requirements.

## Features

- Determine if any hardware camera can cover the desired subject distance range.
- Check if any camera can operate within the specified light level range.
- Return the model name of the first sufficient camera found.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
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
  When the example code is executed, it calls the `find_sufficient_camera` function with the defined distance and light ranges along with the list of hardware cameras. The function checks each camera against the specified requirements:
  
  - If a suitable camera is found that meets both the distance and light level criteria, it will print:
    ```
    The sufficient camera is: Camera B
    ```
    In this case, **Camera B** is suitable because its distance range overlaps with the desired distance range and its light level range also meets the requirements.

  - If no suitable camera is found, it will print:
    ```
    No suitable camera found.
    ```