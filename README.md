# Password Checker and Generator

This is a Python script that allows you to check the strength of passwords and generate random strong passwords.

## Features

- **Password Strength Checking**: Check the strength of passwords based on various criteria such as length, character types, and entropy.
- **Password Strength Feedback**: Provides feedback to users on how to improve their password strength, including specific suggestions on what elements to add or change.
- **Random Password Generation**: Generate strong random passwords of specified lengths.
- **Rich Text Output**: Utilizes the `rich` library for enhanced text output.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ccbaffour/password-strength-checker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd password-strength-checker
    ```

3. Install dependencies:
   
    Directory is a python virtual environment. So would not require any other dependencies but If files are moved to a different directory, make sure to install the following dependencies:
    
    ```bash
    pip install rich numpy scipy
    ```

## Usage

Run the script `main.py` with Python:

```bash
python main.py [--generate length] [--passwd "string"]
```

## Example

### Check the strength of a password:

```bash
python main.py
```
### Generate random password of default length 12:

```bash
python main.py --generate
```
### Generate random password of length 16:

```bash
python main.py --generate 16
```
### Check password strength

```bash
python main.py --passwd "string"
```
Or without string to enter password through prompt
```bash
python main.py --passwd
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Author
[Collins Charles Baffour](https://github.com/ccbaffour)
