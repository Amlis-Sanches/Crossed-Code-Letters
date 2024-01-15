from PIL import Image, ImageDraw, ImageFont

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
    image_width = 400
    image_height = 400
    background_color = "white"

    # Create a blank image
    image = create_blank_image(image_width, image_height, background_color)

    # Letters to combine
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Font size for default font
    font_size = 36

    # Colors for the letters
    colors = ["blue", "red"]

    # Initialize color index
    color_index = 0

    # Loop through pairs of letters and add them to the image with alternating colors
    for i in range(0, len(letters), 2):
        for j in range(0, len(letters), 2):
            letter_pair = letters[i:j]
            text_color = colors[color_index % 2]
            image = add_bold_rotated_letter(image, letter_pair, font_size, text_color)
            color_index += 1

    # Save the generated image
    image.save("combined_letters.png")

if __name__ == "__main__":
    main()
