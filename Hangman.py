import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''')
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

end_of_game=False
difficulty=input("Choose your poison:\n(H for Hard, M for medium, E for easy)\n").lower()
hard=["gold","silver","platinum","bronze","abruptly","blizzard","jinx","pizza"]
medium=["hand","love","sweet","father","uncle","aluminium","buffalo","bunglow"]
easy=["mobile","rubber","doctor","evil","lively","dead","envelope","letter"]
if difficulty=="h":
  word_list=hard
elif difficulty=="m":
  word_list=medium
else:
  word_list=easy
chosen_name= word_list[random.randint(0,7)]
#print(f"{chosen_name}")
lenght_of_name=len(chosen_name)
answer=[]
lives=6
k=0
while k<lenght_of_name:
  answer+="_"
  k+=1
while not end_of_game:
  chosen_letter= input("Guess a letter:").lower()
  if chosen_letter in answer:
    print(f"You've already guessed the letter {chosen_letter}")
  a=0
  for letter in chosen_name:
    if letter==chosen_letter:
      answer[a]=chosen_letter
    a+=1
  if chosen_letter not in chosen_name:
    print(f"Your chosen letter {chosen_letter} is not in the word. You lose a life!!")
    lives-=1
  print(f"{answer}")
  print(stages[lives])
  if "_" not in answer:
    end_of_game=True
    print("You Win")
  if lives==0:
      end_of_game=True
      print("You lose")