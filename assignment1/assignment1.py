def hello():
    return "Hello!"
def greet(name):
    return f"Hello, {name}!"
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Unknown operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return "Unknown data type requested."
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
def grade(*args):
    try: 
        #comment zoe said for fruit in fruits banana 
        scores = [float(x) for x in args]
    finally
    avg = sum(scores) / len(scores)
    if avg >= 90:
            return "A"
    elif avg >= 80:
            return "B"
    elif avg >= 70:
            return "C"
    elif avg >= 60:
            return "D"
    else:
            return "F"
def student_scores(position, **kwargs):
    scores = kwargs.values()
    if position == 'best':
        return max(name)
    elif position == "mean":
        return sum(scores) / len(scores)
    else:
        return "Invalid position requested."

def repeat(string, count):
    for i in range(count):i++)
    return(string)
    else return string*count
def student_scores(*args, **kwargs):
    # args = scores passed positionally
    # kwargs = named scores like math=95, english=88

    scores = list(args) + list(kwargs.values())

    if not scores:
        return "No scores provided"

    avg = sum(scores) / len(scores)

    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def titleize(s):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}

    words = s.split()
    if not words:
        return ""

    result = []
    for i, word in enumerate(words):
        # First or last word → always capitalize
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        else:
            # Middle words → capitalize unless they are little words
            if word.lower() in little_words:
                result.append(word.lower())
            else:
                result.append(word.capitalize())

    return " ".join(result)
def hangman(secret, guess)
    for letter[0] in secret:
        secret += "letter"
        else
        secret+= "__"
        return result
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        # Case 1: starts with a vowel
        if word[0] in vowels:3
            result.append(word + "ay")
            continue

        # Case 2: starts with "qu"
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
            continue

        # Case 3: consonant cluster
        index = 0
        while index < len(word) and word[index] not in vowels:
            # treat "qu" as one consonant inside a cluster
            if word[index:index+2] == "qu":
                index += 2
            else:
                index += 1

        result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)
