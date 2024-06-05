from PIL import Image
import os
import shutil
import time
import random
import pygame as pg

pg.mixer.init()
get_hyped = pg.mixer.Sound("TTT_Body\Olympics - Basic Theme and Fanfare.ogg")
brightside = pg.mixer.Sound("TTT_Body\Monty Python - Always Look on the Bright Side of Life.ogg")
roman_march = pg.mixer.Sound("TTT_Body\Roman March.wav")
background_music = pg.mixer.Sound("TTT_Body\Vangelis - Chariots of Fire.wav")

Folderpath = r'TTT'

path = "C:\\Users\\Isaac\\Intro To Python\\TTT"

def maker(colour, path, location="default"):
    # Define the dimensions of the image
    width, height = 100, 100  # You can change these values as needed
    
    # Color mapping

COLOR_MAP = {
    "black": "#000000",
    "white": "#F9F2EB",
    "background": "#00008B",
    "good": "#385143",
    "bad": "#da4b4b",
    "olympic_blue": "#0286c3",
    "olympic_yellow": "#fbb22e",
    "olympic_black": "#000000",
    "olympic_green": "#168c39",
    "olympic_red": "#ee2f4d",
    "head": "#E3B778",
    "body": "#E3B778",
    "shoe": "#D5B85A",
    "sky": "#87CEEB",
    "ground1": "#654321",
    "ground2": "#8B4513",
    "ground3": "#5C4033",
    "ground4": "#5C4033",
    "cloud": "#D3D3D3",
    "crowd1": "#696969",
    "crowd2": "#708090",
    "crowd3": "#2F4F4F",
    "crowd4": "#36454F",
    "cross": "#3E2723"
}

def maker(color, path, location="default"):
    if color not in COLOR_MAP:
        raise ValueError("Invalid color.")
    width, height = 100, 100
    image_color = COLOR_MAP[color]
    image = Image.new("RGB", (width, height), image_color)
    filename = os.path.join(path, f"{location}.png")
    image.save(filename)

def main():
    # clear the board
    clear() 
    # welcome the player on the inline interface
    print("Welcome to TTT,")
    # Homescreen
    homescreen() 
    # set the board
    set()
    # detector find
    background_music.play()
    play()
    background_music.stop()
    #clear
    clear()
    # conclusion
    if detectwin == True:
        while playagain != True or playagain != False:
            winniner_animation() # crowd runs after bryan
            playagain_decision()
            clear()
        if playagain == True:
            winner_returns_animation() # bryan gets caught by roman gaurds
            main()
        elif playagain == False:
            winner_dies_animation() # bryan trampled by the crowd
            clear()

    elif detectwin == False:
        while playagain != True or playagain != False:
            looser_animation() # walk with cross to the crucifiction site
            playagain_decision()
            clear()
        if playagain == True:
            looser_returns_animation() # walk back with cross in hand
            main()
        elif playagain == False:
            looser_dies_animation() # always look on the bright side of life
            clear()

def clear():
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)  

def homescreen():
    get_hyped.play()
    for j in range(1, 9):
        for i in range(1, 9):
            location = str(i) + str(j)
            if i == 2 and j == 2 or i == 3 and j == 2 or i == 2 and j == 3 or i == 3 and j == 3:
                colour = 'olympic_blue'
            elif i == 4 and j == 3 or i == 4 and j == 4 or i == 5 and j == 3 or i == 5 and j == 4:
                colour = 'olympic_yellow'
            elif i == 2 and j == 4 or i == 2 and j == 5 or i == 3 and j == 4 or i == 3 and j == 5:
                colour = 'olympic_black'
            elif i == 4 and j == 5 or i == 4 and j == 6 or i == 5 and j == 5 or i == 5 and j == 6:
                colour = 'olympic_green'
            elif i == 2 and j == 6 or i == 2 and j == 7 or i == 3 and j == 6 or i == 3 and j == 7:
                colour = 'olympic_red'
            else:
                colour = 'white'
            maker(colour, path, location)  
    play_type = input("Choose you Faction \n1.The Peoples front of Judea (Singleplayer)\n2.The Judeans People Front (Multiplayer)\n")
    get_hyped.stop()
    clear()
    
def set():
    for j in range(1, 9):
        for i in range(1, 9):
            location = str(i) + str(j)
            if i == 3 or i == 6 or j == 3 or j == 6:
                colour = 'black'
            else:
                colour = 'white'
            maker(colour, path, location)

def play():
    #while game win finish is false search for a valid input and if valid input is detected then mark computer input if invalid input detected then do nothing
    print("Let the games commence: ")
    Game = True
    time.sleep(10)
    Game = False

def winniner_animation():
    print("You are the winner, however a giant horde of people run after you they think you are the messiah")
    for t in range(8):
        for j in range(1, 9):
            for i in range(1, 9):
                location = str(i) + str(j)
                # Head animation part 1
                if i == 4 and (j == 8 - t):
                    colour = 'head'
                # Body animation part 1
                elif i == 5 and (j == 8 - t):
                    colour = 'body'
                # Foot forward animation
                elif i == 6 and j == 8 - t:
                    colour = 'shoe'
                elif i == 7 or i == 8:
                    colour = "ground" + str(random.randint(1, 4))
                elif  i == 3 and (j == 4 or j == 3 or j == 2):
                    colour = 'cloud'
                elif i == 2 and (j == 5 or j == 4 or j == 3):
                    colour = 'cloud'
                else:
                    colour = 'sky'

                maker(colour, path, location)

        time.sleep(1.5)
        t += 1

def winner_returns_animation():
    roman_march.play()
    print("You are taken by the romans to fight in the arena again")
    for t in range(8):
        for j in range(1, 9):
            for i in range(1, 9):
                location = str(i) + str(j)
                # Head animation part 1
                if i == 4 and (j == t):
                    colour = 'head'
                # Body animation part 1
                elif i == 5 and (j == t):
                    colour = 'body'
                # Foot forward animation
                elif i == 6 and j == t:
                    colour = 'shoe'
                elif (i == 4 or i == 5 or i == 6) and (j == t - 1 or j == t + 1 or j == t + 3 ):
                    colour = 'olympic_red'
                elif i == 7 or i == 8:
                    colour = "ground" + str(random.randint(1, 4))
                elif  i == 3 and (j == 4 or j == 3 or j == 2):
                    colour = 'cloud'
                elif i == 2 and (j == 5 or j == 4 or j == 3):
                    colour = 'cloud'
                else:
                    colour = 'sky'

                maker(colour, path, location)

        time.sleep(1.5)
        t += 1

def winner_dies_animation():
    print("You were run over by a hoard of people that were following you")
    for t in range(8):
        for j in range(1, 9):
            for i in range(1, 9):
                location = str(i) + str(j)
                # Head animation part 1
                if (i == 4 or i == 5 or i == 6) and (j >= 8 - t):
                    colour = "crowd" + str(random.randint(1, 4))
                elif i == 4 and (j == 4):
                    colour = 'head'
                # Body animation part 1
                elif i == 5 and (j == 4):
                    colour = 'body'
                # Foot forward animation
                elif i == 6 and j == 4:
                    colour = 'shoe'
                elif i == 7 or i == 8:
                    colour = "ground" + str(random.randint(1, 4))
                elif i == 3 and (j == 4 or j == 3 or j == 2):
                    colour = 'cloud'
                elif i == 2 and (j == 5 or j == 4 or j == 3):
                    colour = 'cloud'
                else:
                    colour = 'sky'

                maker(colour, path, location)

        time.sleep(1.5)
        t += 1  # Incrementing t inside the outer loop

def looser_animation():
    print("You lose, dont worry its only your first offecnce will lwt you off lightly with crucifiction")
    for t in range(8):
        for j in range(1, 9):
            for i in range(1, 9):
                location = str(i) + str(j)
                # Head animation part 1
                if i == 4 and (j == 8 - t):
                    colour = 'head'
                # Body animation part 1
                elif i == 5 and (j == 8 - t):
                    colour = 'body'
                # Foot animation
                elif i == 6 and j == 8 - t:
                    colour = 'shoe'
                if i == 4 and (j == 9 - t):
                    colour = 'cross'
                # Body animation part 1
                elif i == 5 and (j == 10 - t):
                    colour = 'cross'
                # Foot forward animation
                elif i == 6 and j == 11 - t:
                    colour = 'cross'
                elif i == 7 or i == 8:
                    colour = "ground" + str(random.randint(1, 4))
                elif  i == 3 and (j == 4 or j == 3 or j == 2):
                    colour = 'cloud'
                elif i == 2 and (j == 5 or j == 4 or j == 3):
                    colour = 'cloud'
                else:
                    colour = 'sky'

                maker(colour, path, location)

        time.sleep(1.5)
        t += 1  

def looser_returns_animation():
    roman_march.play()
    print("You are taken down from the cross by the romans to fight in the arena again")
    for t in range(8):
        for j in range(1, 9):
            for i in range(1, 9):
                location = str(i) + str(j)
                # Head animation part 1
                if i == 4 and (j == t):
                    colour = 'head'
                # Body animation part 1
                elif i == 5 and (j == t):
                    colour = 'body'
                # Foot forward animation
                elif i == 6 and j == t:
                    colour = 'shoe'
                elif (i == 4 or i == 5 or i == 6) and (j == t - 1 or j == t + 1 or j == t + 3 ):
                    colour = 'olympic_red'
                elif i == 7 or i == 8:
                    colour = "ground" + str(random.randint(1, 4))
                elif  i == 3 and (j == 4 or j == 3 or j == 2):
                    colour = 'cloud'
                elif i == 2 and (j == 5 or j == 4 or j == 3):
                    colour = 'cloud'
                else:
                    colour = 'sky'

                maker(colour, path, location)

        time.sleep(1.5)
        t += 1

def looser_dies_animation():
    brightside.play()
    for j in range(1, 9):
        for i in range(1, 9):
            location = str(i) + str(j)
            if i == 7 or i == 8:
                colour = "ground" + str(random.randint(1, 4))
            elif j == 1 or j == 8:   
                colour = 'sky'
            elif j == 4 or j == 5:
                colour = 'cross'
            elif i == 3 or i == 4:
                colour = 'cross'
            else:
               colour = 'sky'
            maker(colour, path, location)
    print("You Die, Always look on the bright side of life: ")

    time.sleep(300)

def scaler():
    os.startfile(Folderpath)
    for j in range(1, 9):
        for i in range(1, 9):
            location = str(i) + str(j)
            if i == j:
                colour = 'black'
            elif i == 9 - j:
                colour = 'black'
            else:
                colour = 'white'
            maker(colour, path, location) 
    x = input("\nOpen the file TTT folder adjacent to the terminal \nScale the window until you see the cross \nWe recomend to use the largest file preview that still allows you to still preview the PNG \nDo you see a black cross: ")

def detector(Game):
    if Game == True:
        print("ice")

def playagain_decision():
    x = input("Would you like to play agian: ")
    y = x.strip()
    if y.lower == "yes" or "ok" or "sure" or "okay" or "y":
        playagain = True
    else:
        playagain = False

detectwin = False

playagain = False

Game = False

scaler()
detector(Game)
main()