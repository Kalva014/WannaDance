# Additional libraries
import random
import requests

# Capactive Sensor 
import time
import board
from random import *
import busio
import adafruit_mpr121
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# THIS IS FOR THE LED SCREEN
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c) # Create the SSD1306 OLED class.
oled.fill(0)
oled.show()
image = Image.new("1", (oled.width, oled.height)) # Create blank image for drawing.
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)

# Spotify Setup
import json
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyOAuth
username = '12169592626'
clientID = '68991d183c0f42c383c005bef367014f'
clientSecret = '6961ade3b8e44d67af0f743d95f1c59f'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
device_id = '1ccefd1dec8aef8e9b81cf247b4a68fb236b1717'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
client_secret=clientSecret, redirect_uri=redirect_uri, scope="user-read-playback-state,user-modify-playback-state"))


# # LED LIGHT STRIP
# import qwiic_led_stick
# my_stick = qwiic_led_stick.QwiicLEDStick()
# red_list = [214, 78, 183, 198, 59, 134, 15, 209, 219, 186]
# green_list = [59, 216, 170, 21, 114, 63, 226, 92, 155, 175]
# blue_list = [214, 147, 25, 124, 153, 163, 188, 33, 175, 221]

# The specific capacitive sensors(aka the tiles) that will light up and need to be stepped on
column = [0,1,2,3,4,5,6,7,8,9,10,11]
plug_ips = ["192.168.0.138", "192.168.0.141", "192.168.0.181"]

# Players' points
player1 = 200
player2 = 200
rounds_lasted = 0

sleep_time = 5

# String inputted will be displayed to the LCD Screen
def displayToLCD(strToDisplay,font_size=12):
    # LED SCREEN
    oled.fill(0) # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
    draw.text((0, 0), strToDisplay, font=font, fill=255) # SET THE LED SCREEN
    oled.image(image) # Display image
    oled.show() # show all the changes we just made

# Checks if user stepped on a tile and gives them points if they did
def checkColumn(dance_columns):
    global player1
    global player2
    global sleep_time
    
    time.sleep(sleep_time) # Give users time to step on a tile 

    # Player 1 Check Columns
    if mpr121[dance_columns[0]].value == True and mpr121[dance_columns[1]].value == True:
        #print("Hitting both columns")
        player1 += 0
    elif mpr121[dance_columns[0]].value == True and mpr121[dance_columns[1]].value == False:
        #print("Only hitting one columns")
        player1 -= 10
    elif mpr121[dance_columns[0]].value == False and mpr121[dance_columns[1]].value == True:
        #print("Only hitting one columns")
        player1 -= 10
    else:
        player1 -= 20
    
    # Player 2 Check Columns
    if mpr121[dance_columns[2]].value == True and mpr121[dance_columns[3]].value == True:
        #print("Hitting both columns")
        player2 += 0
    elif mpr121[dance_columns[2]].value == True and mpr121[dance_columns[3]].value == False:
        #print("Only hitting one columns")
        player2 -= 10
    elif mpr121[dance_columns[2]].value == False and mpr121[dance_columns[3]].value == True:
        #print("Only hitting one columns")
        player2 -= 10
    else:
        player2 -= 20

    
    if(sleep_time > 1):
        sleep_time -= 0.3


# Generates two random tiles that both players have to step on
def randomColumn():
    return randint(1, 3)

# Main game loop ran here
def game():
    global player1
    global player2
    global rounds_lasted
    incr = 0
    prev_plug = None
    rounds_lasted = 0
    player1 = 200
    player2 = 200
    while True:
        displayToLCD(f"Player 1 score: {player1} \n Player 2 score: {player2}" )
        # my_stick.set_all_LED_color(214, 0, 0)

        rand_column = randomColumn()
        dance_columns = [(rand_column*2)-2,(rand_column*2)-1, 11 - ((rand_column*2)-2), 11 - ((rand_column*2)-1)] # [First player tile, First player tile, second player tile, second player tile]
        #print(f"Rand column: {rand_column}")

        if rand_column == 1:
            plug_to_turn = plug_ips[0]
        elif rand_column == 2:
            plug_to_turn = plug_ips[1]
        else:
            plug_to_turn = plug_ips[2]

        #print(f"Plug to turn: {plug_to_turn}")
        ## TURN OFF PREVIOUS ROUND COLUMN IF NOT FIRST ROUND
        if prev_plug != None:
            # api-endpoint
            
            URL = "http://"+ prev_plug +"/cm?cmnd=Power%20TOGGLE"
            #print(f"Prev URL: {URL}")
            # sending get request and saving the response as response object
            r = requests.get(url = URL)
            # extracting data in json format
            data = r.json()
        

        ## TURN ON THIS ROUNDS COLUMN

        # api-endpoint
        URL = "http://"+ plug_to_turn +"/cm?cmnd=Power%20TOGGLE"

        #print(f"Current URL: {URL}")
        # sending get request and saving the response as response object
        r = requests.get(url = URL)
        # extracting data in json format
        data = r.json()

        prev_plug = plug_to_turn
        
        checkColumn(dance_columns)
        incr += 1
        rounds_lasted += 1
        #print(f"Increment: {incr}")

        if player1 <= 0 and player2 <= 0:
            return "Game over players! \n Rounds lasted: " + str(rounds_lasted)
        if player1 <= 0 and player2 > 0: 
            return "Game over player 1! \n Rounds lasted: " + str(rounds_lasted)
        if player1 > 0 and player2 <= 0: 
            return "Game over player 2! \n Rounds lasted: " + str(rounds_lasted)

# Wait for two users to step on a tile 3 times 
def checkIfGameStarted():
    steps_on_tile = 0
    incr = 0
     
    while steps_on_tile < 3:
        displayToLCD("Wanna Dance?")
        incr += 1
        #print(f"Increment: {incr}")
        for i in range(12): 
            if mpr121[i].value == True:
                steps_on_tile += 1
                print("Number of times stepped on the same tile: " + str(steps_on_tile))
            time.sleep(0.2)
        

# Game initialization and ending done here
def main():
    # LED LIGHT STRIP SETUP
    # if my_stick.begin() == False:
    #     print("\nThe Qwiic LED Stick isn't connected to the system. Please check your connection", file=sys.stderr)
    #     return
    # print("\nLED Stick ready!")

    # Wait for users to step on squares
    while True:
        checkIfGameStarted()
        
        # Start music from wanna dance playlist
        print(json.dumps(user_name, sort_keys=True, indent=4))
        sp.shuffle(True, device_id)
        sp.start_playback(device_id, context_uri="spotify:playlist:2t7Z3HHMczgUN3Bc2dch5L")
        ## HERE WE NEED TO turn on plug 3 which should correspond to the main lights
        # Start the game
        winner = game()
        
        # Show game results on LCD
        sp.pause_playback(device_id) # Stop music from playing
        displayToLCD(winner,10)
        time.sleep(10)
        displayToLCD("Resetting")
        steps_on_tile = 0
        incr = 0

if __name__ == "__main__":
    main()
