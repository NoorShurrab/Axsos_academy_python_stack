# Function Intermediate_2 Documentation
### 1. Updating Values in Nested Structures
This question shows how to access and modify data deep within a structure using a combination of Indexes (for lists) and Keys (for dictionaries).

    - Nested List: x[1][0] = 15 (Changes 10 to 15 in the sub-list).
    - List of Dictionaries: students[0]["last_name"] = "Bryant" (Updates a specific value in an object).
    - Dictionary of Lists: sports_directory['soccer'][0] = "Andres" (Targets an element within a list that is stored as a dictionary value).

### 2. Iterating Through a List of Dictionaries
The iterateDictionary(some_list) function demonstrates how to loop through a list of objects and print their contents.

    -  It iterates through each dictionary.
    -  It uses an inner loop to retrieve keys and values.
    -  It dynamically builds a string using f-strings to ensure correct comma placement.

### 3. Get Values From a List of Dictionaries
The iterateDictionary2 function allows one to isolate and print only the values associated with a specific key across an entire list of dictionaries.

    - key_name: The specific dictionary key you wish to display (e.g., 'first_name').
    - some_list: The target list containing the dictionary records.

### 4. Iterate Through a Dictionary with List Values
The printInfo(some_dict) function handles a dictionary where every value is a list (e.g., a "Dojo" with multiple locations and instructors).

    - It calculates the length of each list.
    - Prints the count and the key in uppercase.
    - Iterates and prints every item within those lists.


