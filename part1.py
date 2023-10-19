sum = 0
with open("input.txt", "r") as file:
    for line in file.readlines():

        first_list = line[:int(len(line)/2)]
        second_list = line[int(len(line)/2):]
        
        repeat = set(first_list).intersection(second_list)
        if repeat == {"a"}:
            sum += 1
        elif repeat == {"b"}:
            sum += 2
        elif repeat == {"c"}:
            sum += 3
        elif repeat == {"d"}:
            sum += 4
        elif repeat == {"e"}:
            sum += 5
        elif repeat == {"f"}:
            sum += 6
        elif repeat == {"g"}:
            sum += 7
        elif repeat == {"h"}:
            sum += 8
        elif repeat == {"i"}:
            sum += 9
        elif repeat == {"j"}:
            sum += 10
        elif repeat == {"k"}:
            sum += 11
        elif repeat == {"l"}:
            sum += 12
        elif repeat == {"m"}:
            sum += 13
        elif repeat == {"n"}:
            sum += 14
        elif repeat == {"o"}:
            sum += 15
        elif repeat == {"p"}:
            sum += 16
        elif repeat == {"q"}:
            sum += 17
        elif repeat == {"r"}:
            sum += 18
        elif repeat == {"s"}:
            sum += 19
        elif repeat == {"t"}:
            sum += 20
        elif repeat == {"u"}:
            sum += 21
        elif repeat == {"v"}:
            sum += 22
        elif repeat == {"w"}:
            sum += 23
        elif repeat == {"x"}:
            sum += 24
        elif repeat == {"y"}:
            sum += 25
        elif repeat == {"z"}:
            sum += 26
        elif repeat == {"A"}:
            sum += 27
        elif repeat == {"B"}:
            sum += 28
        elif repeat == {"C"}:
            sum += 29
        elif repeat == {"D"}:
            sum += 30
        elif repeat == {"E"}:
            sum += 31
        elif repeat == {"F"}:
            sum += 32
        elif repeat == {"G"}:
            sum += 33
        elif repeat == {"H"}:
            sum += 34
        elif repeat == {"I"}:
            sum += 35
        elif repeat == {"J"}:
            sum += 36
        elif repeat == {"K"}:
            sum += 37
        elif repeat == {"L"}:
            sum += 38
        elif repeat == {"M"}:
            sum += 39
        elif repeat == {"N"}:
            sum += 40
        elif repeat == {"O"}:
            sum += 41
        elif repeat == {"P"}:
            sum += 42
        elif repeat == {"Q"}:
            sum += 43
        elif repeat == {"R"}:
            sum += 44
        elif repeat == {"S"}:
            sum += 45
        elif repeat == {"T"}:
            sum += 46
        elif repeat == {"U"}:
            sum += 47
        elif repeat == {"V"}:
            sum += 48
        elif repeat == {"W"}:
            sum += 49
        elif repeat == {"X"}:
            sum += 50
        elif repeat == {"Y"}:
            sum += 51
        else:
            sum += 52
    print(sum)


                  
        
        
            

