# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop. Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.
 	
	# Output:
	# Making sandwich #1
	# Making sandwich #2
	# All done; only had enough bread for 2 sandwiches.

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

	# Output:
	# Making sandwich #1
	# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
	# Making sandwich #2
	# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
	# Making sandwich #3
	# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
	# Making sandwich #4
	# All done; I ran out of jelly.

	# AC: I altered this exercise to change the syntax to "I have {0} slices of bread, {1} scoops of jelly, and {2} scoops of peanut butter left."

peanut_butter = 5
jelly = 50
bread_slices = 100
sandwich_bread = bread_slices/2 
sandwiches = min(sandwich_bread, jelly, peanut_butter)
sandwich_number = 1
ingredients = []

while peanut_butter > 0 and jelly > 0 and bread_slices > 1:
	for sandwiches in range (1, ):
		print "Making sandwich #{0}" .format(sandwich_number)
		sandwich_number = sandwich_number + 1
		sandwiches = sandwiches - 1
		bread_slices = bread_slices - 2
		peanut_butter = peanut_butter - 1
		jelly = jelly - 1
		if peanut_butter >= 1 or jelly >= 1 or bread_slices >= 2:
			print "I have {0} slices of bread, {1} scoops of peanut butter, and {2} scoops of jelly left.".format(bread_slices, jelly, peanut_butter)

		if peanut_butter == 0:
			ingredients.append("peanut butter")
		if jelly == 0:
			ingredients.append("jelly")
		if bread_slices <= 1:
			ingredients.append("bread")

		if len(ingredients) == 1:
			print "All done; I ran out of {0}." .format(ingredients.pop())
		if len(ingredients) == 2:
			print "All done; I ran out of {0} and {1}." .format(ingredients.pop(), ingredients[0])
		if len(ingredients) == 3:
			print "All done; I ran out of {0}, {1}, and {2}." .format(ingredients.pop(), ingredients[0], ingredients[1])
