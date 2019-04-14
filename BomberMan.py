import pygame

white = (255,255,255)

try:
	pygame.init()
except:
	print("erro")	
l = 800
a = 600
loop = True
fundo = pygame.display.set_mode((l,a))
pygame.display.set_caption("BomberMan")
fundo_menu = pygame.image.load("bomberman.png")
while loop:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        loop = False
                else:
                        print(event)
        #fundo.fill(white)
        fundo.blit(fundo_menu,[0,0])
        pygame.display.update()
pygame.quit()
