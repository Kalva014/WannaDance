# Additional libraries
import random

# Capactive Sensor 
import time
import board
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

# # LED LIGHT STRIP
# import qwiic_led_stick
# my_stick = qwiic_led_stick.QwiicLEDStick()
# red_list = [214, 78, 183, 198, 59, 134, 15, 209, 219, 186]
# green_list = [59, 216, 170, 21, 114, 63, 226, 92, 155, 175]
# blue_list = [214, 147, 25, 124, 153, 163, 188, 33, 175, 221]

# The specific capacitive sensors(aka the tiles) that will light up and need to be stepped on
tiles = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]

# Players' points
player1 = 0
player2 = 0

# String inputted will be displayed to the LCD Screen
def displayToLCD(strToDisplay):
    # LED SCREEN
    oled.fill(0) # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    draw.text((0, 0), strToDisplay, font=font, fill=255) # SET THE LED SCREEN
    oled.image(image) # Display image
    oled.show() # show all the changes we just made

# Checks if user stepped on a tile and gives them points if they did
def checkTile(tile_to_tap):
    global player1
    global player2

    time.sleep(5) # Give users time to step on a tile 
    if mpr121[tile_to_tap[0]].value == True and mpr121[tile_to_tap[1]].value == True:
        print("Player 1 and 2 get points")
        player1 += 10
        player2 += 10
    elif mpr121[tile_to_tap[0]].value == True and mpr121[tile_to_tap[1]].value == False:
        print("Player 1 gets points but not player 2")
        player1 += 10
    elif mpr121[tile_to_tap[0]].value == False and mpr121[tile_to_tap[1]].value == True:
        print("Player 2 gets points but not player 1")
        player2 += 10
    else:
        print("No one gets any points")

# Generates two random tiles that both players have to step on
def randomTile():
    return tiles[random.randint(0, 5)] # this is 0 to 5 because there are 6 different variations

# Main game loop ran here
def game():
    global player1
    global player2

    while True:
        displayToLCD(f"Player1: {player1}\n Player2: {player2}")
        # my_stick.set_all_LED_color(214, 0, 0)

        tile_to_tap = randomTile()
        print(tile_to_tap)

        checkTile(tile_to_tap)

        if player1 >= 100 and player2 >= 100: # Check if any of the players have over 100 if so end the game
            return "It is a tie!"
        elif player1 >= 100: 
            return "Player 1 has won!"
        elif player2 >= 100:
            return "Player 2 has won!"

# Wait for two users to step on a tile 3 times 
def checkIfGameStarted():
    steps_on_tile = 0

    while steps_on_tile < 3:
        displayToLCD("Wanna Dance?")
        if mpr121[0].value == True and mpr121[11].value == True:
            steps_on_tile += 1
            print("Number of times 2 Players stepped on the same tile: " + str(steps_on_tile))
            time.sleep(2)
        

# Game initialization and ending done here
def main():
    # LED LIGHT STRIP SETUP
    # if my_stick.begin() == False:
    #     print("\nThe Qwiic LED Stick isn't connected to the system. Please check your connection", file=sys.stderr)
    #     return
    # print("\nLED Stick ready!")

    # Wait for users to step on squares
    checkIfGameStarted()

    # Start the game
    winner = game()

    # Show game results on LCD
    displayToLCD(winner)

if __name__ == "__main__":
    main()