import pyautogui
import cv2
from test import *
screenshot_filename = f"screenshot.png"
screenshot = pyautogui.screenshot()
screenshot.save(screenshot_filename)

print(f"Screenshot saved as {screenshot_filename}")

def get_patch(name, bbox:tuple):
    image = cv2.imread('screenshot.png')

    if image is not None:
        x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2], bbox[3]  

        cropped_patch = image[y1:y2, x1:x2]

        cv2.imwrite(name, cropped_patch)
        cv2.destroyAllWindows()
        print(f'Patch saved: {name}')
    else:
        print('Image not found or could not be loaded.')

#get_patch("amount.png",(am_sc_xy[0],am_sc_xy[1],am_sc_lowerxy[0],am_sc_lowerxy[1]))
get_patch("new_option.png",(wider_upper[0],wider_upper[1],wider_lower[0],wider_lower[1]))