# Difficulty Level: Intermediate

# Goal: Create a program that prints out an HTML drop down menu for all 50 states

# Step 1: Define your list of states
# These should all be strings, since they're names of places
# Instead of having to type them all out, I really like liststates.com -- you can even customize the format it gives you the states in to make it super easy to copy/paste into your code here

# Step 2: Create your loop
# Essentially, you're telling Python: for each state in my list: print this HTML code
# A good place to start is by printing the name of the state in the loop; after that you can add the HTML around it

# Step 3: Add the HTML
# A drop-down menu in HTML looks like this:

# <select>
# 			<option value="state_abbreviation">Full state name</option>
# </select>

# At line 14, we create the drop-down menu
# At line 15, we create one drop-down item.  Each additional <option> that we add will add another item to our drop-down menu
# At line 16, we tell HTML that we're done with the drop-down menu

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

state_abbreviation = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

print "<select name='States'>"

for abbreviation, state in zip(state_abbreviation, states):
	print "\t <option value='{0}'>{1}</option>".format(abbreviation, state)

print "</select>"
