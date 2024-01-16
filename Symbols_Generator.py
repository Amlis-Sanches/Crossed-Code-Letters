from PIL import Image, ImageDraw, ImageFont, ImageChops

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
