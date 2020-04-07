import random

import pygame
from pygame import *


class Player():
    def __init__(self):
        self._player_walk = [
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\0.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\1.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\2.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\3.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\4.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\5.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\6.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\7.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\8.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites\9.png'),
            #pygame.image.load(r'D:\Proyectos\imágenes\Sprites_2\1.png'),
            pygame.image.load(r'D:\Proyectos\imágenes\Sprites_2\2.png'),
            #pygame.image.load(r'D:\Proyectos\imágenes\Sprites_2\3.png'),
            #pygame.image.load(r'D:\Proyectos\imágenes\Sprites_2\4.png'),
            #pygame.image.load(r'D:\Proyectos\imágenes\Sprites_2\5.png')
        ]

        (self._posX, self._posY) = (100, 169)  # Posición jugador
        self._hitbox = (self._posX + 10, self._posY + 10, 60, 100)  # Zona de contacto con el player

    def drawPlayerWalk(self, mapa, cont_img):
        self._hitbox = (self._posX + 10, self._posY + 10, 60, 100)
        self._drew_hitbox = pygame.draw.rect(mapa, (255, 0, 0), self._hitbox, 1)
        mapa.blit(self._player_walk[cont_img], (self._posX, self._posY))

    def Colision(self, obst):
        if self._drew_hitbox.colliderect(obst):
            print("HIT")

    def mover(self, vel_x, vel_y):
        self._posX += vel_x
        self._posY += vel_y
        return self._posX


class Level():

    def __init__(self):
        self._objects = [pygame.image.load(r'D:\Proyectos\imágenes\bg_elements\pelican_1.png'),
                         pygame.image.load(r'D:\Proyectos\imágenes\bg_elements\spaceship_1.png'),
                         pygame.image.load(r'D:\Proyectos\imágenes\bg_elements\spaceship_2.png')
                         ]
        self._fire = [
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\0.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\1.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\2.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\3.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\4.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\5.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\6.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\7.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\8.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\9.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\10.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\11.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\12.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\13.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\14.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\15.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\16.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\17.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\18.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\19.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\20.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\21.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\22.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\23.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\24.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\25.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\26.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\27.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\28.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\29.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\30.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\31.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\32.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\33.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\34.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\35.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\36.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\37.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\38.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\39.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\40.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\41.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\42.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\43.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\44.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\45.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\46.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\47.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\48.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\49.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\50.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\51.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\52.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\53.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\54.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\55.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\56.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\57.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\58.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\59.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\60.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\61.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\62.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\63.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\64.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\65.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\66.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\67.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\68.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\69.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\70.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\71.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\72.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\73.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\74.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\75.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\76.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\77.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\78.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\79.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\80.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\81.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\82.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\83.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\84.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\85.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\86.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\87.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\88.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\89.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\90.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\91.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\92.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\93.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\94.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\95.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\96.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\97.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\98.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\99.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\100.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\101.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\102.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\103.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\104.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\105.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\106.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\107.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\108.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\109.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\110.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\111.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\112.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\113.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\114.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\115.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\116.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\117.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\118.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\119.gif'),
            pygame.image.load(r'D:\Proyectos\imágenes\smoke\120.gif')
        ]
        self._bg_lvl = pygame.image.load(r'D:\Proyectos\imágenes\map.png')
        self._ost = pygame.mixer.Sound('D:\Proyectos\sounds\main_ost.wav')

    def createLevel(self, ventana, posx, posy):  # ,posc_1, posc_2, posc_3, posc_1x, posc_2x, posc_3x

        self._posY = 0
        self._posY2 = 100
        self._posY3 = 150
        self._posX = 0
        self._posX2 = 0
        self._posX3 = 0

        self._posY += posy
        self._posY2 += posy
        self._posY3 += random.randrange(1) * posy
        self._posX += 0.25 * posx
        self._posX2 += 2 * posx
        self._posX3 += 0.5 * posx

        ventana.blit(self._bg_lvl, (0, 0))
        ventana.blit(self._objects[1], (self._posX, self._posY))
        ventana.blit(self._objects[0], (self._posX2, self._posY2))
        ventana.blit(self._objects[0], (self._posX2 * 0.5, self._posY2))
        ventana.blit(self._objects[2], (self._posX3, self._posY3))
        self._ost.play()

    def createEffects(self, window, cont_img, posx, posy):
        window.blit(self._fire[cont_img], (posx, posy))

    def createObst(self, posx, posy):
        self._obstacle = (posx, posy, 60, 100)

        return pygame.draw.rect(window, (255, 0, 0), self._obstacle, 1)


# GLOBAL VARIABLES
exit = False
intro = True

if __name__ == "__main__":
    pygame.init()
    import math

    # variables----------------
    cont_img = 0
    act_anim_walk = False
    act_anim_jump = False
    v_x = 0
    pos_x = 0
    pos_y = 0
    posxSky = -600
    posxClouds = 0
    posyPel = 100
    posxpel = 0
    posxcov = -600
    posycov = 100
    cont_effect = 0
    cont_cs = 0

    # Objetos------------------
    player_1 = Player()
    nivel_1 = Level()
    fps = pygame.time.Clock()  # Framerate
    window = pygame.display.set_mode([600, 338])  # Tamaño de la ventana
    pygame.display.set_caption("BETA GAME")  # Nombre de la ventana
    sky_cs = pygame.image.load('D:\Proyectos\imágenes\cutscenes\sky_cs.png')
    cloud_cs = pygame.image.load('D:\Proyectos\imágenes\cutscenes\clouds_cs.png')
    pelican_cs = pygame.image.load('D:\Proyectos\imágenes\cutscenes\pelican_cs.png')
    cov_cs = pygame.image.load('D:\Proyectos\imágenes\cutscenes\covenant_sc1.png')
    cs_sound = pygame.mixer.Sound('D:\Proyectos\sounds\cs_1.wav')
    cs = [
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\0.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\1.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\2.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\3.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\4.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\5.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\6.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\7.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\8.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\9.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\10.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\11.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\12.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\13.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\14.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\15.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\16.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\17.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\18.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\19.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\20.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\21.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\22.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\23.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\24.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\25.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\26.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\27.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\28.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\29.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\30.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\31.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\32.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\33.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\34.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\35.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\36.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\37.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\38.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\39.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\40.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\41.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\42.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\43.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\44.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\45.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\46.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\47.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\48.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\49.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\50.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\51.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\52.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\53.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\54.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\55.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\56.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\57.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\58.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\59.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\60.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\61.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\62.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\63.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\64.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\65.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\66.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\67.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\68.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\69.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\70.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\71.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\72.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\73.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\74.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\75.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\76.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\77.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\78.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\79.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\80.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\81.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\82.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\83.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\84.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\85.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\86.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\87.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\88.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\89.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\90.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\91.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\92.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\93.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\94.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\95.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\96.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\97.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\98.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\99.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\100.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\101.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\102.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\103.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\104.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\105.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\106.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\107.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\108.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\109.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\110.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\111.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\112.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\113.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\114.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\115.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\116.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\117.gif'),
        pygame.image.load(r'D:\Proyectos\imágenes\cinematic\118.gif'),
    ]

    def cutscene(contador):
        return window.blit(cs[contador],(10,10))

    while intro == True:
        fps.tick(20)
        cs_time = pygame.time.get_ticks()


        if cs_time > 22000:
            intro = False
            exit = True

        for evento in pygame.event.get():

            if evento.type == pygame.KEYDOWN:

                if evento.key == K_BACKSPACE:
                    intro = False
                    exit = True

        if intro == True:
            cs_sound.play()
        else:
            cs_sound.stop()

        if cs_time >= 17000:
            posxpel += 0.01
            posyPel += 2*math.sin(posxpel)
        else:
            posxpel += 0.5
            posyPel += 2 * math.sin(posxpel)

        if cs_time >= 6000:
            posxcov += 2
            posycov += math.sin(posxpel)

        posxSky += 0.1
        posxClouds -= 150

        if posxSky == 600:
            posxSky = -1200

        if posxClouds == -1200:
            posxClouds = 900

        window.blit(sky_cs, (posxSky, 0))
        window.blit(cloud_cs, (posxClouds, 200))
        window.blit(cloud_cs, (posxClouds, -250))
        window.blit(cloud_cs, (posxClouds, -100))
        window.blit(pelican_cs, (150, posyPel))
        window.blit(cov_cs, (posxcov, posycov))

        if cs_time > 8500 and cs_time < 14000:
            cont_cs += 1
            if cont_cs >= 118:
                cont_cs = 0
            cutscene(cont_cs)

        pygame.display.update()
        print(cs_time)

    while exit:  # Ciclo que mantiene a la ventana abierta

        for evento in pygame.event.get():

            if evento.type == QUIT:
                exit = False
            if evento.type == pygame.KEYDOWN:

                if evento.key == K_RIGHT:
                    act_anim_walk = True
                    v_x = 5
                if evento.key == K_LEFT:
                    v_x = -5
                if evento.key == K_UP:
                    act_anim_jump = True
                    player_1.mover(0,-20)
            if evento.type == pygame.KEYUP:

                if evento.key == K_RIGHT:
                    act_anim_walk = False
                    v_x = 0
                if evento.key == K_LEFT:
                    v_x = 0
                if evento.key == K_UP:
                    act_anim_jump = False
                    player_1.mover(0,20)

        pos_rel = player_1.mover(v_x,0)
        pos_x += 10         # Posición de los objetos de fondo
        if pos_x == 2500:   # Cambio de posición en Y de los elementos de fondo
            pos_x = -2000
            pos_y = int(random.randrange(50))

        if pos_rel >= 510:
            v_x = 0
            pos_rel = 510
        if pos_rel <= 0:
            v_x = 0
            pos_rel = 0

        cont_effect += 1

        if cont_effect == 121:
            cont_effect = 0

        if act_anim_walk == True:
            cont_img += 1
            print(cont_img)
            if cont_img >= 9:
                cont_img = 0
        else:
            cont_img = 0

        if act_anim_jump == True:
            cont_img = 9
            cont_img += 1
            print(cont_img)

            if cont_img > 10:
                cont_img = 9

        fps.tick(30)
        nivel_1.createLevel(window, pos_x, pos_y)  # , pos_p, pos_sc, pos_p2, pos_py, pos_p2y, pos_scy
        nivel_1.createEffects(window, cont_effect, -150, 0)
        obs_1 = nivel_1.createObst(100, 179)
        obs_2 = nivel_1.createObst(400, 179)
        player_1.drawPlayerWalk(window, cont_img)
        player_1.Colision(obs_1)
        player_1.Colision(obs_2)
        pygame.display.update()
