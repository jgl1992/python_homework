def hello():
    return "Hello!"
def greet(name):
    return "Hello," + name + "!"
def calc(num1, num2, operation="multiply"):
    try:
        if operation == "add": 
            result = num1 + num2
            return result
        elif operation =="subtract":
            result = num1 - num2
            return result
        elif operation == "multiply"
            result = num1 * num2
            return result
        elif operation == "divide":
                if num2 == 0:
                    return "You can't divide by 0!"
                result = num1/num2
                return result
        elif operation = "int_divide":
            if num2 ==0:
                return "You can't divide by 0!"
            return num1 // num2
        elif operation == "power":
                return num1 ** num2
                return result
        else:
             result = num1 * num2
             return result
    except: 
         message = "You can't" + operation + "those values!"
         return message
   
def test_data_type_conversion(value, target_type):
    try:
         if target_type == "int":
            converted_value = int(Value)
            return converted_value
         elif target_type == "float":
              converted_value = float(value)
              return converted_value
         elif target_type =="str":
              converted_value = str(value)
              return converted_value
    except:
        error_message = "You can't convert" + str(value) + " into a" + target_type + "."\
        return error_message
def grade(*args):
    try: 
        avg = sum(args) / len(args)
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
def repeat(string, count)
    result = ""
    for i in range(count):
        result = result + string
    return result
def student_scores(operation, *args, **kwargs):
    if operation =="mean":
        total = 0
        count = 0
        for key, value in kwargs.items():
            total += value
            count +=1
            average = total/count
            return average
    elif operation =="best":
        best_student = ""
        highest_score = 0
        for key, value in kwargs.items():
            if value > highest_score:
                highest_score = value
                best_student = key
            return best_student
def titleize(text):
    little_words = [a", "an", "the", "and", "of", "or", "is", "in"]
    words = text.split()
    result_words = []
    for i in range(len(words)):
        word = words[i]
    #First or last -> always cap
    if i == 0 or i = len(words) -1:
        first_letter = word[0].upper()
        rest_of_word = word[1:].lower()
        titled_word = first_letter + rest_of_word
        result_words.append(titled_word)
        else:
            #Mid word -> cap unless little
            titled_word = word.lower()
            result_words.append(titled_word)
            result = " ".join(result_words)
            return result
                assert.append(word)
            else:
                result.append(word.capitalize())
    return " ".join(result)	
    #words capitalize
    return result
def hangman(secret, guess):
    result = ""
     for letter in word:
            if letter in guess:
                 result = result _ letter
            else:
                 result = result + "_"__annotations__
            return result  
def pig_latin(sentence):
    words = sentence.split()
    result = []
    for word in words:
    word = word.lower()
        if word[0] in "aeiou":
            result.append(word + "ay")
            continue
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
            continue
        vowel_index = -1
        for i, ch in enumerate(word):
            if ch in "aeiou":
                vowel_index = i
                break
        if vowel_index == -1:
            result.append(word + "ay")
        else:
            consonants = word[:vowel_index]
            rest = word[vowel_index:]
            result.append(rest + consonants + "ay")
    return " ".join(result)
