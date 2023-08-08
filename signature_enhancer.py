from PIL import Image
import cv2
import numpy as np

def change_signature_color(image_path, output_path):
    # Open the image
    img = Image.open(image_path)
    
    # Ensure image is in RGB mode
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Access the image's pixel data
    pixels = img.load()
    
    # Loop through the image's pixels
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            
            # If the pixel is black or near black, change it to blue
            if r < 40 and g < 40 and b < 40:  # tweak these values if needed
                pixels[x, y] = (0, 0, 255)
    
    # Save the modified image
    img.save(output_path)

def smooth_signature_edges(image_path, output_path):
    # Load the image in color
    img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # Convert image to grayscale
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    # Apply a Gaussian blur
    blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    
    # Threshold the image to binarize
    _, threshed = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Where the signature is (white in the mask), set the color to blue
    blue_value = [255, 0, 0]  # BGR value for blue
    img_color[threshed == 255] = blue_value
    
    # Save the smoothed signature in blue with original background
    cv2.imwrite(output_path, img_color)

change_signature_color('sigature.jpg', 'blue_sigature.jpg')
smooth_signature_edges('blue_sigature.jpg', 'smoothed_blue_sigature.jpg')
