#!/usr/bin/env python
# coding: utf-8

# In[5]:


                                                            #RANDOM PASSWORD GENERATOR
import random
import string

try:
    length = int(input("Enter password length (minimum 4): "))

    if length < 4:
        print("Password length must be at least 4")
    else:
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice("@#$%&*!")
        ]

        all_chars = string.ascii_letters + string.digits + "@#$%&*!"

        for i in range(length - 4):
            password.append(random.choice(all_chars))

        random.shuffle(password)

        final_password = "".join(password)

        print("Generated Password:", final_password)

except ValueError:
    print("Please enter numbers only.")


# In[ ]:





# In[ ]:




