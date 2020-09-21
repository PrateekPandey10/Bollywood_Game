import getpass
global name

print('lets play Bollywood \n')

quest= getpass.getpass('Enter the question keyword: \n')
hint= input("\n ENTER A HINT FOR THE PLAYER: \n")
print('\n The Hint is:' hint '\n')
moviename= str(quest)
listword= list(quest.lower())
#take hidden input from user and store the value in a list


name= 'Bollywood'
bolly= list(name)
print('Movie length is', len(quest), 'words')

while bolly != []:
  taken= input('\n Enter the letter to check:    ')
  check= taken.lower()

  if check in listword:
    listword.remove(check)
    print('\n ******That was correct, ', len(listword), 'letters remaining*****  \n')
    print('\n', bolly, '\n')
    if len(listword)==0:
      print('\n YOU WON')
      print('\n Movie name was', moviename)
      break
  
  elif check not in listword:
    
    del bolly[0]
    print('\n ******Wrong guess',len(listword), 'letters remaining******* \n')
    print('\n', bolly, '\n')
    if bolly== []:
      print('\n YOU LOST')
      print('\n Movie name was', moviename)
      break
