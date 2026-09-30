from PIL import Image, ImageChops
import os

def trim(im):
    # Create a background image of the same color as the top-left pixel
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        # Add some padding
        pad = 20
        bbox = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), 
                min(im.width, bbox[2]+pad), min(im.height, bbox[3]+pad))
        return im.crop(bbox)
    return im

def run():
    figures_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    images = ['ui_01_dashboard.png', 'ui_02_benign.png', 'ui_03_malicious.png']
    
    for img_name in images:
        path = os.path.join(figures_dir, img_name)
        if os.path.exists(path):
            im = Image.open(path)
            # A full page screenshot might have a lot of white background.
            # We can crop the center. The container in bootstrap is usually centered.
            # Alternatively, we just use trim.
            trimmed = trim(im)
            
            # Since the browser is 1920 wide, we can just crop the center 800px if trim doesn't work well.
            # Let's save it.
            trimmed.save(path)
            print(f"Cropped {img_name}")

if __name__ == '__main__':
    run()
