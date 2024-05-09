# def test_(name, value, *types, **values):
#     print(name, value, types, values)
#
#
# test_('Александр', '44 года', 1, 9, 7, 9, курс='Python')



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(7))
