# -UPI-Payment-QR-Code-Generator
This Python project generates UPI payment QR codes for PhonePe, Paytm, and Google Pay. Just enter your UPI ID, and the script creates and saves QR codes for easy payment collection. Ideal for personal or small business use.

# UPI Payment QR Code Generator

This is a Python project that generates QR codes for accepting UPI payments via PhonePe, Paytm, and Google Pay.

## Features

- Enter your UPI ID once
- Automatically generate QR codes for:
  - PhonePe
  - Paytm
  - Google Pay
- Save and display the QR code images

## Requirements

- Python 3
- Libraries:
  - `qrcode`
  - `Pillow` (used internally by `qrcode` to display images)

## How to Use

1. Clone or download the repository.
2. Install required packages using:

```bash
pip install qrcode pillow
