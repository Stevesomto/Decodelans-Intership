#this is the 4 task

score = 0

question = input("What is the capital of France? ")

if question.lower() == "paris":
    print ("You got it")
    score += 1
else:
    print ("Wrong answer. The correct answer is Paris.")

question = input("What is the capital of Nigeria? ")

if question.lower() == "abuja":
    print ("You got it")
    score += 1
else:
    print ("Wrong answer. The correct answer is Abuja.")
    
    
question = input("What is the capital of Ghana? ")

if question.lower() == "accra":
    print ("You got it")
    score += 1
else:
    print ("Wrong answer. The correct answer is Accra.")


print(f"Your score is {score}/3")