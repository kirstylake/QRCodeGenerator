import qrcode

# Function to generate QR code from URL
def generate_qr_code(url, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of the box where the QR code will be drawn
        border=4,  # Thickness of the border
    )

    # Add data (URL)
    qr.add_data(url)
    qr.make(fit=True)

    # Create image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Example usage
url = 'www.linkedin.com/in/kirsten-lake'
file_name = 'kirstenLinkedInQR.png'
generate_qr_code(url, file_name)
