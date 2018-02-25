"""
Securely check if passwords have been leaked online,
You can manually enter passwords, or check a CSV file of passwords,
which you could export from a password manager.
"""

import csv
import requests
from sys import argv
import requests_cache
from hashlib import sha1
from os import name as os_name
from os import system as run_command


def main():
    if 'type' in str(argv):
        check_manually_entered_passwords()
    else:
        print('Checking passwords.csv')
        tell_me_which_passwords_are_bad(get_passwords_from_csv())


def clear():
    """Clears the console"""
    run_command('cls' if os_name == 'nt' else 'clear')


def sha1_hash(string):
    """Gets a hex digest of a string"""
    return sha1(bytes(string, 'utf8')).hexdigest().lower()


def unique_list(password_list):
    return list(set(password_list))


def get_hash_parts(password):
    """Hashes a password string, returning the first 5 characters of the hash, and the rest"""
    full_hash_string = sha1_hash(password)
    first_five_characters_of_hash = full_hash_string[0:5]
    rest_of_hash = full_hash_string[5:40]
    return first_five_characters_of_hash, rest_of_hash


def password_is_found_in_leaks(password):
    """Searches an API of leaked passwords by sending the first 5 characters of a hash,
    then checks the rest of hash in results locally, so the full password hash is not exposed"""
    api = 'https://api.pwnedpasswords.com/range/'
    first_five_characters_of_hash, rest_of_hash = get_hash_parts(password)
    request = requests.get(api + first_five_characters_of_hash)
    results = request.text.lower()
    return rest_of_hash in results


def get_passwords_from_csv(filename='passwords.csv', column_name='password'):
    """Get unique passwords from a column in a given CSV file"""
    passwords = []
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            passwords.append(str(row[column_name]))
    return passwords


def tell_me_which_passwords_are_bad(passwords):
    for password in unique_list(passwords):
        if password_is_found_in_leaks(password):
            print('CHANGE THE PASSWORD:', password)


def check_manually_entered_passwords():
    password = input('Enter a password to check if it is leaked, or type exit: ')
    if password == 'exit':
        return
    clear()
    if password_is_found_in_leaks(password):
        print('CHANGE THE PASSWORD')
    else:
        print('Password not found in leaks')
    check_manually_entered_passwords()


if __name__ == "__main__":
    requests_cache.install_cache()
    main()
