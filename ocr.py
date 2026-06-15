
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"D:\ACS - WIN 10\Documents\OCR\book.png"

def pre_processing(image_path):
    print("Loading image......")
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not open or find the image: {image_path}")

    print("Image is processed now....")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresholded = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded

def text_extraction(Pimage):
    print("[3/4] Passing processed matrix to Tesseract Engine...")
    custom_configure = r'--psm 3'
    text = pytesseract.image_to_data(Pimage, config=custom_configure, output_type=pytesseract.Output.DICT)
    return text

def filter_and_display(original_image_path, ocr_data):
    CONFIDENCE_THRESHOLD = 80
    extracted_words = []

    n_boxes = len(ocr_data['text'])
    for i in range(n_boxes):
        if int(ocr_data['conf'][i]) >= CONFIDENCE_THRESHOLD:
            word = ocr_data['text'][i].strip()
            if word:
                extracted_words.append(word)

    final_text = " ".join(extracted_words)

    print("\n--- Pristine OCR Output (>= 80% Confidence) ---")
    print(final_text if final_text else "[No high-confidence text detected]")
    print("------------------------------------------------")


if __name__ == "__main__":
    # STEP 1: INPUT & PRE-PROCESSING
    processed_canvas = pre_processing(image_path)

    # STEP 2: MODEL INFERENCE (THE PROCESS)
    raw_ocr_data = text_extraction(processed_canvas)

    # STEP 3: DATA FILTERING & PRINTING (THE OUTPUT)
    filter_and_display(image_path, raw_ocr_data)

