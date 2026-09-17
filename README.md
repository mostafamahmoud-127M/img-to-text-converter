#  Image-to-Text Converter (OCR)

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![OCR Engine](https://img.shields.io/badge/OCR-Tesseract%20%2F%20EasyOCR-007ACC.svg?style=flat)](#)
[![Computer Vision](https://img.shields.io/badge/Vision-OpenCV-5C3EE8.svg?style=flat&logo=opencv&logoColor=white)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A lightweight, automated optical character recognition pipeline designed to extract, parse, and structure text from raster images, scanned documents, and photographic captures. Built with foundational computer vision preprocessing to maximize character detection accuracy.

---

##  Features

* **Multi-Format Ingestion**: Supports common image formats including `.png`, `.jpg`, `.jpeg`, and `.bmp`.
* **Vision Preprocessing Pipeline**: Applies grayscale conversion, thresholding/binarization, and noise suppression to improve OCR precision on degraded inputs.
* **Text Extraction & Post-Processing**: Detects character boundaries, extracts textual content, and strips layout noise or artifacts.
* **Flexible Export**: Displays extracted strings directly in the terminal interface or persists output to `.txt` files.

---

##  Pipeline Architecture

```text
[ Input Image ] 
       │
       ▼
[ Preprocessing (Grayscale, Thresholding, Denoising) ]
       │
       ▼
[ OCR Inference Engine (Character Detection & Recognition) ]
       │
       ▼
[ Extracted Text / Formatted Output (.txt / CLI) ]
