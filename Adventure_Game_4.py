import time
import random

monsters = ["wicked fairie", "gorgon", "dragon", "troll", "pirate"]
monster = random.choice(monsters)


def print_pause(string):
    print(string)
    time.sleep(1.2)


def intro():
    print_pause("\nYou find yourself standing in an open field, filled"
                "with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger. \n")


def in_field_choice(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave. \n")
    print_pause("What would you like to do? \n")


def move_player(items):
    in_field_choice(items)
    move = input("(Please enter 1 or 2.) \n")
    if move == '1':
        house(items)
    elif move == '2':
        cave(items)
    else:
        move_player(items)


def fight(items):
    if "Sword" in items:
        print_pause(f"\nAs the {monster} moves to attack, you unsheath "
                    "your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause(f"But the {monster} takes one look at your shiny "
                    "new toy and runs away! \n")
        print_pause(f"You have rid the town of the {monster}. You are "
                    "victorious! \n")
        play_again()
    else:
        print_pause("\nYou do your best...")
        print_pause(f"but your dagger is no match for the {monster}.")
        print_pause("You have been defeated!")
        play_again()


def run(items):
    if "Sword" in items:
        print_pause("\nGAME OVER")
        print_pause("Tip: Next time try being a little braver. ;-) ")
        play_again()
    else:
        print_pause("\nYou run back into the field. Luckily, you "
                    "don't seem to have been followed. \n")
        move_player(items)


def house(items):
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps"
                f" a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    if "Sword" in items:
        fight_run(items)
    else:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")
        fight_run(items)


def fight_run(items):
    fight_r = input("\nWould you like to (1) fight or (2) run away? \n")
    if fight_r == '1':
        fight(items)
    elif fight_r == '2':
        run(items)
    else:
        print_pause("\nPlease enter '1' or '2'. \n")
        fight_run(items)


def cave(items):
    if "Sword" in items:
        print_pause("\nYou peer cautiously into the cave. \n")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now. \n")
        print_pause("You walk back out to the field. \n")
        move_player(items)
    else:
        print_pause("\nYou peer cautiously into the cave. \n")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth! \n")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you. \n")
        print_pause("You walk back out to the field. \n")
        items.append("Sword")
        move_player(items)


def play_again():
    play_more = input("\nWould you like to play again? (y/n) \n")
    if play_more == 'y':
        print_pause("\nExcellent! Restarting the game ...\n")
        intro()
        items = []
        move_player(items)
    elif play_more == 'n':
        print("\nGoodbye.\n")
    else:
        print_pause("\nPlease enter a either 'y' or 'n'. \n")
        play_again()


def play_game():
    intro()
    items = []
    move_player(items)


play_game()
