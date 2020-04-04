import random

string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%)(^&*?1234567890'
pw_length = 8

pw = ''.join(random.sample(string, pw_length))

print(pw)
