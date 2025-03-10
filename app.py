import streamlit as st
import requests
import pandas as pd

# API Endpoint
TEXT_API_URL = "http://127.0.0.1:8000/get_extracted_text"

def fetch_extracted_text():
    """Fetch extracted text from FastAPI backend."""
    response = requests.get(TEXT_API_URL)
    if response.status_code == 200:
        return response.json()  # Returns {'data': [{image, extracted_text}, {...}]}
    else:
        st.error("❌ Failed to fetch extracted text from API")
        return None

def main():
    st.set_page_config(page_title="OCR Image Processor", page_icon="🖼️", layout="wide")
    st.title("🖼️ OCR Image Processor")
    st.markdown("---")

    if st.button("📤 Extract Text from All Images"):
        extracted_data = fetch_extracted_text()
        
        if extracted_data and "data" in extracted_data:
            table_data = []
            
            for item in extracted_data["data"]:
                image_name = item["image"]
                extracted_text = ", ".join(item["extracted_text"])  # Convert list to string
                
                # Append data for the table
                table_data.append({"Image Name": image_name, "Extracted Text": extracted_text})

            # Convert to DataFrame and add a numbered index starting from 1
            df = pd.DataFrame(table_data)
            df.index = df.index + 1  # Start numbering from 1
            df.index.name = "No."  # Rename the index column to "No."
            
            # Display Table
            st.subheader("📄 Extracted Text from All Images")
            st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    main()
