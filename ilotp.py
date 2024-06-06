
# chocomint li pona mute a!!!

import re


def ante_nanpa(nanpa_open):
	if type(nanpa_open) == int:
		if nanpa_open > 0:
			nanpa = nanpa_open
			ale = nanpa // 100
			nanpa = nanpa % 100
			mute = nanpa // 20
			nanpa = nanpa % 20
			luka = nanpa // 5
			nanpa = nanpa % 5
			tu = nanpa // 2
			nanpa = nanpa % 2
			
			if nanpa == 0:
				nanpa_pini = 'ale ' * ale + 'mute ' * mute + 'luka ' * luka + 'tu ' * tu
			if nanpa == 1:
				nanpa_pini = 'ale ' * ale + 'mute ' * mute + 'luka ' * luka + 'tu ' * tu + 'wan '
			
			return nanpa_pini[:-1]
			
		if nanpa_open == 0:
			nanpa_pini = 'ala'
			return nanpa_pini
		
		if nanpa_open < 0:
			raise ValueError('nanpa ni li lili a.')
	
	if type(nanpa_open) == str:
		if nanpa_open == 'ala':
			nanpa_pini = 0
			return nanpa_pini
		if re.fullmatch(r'(al[ei] +)*(al[ei])?(mute +)*(mute)?(luka +)*(luka)?(tu +)*(tu)?(wan)?',nanpa_open):
			nimi_nanpa = nanpa_open.replace('ali','ale')
			nimi_nanpa = nimi_nanpa.split()
			ale = nimi_nanpa.count('ale')
			mute = nimi_nanpa.count('mute')
			luka = nimi_nanpa.count('luka')
			tu = nimi_nanpa.count('tu')
			wan = nimi_nanpa.count('wan')
			nanpa_pini = ale*100 + mute*20 + luka*5 + tu*2 + wan*1
			return nanpa_pini
		else:
			raise ValueError('sitelen ni li nanpa ala, tawa ilo ni.')
	if type(nanpa_open) != int and type(nanpa_open) != str:
		raise TypeError('nimi nasin ni li ike tawa ilo ni.')



