def announce(f):
    def wrapper():
        print("About to run the function...")
        result = f()
        print("Function has finished running.")
        return result
    return wrapper

@announce
def hello():
    print("Hello, world!") 

hello()