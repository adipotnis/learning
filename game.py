# Write your code here
import random
winning = {}
num_2_word = []

def dictmaker(listofnames):
    winninglist = dict()
    for indexof in range(len(listofnames)):

        ans = listofnames[indexof+1:]     # to the right
        ans.extend(listofnames[:indexof])     #complete = to the right + to the left added to list

        winninglist[listofnames[indexof]] = set(ans[:int(len(ans)/2)])          # winning set

    return winninglist



#print('Enter your name: > ')
username = input('Enter your name: > ')
print('Hello, {}'.format(username))
num_2_word = input().split(',')

#print(len(num_2_word))
print("Okay, let's start")
if len(num_2_word) <= 1:
     winning = {'rock':{'paper'}, 'paper':{'scissors'}, 'scissors':{'rock'}}
     num_2_word = ['rock', 'paper', 'scissors']
else:
    winning = dictmaker(num_2_word)
    #print(winning)


game_score = 0      #value of score

# file to lists of name & score
open_score = open('rating.txt', 'r')
scorefile = open_score.read().split('\n')
full_list = [index.split() for index in scorefile]
name_list = [listrow[0] for listrow in full_list if len(listrow)==2]
scorelist = [int(listrow[1]) for listrow in full_list if len(listrow)==2]
open_score.close()

if username in name_list:
    for indexno in range(len(name_list)):
        if name_list[indexno] == username:
            game_score = scorelist[indexno]
            break
else:
    #append name to list
    indexno = len(name_list)
    name_list.append(username)
    scorelist.append(0)


# actual game
while True:

    compu = num_2_word[random.randint(0, len(num_2_word)-1)]

    user = input()

    if user == '!exit':
        print('Bye!')
        break

    elif user == '!rating':
        print('Your rating: ' + str(game_score))
        continue

    elif user not in num_2_word:
        print('Invalid input')
        continue


    elif user == compu:
        print('There is a draw ({})'.format(compu))
        game_score += 50

    elif compu in winning[user]:
        print('Sorry, but computer chose {}'.format(compu))

    else:
        print('Well done. Computer chose {} and failed'.format(compu))
        game_score += 100

#-------------------------------------------------------------------------
scorelist[indexno] = game_score
scorefile = []
indexno = 0
for indexno in range(len(name_list)):
    scorefile.append(name_list[indexno] + ' ' + str(scorelist[indexno]) +'\n')

open_score = open('rating.txt', 'w')
open_score.writelines(scorefile)
open_score.close()
