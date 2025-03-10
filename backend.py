from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
from paddleocr import PaddleOCR

app = FastAPI()

# Folder containing images
IMAGE_FOLDER = "images"

# Initialize PaddleOCR once
ocr_model = PaddleOCR(use_angle_cls=True, lang='en')

def perform_ocr(image_path):
    """Performs OCR on the given image and returns extracted text."""
    result = ocr_model.ocr(image_path, cls=True)
    extracted_text = [line[1][0] for line in result[0]] if result and result[0] else []
    return extracted_text

@app.get("/get_extracted_text")
def get_extracted_text():
    """Perform OCR on all images in the folder and return extracted text."""
    images = os.listdir(IMAGE_FOLDER)
    if not images:
        return JSONResponse(content={"error": "No images found in folder"})

    extracted_data = []
    for image in images:
        image_path = os.path.join(IMAGE_FOLDER, image)
        extracted_text = perform_ocr(image_path)
        extracted_data.append({"image": image, "extracted_text": extracted_text})

    return JSONResponse(content={"data": extracted_data})

