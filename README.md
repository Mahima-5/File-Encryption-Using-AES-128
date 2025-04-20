# File Encryption System

A simple and secure file encryption tool that utilizes Fernet symmetric encryption to protect your sensitive data.

## Overview

This application provides a user-friendly interface for encrypting and decrypting files using the Fernet encryption specification, which is built on AES in CBC mode with PKCS7 padding and HMAC using SHA256 for authentication. It ensures that your confidential files remain secure and accessible only with the correct key.

## Features

- **Key Generation**: Generate a secure encryption/decryption key
- **File Encryption**: Encrypt any file type with the generated key
- **File Decryption**: Decrypt previously encrypted files using the same key
- **Strong Security**: Utilizes Fernet encryption, which combines AES-128 with message authentication
- **Simple Interface**: Easy-to-use graphical interface that requires minimal technical knowledge
- **Cross-Platform Compatibility**: Works across different operating systems

## How to Use

### Prerequisites

- Python 3.6 or higher
- Required Python packages:
  - cryptography
  - tkinter (usually comes with Python)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/Mahima-5/File-Encryption-Using-AES-128.git
   ```
2. Navigate to the project directory:
   ```
   cd File-Encryption-Using-AES-128
   ```
3. Install required dependencies:
   ```
   pip install cryptography
   ```

### Running the Application

Execute the Python script:
```
python encryption_app.py
```

### Usage Instructions

1. **Generate a Key**:
   - Click on "Generate Key" to create a new encryption key
   - The key will be saved to a file named "key.key" in the same directory
   - Note: This key is essential for decryption - if lost, encrypted files cannot be recovered

2. **To Encrypt a File**:
   - Click on "Encrypt File"
   - Select the file you want to encrypt from the file dialog
   - The file will be encrypted in place (original content will be replaced with encrypted content)

3. **To Decrypt a File**:
   - Click on "Decrypt File"
   - Select the encrypted file from the file dialog
   - The file will be decrypted in place (encrypted content will be replaced with the original content)

## Security Considerations

- The encryption key is stored in the "key.key" file in the same directory as the application
- Keep this key file secure; if lost, encrypted files cannot be recovered
- For maximum security, consider storing the key file separately from encrypted files
- The application encrypts files in place, meaning the original file is replaced with the encrypted version (no backup is created)

## Technical Details

- **Encryption Library**: cryptography.fernet
- **Encryption Method**: Fernet specification (AES-128 in CBC mode with PKCS7 padding)
- **Authentication**: HMAC using SHA256
- **Interface**: Built with Tkinter for a graphical user experience

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- Thanks to all contributors who have helped improve this project
- The cryptography library developers for providing secure encryption implementations
