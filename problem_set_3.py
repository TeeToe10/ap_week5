def problem3():
    # Problem Set 3: String Methods
    # Upper & Lower:
    # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
    phrase1 = "MAY THE FORCE BE WITH YOU"
    print("phrase1 Lowercase:", phrase1.lower())
    # String Joining and Splitting:
    # Given the list motto = ["Make", "haste", "slowly."],
    # a. Convert the list into a single string.
    motto = ["Make", "haste", "slowly."]
    sentence = " ".join(motto)
    split_sentence = sentence.split('a')
    # b. Now, split the string at every occurrence of the letter 'a'.