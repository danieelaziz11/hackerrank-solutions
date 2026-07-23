def solve(s):
    string = s.split(" ")
    
    for i in range (len(string)):
        string[i]= string[i].capitalize()
    
    return " ".join(string)    

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
