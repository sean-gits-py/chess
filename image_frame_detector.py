import cv2
import numpy as np

def draw_chessboard_corners(image_path, grid_size=(7, 7)):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, grid_size, None)

    if ret:
        # Refine the corner positions
        corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), 
                                   criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1))
        
        # Draw the corners on the image
        cv2.drawChessboardCorners(image, grid_size, corners, ret)

        # Display the image with corners drawn
        cv2.imshow('Chessboard Corners', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Chessboard corners not found.")

# Example usage
image_path = 'chessboard.jpg'  # Replace with your image path
draw_chessboard_corners(image_path, grid_size=(7, 7))
