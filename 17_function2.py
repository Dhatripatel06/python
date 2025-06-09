# keyword arguments


def say(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

#keyword arguments
say(name="dhatri")  # Uses default greeting
# we can modify thiss
say(greeting="Hi", name="bro")  # Custom greeting,
#in this  order doesn't matter according arguments

