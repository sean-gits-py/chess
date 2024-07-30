# Chess

Repo for processing the board state (chess piece locations), and calculating optimal checkmate solutions.

Overview
1.	OCR and Image Processing:
	•	pytesseract extracts text from the image or converted PDF images.
	•	pdf2image converts PDF pages to images for OCR processing (where applicable).
2.	Chess Board Recognition:
	•	The script maps Unicode chess symbols to standard FEN notation.
	•	It processes the text to extract rows and reconstructs the board state.
3.	PGN Handling:
	•	chess.pgn is used to create and save the game in PGN format.
	•	The script extracts the player names and date from the text using regex.
