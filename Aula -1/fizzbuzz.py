def fizzbuzz(n):
    if n%3== 0 and n%5== 0:
        return'fizzbuzz'
    elif n%5== 0:
        return 'buzz'
    elif n%3 == 0:
        return 'fizz'
    return n
        
        
print(fizzbuzz(7))
print(fizzbuzz(1))
print(fizzbuzz(10))
print(fizzbuzz(9))
print(fizzbuzz(15))
print(fizzbuzz(30))