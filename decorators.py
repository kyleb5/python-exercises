def reversal(sentence_func):
    def reversed_sentence(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"Reversed: {''.join(reversed(original_sentence))}"
    return reversed_sentence


@reversal
def letterPress():
    return "Adaptogen tote bag drinking vinegar, letterpress pabst locavore migas hella"


def taxidermy():
    return "Taxidermy health goth locavore, pickled post-ironic pork belly kale chips tofu PBR&B bicycle rights"


@reversal
def mustache():
    return "Umami hexagon stumptown enamel pin, mustache echo park readymade celiac"


def lumberSexual():
    return "Jean shorts lumbersexual stumptown tumeric everyday carry readymade"


print(letterPress())
print(taxidermy())
print(mustache())
print(lumberSexual())


# You need to write functions to represent tasks that members of a family need to perform on a regular basis.


def laundry():
    return "The dirty laundry was cleaned"


def garbage():
    return "The garbage was taken out"


def dust():
    return "The house was dusted"


def groom():
    return "The dog was brushed"

# Write a decorator function named @kids that, when placed above a function, will modify the return value of that function to have "by the kids" appended to the end. For example, if the decorator is above the garbage() function, when you invoke the method, it should return "The garbage was taken out by the kids"


def kids(sentenced_func):
    def combine(*args, **kwargs):
        original_stence = sentenced_func(*args, **kwargs)
        return f"{original_stence} by the kids"
    return combine


def mom(sentenced_func):
    def combine(*args, **kawargs):
        original_sentence = sentenced_func(*args, **kawargs)
        return f"{original_sentence} by mom"
    return combine


def dad(sentence_func):
    def combine(*args, **kawargs):
        original_sentence = sentence_func(*args, **kawargs)
        return f"{original_sentence} by dad"
    return combine


@kids
def garbage():
    return "The garbage was taken out"


@mom
def garbage():
    return "The garbage was taken out"


@dad
def garbage():
    return "The garbage was taken out"


result = garbage()
print(result)  # "The garbage was taken out by the kids"

# Now write two more decorator functions named @dad and @mom and place them above the functions that you want to assign to the parents. The output should be appended with "by Dad" or "by Mom".
