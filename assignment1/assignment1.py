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
    try: scores = [float(x) for x in args]
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
def student_score(position, **kwargs):
    scores = kwargs.values()

    if position == "best":
        return max(scores)

    elif position == "mean":
        return sum(scores) / len(scores)

    else:
        return "Invalid position requested."

def repeat(string, count)
    for (count<5, i++)
    return(string)
else return string*count
def student_score(*args, **kwargs)
for key, value kwargs.item()
for key, value in kwargs.items():
score = sum(scores)
if avg >= 90:
return A
elif avg >=80:
return B
elif avg >=70:
return C
elif avg >=60:
returnD
else
return F 
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
            if word in little_words:
                result.append(word)
            else:
                result.append(word.capitalize())

    return " ".join(result)	
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
words = text.split()
    if len(words) == 1:
        return words[0].capitalize()

    result = []
    for i, word in enumerate(words):
        # First word → always capitalize
        if i == 0:
            result.append(word.capitalize())
            continue
        if i == len(words) - 1:
            result.append(word.capitalize())
            continue
10. def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
            continue
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
            continue
        index = 0
        while index < len(word) and word[index] not in vowels:
# treat "qu" as one consonant inside a cluster
            if word[index:index+2] == "qu":
                index += 2
            else:
                index += 1

        result.append(word[index:] + word[:index] + "ay")

def employee_find(employee_id):
    # Find the column index for employee_id
    employee_id_column = column_index("employee_id")
    if employee_id_column is None:
        print("Could not find 'employee_id' column.")
        return []

    # Function INSIDE a function
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    # Use filter() to find matching rows
    matches = list(filter(employee_match, employees["rows"]))

    return matches
.
