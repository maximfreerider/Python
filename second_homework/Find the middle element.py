#https://www.codewars.com/kata/find-the-middle-element/train/python
def gimme(input_array):
    middle = sorted(input_array)[1]
    return input_array.index(middle)

    # Implement this function
