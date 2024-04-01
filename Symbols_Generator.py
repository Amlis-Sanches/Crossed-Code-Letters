from PIL import Image, ImageDraw, ImageFont, ImageChops
import os
import itertools


# Main function
def main():
    # Image settings
    image_width, image_height = 8, 8
    font = ImageFont.load_default()

    # Letters list to iterate through every letter of the alphabet.
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for letterB in letters:
        for letterR in letters:
            for b_suffix in [False, True]:
                for r_suffix in [False, True]:
                    for b_sentance in [False, True]:
                        for r_sentance in [False, True]:
                            # Define the relative path to the 'Symbols Images' directory
                            img = image_gen(image_width, image_height, letterB, letterR, font, b_suffix, r_suffix, b_sentance, r_sentance)
                            images_dir = os.path.join('Crossed-Code-Letters', 'Symbols Images')

                            # Make sure the directory exists
                            os.makedirs(images_dir, exist_ok=True)

                            # Define the filename
                            filename = f"{letterB}{letterR}-{b_suffix}-{r_suffix}-{b_sentance}-{r_sentance}.png"

                            # Join the directory path and filename
                            filepath = os.path.join(images_dir, filename)

                            # Save the image
                            img.save(filepath)

def image_gen(image_width, image_height, letterB, letterR, font, PB = False, PR = False, SB = False, SR = False):
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


    '''
    This is generating a set of symbols for what you would use at the
    end of a word. If the PB and PR are both False, then it will just
    exit the loop. If PB is True, then it will draw a dot at the end.
    This dot will signify if this is the end of a word for the top
    row or bottom row.
    '''
    draw = ImageDraw.Draw(img)
    dot_radius = 1  # Adjust as needed

    match (PB, PR):
        case (True, True):
            # Draw a dot at (image_width, center_y)
            draw.ellipse([(image_width-dot_radius, center_y-dot_radius), (image_width+dot_radius, center_y+dot_radius)], fill=(0, 0, 0))

            # Draw a dot at (center_x, image_height)
            draw.ellipse([(center_x-dot_radius, image_height-dot_radius), (center_x+dot_radius, image_height+dot_radius)], fill=(0, 0, 0))

        case (True, False):
            # Draw a dot at (image_width, center_y)
            draw.ellipse([(image_width-dot_radius, center_y-dot_radius), (image_width+dot_radius, center_y+dot_radius)], fill=(0, 0, 0))

        case (False, True):
            # Draw a dot at (center_x, image_height)
            draw.ellipse([(center_x-dot_radius, image_height-dot_radius), (center_x+dot_radius, image_height+dot_radius)], fill=(0, 0, 0))

    match (SB, SR):
        case (True, True):
            # Draw a dot at (0, center_y)
            draw.ellipse([(dot_radius-1, center_y-dot_radius), (dot_radius-1, center_y+dot_radius)], fill=(0, 0, 0))

            # Draw a dot at (center_x, 0)
            draw.ellipse([(center_x-dot_radius, dot_radius-1), (center_x+dot_radius, dot_radius-1)], fill=(0, 0, 0))

        case (True, False):
            # Draw a dot at (0, center_y)
            draw.ellipse([(dot_radius-1, center_y-dot_radius), (dot_radius-1, center_y+dot_radius)], fill=(0, 0, 0))

        case (False, True):
            # Draw a dot at (center_x, 0)
            draw.ellipse([(center_x-dot_radius, dot_radius-1), (center_x+dot_radius, dot_radius-1)], fill=(0, 0, 0))
    
    return img


if __name__ == "__main__":
    main()
