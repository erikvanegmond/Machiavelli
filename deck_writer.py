from card import Card
import json

# noinspection PyListCreation
cards_list = []

cards_list.append((Card("Wachttoren", 1, "red"), 3))
cards_list.append((Card("Gevangenis", 2, "red"), 3))
cards_list.append((Card("Toernooiveld", 3, "red"), 3))
cards_list.append((Card("Burcht", 5, "red"), 2))

cards_list.append((Card("Taveerne", 1, "green"), 5))
cards_list.append((Card("Winkels", 2, "green"), 3))
cards_list.append((Card("Markt", 2, "green"), 4))
cards_list.append((Card("Handelshuis", 3, "green"), 3))
cards_list.append((Card("Haven", 4, "green"), 3))
cards_list.append((Card("Raadhuis", 5, "green"), 2))

cards_list.append((Card("Tempel", 1, "blue"), 3))
cards_list.append((Card("Kerk", 2, "blue"), 3))
cards_list.append((Card("Klooster", 3, "blue"), 3))
cards_list.append((Card("Kathedraal", 5, "blue"), 2))

cards_list.append((Card("Landgoed", 3, "yellow"), 5))
cards_list.append((Card("Kasteel", 4, "yellow"), 4))
cards_list.append((Card("Paleis", 5, "yellow"), 3))

cards_list.append((Card("Armenhuis", 0, "purple", special_ability=None, description="Als je aan het einde van je beurt geen goud bezit, ontvang je 1 goudstuk van de bank."),1))
cards_list.append((Card("Hof der Wonderen", 2, "purple", special_ability=None, description="Bij het tellen van de overwinningspunten mag je het Hof der Wonderen als een bouwerk met een kleur naar keuze benoemen"),1))
cards_list.append((Card("Kerker", 3, "purple", special_ability=None, description="De kerker kan niet door de Condottiere verwoest worden."),2))
cards_list.append((Card("Vuurtoren", 3, "purple", special_ability=None, description="Op het moment dat je de Vuurtoren bouwt, mag je eenmalig de stapel gebouwenkaarten doorzoeken en er een van in je hand nemen. Schud daarna de stapel."),1))
cards_list.append((Card("Kruittoren", 3, "purple", special_ability=None, description="Je mag tegelijkertijd de Kruittoren en een gebouw van een medespeler naar keuze opblazen."),1))
cards_list.append((Card("Museum", 4, "purple", special_ability=None, description="Je mag in elk van je beurten een van je gebouwenkaarten onder het Museum schuiven. Aan het einde van het spel krijg je voor elke kaart 1 extra overwinningspunt."),1))
cards_list.append((Card("Schatkamer", 4, "purple", special_ability=None, description="Aan het einde van het spel krijg je 1 extra overwinningspunt voor elk goudstuk in je bezit"), 1))
cards_list.append((Card("Kerkhof", 5, "purple", special_ability=None, description="Als de Condottiere een gebouw verwoest, dan mag je een goudstuk betalen om die bouwkaart in de hand te nemen. Je mag dit echter niet doen als je zelf de Condottiere bent."), 1))
cards_list.append((Card("Wensput", 5, "purple", special_ability=None, description="Aan het einde van het spel krijg je 1 extra overwinninspunt voor elk ander lila gebouw"), 1))
cards_list.append((Card("Casino", 5, "purple", special_ability=None, description="Aan het einde van het spel krijg je 1 extra overwinningspunt voor elke kaard, die je in je hand hebt."), 1))
cards_list.append((Card("Observatorium", 5, "purple", special_ability=None, description="Als je aan het begin van je beurt voor een bouwkaart kiest, dan mag je er 3 trekken en er vervolgens 1 uitkiezen en beide andere onder de trekstapel leggen"), 1))
cards_list.append((Card("Laboratorium", 5, "purple", special_ability=None, description="Gedurende je beurt mag je eenmaal een bouwkaart afleggen. Je krijgt daarvoor een goudstuk terug."), 1))
cards_list.append((Card("Fabriek", 5, "purple", special_ability=None, description="Het bouwen van elk volgend lila gebouw is voor jou 1 goudstuk goedkoper"), 1))
cards_list.append((Card("Werkplaats", 5, "purple", special_ability=None, description="Je mag tijdens je beurt eenmaal 3 goudstukken betalen om 2 bouwkaarten te trekken"), 1))
cards_list.append((Card("Klokkentoren", 5, "purple", special_ability=None, description="Op het moment dat je de Klokkentoren bouwt, moet je beslissen of het spel al na het 7e gebouw eindigt. Als de klokkentoren wordt vernietigd, eindigt het spel na het bouwen van het 8e gebouw"), 1))
cards_list.append((Card("Steengroeve", 5, "purple", special_ability=None, description="Betaal 1 goudstuk minder voor elk volgend gelijk gebouw. "), 1))
cards_list.append((Card("Troonzaal", 6, "purple", special_ability=None, description="Je ontvankt elke keer dat de koning van speler wisseld een goudstuk van de bank"), 1))
cards_list.append((Card("Balzaal", 6, "purple", special_ability=None, description="Als je de houten koning bezit moet iedere medespele, die door jou opgeroepen wordt, antwoorden met \'Dank u wel Exellentie\' Wie dit niet doet verliest zijn complete beurt"  ), 1))
cards_list.append((Card("Grote muur", 6, "purple", special_ability=None, description="De Condottiere moet 1 goudstuk meer betalen als hij een van jou gebouwen vernietigt"), 1))
cards_list.append((Card("Hospitaal", 6, "purple", special_ability=None, description="Als je vermoord word mag je desondanks je inkomen incasseren. Daarna is je beurt afgelopen"), 1))
cards_list.append((Card("Park", 6, "purple", special_ability=None, description="Als je aan het einde van je beurt geen kaarten meer hebt, mag je 2 kaarten van de stapel trekken"), 1))
cards_list.append((Card("School voor magiers", 6, "purple", special_ability=None, description="Tijdens de inkomstenfasen neemt de School voor magiers een kleur naar keuze aan. Je krijgt derhalve een goudstuk als je de Koning, de Prediker, de Koopman of de Condottiere bent."), 1))
cards_list.append((Card("Bibiotheek", 6, "purple", special_ability=None, description="Als je aan het begin van je beurt kaarten trekt, mag je ze beide houden."), 1))
cards_list.append((Card("Universiteit", 6, "purple", value=8, special_ability=None, description="Dit presitgeuze gebouw kost 6 goudstukken en levert aan het einde van je beurt 8 overwinningspunten op"), 1))
cards_list.append((Card("Drakenpoort", 6, "purple", value=8, special_ability=None, description="Dit presitgeuze gebouw kost 6 goudstukken en levert aan het einde van je beurt 8 overwinningspunten op"), 1))

deck_list = []
for card, count in cards_list:
    for _ in range(count):
        deck_list.append(card.get_dict())

deck_file = "start_deck.json"
with open(deck_file, "w") as f:
    f.write(json.dumps(deck_list, indent=2))
