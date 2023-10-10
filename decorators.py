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


# Your job is to write a decorator function named sort_by_name that you can use on vendors, employees, customers, and deceased so that the ORDER BY last_name ASC, first_name ASC clause is added to them.
def sort_by_name(func):
    def by_name(self):
        name = func(self)
        if "ORDER BY" not in name:
            name += " ORDER BY last_name ASC, first_name ASC"
        return name
    return by_name


class Queries:

    @sort_by_name
    def customers(self):
        return "SELECT * FROM Customer"

    def coffins(self):
        return "SELECT * FROM Coffin"

    @sort_by_name
    def employees(self):
        return "SELECT * FROM Employee"

    def gravestones(self):
        return "SELECT * FROM GraveStones"

    @sort_by_name
    def deceased(self):
        return "SELECT * FROM Deceased"

    def obelisks(self):
        return "SELECT * FROM Obelisk"

    @sort_by_name
    def vendors(self):
        return "SELECT * FROM Vendor"


# Here's some sample output for a properly implemented decorator.
queries = Queries()

print(queries.customers())
print(queries.coffins())
print(queries.employees())

# # Output
# SELECT * FROM Customer ORDER BY last_name ASC, first_name ASC
# SELECT * FROM Coffin
# SELECT * FROM Employee ORDER BY last_name ASC, first_name ASC
