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
