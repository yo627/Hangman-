import random
word_list=[    "apple", "banana", "orange", "grape", "lemon",
    "coffee", "school", "friend", "window", "mirror",
    "python", "rocket", "planet", "camera", "future",
    "water", "chair", "table", "music", "guitar",
    "jacket", "laptop", "forest", "desert", "ocean"]
filtered_words=[word for word in word_list if len(word)==5]
secret_word=random.choice(filtered_words)
display=["_"]*5
hearts=6
while hearts!=0 and "".join(display)!=secret_word:
    guessed_letter=input(f"Guess a letter from the secret word {"".join(display)}").lower()
   
    if guessed_letter in secret_word :
           for i in range(5):
                if guessed_letter==secret_word[i]:
                   display[i]=secret_word[i]
                   print("".join(display))
          
    else: 
        hearts-=1
        print(f"Now, you have {hearts} hearts")
if  "".join(display)!=secret_word:
    print("Congartulations! you won ")
    
else :
        print("******Game Over!******* ")   import random

