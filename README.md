# Password Strength Checker

A simple Python CLI tool to evaluate and score the strength of a password based on configurable criteria: length, uppercase letters, lowercase letters, digits, and special characters. It also provides actionable feedback for users to improve weak passwords.

## Features

- **Length Check**: Minimum of 8 characters; bonus points for passwords longer than 12 characters.
- **Uppercase Letters**: Detects presence of at least one uppercase letter.
- **Lowercase Letters**: Detects presence of at least one lowercase letter.
- **Digits**: Detects presence of at least one numeric digit.
- **Special Characters**: Detects presence of at least one symbol (e.g., `!@#$%^&*`).
- **Scoring System**: Total score out of 6; categorized as Weak, Moderate, or Strong.
- **User Feedback**: Suggests improvements for missing criteria.
- **Menu Interface**: Easy-to-use CLI menu for checking passwords and exiting the tool.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

## Usage

1. Ensure you have the script in your working directory:
   ```bash
   ls
   # password_strength.py
   ```
2. Run the script:
   ```bash
   python3 password_strength.py
   ```
3. Follow the on-screen menu:
   - Enter `1` to check a password.
   - Enter `2` to exit.
4. When prompted, type the password you wish to evaluate.
5. See the strength rating and feedback:
   ```text
   Password Strength: Moderate (Score: 3/6)
   Feedback:
    - Include special characters (e.g., !@#$%^&*).
    - Consider using more than 12 characters for better security.
   ```

## Example

```bash
$ python3 password_strength.py

=== Password Strength Checker ===
1. Check a password
2. Exit
Enter your choice (1-2): 1
Enter the password to check: MyP@ss123

Password Strength: Moderate (Score: 4/6)
Feedback:
 - Consider using more than 12 characters for better security.
```

## Customization

- **Scoring weights**: Modify `calculate_strength()` to adjust how points are awarded.
- **Minimum length**: Change the length thresholds in the function.
- **Additional checks**: Integrate dictionary checks or pattern blacklists.


_Developed with security and simplicity in mind._

