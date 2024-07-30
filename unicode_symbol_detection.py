import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# Create a mapping dictionary for chess symbols
chess_symbols = {
    '\u2654': '♔',
    '\u2655': '♕',
    '\u2656': '♖',
    '\u2657': '♗',
    '\u2658': '♘',
    '\u2659': '♙',
    '\u265A': '♚',
    '\u265B': '♛',
    '\u265C': '♜',
    '\u265D': '♝',
    '\u265E': '♞',
    '\u265F': '♟︎',
}

def extract_text_from_pdf(pdf_path, start_page, end_page):
    # Convert the pages into images
    images = convert_from_path(pdf_path)[start_page - 1:end_page]

    text = ""

    # Run OCR on each image
    for image in images:
        text += pytesseract.image_to_string(image, lang='eng')

    # Replace misinterpreted characters with the correct chess symbols
    for code, symbol in chess_symbols.items():
        text = text.replace(code, symbol)

    return text

# usage
pdf_path = 'your_file.pdf'  # replace with your file path
start_page = 785
end_page = 1153
text = extract_text_from_pdf(pdf_path, start_page, end_page)
print(text)

--------



import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import chess
import chess.pgn
import re

# Function to extract text from image using pytesseract
def extract_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

# Function to convert PDF to images
def convert_pdf_to_images(pdf_path):
    return convert_from_path(pdf_path)

# Function to recognize chess pieces and board state
def recognize_chess_board(text):
    # Mapping Unicode characters to chess pieces
    unicode_pieces = {
        '♔': 'K', '♕': 'Q', '♖': 'R', '♗': 'B', '♘': 'N', '♙': 'P',
        '♚': 'k', '♛': 'q', '♜': 'r', '♝': 'b', '♞': 'n', '♟': 'p'
    }
    board = chess.Board()
    rows = text.split('\n')
    board_state = ""
    
    # Extract game information (players and date)
    game_info = re.search(r'(\d+)\.\s+(\w+)\s*-\s*(\w+)\n(\w+,\s*\d+)', text)
    if game_info:
        game_number, white_player, black_player, date = game_info.groups()
    else:
        white_player, black_player, date = "Unknown", "Unknown", "Unknown"

    # Read board state
    for row in rows:
        row_state = []
        for char in row:
            if char in unicode_pieces:
                row_state.append(unicode_pieces[char])
            elif char == ' ':
                row_state.append('1')  # Empty square as '1' in FEN notation
        if row_state:
            board_state += ''.join(row_state) + '/'

    # Convert board state to FEN format
    fen = board_state.strip('/').replace('11111111', '8').replace('1111111', '7').replace('111111', '6').replace('11111', '5').replace('1111', '4').replace('111', '3').replace('11', '2')
    board.set_fen(fen + ' w KQkq - 0 1')  # Assuming it's White to move and standard initial conditions
    
    return white_player, black_player, date, board

# Function to save game to PGN format
def save_to_pgn(white_player, black_player, date, board, output_file):
    game = chess.pgn.Game()
    game.headers["White"] = white_player
    game.headers["Black"] = black_player
    game.headers["Date"] = date
    game.setup(board)
    with open(output_file, "w") as pgn_file:
        pgn_file.write(str(game))

# Main function
def process_chess_image(file_path, output_file):
    if file_path.endswith('.pdf'):
        images = convert_pdf_to_images(file_path)
        text = "\n".join([extract_text_from_image(image) for image in images])
    else:
        text = extract_text_from_image(file_path)

    white_player, black_player, date, board = recognize_chess_board(text)
    save_to_pgn(white_player, black_player, date, board, output_file)

# Example usage
process_chess_image('path/to/your/file.jpg', 'output.pgn')
