# TargetHunter

A little 2D game where you have to hunt red targets, with your speed increasing and decreasing as things progress

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

By **B4tiste**, using `Ursina` engine in `Python`
