import tkinter as tk
from tkinter import filedialog
from extract_aadhar import extract_aadhar_number

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        aadhar_number = extract_aadhar_number(file_path)
        result_label.config(text=f"Extracted Aadhar Number: {aadhar_number}")
    else:
        result_label.config(text="No file selected")

root = tk.Tk()
root.title("Aadhar Number Extractor")

upload_button = tk.Button(root, text="Upload Aadhar Image", command=upload_image)
upload_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

root.mainloop()
