"""
Time stuff
"""
# import time
#
# t1 = time.perf_counter_ns()
# # do things
# t2 = time.perf_counter_ns()
# print(t2 - t1)


"""
Idempotence
f(f(x)) = f(x)

Whenever you do something over and over again, you get the same result.

GET
PUT
POST
DELETE

Are always Idempotent

POST is NOT Idempotent (The response can change on multiple tries)
"""
#
# print(abs(abs(-10)))  # Will always be 10
#
"""
Closures

"A closure is an inner function that remembers and has access to variables in
the local scope in which it was created.
"""

# def closure():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return inner
#
#
# start = closure()
# start()
# start()
# start()
#
"""
Memoization: storing the result of a function so it does not need to be re-run
if the same inputs are seen again.
"""
# import time
#
# ef_cache = {}
#
#
# def expensive_func(num):
#     if num in ef_cache:
#         return ef_cache[num]
#
#     print(f"Computing {num}")
#     time.sleep(1)
#     result = num * num
#     ef_cache[num] = result
#     return num * num
#
#
# result = expensive_func(4)
# print(result)
#
# result = expensive_func(10)
# print(result)
#
# result = expensive_func(4)
# print(result)
#
# result = expensive_func(10)
# print(result)
#
"""
Ternary Conditional
"""
# # condition = False
# # x = 1 if condition else 0
#
"""
formatting large numbers.
2_000_000 # Adding underscores does not affect numbers in Python!
"""
# num1 = 10_000_000_000
# num2 = 100_000_000
# total = num1 + num2
#
# print(f"{total:,}")
#
"""
iterate over two lists at once!
"""
# names = [""]
#
#
# def fibonacci_generator(num):
#     a, b = 0, 1
#     for i in range(0, num):
#         yield a
#         a, b = b, a + b
#
#
# fib_gen = fibonacci_generator(10)
#
#
# def test_fibonacci_generator(fib_gen):
#     first_ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for fib, num in zip(fib_gen, first_ten):
#         assert fib == num
#
#
"""
Tuple unpacking
"""
# # set 'a' and 'b' to 1, 2 and c to everything up to the last one [3, 4] d to 5
# a, b, *c, d = (1, 2, 3, 4, 5)
# print(a, b, c, d)
# # Ignore the rest of the arguments completely
# a, b, *_ = (1, 2, 3, 4, 5)
# print(a, b, c, d)
#
"""
Being 'Pythonic'... EAFP (Easier to ask forgiveness than permission)
'Let's try to do something and if it doesn't work, we will handle it.
vs
Look before you leap (LBYL)
'ask permission every step you take.'

Python can be a lot faster in situations where you don't expect a lot of errors
because you don't have to keep accessing the object to ask it questions before
proceeding.
"""
#
#
class Person:
    def quack(self):
        print("Quack, quack!")

    def walk(self):
        print("Waddle, Waddle!")


class Duck:
    def quack(self):
        print("Quack, quack!")

    def walk(self):
        print("Waddle, Waddle!")


# Pythonic
def is_a_duck_pythonic(thing):
    try:
        thing.quack()
        thing.walk()
        print("I think this is a Duck!")
    except AttributeError as e:
        print(e)
        print("I don't think this is a duck!")


#
#
# # Non-Pythonic
def is_a_duck(thing):
    if hasattr(thing, "quack"):
        if callable(thing.quack):
            thing.quack()

        if hasattr(thing, "walk"):
            if callable(thing.walk):
                thing.walk()
        print("I think this is a Duck!")


#
#     else:
#         print("I don't think this is a duck!")
#
#
"""
How being more Pythonic can avoid race conditions
"""
# import os
#
# my_file = "file.txt"
#
# if os.access(my_file, os.R_OK):
#     # Race condition could happen here if something happens to the file before
#     # Python is able to open it.
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print("File could not be accessed")
#
# # Non-Race condition
# try:
#     f = open(my_file)
# except IOError as e:
#     print("File could not be accessed")
# else:
#     with f:
#         print(f.read())

"""
Async Tasks
"""
# import time
# import asyncio

# def print_something(something):
#     time.sleep(0.1)
#     print(something)
#
#
# async def print_something_2(something):
#     time.sleep(0.1)
#     print(something)
#
#
# async def main(loop):
#     colors = [
#         "Black",
#         "Yellow",
#         "Green",
#         "Red",
#         "Blue",
#         "Beige",
#         "Orange",
#         "Burgundy",
#         "Pink",
#         "Brown",
#     ]
#     for color in colors:
#         loop.create_task(print_something_2(color))
#
#     # await asyncio.wait()
#
#
# START_TIME = time.clock()
# LOOP = asyncio.get_event_loop()
# try:
#     LOOP.run_until_complete(main(LOOP))
# except Exception as e:
#     pass
# finally:
#     LOOP.close()
# print(f"I took {time.clock() - START_TIME} seconds to complete")
"""
Multiprocessing
"""
# import time
# from multiprocessing import Process, Queue, Pool, cpu_count
# import time

# def print_something(something):
#     time.sleep(1)
#     print(something)
#
#
# def multiprocess_list(items):
#     processes = []
#
#     for item in items:
#         proc = Process(target=print_something, args=(item,))
#         processes.append(proc)
#         proc.start()
#
#     for proc in processes:
#         proc.join()
#
#
# def multiprocess_tasks(tasks, number_of_processes):
#     tasks_to_accomplish = Queue()
#     processes = []
#
#     for task in tasks:
#         tasks_to_accomplish.put(task)
#
#     for i in range(number_of_processes):
#         while not tasks_to_accomplish.empty():
#             p = Process(target=print_something, args=(tasks_to_accomplish.get(),))
#             processes.append(p)
#             p.start()
#
#     for p in processes:
#         p.join()
#
#
# def pool_tasks(tasks, number_of_processes):
#     p = Pool(number_of_processes)
#     p.map(print_something, tasks)
#
#
# COLORS = [
#     "Black",
#     "Yellow",
#     "Green",
#     "Red",
#     "Blue",
#     "Beige",
#     "Orange",
#     "Burgundy",
#     "Pink",
#     "Brown",
# ]
#
# START_TIME = time.time()
# for COLOR in COLORS:
#     print_something(COLOR)
# # Method 1
# multiprocess_list(COLORS) # 1.5 seconds
#
# # Method 2
# multiprocess_tasks(COLORS, cpu_count())  # 1.67 seconds
#
# # Method 3
# pool_tasks(COLORS, cpu_count()) # 3.2 seconds
#
# # No multiprocessing 10 seconds
# for COLOR in COLORS:
#     print_something(COLOR)
#
# print(f"I took {time.time() - START_TIME} seconds to complete")

"""
Python Logging
"""
# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)  # stream_handler will use this level
#
# formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
#
# file_handler = logging.FileHandler("sample.log")
# file_handler.setLevel(logging.ERROR)  # Only write ERRORS to the sample.log
# file_handler.setFormatter(formatter)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
#
#
# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         logger.exception("Tried to divide by zero")
#
#
# num_1 = 20
# num_2 = 0
#
# divide_result = divide(20, 0)
# logger.debug(f"Divide: {num_1} + {num_2} = {divide_result}")

"""
Github stuff
 # Discard local repo commits
 git reset HEAD~
 # Discard staging area changes NOT committed
 git reset --hard
 # Compare staging directory to master
 git diff
 # Compare committed changes to local repo to master
 git diff --staged
 # Show all local branches
 git branch 
 # Show all remote branches
 git branch -a
 # Switch branches
 git checkout <branch-name>
 # Take newly created local branch, push it to origin while also creating origin branch. This is only done once.
 git push -u origin <branch-name>
 
 
 # How to merge a branch
 # Check out local Master branch
 git checkout master
 
#  If you want to push a deleted file to remote
# git add 'deleted file name'
# 
# git commit -m'message'
# 
# git push -u origin branch
# 
# If you want to delete a file from remote and locally
# git rm 'file name'
# 
# git commit -m'message'
# 
# git push -u origin branch
# 
# If you want to delete a file from remote only
# git rm --cached 'file name'
# 
# git commit -m'message'
# 
# git push -u origin branch
 
"""


"""
What is an iterable, iterator, and a generator? Oh My!
Q: Is a List an iterator?
A: It is iterable, but it is NOT an iterator.
Q: So what does it mean that something is 'iterable?'
A: Something that is iterable is something that can be 'looped' over. These include strings, lists, dictionaries,
tuples, files, generators, etc. The object needs to be able to return an interator object from its dunder __iter__
method. The iterator object returned must define a __next__ method. 
Q: How do we know that something is iterable?
A: It needs to have dunder (magic) method __iter__
A: When you are using a for loop over an object, you are calling its __iter__ method.
Q: So what is an iterator?
A: An iterator is an object with a state so that it remembers where it is during iteration.
Q: How does an iterator get its next value?
A: An iterator gets its next value though the __next__ method
A: One of the reasons a list is not an iterator is that it does not have a __next__ method.
Q: What's the difference between a function and a generator?
A: A generator yields values whereas a function returns values. A generator also maintains state.
"""
# tmp_list = [1, 2, 3]
# iter_list = tmp_list.__iter__()
# iter_list_2 = iter(tmp_list)
# assert type(iter_list) == type(iter_list_2)  # Both are iterators
#
# # Custom implementation of a for loop
# tmp_list = [1, 2, 3]
# iter_list = iter(tmp_list)
# while True:
#     try:
#         item = next(iter_list)
#         print(item)
#     except StopIteration:
#         break
#
# # Custom implementation of the range() function using a generator
# class MyRange:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current
#
# nums = MyRange(1, 10)
# for num in nums:
#     print(num)
#
# nums_2 = MyRange(1, 10)
# print(next(nums_2))
# print(next(nums_2))
# print(next(nums_2))
# print(next(nums_2))

# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1
#
#
# nums = my_range(1, 10)
# for i in range(9):
#     print(next(nums))
"""
Intertools
"""

# # Counter
# import itertools

# counter = itertools.count(start=1, step=1)
#
# data = ["Mark", "Ashley", "Christine", "John", "Holiday"]
# combined = list(
#     zip(counter, data)
# )  # zip pairs iterables together, limited by the shortest one.
# print(combined)

# # Cycle
# cycle_counter = itertools.cycle(("On", "Off"))  # Good for simulating a switch. Takes a tuple and repeats it.
# for _ in range(6):
#     print(next(cycle_counter))

# # Repeat
# squares = map(pow, range(10), itertools.repeat(2))  # pow(2, 2) == 2^2
# print(list(squares))

# # Starmap
# squares = itertools.starmap(
#     pow, [(0, 2), (1, 2), (2, 2)]
# )  # like map(), but takes sets of tuples
# print(list(squares))

# # Combinations and Permutations
# # With combinations, order does not matter, in permutations, they do.
# import time

# letters = ["a", "b", "c"]
# numbers = [1, 2, 3]
# names = ["John", "Ashley"]
# combinations = itertools.combinations(letters, 2)
# permutations = itertools.permutations(letters, 2)
# itertools.combinations(letters, 2)
# itertools.permutations(letters, 2)
# list_generator = itertools.chain(letters, numbers, names)

# # islice
# test_gen = (a for a in range(101))
# slice_of_generator = itertools.islice(
#     test_gen, 90, 101, 2
# )  # (iterator, start, stop, step)
# print(list(slice_of_generator))  # [90, 92, 94, 96, 98, 100]

# # Filtering and Compression
# import string
#
#
# def lt_2(n):
#     if n < 2:
#         return True
#     return False
#
#
# alphabet_list = list(string.ascii_lowercase)
# numbers = range(10)
# names = ["Solly", "Holiday"]
#
# selectors = itertools.cycle((True, False))
#
# filter_result = filter(lt_2, numbers)
# print(list(filter_result))  # [0, 1]
#
# flip_filter_result = itertools.filterfalse(lt_2, numbers)
# print(list(flip_filter_result))  # [2, 3, 4, 5, 6, 7, 8, 9]
#
# compression_result = itertools.compress(alphabet_list, selectors)
# print(
#     list(compression_result)
# )  # ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y']
#
# drop_until_true = itertools.dropwhile(
#     lt_2, numbers
# )  # filter the nums until you reach a True, then return the rest
# print(list(drop_until_true))  # [2, 3, 4, 5, 6, 7, 8, 9]
#
# take_while_true = itertools.takewhile(
#     lt_2, numbers
# )  # return nums until False, then yeet the F out.
# print(list(take_while_true))  # [0, 1]

# # Accumulate
# numbers = range(10)
# acc_result = itertools.accumulate(numbers)  # add each num to the next one
# print(list(acc_result))  # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

# # Groupby (REQUIRES ITERABLE TO ALREADY BE SORTED!!!!)
# def get_state(person):
#     return person["state"]
#
#
# people = [
#     {"name": "John Doe", "city": "Gotham", "state": "NY"},
#     {"name": "Jane Doe", "city": "Kings Landing", "state": "NY"},
#     {"name": "Corey Schafer", "city": "Boulder", "state": "CO"},
#     {"name": "Al Einstein", "city": "Denver", "state": "CO"},
#     {"name": "John Henry", "city": "Hinton", "state": "WV"},
#     {"name": "Randy Moss", "city": "Rand", "state": "WV"},
#     {"name": "Nicole K", "city": "Asheville", "state": "NC"},
#     {"name": "Jim Doe", "city": "Charlotte", "state": "NC"},
#     {"name": "Jane Taylor", "city": "Faketown", "state": "NC"},
# ]
#
# person_group = itertools.groupby(people, get_state)

# for key, group in person_group:
#     print(key)
#     for person in group:
#         print(person)

# copy1, copy2 = itertools.tee(person_group) # create two copies of an iterator
"""
Calling external programs in Python
"""
# import subprocess

# subprocess.run("ls")  # single command
# subprocess.run(
#     "ls -la", shell=True
# )  # You can use shell=True if running more than one command..but this is not safe
# subprocess.run(["ls", "-la"])  # passing in commands with a list is safer.
#
# # capture output
# output = subprocess.run(
#     ["ls", "-la"], capture_output=True, text=True
# )  # text=true returns a string instead of bytes
# print(output)

# # redirecting output to a file
# with open("output.txt", "w") as writer_obj:
#     output = subprocess.run(
#         ["ls", "-la"], stdout=writer_obj, text=True, check=True
#     )  # check=true throws an error in Python if it fails

# # Error handling
# output = subprocess.run(["ls", "-la", "blablah"], capture_output=True, text=True)
# if output.returncode != 0:  # There was an error
#     print(output.stderr)
# else:
#     with open("output.txt", "w") as writer_obj:
#         writer_obj.write(output)

# # Re-direct output to the void
# subprocess.run(["ls", "-la", "blablah"], stderr=subprocess.DEVNULL)

# # Pipe commands | !
# def get_file_line_count_bash(file_path):
#     line_count = subprocess.run(
#         [f"cat {file_path} | wc -l"], capture_output=True, text=True, shell=True
#     )
#     return int(line_count.stdout.strip())
"""
requests with HTTPbin
"""
# import requests
#
# # GET
# payload = {"page": 2, "count": 25}
# r = requests.get("https://httpbin.org/get", params=payload)
#
# # POST
# payload = {"username": "John", "password": "testing123"}
# r = requests.post("https://httpbin.org/post", data=payload)
# r_dict = r.json()
#
# # Basic Auth
# r = requests.get(
#     "https://httpbin.org/basic-auth/john/testing123", auth=("john", "testing123")
# )
# print(r.text)

"""
Python Search Algorithmns
"""


# def bubble_sort(arr):
#     n = len(arr)
#
#     for u in range(n):
#         for v in range(0, n - u - 1):
#             if arr[v] > arr[v + 1]:
#                 arr[v], arr[v + 1] = arr[v + 1], arr[v]
#     return arr
#
#
# def selection_sort(arr):
#     indexing_length = range(0, len(arr) - 1)
#
#     for i in indexing_length:
#         min_value = i
#
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_value]:
#                 min_value = j
#
#         if min_value != i:
#             arr[min_value], arr[i] = arr[i], arr[min_value]
#
#     return arr
#
#
# print(selection_sort([1, 6, 3, 6, 3, 8, 23, 4, 2, 1, 7]))
