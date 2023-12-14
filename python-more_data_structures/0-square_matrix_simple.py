def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []
    
    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the result matrix with squared values
        squared_row = [x ** 2 for x in row]
        
        # Append the squared row to the result matrix
        result_matrix.append(squared_row)
    
    return result_matrix

# Example usage:
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(input_matrix)
print(result)
