def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)  # Return a tuple with length 0 and first character as None
    
    length = len(sentence)
    first_char = sentence[0]  # Get the first character of the sentence
    return (length, first_char)

# Example usage:
sentence = "Holberton"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
