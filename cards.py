class Card:
    def __init__(self, name, number, representation):
        self.name = name
        self.number = number
        self.representation = representation

    def __repr__(self) -> str:
        return self.name + ":" + self.representation

theFool = Card("The Fool", 0, "The Beginning.")
theMagician = Card("The Magician", 1, "The spirituality and healing.")
theHighPriestess = Card("The High Priestess", 2, "The human Wisdom.")
theEmpress = Card("The Empress", 3, "Nature, and fertility.")
theEmperor = Card("The Emperor", 4, "Leadership, influence & stability.")
theHierophant = Card("The Hierophant", 5, "Mastering one's areas of expertise.")
theLovers = Card("The Lovers", 6, "Changes and growth in relationships.")
theChariot = Card("The Chariot", 7, "Empowerment, achievement and overcomig obstacles.")
strength = Card("Strength", 8, "The ego, discipline and refiment of self-interest.")
theHermit = Card("The Hermit", 9, "Introspection and inner reflection.")
wheelOfFortune = Card("Wheel of Fortune", 10, "Positive change and the season of the cycle of life.")
justice = Card("Justice", 11, "Fairness, moral sensitivity, karma, and attention to detail.")
theHangedMan = Card("The Hanged Man", 12, "Consequence, surrender, stagnation, and a situation that must be waited out.")
death = Card("Death", 13, "Endings and harvest, freeing onself, and moving foward.")
temperance = Card("Temperance", 14, "Moderation and balance, self-evolution, and avoiding extremes")
theDevil = Card("The Devil", 15, "Material and worldly pleasure, unhealthy relationships, and entrapment.")
theTower = Card("The Tower", 16, "Imminent or present danger, and unexpected change.")
theStar = Card("The Star", 17, "Spiritually and purpose, connecting to the divine and inspiration.")
theMoon = Card("The Moon", 18, "Illusion and impressionability, deception, confusion and strife.")
theSun = Card("The Sun", 19, "Vitality, joy and good fortune, confidence and authenticity.")
judgement = Card("Judgement", 20, "Resurrection, awakening, freedom from inner conflict, and decisions to be made.")
theWorld = Card("The World", 21, "An end to a cycle, major change, and self-actualization.")

majorArcana = {
    theFool.name: [theFool.number, theFool.representation],
    theMagician.name: [theMagician.number, theMagician.representation],
    theHighPriestess.name: [theHighPriestess.number, theHighPriestess.representation],
    theEmpress.name: [theEmpress.number, theEmpress.representation],
    theEmperor.name: [theEmperor.number, theEmperor.representation],
    theHierophant.name: [theHierophant.number, theHierophant.representation],
    theLovers.name: [theLovers.number, theLovers.representation],
    theChariot.name: [theChariot.number, theChariot.representation],
    strength.name: [strength.number, strength.representation],
    theHermit.name: [theHermit.number, theHermit.representation],
    wheelOfFortune.name: [wheelOfFortune.number, wheelOfFortune.representation],
    justice.name: [justice.number, justice.representation],
    theHangedMan.name: [theHangedMan.number, theHangedMan.representation],
    death.name: [death.number, death.representation],
    temperance.name: [temperance.number, temperance.representation],
    theDevil.name: [theDevil.number, theDevil.representation],
    theTower.name: [theTower.number, theTower.representation],
    theStar.name: [theStar.number, theStar.representation],
    theStar.name: [theStar.number, theStar.representation],
    theMoon.name: [theMoon.number, theMoon.representation],
    theSun.name: [theSun.number, theSun.representation],
    judgement.name: [judgement.number, judgement.representation],
    theWorld.name: [theWorld.number, theWorld.representation]
}