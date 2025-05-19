'''
Similar to switch statement found in other programming languages.

The basic syntax of the match statement involves matching, 
a variable against several cases using the case keyword.
'''


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Status"
        

# Usage:
# print(http_status(200)) #ok
# print(http_status(404))  #Not Found
# print(http_status(500)) #Server Error
print(http_status(4)) #Unknown status