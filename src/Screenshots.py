import time
import logging
from PIL import ImageGrab

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Path where to save the screenshots
screenshot_folder = "C:/Users/Goomie/Documents/Dev/wow-gpt/screenshots/"

# Capture frequency in seconds (increase this value to reduce resource consumption)
capture_frequency = 10

# Loop to periodically capture the screen
while True:
    try:
        # Generate a unique file name based on date and time
        file_name = time.strftime("%Y%m%d%H%M%S") + ".png"

        # Capture the screen and save the image with reduced resolution
        capture = ImageGrab.grab()
        capture.thumbnail((1280, 720))  # Reduce resolution to 720p
        capture.save(screenshot_folder + file_name,
                     "JPEG", quality=60)  # Reduce quality

        # Wait for the next capture
        time.sleep(capture_frequency)

        # Log a message to indicate that the capture was done
        logging.info(
            f"Capture completed and saved as {screenshot_folder + file_name}")

    except Exception as e:
        # In case of error, log an error message
        logging.error(f"Error while capturing screen: {str(e)}")

    # You can add a condition to stop the loop if necessary
