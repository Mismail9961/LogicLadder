# Import required libraries
import qrcode               # Used to generate QR codes
from PIL import Image       # Used to handle image processing (optional in this case)
import os                   # Used to interact with the file system (like creating folders)

# This function generates and saves a QR code image
def generate_qr(data, filename="qr_code.png", fill_color="black", back_color="white"):
    # Create a QRCode object with basic settings
    qr = qrcode.QRCode(
        version=1,  # Controls how much data the QR can hold (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (more reliable scanning)
        box_size=10,  # Size of each box/pixel in the QR code
        border=4      # Border size around the QR code
    )

    qr.add_data(data)    # Add the actual data (text or URL) to the QR code
    qr.make(fit=True)    # Automatically adjust size to fit the data

    # Generate the QR code image with custom colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the QR code image to the specified file
    img.save(filename)
    print(f"✅ QR code saved as {filename}")

# This function asks the user for custom colors
def get_colors():
    fill = input("Enter QR color (e.g. black, blue, red): ").strip()
    back = input("Enter background color (e.g. white, yellow): ").strip()
    return fill, back

# Main function that runs the program
def main():
    print("🔳 Welcome to the QR Code Generator!")

    # Ask user if they want to generate one QR code or multiple
    mode = input("Do you want to generate one QR? (one): ").strip().lower()

    # Ask if the user wants to customize the QR colors
    use_colors = input("Do you want to customize the QR code colors? (yes/no): ").strip().lower()
    
    # Set default colors
    fill_color, back_color = ("black", "white")

    # If user wants to customize colors, ask for them
    if use_colors == "yes":
        fill_color, back_color = get_colors()

    # If the user wants to generate only one QR code
    if mode == "one":
        data = input("Enter the text or URL you want to encode: ")
        filename = input("Enter filename to save (e.g. my_qr.png): ").strip()
        generate_qr(data, filename, fill_color, back_color)

    else:
        # Invalid option
        print("❌ Invalid mode. Please restart the program and choose 'one'.")

# Entry point of the script
if __name__ == "__main__":
    main()
