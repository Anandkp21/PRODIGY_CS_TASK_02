from PIL import Image

def encrypt_image(img):
    try:
        # Encrypt the image
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                r = (r + 50) % 256
                g = (g + 50) % 256
                b = (b + 50) % 256
                img.putpixel((x, y), (r, g, b))
        
        encrypted_path = "encrypted_image.png"
        img.save(encrypted_path)
        print("Image encrypted successfully!")
        print("Encrypted image saved as:", encrypted_path)
        return img
    except Exception as e:
        print("Error:", e)

def decrypt_image(img):
    try:
        # Decrypt the image
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                r = (r - 50) % 256
                g = (g - 50) % 256
                b = (b - 50) % 256
                img.putpixel((x, y), (r, g, b))
        
        print("Image decrypted successfully!")
        return img
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("Choose an option:")
        print("1. Upload and Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Get input image file path
            image_path = input("Enter the path to the image file: ")
            # Open the image
            original_img = Image.open(image_path)
            # Encrypt the image
            encrypted_img = encrypt_image(original_img.copy())
            if encrypted_img:
                # Display the encrypted image
                encrypted_img.show()
        
        elif choice == '2':
            # Get input encrypted image file path
            encrypted_path = input("Enter the path to the encrypted image file: ")
            # Open the encrypted image
            encrypted_img = Image.open(encrypted_path)
            # Decrypt the image
            decrypted_img = decrypt_image(encrypted_img.copy())
            if decrypted_img:
                # Display the decrypted image
                decrypted_img.show()
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
