import zombiedice
import random


class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class TwoBrainZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = diceRollResults['brains']
        shouldRole = brains < 2

        while diceRollResults is not None and shouldRole:
            diceRollResults = zombiedice.roll()  # roll again
            if diceRollResults is not None:
                brains += diceRollResults['brains']
            shouldRole = brains < 2


class RandomZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        #

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shouldRole = random.randint(0, 1) == 1

        while diceRollResults is not None and shouldRole:
            shouldRole = random.randint(0, 1) == 1
            diceRollResults = zombiedice.roll()  # roll again


class TwoShotgunZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        #

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotguns = diceRollResults.get('shotgun', 0)
        shouldRole = shotguns < 2

        while diceRollResults is not None and shouldRole:
            diceRollResults = zombiedice.roll()  # roll again
            if diceRollResults is not None:
                shotguns += diceRollResults['shotgun']
            shouldRole = shotguns < 2


class OneToFourZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        #

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:

        numberOfRolls = random.randint(1, 4)
        timesRolled = 1
        shotguns = diceRollResults.get('shotgun', 0)
        shouldRole = shotguns < 2 and timesRolled < numberOfRolls

        while diceRollResults is not None and shouldRole:
            diceRollResults = zombiedice.roll()  # roll again
            timesRolled += 1
            if diceRollResults is not None:
                shotguns += diceRollResults['shotgun']
            shouldRole = shotguns < 2 and timesRolled < numberOfRolls


class ShotgunZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        #

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:

        numberOfRolls = random.randint(1, 4)
        shotguns = diceRollResults['shotgun']
        brains = diceRollResults['brains']
        shouldRole = shotguns <= brains

        while diceRollResults is not None and shouldRole:
            diceRollResults = zombiedice.roll()  # roll again
            if diceRollResults is not None:
                shotguns += diceRollResults['shotgun']
                brains += diceRollResults['shotgun']
            shouldRole = shotguns <= brains


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    RandomZombie(name='My Random'),
    TwoBrainZombie(name='My TwoBrain stopper'),
    TwoShotgunZombie(name='My TwoShotgun stopper'),
    OneToFourZombie(name='My OneToFour zombie'),
    ShotgunZombie(name='My Shotgun zombie'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
