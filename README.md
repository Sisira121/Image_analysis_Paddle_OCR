# OCR Image Processor

## 📌 Overview
OCR Image Processor is a **Streamlit-based web application** designed to interact with a **FastAPI backend** for extracting text from images using Optical Character Recognition (OCR). The app fetches extracted text from images processed by the backend and presents it in a structured tabular format.

## 🚀 Features
- **Seamless Integration**: Connects with a FastAPI backend for text extraction.
- **Interactive UI**: Built with Streamlit for an intuitive and responsive user experience.
- **Tabular Data Display**: Extracted text is displayed in a structured format with indexed numbering.
- **Error Handling**: Alerts the user in case of API failures.

## 🏗️ Tech Stack
- **Frontend**: Streamlit (Python)
- **Backend API**: FastAPI (for OCR processing)
- **Data Processing**: Pandas
- **HTTP Requests**: Requests Library

## 📦 Installation & Setup
### 1️⃣ Prerequisites
Ensure you have **Python 3.7+** installed.

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ocr-image-processor.git
cd ocr-image-processor
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
Ensure the FastAPI backend is running before starting the Streamlit app.

Start the Streamlit UI:
```bash
streamlit run app.py
```

## 📜 Usage
1. Click **"Extract Text from All Images"** to fetch text from the backend API.
2. View extracted text in a structured table format.
3. If the API request fails, an error message will be displayed.

## 🔄 API Integration
The application interacts with a FastAPI backend via the following API endpoint:
- **GET** `/get_extracted_text`: Retrieves extracted text from processed images.

## 🛠️ Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## 📄 License
This project is licensed under the **MIT License**.

---
_Developed with ❤️ using Streamlit & FastAPI._

