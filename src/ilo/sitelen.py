import io
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont


# by jan Tepo
def display(text: str, font_path: str, font_size: int, color: Tuple[int, int, int]):
    STROKE_WIDTH = round((font_size / 133) * 5)
    LINE_SPACING = round((font_size / 11) * 2)

    font = ImageFont.truetype(font_path, font_size)
    d = ImageDraw.Draw(Image.new("RGBA", (0, 0), (0, 0, 0, 0)))
    x, y, w, h = d.multiline_textbbox(
        (0, 0), text, stroke_width=STROKE_WIDTH, font=font
    )
    image = Image.new(
        "RGBA",
        (x + w + STROKE_WIDTH * 2, y + h + STROKE_WIDTH * 2 + LINE_SPACING),
        (0, 0, 0, 0),
    )
    d = ImageDraw.Draw(image)
    d.multiline_text(
        (STROKE_WIDTH, STROKE_WIDTH),
        text,
        font=font,
        fill=color,
        spacing=LINE_SPACING,
        stroke_width=STROKE_WIDTH,
        stroke_fill=(0x36, 0x39, 0x3F),
    )
    img_out = io.BytesIO()
    image.save(img_out, format="PNG")
    return img_out.getvalue()
