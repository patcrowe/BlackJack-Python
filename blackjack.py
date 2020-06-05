import random

#Begin Card Class
class Card:
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		val = self.determine_face()
		return "{} of {}".format(val, self.suit)

	def determine_face(self):
		if self.value == 11:
			return "Jack"
		elif self.value == 1:
			return "Ace"
		elif self.value == 12:
			return "Queen"
		elif self.value == 13:
			return "King"
		else:
			return str(self.value)
#End Card Class

class Player:
	def __init__(self, p_type, name = "", hand = None, chips = 1000, winnings = 0, total_val = 0):
		self.p_type = p_type
		self.chips = chips
		if hand is None:
			self.hand = []
		self.winnings = winnings
		self.name = name
		self.total_val = total_val

	def __repr__(self):
		out = ""
		if self.p_type == "D":
			out += "Dealer Hand\nUnknown card\n"
			for x in self.hand[1:len(self.hand):1]:
				out += x.__repr__() + "\n"
			out += "\n"
		else:
			out += "{}'s Hand\n".format(self.name)
			for x in self.hand[0:len(self.hand):1]:
				out += x.__repr__() + "\n"
			out += "\n"
		return out

def init_deck(deck):
	deck = []
	suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
	for x in suits:
		for y in range(1,14,1):
			deck.append(Card(x,y))
	return deck

def shuffle(deck):
	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)
	return deck

def deal(player, dealer, deck, counter):
	for x in range(2):
		if counter >= 52:
			counter = 0
			shuffle(deck)
		player.hand.append(deck[counter])
		player.total_val += deck[counter].value
		counter += 1
		if counter >= 52:
			counter = 0
			shuffle(deck)
		dealer.hand.append(deck[counter])
		dealer.total_val += deck[counter].value
		counter += 1


def clear_hands(player, dealer):
	player.hand = []
	dealer.hand = []
	player.total_val = 0
	dealer.total_val = 0


def hit(player, deck, counter):
	if counter >= 52:
		counter = 0
		shuffle(deck)
	player.hand.append(deck[counter])
	player.total_val += deck[counter].value
	print("{} hits, {}".format(player.name, deck[counter]))
	counter += 1

def play_hand(player, deck, counter):
	x = input("Enter H to hit, or S to stay: ")
	while x.upper() == "H":
		hit(player, deck, counter)


deck = []
deck = init_deck(deck)
deck = shuffle(deck)

counter = 0
playing = True
dealer = Player(p_type = "D",name = "Dealer",chips = 1000000)
player_name = input("Type in your name\n")
player = Player(p_type = "H",name = player_name)
winner = ''
wager = 0

while playing:

	tmp_wager = input("Input your wager, current chips = {}\n".format(player.chips))
	wager = int(tmp_wager)
	deal(player, dealer, deck, counter)
	print(player)
	print(dealer)
	player_move = ''
	while player_move != 's':
		player_move = input("Enter \'h\' to hit, \'s\' to stand\n")
		if player_move.lower() == 'h':
			hit(player, deck, counter)
		if player_move == 's':
			print("{} stands\n".format(player.name))
		print(player)
		print(dealer)
		if player.total_val > 21:
			print("{} busts, dealer wins\n".format(player.name))
			winner = 'd'
			break

	if player.total_val < 22:
		while dealer.total_val < 17:
			hit(dealer)
			print(player)
			print(dealer)
			if player.total_val > 21:
				print("Dealer busts, player wins\n")
				winner = 'p'
				break

	if player.total_val > dealer.total_val:
		winner = 'p'
	elif dealer.total_val > player.total_val:
		winner = 'd'
	else:
		winner = 't'

	if winner == 'p':
		player.chips += wager
		print("{} wins this round. Your new chip total = {}\n".format(player.name, player.chips))
	if winner == 'd':
		player.chips -= wager
		print("Dealer wins this round. Your new chip total = {}\n".format(player.chips))
	if winner == 't':
		print("Tie\n")


	x = input("Enter \'q\' to quit, any other input to continue\n")
	if x.lower() == 'q':
		playing = False

	clear_hands(player, dealer)

print("Thanks for playing\n")