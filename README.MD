# QR Code Generator

## Step 1: Install Python and VSCode Extensions

### Python Installation

Ensure you have Python installed. You can download it from here.

### Install Python Extension for VSCode

Open VSCode and install the "Python" extension from the Extensions Marketplace.

## Step 2: Set Up a Python Environment in VSCode

### Create a Project Folder

In VSCode, open a folder where you want to save your QR code generator script (e.g., qr_code_project).
Create a Python File:

Inside the folder, create a new file, for example, generate_qr_code.py.

## Step 3: Install qrcode and Dependencies

### Install the Required Libraries

Open a terminal in VSCode (Ctrl + or Terminal > New Terminal) and run the following command to install the qrcode library:
pip install qrcode[pil]

### Install Pillow if Necessary

The qrcode[pil] package installs the necessary Pillow library for handling images. But if you face any issues, you can manually install Pillow:
pip install Pillow
