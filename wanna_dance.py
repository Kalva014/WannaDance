# Additional libraries
import random

# Capactive Sensor 
import time
import board
import busio
import adafruit_mpr121
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# # LED LIGHT STRIP
# import qwiic_led_stick
# my_stick = qwiic_led_stick.QwiicLEDStick()
# red_list = [214, 78, 183, 198, 59, 134, 15, 209, 219, 186]
# green_list = [59, 216, 170, 21, 114, 63, 226, 92, 155, 175]
# blue_list = [214, 147, 25, 124, 153, 163, 188, 33, 175, 221]

# The specific capacitive sensors(aka the tiles) that will light up and need to be stepped on
tiles = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]


# Checks if user stepped on a tile and gives them points if they did
def checkTile(tile_to_tap):
    time.sleep(5) # Give userse time to step on a tile 
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

# Returns a random tile that both players have to step on
def randomTile():
    return tiles[random.randint(0, 5)]

# Main game loop ran here
def game():
    # Players' points
    player1 = 0
    player2 = 0
    while True:
        # my_stick.set_all_LED_color(214, 0, 0)

        tile_to_tap = randomTile()
        print(tile_to_tap)

        checkTile(tile_to_tap)


        

        # for i in range(12):
        #     if mpr121[i].value:
        #         print(f"Twizzler {i} touched!")
        # time.sleep(0.25)  # Small delay to keep from spamming output messages.

# Game initialization and ending done here
def main():
    # LED LIGHT STRIP SETUP
    # if my_stick.begin() == False:
    #     print("\nThe Qwiic LED Stick isn't connected to the system. Please check your connection", file=sys.stderr)
    #     return
    # print("\nLED Stick ready!")

    # Game
    game()

if __name__ == "__main__":
    main()