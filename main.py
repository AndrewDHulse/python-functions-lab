'''
Write a function named sum_to that accepts a single integer, n, 
and returns the sum of the integers from 1 to n.
'''

def sum_to(n):
    return (n * (n+1)) / 2
#1+2=3+3=6+4=10+5=15
print(sum_to(5))

'''
Write a function named largest that takes a list of numbers as an argument
 and returns the largest number in that list.

'''

def largest(nums):
    large_num=0
    for num in nums:
        if num > large_num:
            large_num=num
    return large_num
        
print(largest([1, 2, 3, 4, 0]))


'''
Write a function named occurrences that takes two string arguments as input 
and counts the number of occurrences of the second string inside the first string.

'''

def occurences(words, letter):
    num=0
    for character in words:
        if character == letter:
            num += 1
    return num

print(occurences('fleep floop', 'e'))

'''
Write a function named product that takes an arbitrary number of numbers, 
multiplies them all together, and returns the product.
(HINT: Review your notes on *args).
'''

def products(*args):
    total=1
    for num in args:
        total *= num
    return total

print(products(-1, 4))

'''
Write a function named steps_to_zero that accepts a non-negative integer 
as an argument, and returns the number of steps it took to reduce the
integer to zero. If the current number is even, 
you have to divide it by 2, otherwise, you have to subtract 1 from it.

'''

def steps_to_zero(num):
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps
 

print(steps_to_zero(14))