# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

# Function to classify the triangle
def classify_triangle(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles"
    else:
        return "Scalene"

# Input: Enter the lengths of the sides of the triangle
side1 = float(input("Enter the length of side side1: "))
side2 = float(input("Enter the length of side side2: "))
side3 = float(input("Enter the length of side side3: "))

# Check if the sides form a valid triangle
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # Classify and display the type of triangle
    triangle_type = classify_triangle(side1, side2, side3)
    print(f"The triangle with sides {side1}, {side2}, and {side3} is {triangle_type}.")
else:
    print("The entered lengths do not form a valid triangle.")

