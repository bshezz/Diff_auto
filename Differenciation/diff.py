

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
    print(" > all equations typed and their answers are added to equations.txt      *")
    print(" > please quit the program before accessing the text file                *")
    print(" > two digits are not supported!                                         *")
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
                text = ""

                base *= exponent
                exponent -= 1

                # checking that the variable is a valid maths variable
                check = (any(char.isalpha() for char in variable))
                # add the base, variable if the exponent is 1 or more
                if exponent >= 1:
                    text += str(base)
                    text += variable
                    # also add the exponent if the exponent is greater than 1
                    if exponent > 1:
                        text += "^"
                        text += str(exponent)

                # for items with no exponent and a variable
                elif exponent == 0 and check:
                    text += str(base)

                result.append(text)

            # square root
            elif element[index] == "/":
                if element[index+1] == "/":
                    result.append(f"{element[0]}/({element})")
        
            try:
                # adding signs into the expressions
                if element[index] == "+" or (element[index] == "/" and element[index+1] != "/") or element[index] == "*" or element[index] == "-":
                    result.append(element[index])
            except Exception:
                pass

    # check that no signs at the end of the expression remain
    if result[-1] == "+" or result[-1] == "/" or result[-1] == "*" or result[-1] == "-":
        result.pop()
    if result[0] == "+" or result[0] == "/" or result[0] == "*" or result[0] == "-":
        result.pop(0)

    return result

# additional post maths checks for the result
def check_format_result(result):
    for term in range(0, len(result)-1):
        if (result[term] == "+" and result[term+1] == "+") or (result[term] == "-" and result[term+1] == "-") or (result[term] == "*" and result[term+1] == "*") or result[term] == "/" and result[term+1] == "/":
            result.remove(result[term])
    return result

def main():
    instructions()
    app = True
    question = 1


    while app == True:
        try:
            command = input("Please enter an Expression or 'quit': ")
            file = open("Differenciation/equations.txt", "+a")
            command = command.lower()
            if command == "quit":
                app = False
                print("Thank you for using Auto-Diff!")
                print("Bye.....")
            else:
                equation = command.split(" ")
                result = maths(equation)
                result2 = check_format_result(result)
                quest = ""
                ans = ""
                print("f' = ", *result2)

                text = str(question) + ". "
                file.write(text)
                for item in equation:
                    quest += item
                    quest += " "
                file.write(quest)
                file.write("\n")

                for item in result2:
                    ans += item
                    ans += " "
                file.write(ans)
                file.write("\n")
                file.write("\n")

                question += 1
                file.close()
            
        except Exception:
            print("Try again, invalid expression or format!")


main()
