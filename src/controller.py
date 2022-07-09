import sys
import pygame
import random

class Controller:
    def __init__(self, width = 680, height = 780):
        self.screen = pygame.display.set_mode((width, height))
        self.game_screen = pygame.display.set_mode((width, height))
        self.newScreen = pygame.display.set_mode((width, height))
        self.game_img = pygame.image.load('images/background.png').convert_alpha()
        self.gameOverScreen = pygame.display.set_mode((width, height))
        self.X = pygame.image.load("images/ticTacToeX.png").convert_alpha()
        self.X = pygame.transform.scale(self.X, [180, 180])
        self.O = pygame.image.load("images/ticTacToeO.png").convert_alpha()
        self.O = pygame.transform.scale(self.O, [180, 180])
        self.state = "BEGIN"
        self.width = width
        self.height = height

        self.white = (255, 255, 255)
        self.mid = False
        self.topLeft = False
        self.topRight = False
        self.midLeft = False
        self.midRight = False
        self.midBottom = False
        self.midTop = False
        self.bottomRight = False
        self.bottomLeft = False
        self.movesList = [[[] for i in range(3)] for i in range(3)]
        self.black = (0, 0, 0)
        self.count = 0

        self.num = random.randint(1,2)
        if self.num == 1:
            self.Xturn = True
        else:
            self.Xturn = False

    def mainLoop(self):
        while True:
            if self.state == "BEGIN":
                self.gameIntro()
            elif self.state == "START":
                self.gameLoop()
            elif self.state == "END":
                self.gameOver()
            else:
                self.updateEveything()


    def gameIntro(self):
        color = (255, 215, 0, 255)
        my_font = pygame.font.SysFont("impact", 30)
        title_font = pygame.font.SysFont("impact", 30)
        name_of_game = title_font.render('Tic Tac Toe', False, self.black)
        instructions = my_font.render('Press space to play.', False, self.black)

        self.screen.fill(color)
        self.screen.blit(name_of_game, ((self.width / 3) + 50, self.height/4))
        self.screen.blit(instructions, ((self.width / 3), self.height/3))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "START"
                    self.setUp()
                    self.mainLoop()

    def setUp(self):
        self.game_screen.fill(color = (255, 215, 0, 255))
        self.game_screen.blit(self.game_img, self.game_img.get_rect())
        my_font = pygame.font.SysFont("impact", 50)
        if self.Xturn:
            first_move = my_font.render('X goes first!', False, self.black)
        else:
            first_move = my_font.render('O goes first!', False, self.black)
        self.screen.blit(first_move, ((self.width / 3), self.height - 60))
        pygame.display.update()

        #reupdates itself too often

    def setUpGameOver(self, winner):
        self.gameOverScreen.fill(color = (255, 215, 0, 255))
        myFont = pygame.font.SysFont("impact", 60)
        if winner == 1:
            gameOverMsg = myFont.render("X's won the game!", False, self.black)
            self.gameOverScreen.blit(gameOverMsg, ((self.width / 3) - 100, self.height / 4))
        elif winner == 2:
            gameOverMsg = myFont.render("O's won the game!", False, self.black)
            self.gameOverScreen.blit(gameOverMsg, ((self.width / 3) - 100, self.height / 4))
        else:
            newMsg = myFont.render("No winner!", False, self.black)
            self.gameOverScreen.blit(newMsg, ((self.width / 3), self.height / 4))
        extra_instructions = myFont.render("Press \'q'" " to quit", False, self.black)
        self.gameOverScreen.blit(extra_instructions, ((self.width / 3) - 65, (self.height / 3) + 50))
        self.mainLoop()


    def gameLoop(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif pygame.mouse.get_pressed()[0]:
                if self.num == 1:
                    if self.Xturn:
                    #This means that X's will go first
                        if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and (pygame.mouse.get_pos()[1] <= 460 and pygame.mouse.get_pos()[1] >= 200):
                            #mid
                            if self.mid:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (250, 250))
                                self.mid = True
                                self.Xturn = False
                                self.movesList[1][1] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] <= 200:
                            #midTop
                            if self.midTop:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (250, 20))
                                self.midTop = True
                                self.Xturn = False
                                #1 for X, 2 for O
                                self.movesList[1][0] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 465 and (pygame.mouse.get_pos()[1] <= 460 and pygame.mouse.get_pos()[1] >= 200):
                            #midRight
                            if self.midRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (480, 250))
                                self.midRight = True
                                self.Xturn = False
                                self.movesList[2][1] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] <= 200:
                            #topLeft
                            if self.topLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (20, 20))
                                self.topLeft = True
                                self.Xturn = False
                                self.movesList[0][0] = 1
                                self.count += 1


                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 460:
                            #midLeft
                            if self.midLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (20, 250))
                                self.midLeft = True
                                self.Xturn = False
                                self.movesList[0][1] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] >= 460 and pygame.mouse.get_pos()[1] <= 680:
                            #bottomLeft
                            if self.bottomLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (20, 480))
                                self.bottomLeft = True
                                self.Xturn = False
                                self.movesList[0][2] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 465 and pygame.mouse.get_pos()[1] <= 200:
                            if self.topRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (480, 20))
                                self.topRight = True
                                self.Xturn = False
                                self.movesList[2][0] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 460 and pygame.mouse.get_pos()[1] >= 460:
                            if self.bottomRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (480, 480))
                                self.bottomRight = True
                                self.Xturn = False
                                self.movesList[2][2] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] >= 460:
                            if self.midBottom:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (250, 480))
                                self.midBottom = True
                                self.Xturn = False
                                self.movesList[1][2] = 1
                                self.count += 1

                    elif not self.Xturn:
                        if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and (pygame.mouse.get_pos()[1] <= 460 and pygame.mouse.get_pos()[1] >= 200):
                            # mid
                            if self.mid:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (250, 250))
                                self.mid = True
                                self.Xturn = True
                                self.movesList[1][1] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] <= 200:
                            # midTop
                            if self.midTop:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (250, 20))
                                self.midTop = True
                                self.Xturn = True
                                self.movesList[1][0] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 460 and (pygame.mouse.get_pos()[1] <= 400 and pygame.mouse.get_pos()[1] >= 200):
                            # midRight
                            if self.midRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (480, 250))
                                self.midRight = True
                                self.Xturn = True
                                self.movesList[2][1] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] <= 200:
                            # topLeft
                            if self.topLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (20, 20))
                                self.topLeft = True
                                self.Xturn = True
                                self.movesList[0][0] = 2
                                self.count += 1


                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] >= 240 and pygame.mouse.get_pos()[1] <= 460:
                            # midLeft
                            if self.midLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (20, 250))
                                self.midLeft = True
                                self.Xturn = True
                                self.movesList[0][1] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] >= 460 and pygame.mouse.get_pos()[1] <= 680:
                            # bottomLeft
                            if self.bottomLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (20, 480))
                                self.bottomLeft = True
                                self.Xturn = True
                                self.movesList[0][2] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 465 and pygame.mouse.get_pos()[1] <= 200:
                            if self.topRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (480, 20))
                                self.topRight = True
                                self.Xturn = True
                                self.movesList[2][0] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 460 and pygame.mouse.get_pos()[1] >= 460:
                            if self.bottomRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (480, 480))
                                self.bottomRight = True
                                self.Xturn = True
                                self.movesList[2][2] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] >= 460:
                            if self.midBottom:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (250, 480))
                                self.midBottom = True
                                self.Xturn = True
                                self.movesList[1][2] = 2
                                self.count += 1

                elif self.num == 2:
                    if not self.Xturn:
                        #This means that O's will go first
                        if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and (pygame.mouse.get_pos()[1] <= 460 and pygame.mouse.get_pos()[1] >= 200):
                            # mid
                            if self.mid:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (250, 250))
                                self.mid = True
                                self.Xturn = True
                                self.movesList[1][1] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] <= 200:
                            # midTop
                            if self.midTop:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (250, 20))
                                self.midTop = True
                                self.Xturn = True
                                self.movesList[1][0] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 460 and (pygame.mouse.get_pos()[1] <= 400 and pygame.mouse.get_pos()[1] >= 200):
                            # midRight
                            if self.midRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (480, 250))
                                self.midRight = True
                                self.Xturn = True
                                self.movesList[2][1] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] <= 200:
                            # topLeft
                            if self.topLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (20, 20))
                                self.topLeft = True
                                self.Xturn = True
                                self.movesList[0][0] = 2
                                self.count += 1


                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] >= 240 and pygame.mouse.get_pos()[1] <= 460:
                            # midLeft
                            if self.midLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (20, 250))
                                self.midLeft = True
                                self.Xturn = True
                                self.movesList[0][1] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] >= 460 and pygame.mouse.get_pos()[1] <= 680:
                            # bottomLeft
                            if self.bottomLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (20, 480))
                                self.bottomLeft = True
                                self.Xturn = True
                                self.movesList[0][2] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 465 and pygame.mouse.get_pos()[1] <= 200:
                            if self.topRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (480, 20))
                                self.topRight = True
                                self.Xturn = True
                                self.movesList[2][0] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 460 and pygame.mouse.get_pos()[1] >= 460:
                            if self.bottomRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (480, 480))
                                self.bottomRight = True
                                self.Xturn = True
                                self.movesList[2][2] = 2
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] >= 460:
                            if self.midBottom:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.O, (250, 480))
                                self.midBottom = True
                                self.Xturn = True
                                self.movesList[1][2] = 2
                                self.count += 1
                    elif self.Xturn:
                        if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and (pygame.mouse.get_pos()[1] <= 460 and pygame.mouse.get_pos()[1] >= 200):
                            #mid
                            if self.mid:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (250, 250))
                                self.mid = True
                                self.Xturn = False
                                self.movesList[1][1] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] <= 200:
                            #midTop
                            if self.midTop:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (250, 20))
                                self.midTop = True
                                self.Xturn = False
                                self.movesList[1][0] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 465 and (pygame.mouse.get_pos()[1] <= 460 and pygame.mouse.get_pos()[1] >= 200):
                            #midRight
                            if self.midRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (480, 250))
                                self.midRight = True
                                self.Xturn = False
                                self.movesList[2][1] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] <= 200:
                            #topLeft
                            if self.topLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (20, 20))
                                self.topLeft = True
                                self.Xturn = False
                                self.movesList[0][0] = 1
                                self.count += 1


                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 460:
                            #midLeft
                            if self.midLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (20, 250))
                                self.midLeft = True
                                self.Xturn = False
                                self.movesList[0][1] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] >= 460 and pygame.mouse.get_pos()[1] <= 680:
                            #bottomLeft
                            if self.bottomLeft:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (20, 480))
                                self.bottomLeft = True
                                self.Xturn = False
                                self.movesList[0][2] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 465 and pygame.mouse.get_pos()[1] <= 200:
                            if self.topRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (480, 20))
                                self.topRight = True
                                self.Xturn = False
                                self.movesList[2][0] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 460 and pygame.mouse.get_pos()[1] >= 460:
                            if self.bottomRight:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (480, 480))
                                self.bottomRight = True
                                self.Xturn = False
                                self.movesList[2][2] = 1
                                self.count += 1

                        elif pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] >= 460:
                            if self.midBottom:
                                print("Can't go here!")
                            else:
                                self.game_screen.blit(self.X, (250, 480))
                                self.midBottom = True
                                self.Xturn = False
                                self.movesList[1][2] = 1
                                self.count += 1


        #print(str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]))
        pygame.display.update()
        if self.count == 9:
            self.state = "END"
            self.setUpGameOver((3))
        elif self.movesList[0][0] == 1 and self.movesList[0][1] == 1 and self.movesList[0][2] == 1:
            self.state = "END"
            self.setUpGameOver(1)

        elif self.movesList[0][0] == 1 and self.movesList[1][1] == 1 and self.movesList[2][2] == 1:
            self.state = "END"
            self.setUpGameOver(1)

        elif self.movesList[0][0] == 1 and self.movesList[1][0] == 1 and self.movesList[2][0] == 1:
            self.state = "END"
            self.setUpGameOver(1)

        elif self.movesList[0][2] == 1 and self.movesList[1][1] == 1 and self.movesList[2][0] == 1:
            self.state = "END"
            self.setUpGameOver(1)

        elif self.movesList[0][2] == 1 and self.movesList[1][2] == 1 and self.movesList[2][2] == 1:
            self.state = "END"
            self.setUpGameOver(1)

        elif self.movesList[2][0] == 1 and self.movesList[2][1] == 1 and self.movesList[2][2] == 1:
            self.state = "END"
            self.setUpGameOver(1)

        elif self.movesList[1][0] == 1 and self.movesList[1][1] == 1 and self.movesList[1][2] == 1:
            self.state = "END"
            self.setUpGameOver(1)

        elif self.movesList[0][1] == 1 and self.movesList[1][1] == 1 and self.movesList[2][1] == 1:
            self.state = "END"
            self.setUpGameOver(1)

        elif self.movesList[0][0] == 2 and self.movesList[0][1] == 2 and self.movesList[0][2] == 2:
            self.state = "END"
            self.setUpGameOver(2)

        elif self.movesList[0][0] == 2 and self.movesList[1][1] == 2 and self.movesList[2][2] == 2:
            self.state = "END"
            self.setUpGameOver(2)

        elif self.movesList[0][0] == 2 and self.movesList[1][0] == 2 and self.movesList[2][0] == 2:
            self.state = "END"
            self.setUpGameOver(2)

        elif self.movesList[0][2] == 2 and self.movesList[1][1] == 2 and self.movesList[2][0] == 2:
            self.state = "END"
            self.setUpGameOver(2)

        elif self.movesList[0][2] == 2 and self.movesList[1][2] == 2 and self.movesList[2][2] == 2:
            self.state = "END"
            self.setUpGameOver(2)

        elif self.movesList[2][0] == 2 and self.movesList[2][1] == 2 and self.movesList[2][2] == 2:
            self.state = "END"
            self.setUpGameOver(2)

        elif self.movesList[1][0] == 2 and self.movesList[1][1] == 2 and self.movesList[1][2] == 2:
            self.state = "END"
            self.setUpGameOver(2)

        elif self.movesList[0][1] == 2 and self.movesList[1][1] == 2 and self.movesList[2][1] == 2:
            self.state = "END"
            self.setUpGameOver(2)



    def gameOver(self):
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

