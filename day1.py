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


# ***** Question-11 *****
print(sum(range(0, 7)))
# Output: 21
# Reason: Range returns a number range from 0(inclusive) to 7(exclusive). Then sum it up from sum function which is 21


# ***** Question-12 *****
q12Cubes = [1, 8, 27]
q12Cubes.append(4 ** 3)
print(q12Cubes)
# Output: [1, 8, 27, 64]
# Reason: Double asterisks means power. 4 power 3 is 64. It is appended to the array


# ***** Question-13 *****
q13Word = "galaxy"
print(q13Word[4:50])
# Output: xy
# Reason: Start from the starting index(4) towards 50th index. If 50 letters are not available then the list will be returns till end.


# ***** Question-14 *****
print(51 % 3)
# Output: 0
# Reason: It is modulus operator and returns the remaining after the division. 51 completely gets divided by 3 so it returns zero.

# ***** Question-15 *****


def if_confusion(x, y):
    if x > y:
        if x - 5 > 0:
            x = y
            return "A" if y == y + y else "B"
        elif x + y > 0:
            while x > y:
                x -= 1
            while y > x:
                y -= 1
            if x == y:
                return "E"
    else:
        if x - 2 > y - 4:
            x_old = x
            x = y * y
            y = 2 * x_old
            if (x - 4) ** 2 > (y - 7) ** 2:
                return "C"
            return "D"
        return "H"


print(if_confusion(3, 7))
# Output: H
# Reason: Dry run the code and follow the if and loop branchings

# ***** Question-16 *****
q16Str = 'cool'
print(q16Str[-1] + q16Str[-2]
      + q16Str[-4] + q16Str[-3])
# Output: loco
# Reason: The negative index gets the last element. -1 defines the last element from end.


# ***** Question-17 *****
q17Words = ['cat', 'mouse']
for word in q17Words:
    print(len(q17Words))
# Output: 3 5
# Reason: in operator gets the value of each element and assign to word(within the loop) and len operator gets the length of the string

# ***** Question-18 *****


def func(x):
    return x + 1


f = func
print(f(2) + func(2))
# Output: 6
# Reason: Line number 141 assigns the function func reference to f. Now we can call the same function with the name f


# ***** Question-19 *****
q19Word = "galaxy"
print(q19Word[:-2] + q19Word[-2:])
# Output: galaxy
# Reason: [:-2] means that start from 0th index towards -2 index which makes gala and [-2:] means start from -2 to end. Now concatenate them which makes galaxy


# ***** Question-20 *****
def q20Func(a, *args):
    print(a)
    for arg in args:
        print(arg)


q20Func("A", "B", "C")
# Output: A B C
# Reason: a simply gets "A" and *args means that it becomes a list with elements "B" and "C" which can further be iterated and printed.
