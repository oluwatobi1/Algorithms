# Write an algorithm (choose the language you prefer) that given a character string, 
# for instance {‘c’,’a’,’i’,’o’,’p’,’a’}, will print out the list of characters 
# appearing at least 2 times. In this specific example, it would return {‘a’}. 
# Afterwards, comment out the cost in terms of space and time.


ls = ['c', 'a', 'i', 'i', 'p', 'a']

def duplicate(ls):
    seen = {}
    res = []

    for i in ls:
        if i in seen:
            res.append(i)
        else:
            seen[i] = 1
    return res

# time: O(n)
# space: O(n)

# other solution:
# sorting the list and checking if the adjacent elements are the same
# time: O(n log n)
# space: O(1)


#######

print(duplicate(ls))

# ##############################
# ##############################
# ##############################

# def duplicate(ls):
#     seen = {}
#     res = []

#     for i in ls:
#         if i in seen:
#             res.append(i)
#         else:
#             seen[i] = 1
#     return res

# # time: O(n)
# # space: O(n)

# # other solution:
# # sorting the list and checking if the adjacent elements are the same
# # time: O(n log n)
# # space: O(1)

# Unit testing and integration testing are both important parts of successful software development. They serve different yet related purposes, one cannot replace the other. They complement each other nicely.
# Unit tests focuses on a single part of a whole application in total isolation, usually, a single functions or clases. While integration test, test how parts of the application work together as a whole. 
# For system test, or system-level tests or system-integration testing, evaluates how the various components of an application interact together in the full, integrated system or application.



#  Design patterns are approaches to solving general problems that software developers faced during software development.
# A design pattern I used recently is FACTORY Design pattern. In simple words its creating a factory that dynamically creates objects based on certain requirement usual specified as factory parameters.



# There are a number of ways to approach writing code and software development generally. These ways comes together to form BEST PRACTICES in programming. In my opinion, writing code works and/or meets the business requirement is the main goal of any software dev project. So the main problem to avoid is writing code and software that does not meet or align with the business requirement for the software. Basically writing code that cannot be used. Why?
# Because It wouldn't matter how beautiful a piece of software is, or the underlying architecture is, if it is not useful.



# Not 100% clear on this, but I could say a thing or two on multiprocessing and single threading.
# Single threaded processes contains instruction of executing in a single sequence and it is processes one at a time.
# while multi process which is on the flip side of the coin, involves execution of multiple parts of a program at the same time.