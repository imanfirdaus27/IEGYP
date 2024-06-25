side_length = int(input("Enter the side in cm of a square tile\n"))
num_tiles = int(input("Enter the number of square tiles available\n"))

# Calculate the maximum number of tiles that can form a square (k x k)
k = int(num_tiles ** 0.5)

# Side of the largest square that can be formed
largest_square_side = k * side_length

# Calculate the area of the largest square
largest_square_area = largest_square_side ** 2

# Output the result
print(f"Area of the largest possible square is {largest_square_area}sqcm")