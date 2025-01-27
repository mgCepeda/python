import pandas as pd
import re

data = [
    [1, 'Winston', 'winston@leetcode.com'],
    [2, 'Jonathan', 'jonathanisgreat'],
    [3, 'Annabelle', 'bella-@leetcode.com'],
    [4, 'Sally', 'sally.come@leetcode.com'],
    [5, 'Marwan', 'quarz#2020@leetcode.com'],
    [6, 'David', 'david69@gmail.com'],
    [7, 'Shapiro', '.shapo@leetcode.com']
]

users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

# Expresión regular para validar correos electrónicos
valid_email_regex = r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$'

# Filtrar usuarios con correos válidos
valid_users = users[users['mail'].apply(lambda x: bool(re.match(valid_email_regex, x)))]
no_valid_users = users[~users['mail'].apply(lambda x: bool(re.match(valid_email_regex, x)))]

# Mostrar validos
print(f"E-mails válidos:\n", valid_users)
print(f"E-mails no válidos:\n", no_valid_users)
