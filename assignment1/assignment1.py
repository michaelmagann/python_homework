# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"

# Task 3
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4
def data_type_conversion(value,data_type):
    try:
       if data_type == "float":
            return float(value)
       elif data_type == "int":
            return int(value)
       elif data_type == "str":
            return str(value)
       else:
            return f"Unsupported data type: {data_type}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
    
#Task 5

def grade(*args):
    try: 
        # Make sure there is at least one value
        if len(args) == 0:
            return "Invalid data was provided."
        
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
    except Exception:
        return "Invalid data was provided."
    
#Task 6

def repeat(text, count):
    result = ""
    for _ in range(count):
        result += text
    return result

#Task 7

def student_scores (option, **kwargs):
   if not kwargs:
        return None
   if option == "best":
       best_student = None
       highest_score = float('-inf')

       for name, score in kwargs.items():
           if score > highest_score:
               highest_score = score
               best_student = name
       return best_student
   
   elif option =="mean":
       total = 0
       count = 0

       for score in kwargs.values():
            total += score
            count += 1
       return total / count 
    
   else:
        return None
   
#Task 8

def titleize(text):
    little_words = {"a", "an", "the", "on", "of", "is", "in", "and"}

    words = text.split()

    for i, word in enumerate (words):
        # Always capitalize the first and last word
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        # Capitalize if the word is not a little word
        elif word.lower() not in little_words:
            words[i] = word.capitalize()
        else:            
            words[i] = word.lower()
    
    return " ".join(words)

#Task 9

def hangman(secret, guess):
    result = ""
    
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

#Task 10

def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result =  []    

    for word in words:
        # Case 1: starts with a vowel
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word):
                # Handle "qu" as a unit
                if word[i:i+2] == "qu":
                    i += 2
                    break
                elif word[i] in vowels:
                    break
                else:
                    i += 1
            
            result.append(word[i:] + word[:i] + "ay")   

    return " ".join(result)
