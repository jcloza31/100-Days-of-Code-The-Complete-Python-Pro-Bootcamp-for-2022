# This need to be run via repl.it

from replit import clear

dragon = """

                                                       ____________
                                 (`-..________....---''  ____..._.-`
                                  \\`._______.._,.---'''     ,'
                                  ; )`.      __..-'`-.      /
                                 / /     _.-' _,.;;._ `-._,'
                                / /   ,-' _.-'  //   ``--._``._
                              ,','_.-' ,-' _.- (( =-    -. `-._`-._____
                            ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.
             _          |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
  _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._
,',)---' /|)          `     `      ``-.   `     /     /     `     `-.
\_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.
 \_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
           `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__
                   ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______   SSt
                                                      ``--------..._``--.__

"""

skull = """
          ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------` 
"""

print(dragon)
print("Welcome to the Game of Thrones.")
print("Your mission is to kill the Night King") 

family = input("You are going to choose between two families who will be with you to fight the Night King. \n On the left are The Starks and on the right are the Lannisters. \n Which one will you choose? 'Starks' or 'Lannisters?' ").lower()
if family == "starks":
    clear()
    print(dragon)
    beast = input("You made the right decision! \n John Snow will help you to fight the Night King together with Daenerys Targaryen. \n  They offered you to bring a beast. Choose between 'Wolf' or 'Dragon'? ").lower()
    if beast == "wolf":
        clear()
        print(dragon)
        war_strategy = input("You are now with John's Snow Wolf 'Ghost' in front of the White Walkers and the Night King. \n This is the final battle! Choose your war strategy: \n'You will kill the Night King by yourself' , \n or 'Let Arya handle the Night King', \n or 'Ask Daenerys to use Dragon's Fire Breath to the King', \n or 'Ask John Snow to have a sword fight by the Night'? \n Who do you want to kill the Night King? \n 'Yourself(please type 'I')', 'Arya', 'Daenerys', or 'Jon' ").lower()
        if war_strategy == 'i':
            clear()
            print("You run into to the white walkers. Unfortunately, they are really alot. \n You died from the battle and turned into a White Walker. \n You lost the game of thrones.")
            print(skull)
        elif war_strategy == 'arya':
            clear()
            print(dragon)
            print("Arya was able to assassinate the Night King thru his heart. \n The White Walkers turned into ashes. You won the Game of thrones!")
        elif war_strategy == 'daenerys':
            clear()
            print("Daenerys found out that the Night King is immune to dragon fire. \n The Night King fights back and killed Daenerys and her dragon. \n You lost the Game of Thrones")
            print(skull)
        elif war_strategy == "jon":
            clear()
            print("John Snow Strength is no match to the Night King. \n He became exhausted and wasn't able to stand up. \n The Night King killed him and turned him into a White Walker. You lost the Game of Thrones.")
            print(skull)  
        else:
            print("Idiot! Restart the game and choose between the selection")

        
    elif beast == "dragon":
        clear()
        print("Drogon doesn't like you when you rode his back.\n Unfortunately, you fell from the sky and you died. You lost the Game of Thrones")
        print(skull)
    else:
        print("Idiot! Restart the game and choose between the selection")
elif family == "lannisters":
    clear()
    print("You chose to side with Cercei. \n While you were sleeping, she commanded the 'Mountain' to kill you while you were sleeping. \n You lost the Game of Thrones")
    print(skull)
else: 
    print("Idiot! Restart the game and choose between the selection")
    
    



#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

