import math


def instructions():
    print()
    print("**************************************************************************")
    print("*              WELCOME TO THE AUTO-DIFFERENCIATION PROGRAM!              *")
    print("**************************************************************************")
    print("To use type in your equations using these criteria:                      *")
    print(" > use the ^ character for raising to the power                          *")
    print(" > use the // pair of characters for square root                         *")
    print(" > e.g. the square root of 4; 4//2                                       *")
    print(" > for each term put no spaces. e.g. 3x^2                                *")
    print(" > do not use brackets; expand brackets ready for differenciation        *")
    print(" > use spaces between terms and between operators and terms e.g 3x^2 + 9 *")
    print(" > for any number raised to the power of 1 please type it, e.g. 3x^1     *")
    print(" > to quit type in 'quit'                                                *")
    print("**************************************************************************")
    print()


# performs the differenciation on the expression given
def maths(eq):
    result = []

    for element in eq:
        for index in range(len(element)):
            # raising to the power
            if element[index] == "^":
                # using the power rule; multiply the base and reduce the exponent
                base = int(element[index-2])
                exponent = int(element[index+1])
                variable = element[index-1]

                base *= exponent
                exponent -= 1

                # checking that the variable is a valid maths variable
                check = ("a" in variable or "b" in variable or "c" in variable or "d"in variable or "e"in variable or "f"in variable or "g"in variable or "h"in variable or "i"in variable or "j"in variable or "k"in variable or "l"in variable or "m"in variable or "n"in variable or "o"in variable or "p"in variable or "q"in variable or "r"in variable or "s"in variable or "t"in variable or "u"in variable or "v"in variable or "w"in variable or "x"in variable or "y"in variable or "z" in variable)
                # add the base, variable if the exponent is 1 or more
                if exponent >= 1:
                    result.append(str(base))
                    result.append(variable)
                    # also add the exponent if the exponent is greater than 1
                    if exponent > 1:
                        result.append("^")
                        result.append(exponent)


                elif exponent == 0 and check:
                    result.append(str(base))

            # square root
            elif element[index] == "/":
                if element[index+1] == "/":

                    text = f"{element[0]}/({element})"
                    result.append(text)
                    



            # adding signs into the expressions
            if element[index] == "+" or (element[index] == "/" and element[index+1] != "/") or element[index] == "*" or element[index] == "-":
                result.append(element[index])

    # check that no signs at the end of the expression remain
    if result[-1] == "+" or result[-1] == "/" or result[-1] == "*" or result[-1] == "-":
        result.pop()
    if result[0] == "+" or result[0] == "/" or result[0] == "*" or result[0] == "-":
        result.pop(0)

    return result


def main():
    instructions()
    app = True
    while app == True:
        try:
            command = input("Please enter an Expression or 'quit': ")
            command = command.lower()
            if command == "quit":
                app = False
                print("Thank you for using Auto-Diff!")
                print("Bye.....")
            else:
                equation = command.split(" ")
                result = maths(equation)
                print("f' = ", *result)
        except Exception:
            print("Try again, invalid expression/expression format!")


main()
