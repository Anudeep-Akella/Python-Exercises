# Finding the Area and Volume

# Function for finding the area
def area(length,width):
    if not isinstance(length,(int,float)) or not isinstance(width,(int,float)):
        raise TypeError("Enter a valid number")
    return length * width

# Function for finding the perimeter
def perimeter(length,width):
    if not isinstance(length,(int,float)) or not isinstance(width,(int,float)):
        raise TypeError("Enter a valid number")
    return 2 * (length + width)

# Function for finding the volume
def volume(length,width,height):
    if not isinstance(length,(int,float)) or not isinstance(width,(int,float)) or not isinstance(height,(int,float)):
        raise TypeError("Enter a valid number")
    return length * width * height

# Function for finding the surface area
def surfaceArea(length,width,height):
    if not isinstance(length,(int,float)) or not isinstance(width,(int,float)) or not isinstance(height,(int,float)):
        raise TypeError("Enter a valid number")
    return 2 * ((length * width) + (width * height) + (length * height))


assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340
