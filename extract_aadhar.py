import easyocr
import re

def extract_aadhar_number(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    def extract_numeric_sequences(text):
        return re.findall(r'\d+', text)

    aadhar_numbers = []

    for detection in result:
        text = detection[1]
        numeric_sequences = extract_numeric_sequences(text)
        aadhar_numbers.extend(numeric_sequences)

    aadhar_numbers = list(set(aadhar_numbers))  # Remove duplicates
    
    return aadhar_numbers
