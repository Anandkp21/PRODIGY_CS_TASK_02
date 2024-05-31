--- 

# Image Encryption and Decryption Tool

A simple command-line tool for encrypting and decrypting images using Python's PIL library. This tool modifies the RGB values of each pixel in the image to achieve encryption and decryption.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)
- [Contributing](#contributing)

## Overview

The Image Encryption and Decryption Tool allows users to encrypt and decrypt images by modifying the RGB values of each pixel. The encryption adds a fixed value to each color component, and the decryption subtracts the same value to retrieve the original image.

## Features

- **Encrypt Image:** Add a fixed value to each color component of every pixel in the image.
- **Decrypt Image:** Subtract the same fixed value to retrieve the original image.
- **User-friendly Interface:** Simple menu-driven command-line interface.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/image-encryption-tool.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd image-encryption-tool
   ```

3. **Install required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

   Alternatively, you can install dependencies individually:
   ```sh
   pip install pillow
   ```

## Usage

1. **Run the image encryption tool:**
   ```sh
   python pixel.py
   ```

2. **Choose an option from the menu:**
   - Enter `1` to upload and encrypt an image.
   - Enter `2` to decrypt an image.
   - Enter `3` to exit the tool.

3. **Follow the prompts:**
   - For encryption, enter the path to the image file you want to encrypt. The encrypted image will be saved as `encrypted_image.png`.
   - For decryption, enter the path to the encrypted image file. The decrypted image will be displayed.

## Example

### Encrypting an Image
```sh
$ python image_encryption_tool.py
Choose an option:
1. Upload and Encrypt an image
2. Decrypt an image
3. Exit
Enter your choice (1/2/3): 1
Enter the path to the image file: path/to/your/image.png
Image encrypted successfully!
Encrypted image saved as: encrypted_image.png
```

### Decrypting an Image
```sh
$ python image_encryption_tool.py
Choose an option:
1. Upload and Encrypt an image
2. Decrypt an image
3. Exit
Enter your choice (1/2/3): 2
Enter the path to the encrypted image file: encrypted_image.png
Image decrypted successfully!
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

