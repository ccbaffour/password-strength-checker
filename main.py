"""
Password strength checker and password generator
"""

#!/bin/python3

# Import necessary libraries
import argparse

from rich import print

from checker import (  # Importing functions from checker module
    generate_password,
    password_checker,
)


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(
        description="This is a program that checks the strength of passwords or generates random passwords."
    )

    # Add command-line arguments
    parser.add_argument(
        "--generate",
        nargs="?",
        type=int,
        const=12,
        metavar="length",
        help="Generate a random password (default length: 12)",
    )
    parser.add_argument(
        "--passwd",
        nargs="?",
        type=str,
        metavar="string",
        help="Check password string strength or prompt for input if no string is provided",
    )

    args = parser.parse_args()

    if args.generate:
        # Generate a random password with specified length or default length 12
        try:
            generated_password, generated_entropy_classification = generate_password(
                length=args.generate
            )
            print("Generated Password:", generated_password)
            print(
                "Generated Password Entropy Classification:",
                generated_entropy_classification,
            )

        except Exception as e:
            print(f"[red]Error generating strength: {e}[/red]")

    elif args.passwd:
        # Check password input strength
        try:
            password_checker(passwd=args.passwd)

        except Exception as e:
            print(f"[red]Error checking password strength: {e}[/red]")

    else:
        # Prompt user to input a password and check its strength
        try:
            password_checker()
        except Exception as e:
            print(f"[red]Error checking password strength: {e}[/red]")


if __name__ == "__main__":
    main()  # Execute main function if script is run directly
