class living_animalls:
	def living_things(self):
		print('i support the living things')
	def life(self):
		print('i keep every thing alive')
class the_universe(living_animalls):

	def walk(self):
		print('i can walk')
	def talk(self):
		print('i surely talk')

def main():
 	birds=the_universe()
 	birds.walk()
 	birds.life()

main()