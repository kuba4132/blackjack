import pygame, sys
from sys import exit
import random



global punkty
punkty = 0
#################guzik######################################
class Button:
	def __init__(self,text,width,height,pos,elevation):
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		
		###top
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
		###bottom
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'


		#tekst
		self.text_surf = test_font.render(text, False, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
	
	def draw(self):
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
		
		
		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect, border_radius =12)
		pygame.draw.rect(screen,self.top_color, self.top_rect, border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()
		
		
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		
		global karta1
		global karta2


		karta1 = 0
		karta2 = 0
								
		
		
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			#screen.blit(karta_2_surface,(900,500))					#na najechaniu
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				
			else:
					self.dynamic_elecation = self.elevation
					if self.pressed == True:
						print('dziala')	
						screen.blit(czarny_surface,(500,500))
						screen.blit(czarny_surface,(600,410))
						screen.blit(deltext,(350,400))															# <----co robi guzik
													
																					
						ran = random.randint(1, 13)
						ran2 = random.randint(1, 13)
						ran3 = random.randint(1, 13)
						print (ran)
						print (ran2)
						
						
#losowanie pierwszej karty xdd#########################################						

						if ran == 2:
							screen.blit(karta_2_surface,(700,500))
							karta1 = 2
						elif ran == 3:
							screen.blit(karta_3_surface,(700, 500))	
							karta1 = 3
						elif ran == 4:
							screen.blit(karta_4_surface,(700, 500))	
							karta1 = 4
						elif ran == 5:
							screen.blit(karta_5_surface,(700, 500))
							karta1 = 5
						elif ran == 6:
							screen.blit(karta_6_surface,(700, 500))	
							karta1 = 6
						elif ran == 7:
							screen.blit(karta_7_surface,(700, 500))	
							karta1 = 7
						elif ran == 8:
							screen.blit(karta_8_surface,(700, 500))
							karta1 = 8
						elif ran == 9:
							screen.blit(karta_9_surface,(700, 500))
							karta1 = 9
						elif ran == 10:
							screen.blit(karta_10_surface,(700, 500))
							karta1 = 10
						elif ran == 11:
							screen.blit(karta_j_surface,(700, 500))
							karta1 = 10
						elif ran == 12:
							screen.blit(karta_q_surface,(700, 500))
							karta1 = 10
						elif ran == 13:
							screen.blit(karta_k_surface,(700, 500))
							karta1 = 10
						elif ran == 1:
							screen.blit(karta_a_surface,(700, 500))	
							karta1 = 1

#############################losowanie drugiej##########################################						

						if ran2 == 2:
							screen.blit(karta_2_surface,(900,500))
							karta2 = 2
						elif ran2 == 3:
							screen.blit(karta_3_surface,(900, 500))	
							karta2 = 3
						elif ran2 == 4:
							screen.blit(karta_4_surface,(900, 500))	
							karta2 = 4
						elif ran2 == 5:
							screen.blit(karta_5_surface,(900, 500))
							karta2 = 5
						elif ran2 == 6:
							screen.blit(karta_6_surface,(900, 500))	
							karta2 = 6
						elif ran2 == 7:
							screen.blit(karta_7_surface,(900, 500))	
							karta2 = 7
						elif ran2 == 8:
							screen.blit(karta_8_surface,(900, 500))
							karta2 = 8
						elif ran2 == 9:
							screen.blit(karta_9_surface,(900, 500))
							karta2 = 9
						elif ran2 == 10:
							screen.blit(karta_10_surface,(900, 500))
							karta2 = 10
						elif ran2 == 11:
							screen.blit(karta_j_surface,(900, 500))
							karta2 = 10
						elif ran2 == 12:
							screen.blit(karta_q_surface,(900, 500))
							karta2 = 10
						elif ran2 == 13:
							screen.blit(karta_k_surface,(900, 500))
							karta2 = 10
						elif ran2 == 1:
							screen.blit(karta_a_surface,(900, 500))	
							karta2 = 1						

#---------------- -------- losowanie dilera ----------
						global karta4
						karta4 = 0

						if ran3 == 2:
							screen.blit(karta_2_surface,(850,150))
							karta4 = 2
						elif ran3 == 3:
							screen.blit(karta_3_surface,(850, 150))	
							karta4 = 3
						elif ran3 == 4:
							screen.blit(karta_4_surface,(850, 150))	
							karta4 = 4
						elif ran3 == 5:
							screen.blit(karta_5_surface,(850, 150))
							karta4 = 5
						elif ran3 == 6:
							screen.blit(karta_6_surface,(850, 150))	
							karta4 = 6
						elif ran3 == 7:
							screen.blit(karta_7_surface,(850, 150))	
							karta4 = 7
						elif ran3 == 8:
							screen.blit(karta_8_surface,(850, 150))
							karta4 = 8
						elif ran3 == 9:
							screen.blit(karta_9_surface,(850, 150))
							karta4 = 9
						elif ran3 == 10:
							screen.blit(karta_10_surface,(850,150))
							karta4 = 10
						elif ran3 == 11:
							screen.blit(karta_j_surface,(850, 150))
							karta4 = 10
						elif ran3 == 12:
							screen.blit(karta_q_surface,(850, 150))
							karta4 = 10
						elif ran3 == 13:
							screen.blit(karta_k_surface,(850, 150))
							karta4 = 10
						elif ran3 == 1:
							screen.blit(karta_a_surface,(850, 150))	
							karta4 = 1							
						dilerstr = str(karta4)
						dilerpunkt = test_font.render('Diler: '+ dilerstr, False, 'White').convert()
						screen.blit(dilerpunkt,(850, 400))



						global punkty
						punkty = 0
						punkty = karta1 + karta2
						
						
						punktystring = str(punkty)
						iloscpunkt = test_font.render('Punktow:' + punktystring, False, 'White').convert()
						screen.blit(iloscpunkt,(700, 420))

						if punkty == 20:
							print ('dupka')
						print(punkty)



						#print (karta1+karta2)
						#print (type(karta1))
						#screen.blit(karta_2_surface,(900,500))
						#screen.blit(karta_3_surface,(700, 500))								
						#print(type(karta_2_surface))

						
						
					self.pressed = False

		else:
				self.dynamic_elecation = self.elevation
				self.top_color = '#475F77'



####################### BUTTON 2 HIT ########################################

class Button2:
	def __init__(self,text,width,height,pos,elevation):
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		
		###top
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
		###bottom
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'


		#tekst
		self.text_surf = test_font.render(text, False, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
	
	def draw(self):
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
		
		
		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect, border_radius =12)
		pygame.draw.rect(screen,self.top_color, self.top_rect, border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()
			
		
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		
		global karta3
		karta3 = 0
	
		


		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			#screen.blit(karta_2_surface,(900,500))					#na najechaniu
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				
			else:
					self.dynamic_elecation = self.elevation
					if self.pressed == True:
						#screen.blit(czarny_surface,(500,500))
						screen.blit(deltext,(250,415))
						print('dziala buton 2')
						
						def hit():
							global ranhit
							ranhit = random.randint(1, 13)
							
							
							if ranhit == 2:
								screen.blit(karta_2_surface,(500,500))
								karta3 = 2
							elif ranhit == 3:
								screen.blit(karta_3_surface,(500, 500))	
								karta3 = 3
							elif ranhit == 4:
								screen.blit(karta_4_surface,(500, 500))	
								karta3 = 4
							elif ranhit == 5:
								screen.blit(karta_5_surface,(500, 500))
								karta3 = 5
							elif ranhit == 6:
								screen.blit(karta_6_surface,(500, 500))	
								karta3 = 6
							elif ranhit == 7:
								screen.blit(karta_7_surface,(500, 500))	
								karta3 = 7
							elif ranhit == 8:
								screen.blit(karta_8_surface,(500, 500))
								karta3 = 8
							elif ranhit == 9:
								screen.blit(karta_9_surface,(500, 500))
								karta3 = 9
							elif ranhit == 10:
								screen.blit(karta_10_surface,(500, 500))
								karta3 = 10
							elif ranhit == 11:
								screen.blit(karta_j_surface,(500, 500))
								karta3 = 10
							elif ranhit == 12:
								screen.blit(karta_q_surface,(500, 500))
								karta3 = 10
							elif ranhit == 13:
								screen.blit(karta_k_surface,(500, 500))
								karta3 = 10
							elif ranhit == 1:
								screen.blit(karta_a_surface,(500, 500))	
								karta3 = 1	
							print ('karta 3 = ')
							print (karta3)

							print ('punkty teraz:')
							punktow = punkty + karta3
							print (punktow)
							
							punktystring = str(punktow)
							iloscpunkt = test_font.render('Punktow:' + punktystring, False, 'White').convert()

							print (punkty+karta3)
							screen.blit(iloscpunkt,(700, 420))
							if punktow > 21:
								print('przejebane')
								screen.blit(deltext,(250,415))
								#screen.blit(czarny_surface,(600,180))
								przejebane = test_font.render('Przegrane!', False,'White').convert()
								screen.blit(przejebane,(700,460))
								screen.blit(iloscpunkt,(700, 420))

						hit()
						
						
					self.pressed = False

		else:
				self.dynamic_elecation = self.elevation
				self.top_color = '#475F77'
################################  BUTTON 2 HIT  ##########################################
################################  BUTTON 3 STAND  ##########################################
class Button3:
	def __init__(self,text,width,height,pos,elevation):
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		
		###top
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
		###bottom
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'


		#tekst
		self.text_surf = test_font.render(text, False, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
	
	def draw(self):
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
		
		
		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect, border_radius =12)
		pygame.draw.rect(screen,self.top_color, self.top_rect, border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()
		
		
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		
		
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				
			else:
					self.dynamic_elecation = self.elevation
					if self.pressed == True:
						print('diler ma:')
						print (karta4)

						diler2 = karta4 + random.randint(1,10)
						print('diler ma razem:')
						print (diler2)
						if diler2 > punkty:
							print('przejebane')
							screen.blit(deltext,(250,415))
							#screen.blit(czarny_surface,(600,180))
							przejebane = test_font.render('Przegrane!', False,'White').convert()
							screen.blit(przejebane,(700,460))
							screen.blit(iloscpunkt,(700, 420))
						
							
						if diler2 < punkty:
							print('wygrane')
							screen.blit(deltext,(250,415))
							#screen.blit(czarny_surface,(600,180))
							przejebane = test_font.render('Wygrane!', False,'White').convert()
							screen.blit(przejebane,(700,460))
							screen.blit(iloscpunkt,(700, 420))


					self.pressed = False

		else:
				self.dynamic_elecation = self.elevation
				self.top_color = '#475F77'



################################  BUTTON 3 STAND ##########################################
###############################################################################
class Karta_3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('grafika/karty/karta_3.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = (200, 300))




###############################################################################





pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Okno')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/pixelfont.ttf', 20)
punkty = 0
punktystring = str(punkty)


################################################################################
button1 = Button('Restart', 200,50,(500,100),5)
button2 = Button2('Hit', 200,50,(300, 200),5)
button3 = Button3('Stand',200,50,(600, 200),5)

tlo_surface = pygame.image.load('grafika/tloo2.png').convert_alpha()
karta_surface = pygame.image.load('grafika/karta.png').convert_alpha()
text_surface = test_font.render('abc012ABC', False, 'Black').convert()
iloscpunkt = test_font.render(punktystring, False, 'White').convert()
deltext = pygame.image.load('grafika/karty/deltekst.png').convert()

#karty
karta_2_surface = pygame.image.load('grafika/karty/karta_2.png').convert()
karta_3_surface = pygame.image.load('grafika/karty/karta_3.png').convert_alpha()
karta_4_surface = pygame.image.load('grafika/karty/karta_4.png').convert_alpha()
karta_5_surface = pygame.image.load('grafika/karty/karta_5.png').convert_alpha()
karta_6_surface = pygame.image.load('grafika/karty/karta_6.png').convert_alpha()
karta_7_surface = pygame.image.load('grafika/karty/karta_7.png').convert_alpha()
karta_8_surface = pygame.image.load('grafika/karty/karta_8.png').convert_alpha()
karta_9_surface = pygame.image.load('grafika/karty/karta_9.png').convert_alpha()
karta_10_surface = pygame.image.load('grafika/karty/karta_10.png').convert_alpha()
karta_j_surface = pygame.image.load('grafika/karty/karta_j.png').convert_alpha()
karta_q_surface = pygame.image.load('grafika/karty/karta_q.png').convert_alpha()
karta_k_surface = pygame.image.load('grafika/karty/karta_k.png').convert_alpha()
karta_a_surface = pygame.image.load('grafika/karty/karta_a.png').convert_alpha()
czarny_surface = pygame.image.load('grafika/karty/czarny.png').convert()


karta_3 = pygame.sprite.GroupSingle()
karta_3.add(Karta_3())




	#petla gry:
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	
			
	screen.blit(tlo_surface,(0,0))
	button1.draw()
	button2.draw()
	button3.draw()
	screen.blit(karta_surface,(1100,15))
	screen.blit(text_surface,(300, 50))
	#screen.blit(karta_2_surface,(900, 500))
	

	#karta_3.draw()

	pygame.display.update()
	clock.tick(60)

