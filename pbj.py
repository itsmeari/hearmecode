# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

peanut_butter = 5
jelly = 5
bread_slices = 10
bread_sandwich = bread_slices/2 
bread_dif = (bread_slices - bread_sandwich) - bread_sandwich
bread_dif = bread_slices % bread_sandwich
sandwiches = min(bread_sandwich, jelly, peanut_butter) 
open_face = min(bread_slices, jelly, peanut_butter)
sandwich_dif = min(peanut_butter - sandwiches, jelly - sandwiches, bread_dif)
pb_sandwiches = min(bread_sandwich, peanut_butter)
open_face_pb = min(bread_slices, peanut_butter)
pb_sandwich_dif = min(peanut_butter - pb_sandwiches, bread_dif)

if peanut_butter >= 1 and jelly >= 1 and bread_slices >= 1: 
	if sandwich_dif == 0:
		print "You can make {0} sandwiches.".format(sandwiches)
	elif bread_slices == 1:
		print "You can make an open-faced sandwich."
	elif sandwich_dif == 1:
		print "You can make {0} closed-faced sandwiches and 1 open-faced sandwich. Or, you can make {1} open-faced sandwiches.".format(sandwiches, open_face)
elif peanut_butter >= 1 and jelly < 1 and bread_slices >= 1:
	if pb_sandwich_dif == 0:
		print "You can make {0} peanut butter sandwiches without jelly.".format(pb_sandwiches)
	elif bread_slices == 1:
		print "You can make an open-faced peanut butter sandwich without jelly."
	elif pb_sandwich_dif == 1:
		print "You can make {0} peanut butter sandwiches and 1 open-faced peanut butter sandwich. Or, you can make {1} open-faced peanut butter sandwiches without jelly.".format(pb_sandwiches, open_face_pb)
elif peanut_butter < 1 and jelly >= 1:
	if bread_slices > 1:
		print "You need to buy peanut butter. You only have bread and jelly, which isn't that appealing, right? I mean you could still eat it, but it sort of sucks."	
else:
	print "You cannot make a peanut butter sandwich. Better luck next time."