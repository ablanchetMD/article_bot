def main():    
    path_to_file = "articles/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path_to_file} ---")        
        print(f"{calc_words(file_contents)} words found in the document \n")
        dict = calc_letters(file_contents)        
        my_dict = list(dict)
        my_new_list =[]
        for item in my_dict:
            if item.isalpha() == True:
                my_new_list.append({'key':item,'num':dict[item]})
        
        my_new_list.sort(reverse=True,key=sort_on)       
        for char in my_new_list:
            print(f"The '{char['key']}' character was found {char['num']} times")
        print(f"--- End report ---")       
        
def sort_on(dict):
    return dict['num']


def calc_words(str):
    words = str.split()
    return len(words)

def calc_letters(str):
    words = str.split()
    dict = {}
    for i,word in enumerate(words):
        for letter in word.lower():
            dict[letter] = dict.get(letter,0) + 1            
    return dict

main()