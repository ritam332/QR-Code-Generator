import qrcode

def generate_qr_code(data, file_name):
    """
    Generate a QR code and save it as an image file.
    
    Args:
        data (str): The data to encode in the QR code.
        file_name (str): The name of the output image file (e.g., "my_qr_code.png").
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def main():
    print("Welcome to the QR Code Generator!")
    data = input("Enter the data you want to encode: ")
    file_name = input("Enter the output file name (e.g., 'my_qr_code.png'): ")

    generate_qr_code(data, file_name)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    main()
