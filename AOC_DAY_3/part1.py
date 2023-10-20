dict = {}
sum =0
with open("input.txt", "r") as file:
    for line in file.readlines():

        first_string = line[:int(len(line)/2)]
        second_string = line[int(len(line)/2):]
        
    
        for i in first_string:
            if i not in dict and 'A' <= i <= 'Z':
                dict[i] = ord(i) - 38
            elif i not in dict and 'a' <= i <= 'z':
                dict[i] = ord(i) - 96

        for i in first_string:
            if i in second_string:
                sum += dict[i]
                break

            

    print(dict)
    print(sum)
        
    

    # de refacut cu hash


                  
        
        
            

