import argparse
from PIL import Image, ImageFilter

def apply_filter(image_path, filter_name):
    image = Image.open(image_path)
    if filter_name == 'blur':
        filtered_image = image.filter(ImageFilter.BLUR)
    elif filter_name == 'contour':
        filtered_image = image.filter(ImageFilter.CONTOUR)
    elif filter_name == 'detail':
        filtered_image = image.filter(ImageFilter.DETAIL)
    elif filter_name == 'edge_enhance':
        filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_name == 'emboss':
        filtered_image = image.filter(ImageFilter.EMBOSS)
    elif filter_name == 'find_edges':
        filtered_image = image.filter(ImageFilter.FIND_EDGES)
    elif filter_name == 'sharpen':
        filtered_image = image.filter(ImageFilter.SHARPEN)
    else:
        filtered_image


