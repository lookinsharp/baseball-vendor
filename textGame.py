#text based game
#where you are a worker at a ball park
#based on the one npr planet money episode about fenway hawkers

from attendee import Attendee #import different classes of game 
from items import Item
from weatherStuff import Weather

bug = "sup"

class Game:
	#main game class
	weather = Weather()

bert = Attendee(5, ["beer", "fries", "chowder"], "bleechers", 15)
bob = Attendee(10, ["coke, burger"], "home", 5)
print(bert.seat)
print(bob.seat)