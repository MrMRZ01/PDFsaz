import os
from PIL import Image

imgs = input("Enter name of images folder: ")

file_list = os.listdir(imgs)

image_files = [f for f in file_list if f.lower().endswith((
    '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.tiff', '.heif'
))]

pil_img = [Image.open(os.path.join(imgs, image)).convert('RGB') for image in image_files]

if pil_img:
    output_filename = input("Enter the output PDF file name: ")


    if not output_filename.lower().endswith('.pdf'):
        output_filename += '.pdf'

    pil_img[0].save(output_filename, save_all=True, append_images=pil_img[1:])
    print(f"PDF created successfully as {output_filename}!")
else:
    print("No images found in the specified folder.")