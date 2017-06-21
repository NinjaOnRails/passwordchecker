#! /usr/bin/env python3
# passwordChecker.py - Checks if password is strong.
import re, pyperclip

def passwordCheck(password):
    charRegex = re.compile(r'.{8,}')
    lowerRegex = re.compile(r'[a-z]')
    upperRegex = re.compile(r'[A-Z]')
    digitRegex = re.compile(r'\d')
    if charRegex.search(password) == None:
        print('Password must be at least 8 characters long')
    if lowerRegex.search(password) == None:
        print('Password must contain at least one lowercase letter')
    if upperRegex.search(password) == None:
        print('Password must contain at least one uppercase letter')
    if digitRegex.search(password) == None:
        print('Password must contain at least one digit')
    else:
        print('Password is valid')
        
passwordCheck(str(pyperclip.paste()))
