from PIL import Image

# Function to encrypt an image
def encrypt_image(image_name, key):
    try:
        img = Image.open(image_name)
        img = img.convert("RGB")
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

        encrypted_name = "encrypted_" + image_name
        img.save(encrypted_name)
        print(f"Image encrypted successfully! Saved as {encrypted_name}")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

# Function to decrypt an image
def decrypt_image(image_name, key):
    try:
        img = Image.open(image_name)
        img = img.convert("RGB")
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

        decrypted_name = "decrypted_" + image_name
        img.save(decrypted_name)
        print(f"Image decrypted successfully! Saved as {decrypted_name}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

# Function to swap pixel values
def swap_pixels(image_name):
    try:
        img = Image.open(image_name)
        img = img.convert("RGB")
        pixels = img.load()

        for i in range(0, img.size[0] - 1, 2):  # Swap every two adjacent pixels horizontally
            for j in range(img.size[1]):
                r1, g1, b1 = pixels[i, j]
                r2, g2, b2 = pixels[i + 1, j]
                pixels[i, j], pixels[i + 1, j] = (r2, g2, b2), (r1, g1, b1)

        swapped_name = "swapped_" + image_name
        img.save(swapped_name)
        print(f"Image pixels swapped successfully! Saved as {swapped_name}")
    except Exception as e:
        print(f"An error occurred during pixel swapping: {e}")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Swap Pixels")
        print("4. Exit")
        choice = input("Select an option (1/2/3/4): ").strip()

        if choice == "4":
            print("Exiting...")
            break

        image_name = input("Enter the image file name (with extension): ").strip()

        if choice == "1":
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(image_name, key)
        elif choice == "2":
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(image_name, key)
        elif choice == "3":
            swap_pixels(image_name)
        else:
            print("Invalid choice! Please select a valid option.")