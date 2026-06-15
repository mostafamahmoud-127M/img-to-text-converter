# OCR Text Extraction with OpenCV and Tesseract

A Python-based Optical Character Recognition (OCR) pipeline that preprocesses images using **OpenCV** to improve text readability, extracts text data via **Tesseract OCR**, and filters out low-confidence results to deliver clean, accurate text output.


## Features
* **Image Preprocessing:** Automatically converts images to grayscale, applies Gaussian blurring to reduce noise, and utilizes **Otsu's Thresholding** to create a clean binary (black and white) image optimized for OCR.
* **Structured Data Extraction:** Uses Tesseract’s `image_to_data` to fetch not just the raw text, but positional data and confidence scores for every single word.
* **Confidence Filtering:** Filters out noisy or misread characters by only printing words that meet a customizable confidence threshold (default: >= 80%).

---

## Prerequisites
Before running the script, ensure you have the following installed on your system:

1. **Python 3.x**
2. **Tesseract OCR Engine** (Windows installer required for the default path used in this script).

---

## Installation & Setup

### 1. Install Python Dependencies
Install the required libraries using `pip`:
```bash
pip install opencv-python numpy pytesseract
pytesseract.pytesseract.tesseract_cmd = r"YOUR_TESSERACT_PATH_HERE"
image_path = r"C:\Your\Path\To\Your\image.png"
python your_script_name.py
