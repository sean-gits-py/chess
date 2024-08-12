import cv2

def extract_puzzle_by_bounds(image, bounds: list, section_id: int, puzzle_id: int):
    """Extracts a puzzle from the given image using specified bounds and saves it."""
    (x0, y0, x1, y1) = bounds
    cropped_img = image[y0:y1, x0:x1]
  
    cv2.imwrite(problem_file(section_id, puzzle_id), cropped_img)

def extract_section(section_id: int, first_page: int, last_page: int, first_puzzle_id: int):
    """Extracts puzzles from a section by iterating through pages and extracting image areas."""
    
    # Constants based on the page layout
    inch_to_pixel = 300  # DPI conversion (assuming images are 300 DPI)
    image_size = 2.25 * inch_to_pixel  # Size of each image
    margin_size = 1.25 * inch_to_pixel  # Size of margin between images
    header_size = 2.0 * inch_to_pixel  # Header size
    footer_size = 1.4 * inch_to_pixel  # Footer size

    # Initial coordinates for the top-left image
    start_x = margin_size / 2
    start_y = header_size + (margin_size / 2)

    puzzle_id = first_puzzle_id

    for page_number in range(first_page, last_page + 1):
        img = load_page_image(page_number)
        if img is not None:
            for row in range(3):  # Three rows
                for col in range(2):  # Two columns
                    x0 = int(start_x + col * (image_size + margin_size))
                    y0 = int(start_y + row * (image_size + margin_size))
                    x1 = int(x0 + image_size)
                    y1 = int(y0 + image_size)

                    # Extract the puzzle image using calculated bounds
                    extract_puzzle_by_bounds(img, [x0, y0, x1, y1], section_id, puzzle_id)
                    puzzle_id += 1
