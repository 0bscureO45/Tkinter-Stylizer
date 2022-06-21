import prerequisites as pre
from PIL import Image, ImageDraw, ImageFont
from os import path, getcwd
from pathlib import Path


def rounded_rectangle(width, height, resolution=5,
                   text="Stylized Button", font_prop={}, opacity=1.0,
                   radius=0, fill_color=None, border_color='darkgreen',
                   border_width=1, image_name=None):
    """A function that generates a rounded or unrounded rectangular image with centered text using pillow.

    Args:
        width (int): the width of the image/rectangle
        height (int): the height of the image/rectangle
        resolution (int, optional): the upscaling factor or resolution. Defaults to 5.
        text (str, optional): the text in the center of the rectangle. Defaults to "Stylized Button".
        font_prop (stylized_font(custom_class), optional): the font and its properties. Defaults to stylized_font().
        radius (int, optional): the corner radius of the rectangle. Defaults to 0.
        fill_color (str, optional): the inside color of the image. Default is same as border_color.
        border_color (str, optional): the color of the border. Defaults to 'darkgreen'.
        border_width (int, optional): the width of the border. Defaults to 1.
        image_name (str, optional): the name of the image. Default is a string of random 5 digits number.
    Returns:
        str: the path to the created image.
    """
    if font_prop == {}:
        font_prop = {
            "name": "comicz.ttf",
            "size": 20,
            "color": "darkgreen",
            "style": "italic"
        }
        font_prop["id"] = str(font_prop["name"]) + str(font_prop["size"]) + str(font_prop["color"]) + str(font_prop["style"])
    if fill_color is None:
        fill_color = border_color
    if opacity > 1.0:
        opacity = 1.0
    elif opacity < 0.0:
        opacity = 0.0
    if image_name is None:
        # creating a unique id for the image to avoid multiple images of same properties
        id_initial = f'{width}{height}{resolution}{text}{font_prop["id"]}{radius}{border_color}{border_width}{fill_color}'
        image_name = id_initial
        

    if radius > (height / 2):
        radius = height / 2
    image = Image.new(mode="RGBA",
                      color=(255, 255, 255, 0),
                      size=(width * resolution, height * resolution))
    font = ImageFont.truetype(font_prop["name"],
                              font_prop["size"] * resolution)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle(xy=(0, 0, width * resolution, height * resolution),
                           fill=fill_color,
                           outline=border_color,
                           width=border_width * resolution,
                           radius=radius * resolution)
    draw.text(xy=(image.size[0] / 2, image.size[1] / 2), text=text,
              font=font, fill=pre.color_convert((font_prop["color"]), "hex"), anchor='mm')
    # Antialising
    image.thumbnail(size=(width * resolution, height * resolution),
                    resample=Image.LANCZOS)
    image.thumbnail(size=(width, height), resample=Image.LANCZOS)
    # returning image
    return image