# // write a program to calculate fuctorial through recursion

def fact(n):
    if n == 1:
        return 1
    return fact(n-1)*n

# // write a program to print reverse string

def reverse(str):
    # str1=""
    # for n in range(-1,-(len(str)+1),-1):
    #     str1 += str[n]
    # return str1
    return str[-1:-1:-1]

# // write a program to extend a list to another list

def extend(lst1, lst2):
    for i in range(len(lst2)):
        lst1.append(lst2[i])
    return lst1

# // write a program to create a class named as rectangle and define functions as area and perimeter

# class rectangle(lenght, breath):
#     length = this.lenght
#     breath = this.breath
#     area = lenght * breath
#     perimeter = (length + breath) * 2
    

# find the greatest number among 3 numbers

def greatest(a,b,c):
    big = a
    if big < b:
        big = b
    if big < c:
        big = c
    return big





# print(fact(5))
print(reverse("hello world"))
# print(extend([1,2,3,4],[9,8,7,4]))
# print(greatest(5,7,8))

# write a program wheather a number is positive, negative or zero. take the number as user input.

def checkpno(n):
    if n > 0:
       return 'positive'
    elif n < 0:
        return "negative"
    else:
        return "zero"

    
# print(checkpno(4))
# print(checkpno(-5))
# print(checkpno(0))
# print(checkpno(-27))


#   wap to creat a list and print a list
def creat_print():
    n = int(input("enter the number of elements"))
    lst = []
    for i in range(n):
        lst[i] = i
    print(lst)
    
#   wap to append an element to the list 



#   wap to insert element at position 2
#   wap to remove an element from the list 
#   wap to sort a list of number
#   wap to extend a list with another list

# ------------------------------------------------------------------------------------------------

action = {"green":"go","yellow":"ready","red":"stop"}
color = input("enter the color")
print(action[color])