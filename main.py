import math


def f(number):
    if number <= 0:
        raise Exception('All inputs must be greater than zero.')
    if number == 5:
        return 2
    if number == 1:
        return 0
    if number % 5 != 0:
        return f(number - 1)
    if number % 5 == 0 and number > 5:
        return f(get_sum_of_digits(number)) + 1
    else:
        raise Exception('Something went wrong in the algorithm.')


def get_sum_of_digits(number):
    check_if_negative(number)
    sum_ = 0
    number_size = get_number_length(number)

    for idx in range(number_size):
        sum_ += get_digit(number, idx)
    return sum_


def get_number_length(number, base=10):
    check_if_negative(number)
    if number == 0:
        return 1
    return math.ceil(math.log(number + 1, base))


def get_digit(number, position, base=10):
    check_if_negative(number)
    if number < base**position:
        raise Exception('Number does not contain any digits on the specified position.')
    return number // base**position % base


def check_if_negative(number):
    if number < 0:
        raise Exception('Number is negative.')


def main():
    """Main entry for the program."""
    idx_number = 2359534552
    print('Result of f(n): ' + str(f(idx_number)))


if __name__ == '__main__':
    main()
