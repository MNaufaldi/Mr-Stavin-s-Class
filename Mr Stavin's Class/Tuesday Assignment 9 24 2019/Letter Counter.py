#Letter counter
def letter_counter(word):
    result_list_letter = []
    result_list_count = []
    for index in range(len(word)):
        if word[index] not in result_list_letter:
            result_list_letter.append(word[index])
            result_list_count.append(1)
        else:
            for letter in range(len(result_list_letter)):
                if result_list_letter[letter] == word[index]:
                    result_list_count[letter] += 1
    for element_index in range(len(result_list_letter)):
        print(result_list_letter[element_index],"=",result_list_count[element_index])
    
                
input_list = input("Input a string: ")
letter_counter(input_list)