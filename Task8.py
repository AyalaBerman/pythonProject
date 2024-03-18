import os
import re

class SmartArray:
    def __init__(self, users):
        self._array = users
    def get_array(self):
        return self._array[round(len(self._array) * 0.1):]
    #4
    def get_even_users(self):
        return [user for i, user in enumerate(self._array) if i % 2 == 0]

class Task8:
    def __init__(self):
        print("Task 8 constructor")


    #1
    def read_or_create_file(self, file_path, default_content=''):
        if not os.path.isfile(file_path):
            with open(file_path,'w') as file:
                file.write(default_content)
                print(file_path + " was created successfuly")

        with open(file_path, 'r') as file:
            return file.read()


    #2

    def read_users_to_generator(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()


    #3
    def read_users_to_array(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    #5
    def check_email_correct(self, file_path):
        EMAIL_REGEX = re.compile(r"""^[^@]+@[^@]+\.[^@]+$""")
        with open(file_path, 'r') as file:
            email_addresses = file.readlines()
            for email_address in email_addresses:
                if re.match(EMAIL_REGEX, email_address):
                    print(email_address + "is correct")
                else:
                    print(email_address + "is not correct")


    #6
    def get_gmail_emails(self, file_path):
        gmail_addressess = []
        GMAIL_REGEX = re.compile(r"""^[a-zA-Z0-9_.+-]{1,64}@gmail\.com$""")
        with open(file_path, 'r')as file:
            email_addresses = file.readlines()
            for email_address in email_addresses:
                if re.match(GMAIL_REGEX, email_address):
                    gmail_addressess.append(email_address)
        return gmail_addressess

    #7
    def check_username_in_email(self, emails_file, users):
        with open(emails_file, 'r') as e_file, open(users, 'r') as u_file:
            emails = e_file.readlines()
            users = u_file.readlines()
            for email, user in zip(emails, users):
                email = email.strip()
                user = user.strip()
                if user in email:
                    print(f"The email {email} contains the username {user}")
                else:
                    print(f"The email {email} does not contain the username {user}")


    #8
    def is_exist_name_count_a(self, path_name, name):
        count_A = 0
        ascii_str = ""
        for char in name:
            ascii_value = ord(char)
            ascii_str += str(ascii_value) + " "
            if char == 'A':
                count_A += 1
        print(f"the count of A is:{count_A}")
        ascii_values = ascii_str.split()
        string = ''.join([chr(int(ascii_value)) for ascii_value in ascii_values])
        with open(path_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                clean_line = line.strip()
                if name == clean_line:
                    return True
        return False

    #9
    def upper_letter(self, file_path):
        names = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name = line.strip()
                names.append(name)
                if not name[0].isupper():
                    print(f"Warning: Name '{name}' does not start with an uppercase letter!")
        return names

    #10

    def calculate_total_sum(self, members):

        total_sum = 0
        for member in members:
            groups = member // 8
            rest = member % 8
            sum_group = groups * 200
            sum_rest = rest * 50
            sum = sum_rest + sum_group
            total_sum = total_sum + sum

        return total_sum









