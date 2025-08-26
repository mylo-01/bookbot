

def get_num_words(text):
    num_words = len(text.split())
    #print(f"{num_words} words found in the document")
    return num_words

def get_character_dictionary(text):
    char_dic = {}
    for charz in text:
        char = charz.lower()
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic

def format_char_dic(char_dic):
    # Pasar de un diccionario gigante a una lista de diccionarios Key:Value
    char_dic_clean = {}
    for key, value in char_dic.items():

        if key.isalpha():
            char_dic_clean[key] = value

    # Organizar la lista de mayor a menor
    char_dic_sorted = sorted(char_dic_clean.items(), key = lambda item : item[1], reverse = True)

    # Dar formato al print
    for key, value in char_dic_sorted:
        print(f"{key}: {value}")
