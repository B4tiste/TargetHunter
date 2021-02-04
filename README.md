# TargetHunter

A little 2D game where you have to hunt red targets, while your speed is increasing and decreasing as things progress, with a score saving system

Be sure to check all the information below before playing 

### In game screenshot : 
![alt text](https://github.com/B4tiste/TargetHunter/blob/main/Pictures/Game.PNG?raw=true "In Game Screenshot")

### Final score screen : 
![alt text](https://github.com/B4tiste/TargetHunter/blob/main/Pictures/Score.PNG?raw=true "Final ")

## How to play : 
### Requirements
Be sure to have `Ursina` installed, the render engine I used for this project by using :
> pip install ursina

Your goal is to catch as much red targets as you can, using the WASD key, you can change them to ZQSD for French people or anything you want, in this part of the `TargetHunter.py` code, by changing the letter in the [ ] :

```python
# WASD case :
	if held_keys['w']:#Go Up
		player.y = player.y + SPEED * time.dt
	if held_keys['a']:#Go to the Left
		player.x = player.x - SPEED * time.dt
	if held_keys['s']:#Go Down
		player.y = player.y - SPEED * time.dt
	if held_keys['d']:#Go to the Right
		player.x = player.x + SPEED * time.dt
```

You can use the `ESCAPE` key to acces the Game Menu, and press `SPACE` to restart a game.

You can use the `L` key to close and leave the Game.

### Bonus and Penalty
Be careful, each time you hit a target, your speed increases and you'll gain 1 point, but if you touch a wall, you'll be slower, and you'll lose a point !

You can also catch a Bonus, wich is represented by a magenta square flying around during the game. This bonus will give you 5 extra seconds to play the game and try to catch as much targets as you can !

### Game Settings
The default time of a game is 30s, wich depends of the refresh rate of your computer screen, but you can modify the value of your screen refresh rate in this part of the code to fit your needs :

**/!\ Change this value according to your screen refresh rate : **

```python
#Refresh Rate value : 60hz
REFRESH_RATE = 60
```

You can change the duration of a game in this part of the code

```python
#Duration of a game : 30s
GAME_TIME = 30
```

### Information

Using `Ursina` engine in `Python` 

By [B4tiste](github.com/B4tiste "Go to B4tiste GitHub Page"), *a French guy who doesn't know how to code anything else beside `Hello World`, and who's pretty garbage in English, but who wanna have fun*

My first GitHub repository ever made ツ
