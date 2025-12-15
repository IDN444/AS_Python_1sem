#пункт а
def filter_numbers(numbers, condition = None):
    if condition is None:
        return numbers
    result = []
    for number in numbers:
        if condition(number):
            result.append(number)
    return result

#пункт б
def transform_numbers(numbers, transform_function = None):
    if transform_function is None:
        return numbers
    result = []
    for number in numbers:
        transformed_number = transform_function(number)
        result.append(transformed_number)
    return result

#пункт в
def cube_numbers(lists):
    result = []
    for numbers_list in lists:
        for number in numbers_list:
            cube = number ** 3
            result.append(cube)
    return result
