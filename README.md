# check_for_password_leaks
Securely check if passwords have been leaked online, You can manually enter passwords, or check a CSV file of passwords, which you could export from a password manager.



Clone:

    git clone git@github.com:lukestanley/check_for_password_leaks.git

    cd check_for_password_leaks


Requires Python 3.8+. Install dependencies with [Astral uv](https://docs.astral.sh/uv/), a fast Python package manager:
    
    uv sync


To manually enter a password to your shell and securely check it for leaks online:

    uv run python check_for_password_leaks.py type


To check a passwords.csv file:

    uv run python check_for_password_leaks.py
