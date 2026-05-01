import re

text = "Hello, my number is 12345 and my email is alice@example.com"

print("--- REGEX DEMONSTRATION ---")

search_result = re.search(r"\d+", text)
print("First number found using search():", search_result.group() if search_result else "Not found")

all_numbers = re.findall(r"\d+", text)
print("All numbers using findall():", all_numbers)

match_result = re.match(r"Hello", text)
print("Match at beginning using match():", "Matched" if match_result else "Not matched")

replaced_text = re.sub(r"\d+", "XXXXX", text)
print("Text after substitution:", replaced_text)

split_text = re.split(r"\s", text)
print("Text after split:", split_text)

email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)
print("Extracted email:", email)
