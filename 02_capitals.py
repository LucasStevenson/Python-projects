with open("statesncapitals.txt") as f: # Opening the file
    line = f.readline() # This reads the first line of txt file into line variable
    dictionary = {}
    while line: #iterating through the entire text file
        result = line.strip().split(", ")
        dictionary[result[0].lower()] = result[1].lower()
        line = f.readline() #reads second line of txt file into line and beyond

inverted_dict = inv_map = {v: k for k, v in dictionary.items()}

while True:
    answer = input("Ready: ").lower()
    if answer == "done":
        exit()
    elif answer in dictionary:
        print(dictionary[answer])
    elif answer in inverted_dict:
        print(inverted_dict[answer])
    else:
        print("Key isn't valid")
 
#dictionary["five"] = "six" 
# readline = get line 
# After that, strip line of newline 
# After that, split by comma (This will create an array) 
# Put state in key, capital as value 
# Have a full dict

# while true 
# if answer = "done" => exit 
# if answer = "state" => return state capitol 

# if answer = "state capitol => return state BONUS: Do this later
# Bonus: Switch key and values and create second dict without mutating the first
# Or you can be really lazy and just use a finder function in dictionary.values  



