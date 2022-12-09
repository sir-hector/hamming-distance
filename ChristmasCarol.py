things = ["", " and a Partridge in a Pear Tree.", " two Turtle Doves,", " three French Hens,", " four Calling Birds,",
          " five Gold Rings,", " six Geese-a-Laying,", " seven Swans-a-Swimming,", " eight Maids-a-Milking,",
          " nine Ladies Dancing,", " ten Lords-a-Leaping,", " eleven Pipers Piping,", " twelve Drummers Drumming,"]
numbers = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
           "eighth", "ninth", "tenth", "eleventh", "twelfth"]


def generateSingle(number):
    base = " day of Christmas my true love gave to me:"
    if number == 1:
        return "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree"

    response = "On the " + numbers[number] + base

    for i in range(number, 0, -1):
        response = response + things[i]

    return response
