import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import pickle

def find_board(img, section_id, image_size, model, lb):
    """Detects and labels chess pieces on a board."""
    board = Board()
    board.empty()
    for i in range(0, 8):
        for j in range(0, 8):
            crop_img = extract_custom_cell_from_board(img, i, j)
            crop_img = preprocess(crop_img)
            label = predict(model, crop_img, lb)
            if label != 'e' and label != 'E':
                # We plot the non-empty labels
                board.board[j][i] = label[0]

    return board

def preprocess(image):
    """Resizes and normalizes the image for prediction."""
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

def load_cnn_with_labels(model_file: str, label_binarizer: str):
    """Loads the CNN model and label binarizer from files."""
    model = load_model(model_file)
    lb = pickle.loads(open(label_binarizer, "rb").read())
    return model, lb

def extract_custom_cell_from_board(img, i, j):
    """Extracts the square cell (i, j) from the board image."""
    cell_height, cell_width = img.shape[0] // 8, img.shape[1] // 8

    x = i * cell_width
    y = j * cell_height
    crop_img = img[y:y + cell_height, x:x + cell_width]
    return crop_img

def predict(model, image, lb):
    """Predicts the label of a preprocessed image."""
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    return label
