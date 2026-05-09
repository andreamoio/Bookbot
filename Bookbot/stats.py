def counting(text):
    
    single_words = text.split()
    counter = len(single_words)
            
    return counter

def character_counter(text): 

    my_dictionary = {}

    for character in text: 

        character = character.lower()
        
        if character in my_dictionary:
            my_dictionary[character] = my_dictionary[character] +1

        else: 
            my_dictionary[character] = 1

    return my_dictionary


def sort_list(my_dictionary):
    
    return my_dictionary["num"]

def real_function(my_dictionary):

    new_list =[]

    for item in my_dictionary: 

        new_list.append({"char": item, "num": my_dictionary[item]})

    new_list.sort(reverse = True, key = sort_list)
    return new_list



