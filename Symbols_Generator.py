from PIL import Image, ImageDraw, ImageFont, ImageChops

# Main function
def main():
    # Image settings
    image_width, image_height = 8, 8
    font = ImageFont.load_default()

    # Letters list
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for letterB in letters:
        for letterR in letters:
            for b_suffix in [False, True]:
                for r_suffix in [False, True]:
                    img = image_gen(image_width, image_height, letterB, letterR, font, b_suffix, r_suffix)
                    img.save(fr"C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\Symbols Images\combined_letters{letterB}{letterR}{b_suffix}{r_suffix}.png")

def image_gen(image_width, image_height, letterB, letterR, font, PB = False, PR = False):
    '''
    Create a two new images with the right size and a white background.
    The first image will be where the letters are drawn on while the
    second image will be the final image where the merged images be
    printed on. 
    '''
    img1 = Image.new('RGB', (image_width, image_height), color = (255, 255, 255))
    img2 = Image.new('RGB', (image_width, image_height), color = (255, 255, 255))
    draw1 = ImageDraw.Draw(img1)
    draw2 = ImageDraw.Draw(img2)

    # Calculate the size of the text
    text_width, text_height = draw1.textsize(letterB, font=font)

    # Calculate the position to draw the text
    center_x = image_width // 2
    center_y = image_height // 2
    text_x = center_x - text_width // 2
    text_y = center_y - text_height // 2

    # Draw the text at the calculated position
    draw1.text((text_x, text_y), letterB, fill=(0, 0, 255), font=font)

    # Rotate the first image
    img1 = img1.rotate(90, expand=1)

    # Add second layer of text in red
    draw2.text((text_x, text_y), letterR, fill=(255, 0, 0), font=font)

    # Merge the two images
    img = ImageChops.add(img1, img2)

    # Create a draw object for the merged image
    draw = ImageDraw.Draw(img)

    match (PB, PR):
        case (True, True):
            draw.text((image_width-2, center_y), '.', fill=(0, 0, 0), font=font)
            draw.text((center_x, image_height-2), '.', fill=(0, 0, 0), font=font)
            return img
        case (True, False):
            draw.text((image_width-2, center_y), '.', fill=(0, 0, 0), font=font)
            return img
        case (False, True):
            draw.text((center_x, image_height-2), '.', fill=(0, 0, 0), font=font)
            return img
        case _:
            return img

if __name__ == "__main__":
    main()
