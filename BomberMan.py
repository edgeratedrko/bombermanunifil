import pygame


##Inicializa o pygame.
pygame.init()

##Classe player, que contém os atributos e métodos relacionados ao jogador.

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0

    def existPlayer(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            window.blit(walkRight[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkLeft[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            window.blit(walkUp[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            window.blit(walkDown[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y))

##Tamanho da tela
scWidth , scHeight = 1200, 600

##Quadros por Segundo
fps = 60

##booleano de o game estiver executando
start = False

##Arrays contendo os sprites do Bomberman
walkRight = [pygame.image.load('Sprites/Bomberman/Side2/Bman_F_f00.png'), pygame.image.load('Sprites/Bomberman/Side2/Bman_F_f01.png'), pygame.image.load('Sprites/Bomberman/Side2/Bman_F_f02.png'), pygame.image.load('Sprites/Bomberman/Side2/Bman_F_f03.png'), pygame.image.load('Sprites/Bomberman/Side2/Bman_F_f04.png'), pygame.image.load('Sprites/Bomberman/Side2/Bman_F_f05.png'), pygame.image.load('Sprites/Bomberman/Side2/Bman_F_f06.png'), pygame.image.load('Sprites/Bomberman/Side2/Bman_F_f07.png')]
walkLeft = [pygame.image.load('Sprites/Bomberman/Side/Bman_F_f00.png'), pygame.image.load('Sprites/Bomberman/Side/Bman_F_f01.png'), pygame.image.load('Sprites/Bomberman/Side/Bman_F_f02.png'), pygame.image.load('Sprites/Bomberman/Side/Bman_F_f03.png'), pygame.image.load('Sprites/Bomberman/Side/Bman_F_f04.png'), pygame.image.load('Sprites/Bomberman/Side/Bman_F_f05.png'), pygame.image.load('Sprites/Bomberman/Side/Bman_F_f06.png'), pygame.image.load('Sprites/Bomberman/Side/Bman_F_f07.png')]
walkUp = [pygame.image.load('Sprites/Bomberman/Back/Bman_B_f00.png'), pygame.image.load('Sprites/Bomberman/Back/Bman_B_f01.png'), pygame.image.load('Sprites/Bomberman/Back/Bman_B_f02.png'), pygame.image.load('Sprites/Bomberman/Back/Bman_B_f03.png'), pygame.image.load('Sprites/Bomberman/Back/Bman_B_f04.png'), pygame.image.load('Sprites/Bomberman/Back/Bman_B_f05.png'), pygame.image.load('Sprites/Bomberman/Back/Bman_B_f06.png'), pygame.image.load('Sprites/Bomberman/Back/Bman_B_f07.png')]
walkDown = [pygame.image.load('Sprites/Bomberman/Front/Bman_F_f00.png'), pygame.image.load('Sprites/Bomberman/Front/Bman_F_f01.png'), pygame.image.load('Sprites/Bomberman/Front/Bman_F_f02.png'), pygame.image.load('Sprites/Bomberman/Front/Bman_F_f03.png'), pygame.image.load('Sprites/Bomberman/Front/Bman_F_f04.png'), pygame.image.load('Sprites/Bomberman/Front/Bman_F_f05.png'), pygame.image.load('Sprites/Bomberman/Front/Bman_F_f06.png'), pygame.image.load('Sprites/Bomberman/Front/Bman_F_f07.png')]

clock = pygame.time.Clock()


##Background do Jogo e o Sprite do Personagem quando parado.
bg = pygame.image.load('bomberman.png')
char = pygame.image.load('Sprites/Bomberman/Front/Bman_F_f00.png')


##Definição das dimensões da tela e nome que ficará na janela do jogo.
window = pygame.display.set_mode((scWidth,scHeight))
pygame.display.set_caption("BomberPY")


##Função Existir: responsável por instanciar o fundo do jogo e realizar a troca de Sprites durante
## a movimentação do personagem.
def exist():
    bomber.existPlayer(window)
    
    
##Loop Principal
bomber = player(50,50,64,128)
run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            bg = pygame.image.load("cenario1.png")
            start = True
##Movimentação do personagem
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bomber.x > bomber.vel:
        bomber.x -= bomber.vel
        bomber.left = True
        bomber.right = False
        bomber.up = False
        bomber.down = False
    elif keys[pygame.K_RIGHT] and bomber.x <  scWidth - bomber.width - bomber.vel:
        bomber.x += bomber.vel
        bomber.right = True
        bomber.left = False
        bomber.up = False
        bomber.down = False
    elif keys[pygame.K_UP] and bomber.y > bomber.vel:
        bomber.y -= bomber.vel
        bomber.up = True
        bomber.down = False
        bomber.left = False
        bomber.right = False
    elif keys[pygame.K_DOWN] and bomber.y < scHeight - bomber.height - bomber.vel:
        bomber.y += bomber.vel
        bomber.down = True
        bomber.up = False
        bomber.left = False
        bomber.right = False
    else:
        bomber.right = False
        bomber.left = False
        bomber.up = False
        bomber.down = False
        bomber.walkCount = 0

    #eventos tela
    window.blit(bg,(0,0))
    if start:
        exist()
    pygame.display.update()

pygame.quit()


