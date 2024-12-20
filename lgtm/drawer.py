# a script to have the message included in the image and produce the output image.
import os
from PIL import Image, ImageDraw, ImageFont


# ratio that the mesage is displayed compared to the whole image size
MAX_RATIO = 0.8 

# Constants for fonts
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24
FONT_NAME = os.path.abspath('C:\Windows\Fonts\Arial.ttf')
FONT_COLOR_WHITE = (255, 255, 255, 0)

# constants for output
OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'


def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)

    # calculate the size of the field for the messge
    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    # Get the proper font size by decrementing by 1
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)

        text_width, text_height = draw.textsize(message, font=font)
        w = message_area_width - text_width
        h = message_area_height - text_height

        if w > 0 and h > 0:
            position = ((image_width - text_width) / 2,
                        (image_height - text_height) / 2)
            draw.text(position, message, fill=FONT_COLOR_WHITE, font=font)
            break
    
    # save the image
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)