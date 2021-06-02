#!/usr/bin/env python
# Function to replace a character c1 with c2 
# and c2 with c1 in a string S 

def replaceChars(input,c1,c2): 

	# create lambda to replace c1 with c2, c2 
	# with c1 and other will remain same 
	# expression will be like "lambda x: 
	# x if (x!=c1 and x!=c2) else c1 if (x==c2) else c2" 
	# and map it onto each character of string 
	newChars = map(lambda x: x if (x!=c1 and x!=c2) else \
				c1 if (x==c2) else c2,input) 

	# now join each character without space 
	# to print resultant string 
	print (''.join(newChars)) 

# Driver program 
if __name__ == "__main__": 
	input = 'grrksfoegrrks'
	c1 = 'e'
	c2 = 'r'
	replaceChars(input,c1,c2) 

