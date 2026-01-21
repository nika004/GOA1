# 1 multiply codewars

# def multiply(a, b):
#   return a * b

# 2 Reversed sequence

# def reverse_seq(n):
#     l = []
#     for i in range(n,0,-1):
#         l.append(i)
#     return l

#3 ount of positives / sum of negatives

# def count_positives_sum_negatives(arr):
#     count_positives = 0
#     sum_negatives = 0
#     if arr == []:
#         return []

#     for i in arr:
#         if i > 0:
#             count_positives += 1
#         else:
#             sum_negatives += i
#     return [count_positives,sum_negatives]

#4Are You Playing Banjo?

# def are_you_playing_banjo(name):
    # if name.lower()[0] == "r":
    #     return f"{name} plays banjo"
    # else:
    #     return f"{name} does not play banjo"
    # return name

#5 Sum of positive

# def positive_sum(arr):
#     sum = 0
#     for i in arr:
#         if i > 0:
#             sum += i
#     return sum

#6 Swap Values

# def swap_values(args): 
#     return args.reverse()

#7 Beginner - Reduce but Grow

# def grow(arr):
#     sum = 1
#     for i in arr:
#         sum = sum * i
#     return sum

#8 Century From Year

# def century(year):
#     sum = year // 100
#     if year % 100 == 0:
#         return sum
#     else:
#         return sum + 1

#9 Find Maximum and Minimum Values of a List

# def minimum(arr):
#     return min(arr)

# def maximum(arr):
#     return max(arr)

#10 Grasshopper - Basic Function Fixer

# def add_five(num):
#     total = num + 5
#     return total

#11 Basic variable assignment

# a = "code"
# b = "wa.rs"
# name = a + b

#12 Grasshopper - Messi goals function

# def goals(laLiga, copaDelRey, championsLeague):
#     return laLiga + copaDelRey + championsLeague

#13 You only need one - Beginner

# def check(seq, elem):
#     if elem in seq:
#         return True
#     else:
#         return False

#14 Is he gonna survive?

# def hero(bullets, dragons):
#     if bullets / 2 >= dragons:
#         return True
#     else:
#         return False


#15 Is it even?

# def is_even(n): 
#     if n % 2 == 0:
#         return True
#     else:
#         return False

#16 Convert a Boolean to a String

# def boolean_to_string(b):
#     if b == True:
#         return "True"
#     else:
#         return "False"

#17 String repeat

# def repeat_str(repeat, string):
#     return repeat*string

#18 Switch it Up!

# def switch_it_up(number):
#     if number == 0:
#         result = "Zero"
#     elif number == 1:
#         result = "One"
#     elif number == 2:
#         result = "Two"
#     elif number == 3:
#         result = "Three"
#     elif number == 4:
#         result = "Four"
#     elif number == 5:
#         result = "Five"
#     elif number == 6:
#         result = "Six"
#     elif number == 7:
#         result = "Seven"
#     elif number == 8:
#         result = "Eight"
#     elif number == 9:
#         result = "Nine"
#     return result

#19 Grasshopper - Personalized Message

# def greet(name, owner):
#     if name == owner:
#         return "Hello boss"
#     else:
#         return "Hello guest"

#20 altERnaTIng cAsE <=> ALTerNAtiNG CaSe

# def to_alternating_case(string):
#     return string.swapcase()
