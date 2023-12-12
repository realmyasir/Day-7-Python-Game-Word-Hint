import random

word_list=['yasir','iqbal','aon','asim','ibrahim','ali','john', 'jane', 'Bob', 'Alice']

chosen_word=random.choice(word_list)

print(f'Pssst, The Solution is  {chosen_word}')

display=[]
word_length=len(chosen_word)
for _ in range(word_length):
    display+='_'
print(display)
end_of_game=False
while not end_of_game:
    guess=input('Guess a latter:').lower()

    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
                display[position]=letter
   
    print(display)

    if '_' not in display:
         end_of_game=True
         print('You Win')



