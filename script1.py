from PIL import Image
import os

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Encrypt the image
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (b, g, r)  # Swap R and B

    # Save the encrypted image
    base, ext = os.path.splitext(image_path)
    encrypted_image_path = f"{base}_encrypted{ext}"
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}.")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Decrypt the image
    for y in range(height):
        for x in range(width):
            b, g, r = pixels[x, y]  # Reverse the swap
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    base, ext = os.path.splitext(encrypted_image_path)
    decrypted_image_path = f"{base.replace('_encrypted', '_decrypted')}{ext}"
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1':
            image_path = input("Enter the path of the image to encrypt: ").strip()
            encryption_key = 77
            encrypt_image(image_path, encryption_key)

        elif choice == '2':
            encrypted_image_path = input("Enter the path of the image to decrypt: ").strip()
            encryption_key = 77
            decrypt_image(encrypted_image_path, encryption_key)

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
