# check_for_password_leaks
Securely check if passwords have been leaked online, You can manually enter passwords, or check a CSV file of passwords, which you could export from a password manager.



Clone:

    git clone git@github.com:lukestanley/check_for_password_leaks.git

    cd check_for_password_leaks


Install requests_cache with pip:
    

    pip install requests_cache

    python check_for_password_leaks.py


Or pipenv, if that suits you sir! 

    pipenv install

    pipenv shell


To manually enter a password to your shell and securely check it for leaks online:

    python check_for_password_leaks.py type


To check a passwords.csv file:

    python check_for_password_leaks.py type


