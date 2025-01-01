# SCT_CS_2
Skillcraft technology internship in cyber security task 2) Develop a simple image encryption tool using pixel manipulation. Support operations like swapping pixel values or applying a basic mathematical operation to each pixel.
# Image Encryption, Decryption, and Pixel Swapping Tool

This Python script allows you to:
1. **Encrypt** an image using a key.
2. **Decrypt** an encrypted image using the same key.
3. **Swap adjacent pixels** horizontally in an image for a simple scrambling effect.

It uses the **Pillow** library for image processing and manipulates the RGB pixel values for encryption and decryption.

---

## Features
- **Encryption:** Adds the key value to the RGB pixel components and wraps around using modulo 256.
- **Decryption:** Subtracts the key value from the RGB pixel components to retrieve the original image.
- **Pixel Swapping:** Swaps adjacent horizontal pixels for scrambling.

---

## Prerequisites
- Python 3.x
- Pillow library (for image processing)

---

## Steps to Run on Kali Linux

1. **Open the Terminal.**
2. **Install Python (if not already installed):**
   ```bash
   sudo apt update
   sudo apt install python3
3. **Install pip and pillow(if not already installed).**
   ```bash
   pip install Pillow
4. **Run the code/tool**
   ```bash
   python3 SCT_CS_2.py
