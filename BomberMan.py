import pygame

white=(255,255,255)

try:
	pygame.init()
except:
	print("erro")	

l=640
a=480
loop = True
fundo = pygame.display.set_mode((l,a))
pygame.display.set_caption("BomberMan")
while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
		else:
			print(event)
	fundo.fill(white)
	pygame.display.update()

pygame.quit()