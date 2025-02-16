def sqr(start, end):
    sqr = [num ** 2 for num in range(start, end + 1)]
    
    even_squares = [sq for sq in sqr if sq % 2 == 0]
    odd_squares = [sq for sq in sqr if sq % 2 != 0]

    print('Even squares:', even_squares)
    print('Odd squares:', odd_squares)

sqr(1, 10)