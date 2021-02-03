# -*- coding: utf-8 -*-
"""
TargetHunter game code

github.com/B4tiste/TargetHunter

@author: B4tiste
"""

from ursina import * #Import all the Urdina lib
import random
import time
import os

clear = lambda : os.system('cls')

# Change this value according to your screen refresh rate (60Hz for instance):
REFRESH_RATE = 60

#Duration of a game : 30s
GAME_TIME = 30

SPEED = 5
spd = SPEED
STARTUP_POSITION = (0, 0)
SIZE_PLAYER = (1, 1)
SIZE_TARGET = (0.5, 0.5)
GAP = 0.75
DELAY = 0
score = 0
hits = 0
time.sleep(DELAY)
rem_time = GAME_TIME
cpt = 0
menu_start = 0
var = 0

is_in_menu = 0

window.borderless = False

def menu() :

	global menu_start
	global var
	global score
	global hits
	global is_in_menu

	is_in_menu = 1
		
	target.scale = (0, 0)

	info.size = 0.00
	text_score.text = '\nFinal Score = ' + str(score) + '\nTarget hit = ' + str(hits) + '\nYou touched ' + str(abs(hits-score)) + ' times the side !'

	best_score_check()

	text_menu.x = 0
	text_menu.y = 0.25

	text_menu.text = 'Press SPACE to start the game'

def update():

	global cpt
	global score
	global hits
	global spd
	global rem_time
	global menu_start
	global REFRESH_RATE
	global var
	global is_in_menu

	cpt = cpt + 1
	
	if cpt == REFRESH_RATE :
		rem_time = rem_time - 1
		cpt = 0
	
	info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'

	if held_keys['z']:#Go Up
		player.y = player.y + spd * time.dt
	if held_keys['q']:#Go to the Left
		player.x = player.x - spd * time.dt
	if held_keys['s']:#Go Down
		player.y = player.y - spd * time.dt
	if held_keys['d']:#Go to the Right
		player.x = player.x + spd * time.dt

	if held_keys['escape'] or rem_time == 0:
		menu()

	if held_keys['l'] :
		exit()

	if held_keys['space'] and is_in_menu :

		is_in_menu = 0

		time.sleep(0.1)
		menu_start = 1
		score = 0
		hits = 0
		rem_time = GAME_TIME
		target.scale = SIZE_TARGET
		player.position = STARTUP_POSITION
		spd = SPEED
		info.size = 0.03
		info.color = color.white
		info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'
		text_score.text = ''
		text_menu.x = -0.65
		text_menu.y = 0.45
		text_menu.text = 'ESCAPE ==> MENU'
		text_new_best_score.text = ''
		text_current_score.text = ''
	
	if player.x < (target.x + GAP) and player.x > (target.x - GAP):
		if player.y < (target.y + GAP) and player.y > (target.y - GAP):
			x_rdm = random.randint(-5, 5)
			y_rdm = random.randint(-3, 3)
			
			target.x = x_rdm
			target.y = y_rdm
			
			score = score + 1
			hits = hits + 1
		
			info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'
			
			spd = spd + 1
	
	if player.x < -7 or player.x > 7:
		
		score = score - 1
		info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'
		
		player.position = STARTUP_POSITION
		
		spd = spd - 1
		
		if score < 0:
			score = 0
		if spd  < 1:
			spd = 1

	if player.y < -4 or player.y > 4:
		
		score = score - 1
		info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'
		
		player.position = STARTUP_POSITION
		
		spd = spd - 1
		
		if score < 0:
			score = 0
		if spd  < 1:
			spd = 1

	if rem_time < 6:
		info.color = color.red
		
def best_score_check():
	global score
	
	f_score = open('TargetHunter_score.txt', 'r')
	saved_score = f_score.read()

	f_score.close()

	if int(saved_score) < score :
	
		text_new_best_score.text = 'Congratulations, You beat your best score by ' + str(score - int(saved_score))

		f_score = open('TargetHunter_score.txt', 'w')
	
		f_score.write(str(score))
	
		f_score.close()
	
	text_current_score.text = 'Current best score = ' +str(score)
			

#Create an instance of Ursina ~Window
app = Ursina()

# Usina use Entities, 'elements' that can be almost anything in the instance
# [entity_name] = Entity(model = 'model', color = color.COLOR_NAME, scale = (x, y), position = (x, y))
# The center of the window is the point with (x, y) = (0, 0)

player = Entity(model = 'quad', color = color.green, scale = SIZE_PLAYER, position = STARTUP_POSITION)

target = Entity(model = 'quad', color = color.red, scale = SIZE_TARGET, position = (1, 1))

info = Text(text = 'Score', origin = (0, 0), size = 0.03, color = color.white)

text_score = Text(text = '', origin = (0, 0), size = 0.03, color = color.cyan)

text_new_best_score = Text(text = '', origin = (0, 0), size = 0.03, color = color.green, x = 0, y = -0.30)

text_current_score = Text(text = '', origin = (0, 0), size = 0.03, color = color.green, x = 0, y = -0.20)

text_menu = Text(text = 'ESCAPE ==> MENU', size = 0.03, origin =(0, 0), color = color.peach, font = 'assets/Minecraft.ttf', x = -0.65, y = 0.45)

text_exit = Text(text = 'PRESS L TO LEAVE THE GAME', size = 0.03, origin =(0, 0), color = color.peach, font = 'assets/Minecraft.ttf', x = -0.65, y = 0.35)

#Start the instance created at l.109
app.run()
