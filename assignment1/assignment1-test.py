def test_hello():
    assert "Hello!!"
def test_greet():
    assert a1.greet("Edwards") == "Hello, Edwards!"
def test_calc()
    assert a1.calc(17,2)==34
    assert a1.calc(6, 7, "add") == 13
    assert a1.calc(25, 5 "subract") == 20
    assert a1.calc(17, 2.0, "multiply") == 34.0
    assert a1.calc(10, 0, "divide") == "You can't divide by 0!"
    assert a1.calc(99, 5, "modulo") ==4
    assert a1.calc("first", "second", "multiply") == "You can't multiply those values!"
def test_data_type_conversion():
    result = a1.data_type_convesion("100", "int")
    assert type(result).__name__=="int"
    assert result = 100 
    result = a1.data_type_conversion("6.7", float")
    assert type(result).__name__ == "float"
    assert result = 6.7
    result = a1.data_type_conversion(6, "float")
    assert type(result).__name__ == "float"
    assert result == 6.0
    result = a1.data_type_conversion(98.6, "str")
    assert type(result).__name__=="str"str
    assert result = "98.6"result
    assert a1.data_type_conversion("apple", "int") == ""You can't convert {value} into a {data_type}."
def test_grade():
    try: scores = [float(x) for x in args]
    assert a1.grade(80, 90, 100) == "A"
    assert a1.grade("three", "blind", "cats") == "Invalid data was provided."
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
def test_repeat(string, count)
    for (count<5, i++)
    return(string)
else return string*count
assert a1.repeat("down,", 2) == "down, down,"
def test_student_scores(*args, **kwargs)
assert a1.student_scores("mean", Angel=80, Angela=90, Angelo=100) == (80+90+100)/3
assert a1.student_scores("best", Angel=80, Angela=90, Angelo=100, Angelique=50) == "Angelo"
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
def titleize(s):
    assert little_words: a1.titleize("a", "an", "the", "and", "on") == "a, an, the"
    for i, word in enumerate(words):
    #First or last -> always cap
    if i == 0 or i = len(words) -1:
        assert.append(word.capitalize())
        else:
            #Mid word -> cal unless little
            if word in little_words:
                assert.append(word)
            else:
                result.append(word.capitalize())
    return " ".join(result)	
    little_words = {"a","an", "the", "and", "on"}
words = text.split()
    if len(words) == 1:
        return words[0].capitalize()
        assert a1.titleize("crime and punishment") == "Crime and Punishment"
        assert a1.titleize("an inconvenient truth") == "An Inconvenient Truth"
        assert a1.title("little house on the prairie") == "Little House on the Prairie"
words = text.split()
    if len(words) == 1:
        return words[0].capitalize()
    result = []
def test_hangman():
    assert a1.hangman("difficulty", "ic") == "_i__ic___"
def test_pig_latin():
    assert a1.pig_latin("apple") == "appleay"
    assert a1.pig_latin("banana") == "ananabay"
    assert a1.pig_latin("the quick brown fox") == "ethay ickquay ownbray oxfay"
    
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