# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

peanut_butter = 100
jelly = 0
bread_slices = 2
sandwich_bread = bread_slices/2 
bread_dif = (bread_slices - sandwich_bread) - sandwich_bread
sandwiches = min(sandwich_bread, jelly, peanut_butter) 
sandwich_dif = min(bread_dif, jelly, peanut_butter)
open_face = min(bread_slices, jelly, peanut_butter)

if peanut_butter >= 1 and jelly >= 1 and bread_slices == 2:
	print "You can make a sandwich.".format(sandwiches)
elif peanut_butter >= 1 and jelly >= 1 and bread_slices == 1:
	print "You can make an open-faced sandwich."
elif peanut_butter >= 1 and jelly >= 1 and bread_slices >= 2 and bread_dif == 0:
	print "You can make {0} sandwiches.".format(sandwiches)
elif peanut_butter >= 1 and jelly >= 1 and bread_slices >= 2 and bread_dif != 0:
	print "You can make {0} closed-faced sandwiches and {1} open-faced sandwich. Or, you can make {2} open-faced sandwiches.".format(sandwiches, sandwich_dif, open_face)
elif peanut_butter == 0:
	print "You don't have any peanut butter. You have to buy some."
elif bread_slices == 0:
	print "You don't have any bread. You have to buy some."
elif jelly == 0 and peanut_butter >= 1 and bread_slices == 2:
	print "You can make a peanut butter sandwich. But you don't have any jelly."
elif jelly == 0 and peanut_butter >= 1 and bread_slices >= 2:
	print "You can make {0} peanut butter sandwiches. But you don't have any jelly.".format(min(sandwich_bread, peanut_butter))
else:
	print "You cannot make a peanut butter and jelly sandwich. Better luck next time."