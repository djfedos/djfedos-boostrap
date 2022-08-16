def rotate(matrix: list[list[int]]):
    if matrix == []:
        pass
    else:
        n = len(matrix)
        for layer in range(n//2):
            first = layer
            last = n - 1 - layer
            for i in range(first, last):
                offset = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[i][last]
                matrix[i][last] = top




if __name__ == '__main__':
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

