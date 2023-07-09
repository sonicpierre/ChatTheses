"""
The objective is to extract the text from a pdf correctly
"""

from PyPDF2 import PdfReader

def get_text(pdf_path:str, page:int)->None:

    reader = PdfReader(pdf_path)
    page = reader.pages[page]
    parts = []

    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if y > 50 and y < 720:
            parts.append(text)

    page.extract_text(visitor_text=visitor_body)
    text_body = "".join(parts)

    return text_body


def get_images(pdf_path:str, page:int)->None:

    reader = PdfReader(pdf_path)
    page = reader.pages[page]

    count = 0
    for image_file_object in page.images:
        with open(str(count) + image_file_object.name, "wb") as fp:
            fp.write(image_file_object.data)
            count += 1