# Chess Computer Vision Project

Repo for processing images/PDFs of chess puzzles and calculating chess piece locations into standardized FEN notation using python's [OpenCV](https://pypi.org/project/opencv-python/) package.

A complete step-by-step breakdown of the project steps can be seen in the Work Breakdown Structure (WBS) document in the [python_testing](https://github.com/sean-gits-py/chess/tree/main/python_testing#readme) folder.

**1. Preprocessing Steps:**
* Bash script to import chess puzzle pages and save each puzzle as an independent image file.
* Python script to extract text from pages and save information in csv format. Specifically extracted text will note puzzle number ID and any relevant information for each puzzle, for example if black or white plays the next move.
* Load puzzle number, page number, and chapter section information from csv.
* Open and assign the chess puzzle image to it's puzzle ID number.
*	Open and assign which side, black or white, plays next move to each puzzle ID number.

**2.	Chess Board Recognition:**
* Script [image_frame_detector.py](https://github.com/sean-gits-py/chess/blob/main/image_frame_detector.py) uses OpenCV to detect the chessboard corners in each image and standardize coloring of each image into grayscale.
* Define function to save each square of chess board into independent images for future OCR processing. Each cell is assigned it's own unique ID.
* Define function to use OCR to identify chess piece in each unique cell. Save identified chess piece information as text and assign chess piece value to each cell unique ID.
* Process extracted text information and reconstruct the chess board.

**3.	Chess PGN (portable game notation) Handling:**
* Read reconstructed text string information for each puzzle.
* Define function to use python chess package and translate text string into standard FEN notation.
*	Save each puzzles FEN notation
*	Use Lichess API or Chess.com API to load FEN notation to online chess game engine

Example Chess Puzzle Image:

![Puzzle-001](https://github.com/sean-gits-py/chess/blob/main/images/puzzle_images/cm_puzzle_one.png)
