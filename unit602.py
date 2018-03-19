# Created by Amin Zeina 
# Created on Mar 2018
# Shows if number is negative or positive 

numberEntered = int(input( "Enter A number: "))

if numberEntered == 0 :
	print( '"0" is an invalid number')
elif numberEntered < 0 :
	print( 'The number is negative.')
else:
	print( 'The number is positive.')

input( 'Program End.')