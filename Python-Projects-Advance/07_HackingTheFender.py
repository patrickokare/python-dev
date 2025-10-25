# ## Project VII: **Hacking The Fender** 🔐

# `The Fender`, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold:

# - Gain access to `The Fender`'s systems
# - Update the `"passwords.csv"` file to scramble the secret data
# - Plant the signature of `Slash Null`, a rival hacker whose activities could be halted if `The Fender` perceives them as a threat

# Use your Python file handling skills to retrieve, manipulate, obscure, and create data in this cybersecurity mission. You'll work with CSV files and other text files to demonstrate the power of Python's file programming capabilities.

# ### Project Overview

# In this project, you will:

# - Read and parse CSV data containing compromised credentials
# - Create a comprehensive list of affected users
# - Generate notification files in multiple formats (TXT, JSON)
# - Replace the original password file with a decoy


import csv

compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)

  for password_row in password_csv:
  
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  fields =['compromised_users']

  output_writer = csv.DictWriter(compromised_user_file, fieldnames=fields)
  

  for compromised_user in compromised_users:
     output_writer.writerow({'compromised_users':compromised_user})

    compromised_user_file.write(compromised_user + '\n')


import json

with open('boss_message.json', 'w') as boss_message:

  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

slash_null_sig = """ 
_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
 """

with open("new_passwords.txt", 'w') as new_passwords_obj:
  new_passwords_obj.write(slash_null_sig)








