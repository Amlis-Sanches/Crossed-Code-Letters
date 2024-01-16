from PIL import Image, ImageDraw, ImageFont, ImageChops

# Function to create a blank image with a specified size and background color
def create_blank_image(width, height, background_color):
    return Image.new("RGB", (width, height), background_color)

# Function to add a bold, rotated letter to the image with specified text color
def add_bold_rotated_letter(image, letter, font_size, text_color):
    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Load a default bold font (you can change this if needed)
    font = ImageFont.load_default()

    # Measure the size of the letter
    letter_width, letter_height = draw.textsize(letter, font)

    # Calculate the position to center the letter
    x = (image.width - letter_width) / 2
    y = (image.height - letter_height) / 2

    # Draw the rotated letter on the image with the specified text color
    draw.text((x, y), letter, font=font, fill=text_color)

    # Rotate the image by 90 degrees
    image = image.rotate(90, expand=True)

    return image

# Main function
def main():
    # Image settings
    image_width = 8
    image_height = 8
    background_color = "white"
    font = ImageFont.load_default()

    # Letters list
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for letterB in letters:
        for letterR in letters:
        # Create a blank image
            img1 = Image.new('RGB', (image_width, image_height), color = (255, 255, 255)) #for testing
            img2 = Image.new('RGB', (image_width, image_height), color = (255, 255, 255)) #for testing
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

            # Save the image
            img.save(fr"C:\Users\natha\Documents\GitHub\Crossed-Code-Letters\Symbols Images\combined_letters{letterB}{letterR}.png")


if __name__ == "__main__":
    main()
