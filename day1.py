# ***** Question-1 *****
print('hello world')
# Output: hello world
# Reason: print statement outputs the string


# ***** Question-2 *****
print(55 / 11)
# Output: 5.0
# Reason: single divide sign(/) returns the result in floating point number


# ***** Question-3 *****
print(50 * 2 + (60 - 20) / 4)
# Output: 110.0
# Reason: First the parenthesis are calculated. Then the divide  sign. Then the multiplication sign-->This is operator precedence


# ***** Question-4 *****
q4Text = "# Is this a comment?"
print(q4Text)
# Output: # Is this a comment?
# Reason: # is within the quotes so it is a string

# ***** Question-5 *****
q5Str = 'silent'
print(q5Str[2] + q5Str[1] + q5Str[0]
      + q5Str[5] + q5Str[3] + q5Str[4])
# Output: listen
# Reason: The sequences like string has indexes with which we can access each index's location

# ***** Question-6 *****
q6Squares = [1, 4, 9, 16, 25]
print(q6Squares[0])
# Output: 1
# Reason: Get the value at index 0 which is 1


# ***** Question-7 *****
q6Word = "galaxy"
print(len(q6Word[1:]))
# Output: 5
# Reason: This is slicing. The length of string from index 1 to end is 5.

# ***** Question-8 *****
print(50 // 11)
# Output: 4
# Reason: Double divide sign(//) returns the floor of the integer


# ***** Question-9 *****
print(3 * 'un' + 'ium')
# Output: unununium
# Reason: multiplication has more precedence so un is output 3 times and then concatenated with ium


# ***** Question-10 *****
print('py' 'thon')
# Output: python
# Reason: Implicitly the string gets concatenated
