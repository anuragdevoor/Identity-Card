import os
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import re

# Function to process student information and generate ID card
def generate_id_card(name, photo_path, trade_name, start_date, end_date, location):
    # Convert name to desired format "A Arul Suganthi"
    name_parts = re.findall(r'\w+', name)
    formatted_name = ' '.join([part.capitalize() for part in name_parts])

    # Convert trade name to title case
    formatted_trade_name = trade_name.title()

    # Convert location name to title case
    formatted_location = location.title()

    # Format start date and end date to "DD/MM/YYYY" format
    formatted_start_date = pd.to_datetime(start_date).strftime('%d/%m/%Y')
    formatted_end_date = pd.to_datetime(end_date).strftime('%d/%m/%Y')

    # Load the template image
    template_image = Image.open("D:\\python\\template.jpg")

    # Load the student's photo
    student_photo = Image.open(photo_path)

    # Resize the photo to fit the desired size on the ID card template
    resized_photo = student_photo.resize((390, 395))

    # Overlay the photo and information on the template image
    x, y, w, h = 1930, 90, 390, 395
    template_image.paste(resized_photo, (x, y))

    # Set the font parameters
    font_path = r"D:\python\slavefont.ttf"
    goudy_bold_font_path = r"D:\python\GOUDOSB.ttf"
    goudy_regular_font_path = r"D:\python\GOUDOS.ttf"
    font_size = 80
    small_font_size = 57
    font_color = (0, 0, 0)
    font = ImageFont.truetype(font_path, font_size)
    goudy_bold_font = ImageFont.truetype(goudy_bold_font_path, font_size)
    goudy_regular_font = ImageFont.truetype(goudy_regular_font_path, small_font_size)

    # Set the starting position of the name text
    text_x = 1020
    text_y = y + h + 160

    # Create a PIL draw object
    draw = ImageDraw.Draw(template_image)

    # Calculate the size of the name text using textbbox
    text_bbox = draw.textbbox((0, 0), formatted_name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate the text position
    text_org = (text_x, text_y)

    # Draw the name field with the custom font
    draw.text(text_org, formatted_name, font=font, fill=font_color)

    # Draw additional fields (trade_name, start_date, end_date, location)
    field_y = text_y + text_height + 50
    draw.text((1370, 780), formatted_trade_name, font=goudy_bold_font, fill=font_color)

    field_y += text_height + 50
    draw.text((1028, 1100), formatted_start_date, font=goudy_regular_font, fill=font_color)

    field_y += text_height + 50
    draw.text((1400, 1100), formatted_end_date, font=goudy_regular_font, fill=font_color)

    field_y += text_height + 50
    draw.text((1255, 1235), formatted_location, font=goudy_bold_font, fill=font_color)

    # Create the output directory if it doesn't exist
    os.makedirs("D:\\python\\output", exist_ok=True)

    # Save the ID card image with a unique filename in the output directory
    output_filename = os.path.join("D:\\python\\output", f"{formatted_name}_id_card.jpg")
    template_image.save(output_filename)

    # Display a success message
    print(f"ID card generated for {formatted_name}")

# Specify the range of rows to generate ID card images from (modify as needed)
start_row = 1
end_row = 2

# Load the Excel sheet and retrieve student information within the specified range
excel_data = pd.read_excel("D:\python\FVTRS_Trainees Certificates.xlsx", skiprows=range(1, start_row), nrows=end_row-start_row)

for index, row in excel_data.iterrows():
    name = row["Name"]
    photo_path = row["Passport Size Photo"]
    trade_name = row["Trade Name"]
    start_date = str(row["Starting Date "].date())
    end_date = str(row["Ending Date "].date())
    location = row["Coordinate Location name "]
    # Process the student information and generate ID card
    generate_id_card(name, photo_path, trade_name, start_date, end_date, location)
