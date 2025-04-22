import re

text = "The price is $100"
match = re.search(r"\$\d+", text)
print(match.group())  # $100

# This code uses the re module to search for a pattern in a string. The pattern looks for a dollar sign followed by one or more digits. The match.group() method returns the matched string.

text = "My emails are a@x.com and b@y.com"
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
print(emails)  # ['a@x.com', 'b@y.com']

# This code uses the re module to find all email addresses in a string. The pattern uses a non-word character (\b) to match the start and end of the email address.

text = "My phone number is 123-456-7890"
masked = re.sub(r"\d", "*", text)
print(masked)  # My phone number is ***-***-****

# This code uses the re module to replace all digits in a string with asterisks.

text = "apple, banana; orange"
fruits = re.split(r"[,;]\s*", text)
print(fruits)  # ['apple', 'banana', 'orange']

# This code uses the re module to split a string into a list of substrings based on a comma or semicolon followed by one or more spaces.

