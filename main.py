import random
import cards

majorCards = [card for card in cards.majorArcana.keys()]

def card_picker():
    card_picked = majorCards.pop(random.randint(0, len(majorCards) - 1))
    return card_picked

print("TAROT READING")
enter = input("Press ENTER to shuffle the cards")
random.shuffle(majorCards)
enter = input("Now press ENTER to pick the first card")
card1 = card_picker()
enter = input("Now press ENTER to pick the second card")
card2 = card_picker()
enter = input("Now press ENTER to pick the third card")
card3 = card_picker()

#print(majorCards)
print(card1)
print(card2)
print(card3)