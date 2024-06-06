
import ilotp
import re

ijo = input('o sitelen e nanpa:')
if re.fullmatch(r'-?[0-9]+',ijo):
	ijo = int(ijo)
print(ilotp.ante_nanpa(ijo))













