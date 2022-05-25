# https://dev.to/ihtesham_haider/python-project-click-bait-titles-generator-with-infinity-4iap <- source of code
import random

class RandomTitleGenerator:
    OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
    SUSPECIOUS_PRONOUNS = ['Her', 'His', 'They']
    PERSONAL_PRONOUNS = ['She', 'His', 'Their']
    CITIES = ['Warszawa', 'Krakow', 'Lodz', 'Poznan', 'Wroclaw',
            'Gdansk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Bialystok',
            'Zielona Gora', 'Swinoujscie', 'Dabrowa Gornicza', 'Katowice']
    NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor',
            'Parent', 'Cat','Dog', 'Chicken', 'Robot', 'Video Game',
            'Avocado', 'Plastic Straw', 'Seriel Killer','Telephone Pyschic']
    PLACES = [
        'House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
        'Workplace', 'Donut Shop', 'Apocalypse Bunker'
    ]
    WHEN = ['Soon', 'This Year', 'Later', 'RIGHT NOW', 'Next Week']

    @staticmethod
    def generateAreMillennialsKillingHeadline():
        noun = random.choice(RandomTitleGenerator.NOUNS)
        return 'Are Millennials Killing the {} Industry?'.format(noun)

    @staticmethod
    def generateWhatYouDontKnowHeadline():
        noun = random.choice(RandomTitleGenerator.NOUNS)
        pluralNoun = random.choice(RandomTitleGenerator.NOUNS) + 's'
        when = random.choice(RandomTitleGenerator.WHEN)
        return 'Without This {}, {} Could Kill You {}'.format(noun, pluralNoun, when)

    @staticmethod
    def generateBigCompaniesHateHerHeadline():
        pronoun = random.choice(RandomTitleGenerator.OBJECT_PRONOUNS)
        state = random.choice(RandomTitleGenerator.CITIES)
        noun1 = random.choice(RandomTitleGenerator.NOUNS)
        noun2 = random.choice(RandomTitleGenerator.NOUNS)
        return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)

    @staticmethod
    def generateYouWontBelieveHeadline():
        state = random.choice(RandomTitleGenerator.CITIES)
        noun = random.choice(RandomTitleGenerator.NOUNS)
        pronoun = random.choice(RandomTitleGenerator.SUSPECIOUS_PRONOUNS)
        place = random.choice(RandomTitleGenerator.PLACES)
        return 'You Won\'t Believe What This {} {} Found in {} {}'. format(state, noun, pronoun, place)

    @staticmethod
    def generateDontWantYouToKnowHeadline():
        pluralNoun1 = random.choice(RandomTitleGenerator.NOUNS) + 's'
        pluralNoun2 = random.choice(RandomTitleGenerator.NOUNS) + 's'
        return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)

    @staticmethod
    def generateGiftIdeaHeadline():
        number = random.randint(7, 15)
        noun = random.choice(RandomTitleGenerator.NOUNS)
        state = random.choice(RandomTitleGenerator.CITIES)
        return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)

    @staticmethod
    def generateReasonsWhyHeadline():
        number1 = random.randint(3, 19)
        pluralNoun = random.choice(RandomTitleGenerator.NOUNS) + 's'
        #number 2 should no longer than number1
        number2 = random.randint(1, number1)
        return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)

    @staticmethod
    def generateJobAutomatedHeadline():
        state = random.choice(RandomTitleGenerator.CITIES)
        noun = random.choice(RandomTitleGenerator.NOUNS)

        i = random.randint(0, 2)
        pronoun1 = RandomTitleGenerator.SUSPECIOUS_PRONOUNS[i]
        pronoun2 = RandomTitleGenerator.SUSPECIOUS_PRONOUNS[i]
        if pronoun1 == 'Their':
            return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
        else:
            return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong'.format(state, noun, pronoun1, pronoun2)