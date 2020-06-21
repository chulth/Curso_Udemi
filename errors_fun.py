def divide (a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print('Don´t divide by zero please')
    except TypeError as err:
        print(f'{a} and {b} must be ints or floats')
    else :
        print(f'{a} divide {b} is {result}')


def divide_two_values(d,e):
    try:
        result = d/e4
    except(ZeroDivisionError, TypeError, ValueError) as err:
        print('Something went wrong')
        print(err)
    else:
        print(f'{e} divide by {d} is {result}')