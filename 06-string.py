# Multiline and Formatting Strings
name = "Doe"
message = """
Hello {},
This is a multiline pattern of 
commenting in Python that many
other programming language lacks
"""
print(message.format(name))  # style 1


message = f"""
Hello {name},
This is a multiline pattern of 
commenting in Python that many
other programming language lacks.
age {3+7}
"""
print(message.format(name))  # style 2

