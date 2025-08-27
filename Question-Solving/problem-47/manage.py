import re

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

# Example usage
sample = "Hello, world! How's everything going?"
print(remove_punctuation(sample))
# Output: Hello world Hows everything going
