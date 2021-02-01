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

SPEED = 5
startup_position = (0, 0)
size_player = (1, 1)
size_target = (0.5, 0.5)
GAP = 0.75
DELAY = 0
score = 0
hits = 0
time.sleep(DELAY)
#Duration of a game : 30s
rem_time = 10
cpt = 0

def update():

	global cpt
	global score
	global hits
	global SPEED
	global rem_time
	
	cpt = cpt + 1
	
	if cpt == 60 :
		rem_time = rem_time - 1
		cpt = 0
	
	info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'

	if held_keys['z']:#Go Up
		player.y = player.y + SPEED * time.dt
	if held_keys['q']:#Go to the Left
		player.x = player.x - SPEED * time.dt
	if held_keys['s']:#Go Down
		player.y = player.y - SPEED * time.dt
	if held_keys['d']:#Go to the Right
		player.x = player.x + SPEED * time.dt
	"""if held_keys['r']:#Reset the position of the player
		player.x = 0
		player.y = 0"""
	if held_keys['escape']:
		exit()
	
	print('\nx = ' + str(player.x))
	print('y = ' + str(player.y))
	
	if player.x < (target.x + GAP) and player.x > (target.x - GAP):
		if player.y < (target.y + GAP) and player.y > (target.y - GAP):
			x_rdm = random.randint(-5, 5)
			y_rdm = random.randint(-3, 3)
			
			target.x = x_rdm
			target.y = y_rdm
			
			score = score + 1
			hits = hits + 1
		
			info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'
			
			SPEED = SPEED + 1
	
	if player.x < -7 or player.x > 7:
		
		score = score - 1
		info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'
		
		player.position = startup_position
		
		SPEED = SPEED - 1

	if player.y < -4 or player.y > 4:
		
		score = score - 1
		info.text = 'Score = ' + str(score) + '\nTime remaining : ' + str(rem_time) + 's'
		
		player.position = startup_position
		
		SPEED = SPEED - 1
		
	if rem_time == 0:
	
		clear()
		
		print("\nFinal Score = " + str(score))
		print("\nTarget hit = " + str(hits))
		print("\nYou touched " + str(hits-score) + ' times the side !')
		
		print('\n')
		best_score_check()
		
		exit()
		
def best_score_check():
	global score
	
	f_score = open('TargetHunter_score.txt', 'r')
	saved_score = f_score.read()

	f_score.close()

	if int(saved_score) < score :
	
		print('Congratulations, You beat your best score by ' + str(score - int(saved_score)))
	
		f_score = open('TargetHunter_score.txt', 'w')
	
		f_score.write(str(score))
	
		score = int(score)
	
		f_score.close()

	else :
		score = int(saved_score)
		
		
	print('Current best score = ' +str(score))

#Create an instance of Ursina ~Window
app = Ursina()

# Usina use Entities, 'elements' that can be almost anything in the instance
# [entity_name] = Entity(model = 'model', color = color.COLOR_NAME, scale = (x, y), position = (x, y))
# The center of the window is the point with (x, y) = (0, 0)

player = Entity(model = 'quad', color = color.green, scale = size_player, position = startup_position)

target = Entity(model = 'quad', color = color.red, scale = size_target, position = (1, 1))

info = Text(text = 'Score', origin = (0, 0), color = color.white)

#Start the instance created at l.109
app.run()
