import random

class Card:
    def __init__(self, name, number, upright, reverse):
        self.name = name
        self.number = number
        self.upright = upright
        self.reverse = reverse
        self.isReverse = False if random.randint(0, 1) == 0 else True
        

    def __repr__(self) -> str:
        if self.isReverse == False:
            return self.name + ": " + self.upright
        else:
            return self.name + " (Reversed): " + self.reverse

theFool = Card("The Fool", 0, "Innoncence, New Beginnings, Wonder, Foolishness.", "Being Naive, Taken Advantage Of, Recklessness")
theMagician = Card("The Magician", 1, "Willpower, Creation, Mastery, Adaptation.", "Trickery, Cunning, Deception, Craftiness")
theHighPriestess = Card("The High Priestess", 2, "Inner Voice, Intution, Devine Truth, Wisdom, Unconscous.", "Loss of Self, Repression, Secrs, Hidden Agendas.")
theEmpress = Card("The Empress", 3, "Beauty, Fertility, Nurturing, Luxury, Creativity.", "Smothering, Excess, Selfishness.")
theEmperor = Card("The Emperor", 4, "Structure, Ambition, Authority, Rationality.", "Chaos, Anger, Tiranny, Domination.")
theHierophant = Card("The Hierophant", 5, "Tradition, Legacy, Society, Organized Religion.", "Servitude, Convention, Blind Faith")
theLovers = Card("The Lovers", 6, "Choices, Union, Love, Realationship.", "Indecision, Ending of Relationship, Conflict")
theChariot = Card("The Chariot", 7, "Self Control, Discipline, Success.", "Loss of Direction, Loss of Will, Lack of Discipline")
strength = Card("Strength", 8, "Courage, Inner Strength, Conviction, Compassion.", "Doubt, Pride, Weakness, Cowardice.")
theHermit = Card("The Hermit", 9, "Contemplation, Solitude, Insight, Awareness.", "Isolation, Withdrawal, Loneliness, Rejection.")
wheelOfFortune = Card("Wheel of Fortune", 10, "Fate, Karma, Destiny, Fortune, Cycle.", "Bad Luck, Lack of Control, Clinging to Control.")
justice = Card("Justice", 11, "Truth, Fairness, Law, Clarity, Cause and Effect.", "Dishonesty, Unaccountability, Unfairness.")
theHangedMan = Card("The Hanged Man", 12, "Sacrifice, Suspension, Release, Martyrdrom.", "Stalling, Fear of Sacrifice, Neddless Sacrifice.")
death = Card("Death", 13, "End of Cycle, New Beginning, Change, Metamorphosis.", "Fear of Change, Holding On, Stagnationi, Decay.")
temperance = Card("Temperance", 14, "Middle Path, Patience, Finding Meaning.", "Extremes, Escess, Lack of Balance, Lack of Harmony.")
theDevil = Card("The Devil", 15, "Materialism, Playfulness, Pleasure, Addiction.", "Freedom, Release, Restoring Control.")
theTower = Card("The Tower", 16, "Upheaval, Disaster, Foundational Shift.", "Disaster Avoided, Dalaying Disaster, Fear of Suffering.")
theStar = Card("The Star", 17, "Hope, Faith, Rejuvenation, Rebuilding, Healing.", "Dusciyragenebtm Fautgkessness, Insecurity.")
theMoon = Card("The Moon", 18, "Unconscious, Illusions, Intuition, Unclarity.", "Confusion, Fear, Misinterpretation.")
theSun = Card("The Sun", 19, "Joy, Success, Celebration, Pleasure.", "Negativity, Depression, Sadness.")
judgement = Card("Judgement", 20, "Reflection, Reckoning, Awakening.", "Loack of Self Awareness, Doubt, Self Loathing.")
theWorld = Card("The World", 21, "Fulfillment, Harony, Completion.", "Incompletion, Lack of Closure, Emptiness.")

majorArcana = {
    theFool.name: [theFool.number, theFool.upright, theFool.reverse],
    theMagician.name: [theMagician.number, theMagician.upright, theMagician.reverse],
    theHighPriestess.name: [theHighPriestess.number, theHighPriestess.upright, theHighPriestess.reverse],
    theEmpress.name: [theEmpress.number, theEmpress.upright, theEmpress.reverse],
    theEmperor.name: [theEmperor.number, theEmperor.upright, theEmperor.reverse],
    theHierophant.name: [theHierophant.number, theHierophant.upright, theHierophant.reverse],
    theLovers.name: [theLovers.number, theLovers.upright, theLovers.reverse],
    theChariot.name: [theChariot.number, theChariot.upright, theChariot.reverse],
    strength.name: [strength.number, strength.upright, strength.reverse],
    theHermit.name: [theHermit.number, theHermit.upright, theHermit.reverse],
    wheelOfFortune.name: [wheelOfFortune.number, wheelOfFortune.upright, wheelOfFortune.reverse],
    justice.name: [justice.number, justice.upright, justice.reverse],
    theHangedMan.name: [theHangedMan.number, theHangedMan.upright, theHangedMan.reverse],
    death.name: [death.number, death.upright, death.reverse],
    temperance.name: [temperance.number, temperance.upright, temperance.reverse],
    theDevil.name: [theDevil.number, theDevil.upright, theDevil.reverse],
    theTower.name: [theTower.number, theTower.upright, theTower.reverse],
    theStar.name: [theStar.number, theStar.upright, theStar.reverse],
    theMoon.name: [theMoon.number, theMoon.upright, theMoon.reverse],
    theSun.name: [theSun.number, theSun.upright, theSun.reverse],
    judgement.name: [judgement.number, judgement.upright, judgement.reverse],
    theWorld.name: [theWorld.number, theWorld.upright, theWorld.reverse]
}