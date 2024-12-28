"""
Exception handling in python?

theory:

An exception is an error that occurs during the execution of a program. When an exception occurs, the program stops and passes control to the calling function or the Python interpreter.

- try, except, else, finally, assert, raise
"""

# print("start")
# print(a)
# print("end")

# print("start")
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     # print(num1 + num2 + 10)

#     total  = num1 / num2
# # except ZeroDivisionError:
# #     print("Cannot divide by zero.")
# except TypeError:
#     print("Invalid input. Please enter a number.")
# except NameError:
#     print("Something is not defined.")
# # except Exception as err:
# #     print(f"ERROR: {err}")
# else:
#     print(f"The total is: {total}")
# finally:
#     print("This block is always executed.")
# print("end")


bal = 1000
# assert bal > int(input("Enter a withdrow amount: ")), "Insufficent balance"

if int(input("Enter a withdrow amount: ")) > bal:
    raise ValueError("Insufficent balance")

# https://docs.python.org/3/library/exceptions.html

# BaseException
#  ├── BaseExceptionGroup
#  ├── GeneratorExit
#  ├── KeyboardInterrupt
#  ├── SystemExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ExceptionGroup [BaseExceptionGroup]
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── OSError
#       │    ├── BlockingIOError
#       │    ├── ChildProcessError
#       │    ├── ConnectionError
#       │    │    ├── BrokenPipeError
#       │    │    ├── ConnectionAbortedError
#       │    │    ├── ConnectionRefusedError
#       │    │    └── ConnectionResetError
#       │    ├── FileExistsError
#       │    ├── FileNotFoundError
#       │    ├── InterruptedError
#       │    ├── IsADirectoryError
#       │    ├── NotADirectoryError
#       │    ├── PermissionError
#       │    ├── ProcessLookupError
#       │    └── TimeoutError
#       ├── ReferenceError
#       ├── RuntimeError
#       │    ├── NotImplementedError
#       │    ├── PythonFinalizationError
#       │    └── RecursionError
#       ├── StopAsyncIteration
#       ├── StopIteration
#       ├── SyntaxError
#       │    └── IndentationError
#       │         └── TabError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       │    └── UnicodeError
#       │         ├── UnicodeDecodeError
#       │         ├── UnicodeEncodeError
#       │         └── UnicodeTranslateError
#       └── Warning
#            ├── BytesWarning
#            ├── DeprecationWarning
#            ├── EncodingWarning
#            ├── FutureWarning
#            ├── ImportWarning
#            ├── PendingDeprecationWarning
#            ├── ResourceWarning
#            ├── RuntimeWarning
#            ├── SyntaxWarning
#            ├── UnicodeWarning
#            └── UserWarning