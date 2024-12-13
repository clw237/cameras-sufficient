from typing import List, Dict, Tuple

def is_hardware_sufficient(
    target_distance_range: Tuple[float, float],
    target_light_range: Tuple[float, float],
    camera_list: List[Dict[str, Tuple[Tuple[float, float], Tuple[float, float]]]]
) -> bool:
    """
    Check if the hardware cameras can meet the software camera's requirements.

    Parameters:
    - target_distance_range: (min_distance, max_distance) tuple for distance.
    - target_light_range: (min_light, max_light) tuple for light levels.
    - camera_list: List of dictionaries with 'model', 'distance_limits', and 'light_limits'.

    Returns:
    - bool: True if sufficient, False otherwise.
    """

    # Use any() to check if there is at least one camera that meets both distance and light requirements
    return any(
        # Check if the camera's distance limits overlap with the target distance range
        (cam['distance_limits'][0] <= target_distance_range[1] <= cam['distance_limits'][1] or
         cam['distance_limits'][0] <= target_distance_range[0] <= cam['distance_limits'][1]) and
        
        # Check if the camera's light limits overlap with the target light range
        (cam['light_limits'][0] <= target_light_range[1] <= cam['light_limits'][1] or
         cam['light_limits'][0] <= target_light_range[0] <= cam['light_limits'][1])
        
        # Iterate through each camera in the camera list
        for cam in camera_list
    )

# Example usage:
desired_distance = (0.5, 5.0)  # Desired subject distance range in meters
desired_light = (100, 1000)     # Desired light level range in lux
hardware_cameras = [
    {'model': 'Camera A', 'distance_limits': (0.3, 2.0), 'light_limits': (50, 500)},
    {'model': 'Camera B', 'distance_limits': (1.5, 6.0), 'light_limits': (200, 1200)},
]

# Check if the selected hardware cameras are sufficient for the desired characteristics
result = is_hardware_sufficient(desired_distance, desired_light, hardware_cameras)
print("Is the hardware sufficient?", result)
