print("Welcome")

playing = input("Do you want to play??")

if playing !="yes":
    quit()

print("Okay! Let's start the game :")
score = 0

answer = input("Is KNN a supervised learning algorithm?")
if answer == "yes":
    print("correct")
    score += 1
else:
    print("wrong")

answer = input("Does KNN require labeled data during training?")
if answer == "yes":
    print("correct")
    score += 1
else:
    print("wrong")

answer = input("Is K-Means a clustering algorithm?")
if answer == "yes":
    print("correct")
    score += 1
else:
    print("wrong")

answer = input("Does K-Means aim to minimize the within-cluster sum of squared distances?")
if answer == "yes":
    print("correct")
    score += 1
else:
    print("wrong")


answer = input("Is K-Means sensitive to the initial placement of centroids?")
if answer == "yes":
    print("correct")
    score += 1
else:
    print("wrong")


answer = input("Is KNN suitable for regression tasks?")
if answer == "yes":
    print("correct")
    score += 1
else:
    print("wrong")


answer = input("Does K-Means require a pre-defined number of clusters (K)?")
if answer == "yes":
    print("correct")
    score += 1
else:
    print("wrong")


answer = input("Does unsupervised learning use labeled data for training?")
if answer == "no":
    print("correct")
    score += 1
else:
    print("wrong")


answer = input("Is feature scaling important for K-Means clustering?")
if answer == "yes":
    print("correct")
    score += 1
else:
    print("wrong")


answer = input("Does KNN make assumptions about the underlying data distribution?")
if answer == "no":
    print("correct")
    score += 1
else:
    print("wrong")


                              


print("Congratulations!!! You got " + str(score ) + " marks.")