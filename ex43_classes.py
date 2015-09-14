#"""Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can
#   escape into an escape pod to the planet below. The game will be more like a Zork or Adventure type game 
#	with text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms 
#	or scenes. Each room will print its own description when the player enters it and then tell the engine 
#	what room to run next out of the map."""

# Death
# 	This is when the player dies and should be something funny
# Central Corridor
#	This is the starting point and has a Gothon already standing there they have to defeat with a joke 
#	before continuing.
# Laser Weapon Armory
#	This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It 
#	has a keypad the hero has to guess the number for.
# The Bridge
#	Another battle scene with a Gothon where the hero places the bomb.
# Escape Pod
#	Where the hero escapes but only after guessing the right escape pod.

# NOUNS
#
# Alien
# Player
# Ship
# Maze
# Room
# Scene
# Gothon
# Escape Pod
# Planet
# Map
# Engine
# Death
# Central Corridor
# Laser Weapon Armory
# The Bridge

# HIERARCHY AND OBJECT MAP
#
# * Map
#	- next_scene
#	- opening_scene
# * Engine
#	- play
# * Scene
#	- enter
#	* Death
#	* Central Corridor
#	* Laser Weapon Armory
#	* The Bridge
#	* Escape Pod

# CODING THE CLASSES
class Scene(object):

	def enter(self):
		pass


class Engine(object):

	def __init__(self, scene_map):
		pass

	def play(self):
		pass

class Death(Scene):

	def enter(self):
		pass

class CentralCorridor(Scene):

	def enter(self):
		pass

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass


class Map(object):

	def __init__(self, Start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

