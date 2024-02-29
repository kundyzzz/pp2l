#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
def mp(text):
    p = r'ab*'
    if re.match(p, text):
        return True
    else:
        return False
    
test_strings = ["a", "ab", "abb", "abbb", "ac", "abc", "ba", "bbb"]
for string in test_strings:
    print(f"{string}: {mp(string)}")