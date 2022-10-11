import random
import cards

majorCards = [card for card in cards.majorArcana.keys()]

def card_picker():
    card_picked = majorCards.pop(random.randint(0, len(majorCards) - 1))
    return card_picked

def threeCards():
    print("TAROT READING")
    enter = input("Press ENTER to shuffle the cards")
    random.shuffle(majorCards)
    enter = input("Now press ENTER to pick the first card")
    past = card_picker()
    enter = input("Now press ENTER to pick the second card")
    present = card_picker()
    enter = input("Now press ENTER to pick the third card")
    future = card_picker()


    print(past)
    print(present)
    print(future)