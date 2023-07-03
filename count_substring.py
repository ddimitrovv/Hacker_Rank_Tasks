def count_substring(string, sub_string):
    len_string = len(string)
    len_substring = len(sub_string)
    i = 0
    counter = 0
    while(i < len_string):
        if(string[i] == sub_string[0]):
            if(string[i:i + len_substring] == sub_string):
                counter += 1
        i += 1

    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)