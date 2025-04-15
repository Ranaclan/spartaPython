str_with_extra_spaces = " extra spaces at the start and end "

# Write comment to explain what this does

print(len(str_with_extra_spaces)) #prints length of string

# Write comment to explain what this does

print(len(str_with_extra_spaces.strip())) #prints length of string with leading and trailing spaces removed



example_text = "here's some text with some words of text"

print(example_text.count("text"))
print(example_text.lower())
print(example_text.upper())
print(example_text.capitalize())
print(example_text.replace("with", ","))
# replace the word 'with' in example_text with a comma (,) instead & print it to the screen