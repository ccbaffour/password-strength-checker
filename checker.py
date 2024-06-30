#!/bin/python3


# Import necessary libraries
import re
import secrets
import string

import numpy as np
from rich import print
from scipy.stats import entropy

# Define entropy thresholds for classification
entropy_thresholds = {
    'low': 2.5,
    'moderate': 3.5,
    'high': 4.5,
}


# Function to classify entropy value into categories
def classify_entropy(entropy_value):
    if entropy_value < entropy_thresholds['low']:
        return "[bold red] Low! [/bold red]"

    elif entropy_thresholds['low'] <= entropy_value < entropy_thresholds['moderate']:
        return "[bold yellow] Moderate! [/bold yellow]"

    else:
        return "[bold green] High! [/bold green]"

# Function to check if password is common
def check_common_password(password):
    try:
        with open('dictionary.txt', 'r') as dict_file:
            for line in dict_file:
                if password.lower() == line.strip():
                    return True

    except FileNotFoundError:
        print("[bold red]Error: dictionary.txt not found.[/bold red]")
        return False

    return False

# Function to calculate entropy of password
def calculate_entropy(password):
    char_counts = np.array([password.count(c) for c in set(password)])
    probabilities = char_counts / len(password)
    entropy_value = entropy(probabilities, base=2)
    return entropy_value


# Function to check Password strength and provide feedback
def strength_check(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
        feedback.append("[bold green] ✔︎ Password length is sufficient. [/bold green]")
    else:
        feedback.append("[bold red] ✖ Password should be at least 12 characters long. [/bold red]")

    if re.search(r'[0-9]+', password):
        score += 1
        feedback.append("[bold green] ✔︎ Password contains numbers. [/bold green]")
    else:
        feedback.append("[bold red] ✖ Password should contain at least one number. [/bold red]")

    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("[bold green] ✔︎ Password contains lowercase letters. [/bold green]")
    else:
        feedback.append("[bold red] ✖ Password should contain at least one lowercase letter. [/bold red]")

    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("[bold green] ✔︎ Password contains uppercase letters. [/bold green]")
    else:
        feedback.append("[bold red] ✖ Password should contain at least one uppercase letter. [/bold red]")

    if re.search(r'[!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]', password):
        score += 1
        feedback.append("[bold green] ✔︎ Password contains special characters. [/bold green]")
    else:
        feedback.append("[bold red] ✖ Password should contain at least one special character.[/bold red]")
    
    entropy_value = calculate_entropy(password)
    entropy_classification = classify_entropy(entropy_value)

    return feedback, score, entropy_classification


# Function to prompt user for password and check its strength
def password_checker(passwd=None):
    if passwd is None:
        passwd = str(input("Please input password: "))

    if check_common_password(passwd):
        print("[bold red] Password is common! [/bold red]")

    else:
        feedback, score, entropy_classification = strength_check(passwd)
        print("Score:", score)
        print("Feedback:")
        for msg in feedback:
            print(msg)
        print("Entropy Classification:", entropy_classification)


# Function to generate a strong random password
def generate_password(length=None):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    generated_entropy_value = calculate_entropy(password)
    generated_entropy_classification = classify_entropy(generated_entropy_value)
    return password, generated_entropy_classification
