def most_frequent(text):
    """
    Takes a string and prints the letters in decreasing order of frequency.
    """
    # Create a dictionary to store the frequency of each letter
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    # Sort the dictionary by value in descending order
    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Print the letters and their frequency in the desired format
    for item in sorted_dict:
        print(f"{item[0]} = {item[1]:02}")