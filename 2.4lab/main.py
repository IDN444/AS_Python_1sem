#gункт а
def filter_numbers(numbers, condition = None):
    if condition is None:
        return numbers
    result = []
    for number in numbers:
        if condition(number):
            result.append(number)
    return result
