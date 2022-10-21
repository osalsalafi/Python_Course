from random import choice
quotes_list = [
    "For every complex problem there is an answer that is clear, simple, and wrong.",
    "You can't be successful in business without taking risks. It's really that simple",
    "Only great minds can afford a simple style"
    ]

def get_quotes():
    return "\n".join(quotes_list)

def add_quote(quote):
    if isinstance(quote, str) :
        quotes_list.append(quote)
    else :
        return 'The quote must be a string'
    
def get_random_quote():
    return choice(quotes_list)

# if we apply any print of functions to the functions
# it will affect the file after importing it so we have to add

if __name__ == '__main__' :
    print(get_random_quote())
    add_quote("You only live once, but if you do it right, once is enough.")
    print(get_quotes())