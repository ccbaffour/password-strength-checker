#!/bin/python3

# Import necessary libraries
import argparse
from rich import print
from checker import password_checker, generate_password     # Importing functions from checker module

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='This is a program that checks the strength of passwords or generates random passwords.')

    # Add command-line arguments 
    parser.add_argument('--generate', action='store_true', help='Generate a random password')
    parser.add_argument('--length', nargs='?', type=int, default=12, help='Length of the generated password (default: 12)')

    # Parse command-line arguments
    args = parser.parse_args()

    if args.generate:
        # Generate a random password with specified length
        generated_password, generated_entropy_classification = generate_password(length=args.length)
        print("Generated Password:", generated_password)
        print("Generated Password Entropy Classification:", generated_entropy_classification)
    
    else:
        # Prompt user to input a password and check its strength
        password_checker()

if __name__ == "__main__":
    main()  # Execute main function if script is run directly