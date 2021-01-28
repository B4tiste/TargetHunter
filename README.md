# TargetHunter

A little 2D game where you have to hunt red targets, while your speed is increasing and decreasing as things progress

## How to play : 

Be sure to have `Ursina` installed, the render engine I used for this project by using :
> pip install ursina

Your goal is to catch as much red targets as you can, using the WASD key, you can change them to ZQSD for French people or anything you want, in this part of the `TargetHunter.py` code, by changing the letter in the **[LETTER]** :

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

Be careful, each time you hit a target, your speed increases and you'll gain 1 point, but if you touch a wall, you'll be slower, and you'll lose a point !

The default time of a game is 30s, but you can modify this value in this part of the code to fit your needs (l.25):

**/!\ This value is only equal to the number of second of a single game if you are running on a 60 Hz monitor**

```python
#Duration of a game : 30s
rem_time = 30
```

Using `Ursina` engine in `Python` 

By **B4tiste**, *a French guy who doesn't know how to code at all, and who's pretty garbage in English, but who wanna have fun*
First GitHub repository ever made ¯\_(ツ)_/¯
