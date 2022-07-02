# import pygame


# pygame.init()
# screen = pygame.display.set_mode((1200, 700))
# bgimg = pygame.image.load('level.png')
# playerimg = pygame.image.load('bandicoot_crouch1.png')

# playerx = 100
# playery = 500
# playerstepx = 0
# playerstepy = 0


# def zuo():

#     filepath = r"D:\Python文件\zuo.ogg"
#     pygame.mixer.init()
#     pygame.mixer.music.load(filepath)
#     pygame.mixer.music.play()


# def you():

#     filepath = r"D:\Python文件\you.ogg"
#     pygame.mixer.init()
#     pygame.mixer.music.load(filepath)
#     pygame.mixer.music.play()


# def jump():

#     filepath = r"D:\Python文件\jump.ogg"
#     pygame.mixer.init()
#     pygame.mixer.music.load(filepath)
#     pygame.mixer.music.play()


# def space():

#     filepath = r"D:\Python文件\space.ogg"
#     pygame.mixer.init()
#     pygame.mixer.music.load(filepath)
#     pygame.mixer.music.play()


# running = True
# while running:
#     screen.blit(bgimg, (0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 you()
#             if event.key == pygame.K_LEFT:
#                 zuo()
#             if event.key == pygame.K_UP:
#                 jump()
#             if event.key == pygame.K_SPACE:
#                 space()
#     screen.blit(playerimg, (playerx, playery))
#     pygame.display.update()
