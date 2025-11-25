def get_num_words(f):
    return len(f.split())
        #file_num_words = len(f.read().split())
    #return f"Found {file_num_words} total words."

def get_char(text_string):
    new_dict = {}
    text_as_list = text_string.lower()
    #text_as_list = list(text_as_list)
    for char in text_as_list:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict

def sorted_dict(new_dict):
    unsorted_dict_list = []    
    
    dict_list = list(new_dict.items())
    for i in range(0,len(dict_list),1):
        temp_new_dict = {}
        temp_key = dict_list[i][0]
        temp_value = dict_list[i][1]
        temp_new_dict["char"] = temp_key
        temp_new_dict["num"] = temp_value
        unsorted_dict_list.append(temp_new_dict)
        
    unsorted_dict_list.sort(reverse=True, key=sort_on)
    return unsorted_dict_list
    #print(sorted_dict)
    #return sorted_dict

def sort_on(unsorted_dict_list):
    #print(unsorted_dict_list["num"])
    return unsorted_dict_list["num"]
    #return unsorted_dict_list.values()