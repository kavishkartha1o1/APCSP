# Libraries:
import random
import time
import pygame
pygame.init()

# Game Window
gameWindowWidth = 500
gameWindowHeight = 500
gameWindow = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))
background = pygame.image.load("galaxy.jpg")
pygame.display.set_caption("Game Window")

# Public Text Class
class textClass():
    def __init__(self, txt, color, size):
        self.text = txt
        self.textColor = color
        self.textSize = size
        self.textFont = "freesansbold.ttf"
    def textDisplay(self):
        font = pygame.font.Font(self.textFont, self.textSize)
        displayText = font.render(self.text, True, self.textColor)
        return displayText

# Score Tracking List:
scoreList = []

def gameLoop():
    # Characters and Objects:
    class playerSpaceShip():
        def __init__(self, x, y):
            self.playerSpaceShipx = x
            self.playerSpaceShipy = y
            self.playerSpaceShipWidth = 64
            self.playerSpaceShipHeight = 64
            self.playerSpaceShipSpeed = 10
            self.playerSpaceShipSprite = pygame.image.load("spaceship.png") 
        def drawSpaceShip(self):
            gameWindow.blit(self.playerSpaceShipSprite, (self.playerSpaceShipx, self.playerSpaceShipy))

    class bulletClass():
        def __init__(self, x, y):
            self.bulletx = x
            self.bullety = y
            self.bulletWidth = 3
            self.bulletHeight = 7
            self.bulletSpeed = 8
            self.bulletColor = (255, 0, 0)
        def bulletCollision(self):
            bulletList.pop(bulletList.index(bullet))
        def drawBullet(self):
            pygame.draw.rect(gameWindow, self.bulletColor, (self.bulletx, self.bullety, self.bulletWidth, self.bulletHeight))

    class fireballClass():
        def __init__(self, x, y):
            self.fireballx = x
            self.firebally = y
            self.fireballWidth = 29
            self.fireballHeight = 65   
            self.fireballSpeed = 8
            self.fireballRandNum = random.randint(0, 1)
            self.fireballPlus = False
            self.fireballMinus = False
            self.fireballSprite = pygame.image.load("fireball.png")
        def fireballCollision(self):
            fireballList.pop(fireballList.index(fireball))
        def drawFireball(self):
            gameWindow.blit(self.fireballSprite, (self.fireballx, self.firebally))

    # Draw Characters and Objects:      
    def drawGameWindow():
        gameWindow.blit(background, (0, 0))
        spaceship.drawSpaceShip()
        for bullet in bulletList:
            bullet.drawBullet()
        for fireball in fireballList:
            fireball.drawFireball()
        gameWindow.blit(scoreDisplayText, (430, 20))
        gameWindow.blit(highScoreDisplayText, (392, 35))
        pygame.display.update()

    # Main Loop:
    spaceship = playerSpaceShip(215, 400)
    bulletList = []
    fireballList = []
    score = 0
    def scoreListMethod():
        scoreList.append(str(score) + " ")
        
    def scoreFileWriteMethod():
        scoreFileWrite = open("playerScore.txt", "a")
        scoreFileWrite.writelines(scoreList)

    def listSplitMethod(list):
        return list[0].split()

    def listConvertNum(list):
        for n in range(0, len(list)): 
            list[n] = int(list[n]) 

    scoreFileRead = open("playerScore.txt", "r")
    scoreFileText = scoreFileRead.read()
    scoreFileList = []
    scoreFileList.append(scoreFileText)
    scoreFileList2 = listSplitMethod(scoreFileList)
    listConvertNum(scoreFileList2)
    playerHighScore = max(scoreFileList2)
    if len(scoreFileList2) == 0:
        playerHighScore = 0
    gameRunning = True
    while gameRunning == True:
        gameClock = pygame.time.Clock()
        gameClock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

        # Bullets:
        for bullet in bulletList:
            if bullet.bullety < gameWindowHeight and bullet.bullety > 0:
                bullet.bullety -= bullet.bulletSpeed
            else:
                bulletList.pop(bulletList.index(bullet))
        
        # Fireballs:
        for fireball in fireballList:
            if fireball.firebally < gameWindowHeight and fireball.firebally > 0:
                fireball.firebally += fireball.fireballSpeed
            else:
                fireballList.pop(fireballList.index(fireball))
            if fireball.fireballRandNum == 1:
                fireball.fireballSprite = pygame.image.load('fireball2.png')
                fireball.fireballPlus = False
            else:
                fireball.fireballSprite = pygame.image.load('fireball.png')
                fireball.fireballPlus = True
        if len(fireballList) < 4:
            fireballList.append(fireballClass(random.randrange((spaceship.playerSpaceShipWidth // 2), (gameWindowWidth - (spaceship.playerSpaceShipWidth))), 1))
        
        # Game Over:
        red = (255, 0, 0)
        gameOver = textClass("Game Over!", red, 50)
        gameOverTextDisplay = gameOver.textDisplay()
        gameOverRect = gameOverTextDisplay.get_rect()
        gameOverRect.center = ((gameWindowWidth//2), (gameWindowHeight//2))
        def gameOverMethod():
            score = 0
            gameWindow.blit(gameOverTextDisplay, gameOverRect)
            pygame.display.update()
            time.sleep(2)
            gameLoop()

        # New Record:
        newRecord = textClass("New Record!", red, 50)
        newRecordTextDisplay = newRecord.textDisplay()
        newRecordRect = newRecordTextDisplay.get_rect()
        newRecordRect.center = ((gameWindowWidth//2), (gameWindowHeight))
        def newRecordMethod():
            gameWindow.blit(newRecordTextDisplay, gameOverRect)
            pygame.display.update()
            time.sleep(2)
            gameLoop()

        # Score Text:
        scoreText = textClass("Score: " + str(score), red, 15)
        scoreDisplayText = scoreText.textDisplay()
        highScoreText = textClass("High Score: " + str(playerHighScore), red, 15)
        highScoreDisplayText = highScoreText.textDisplay()

        # Collisions:
        def bulletCollision(x1, y1, width1, height1, x2, y2, width2, height2):
            if x2 <= x1 <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            elif x2 <= x1 + width1 <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            else:
                return False
        
        def spaceshipCollision(x1, y1, width1, height1, x2, y2, width2, height2):
            if x2 <= x1 <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            elif x2 <= x1 + width1 <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            elif x2 <= x1 + width1 <= x2 + width2 and y2 <= y1 + height1 <= y2 + height2:
                return True
            elif x2 <= x1 + width1 <= x2 + width2 and y2 <= y1 + height1 <= y2 + height2:
                return True
            elif x1 <= x2 <= x1 + width1 and x1 <= x2 + width2 <= x1 + width1:
                if y1 <= y2 + height2 <= y1 + height1 and y1 <= y2 + height2 <= y1 + height1:
                    return True 
            else:
                return False
        
        for bullet in bulletList:
            for fireball in fireballList:
                collision = bulletCollision(bullet.bulletx, bullet.bullety, bullet.bulletWidth, bullet.bulletHeight, fireball.fireballx, fireball.firebally, fireball.fireballWidth, fireball.fireballHeight)
                if collision == True:
                    fireball.fireballCollision()
                    bullet.bulletCollision()
                    if fireball.fireballPlus == True:
                        score += 1
                    elif score == 0 and fireball.fireballPlus == False:
                        scoreListMethod()
                        scoreFileWriteMethod()
                        gameOverMethod()
                    else:
                        score -= 1
        
        for fireball in fireballList:
            crash = spaceshipCollision(spaceship.playerSpaceShipx, spaceship.playerSpaceShipy, spaceship.playerSpaceShipWidth, spaceship.playerSpaceShipHeight, fireball.fireballx, fireball.firebally, fireball.fireballWidth, fireball.fireballHeight)
            if crash == True:
                scoreListMethod()
                scoreFileWriteMethod()
                if score > playerHighScore:
                    newRecordMethod()
                else:
                    gameOverMethod()

        # Music and Sound Effects:
        def bulletSoundEffect():
            pygame.mixer.music.load("bulletsoundeffect.wav")
            pygame.mixer.music.play()

        # Key Presses:
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_LEFT] == True and spaceship.playerSpaceShipx >= spaceship.playerSpaceShipSpeed:
            spaceship.playerSpaceShipx -= spaceship.playerSpaceShipSpeed
        if keyPressed[pygame.K_RIGHT] == True and spaceship.playerSpaceShipx < gameWindowWidth - spaceship.playerSpaceShipWidth - spaceship.playerSpaceShipSpeed:
            spaceship.playerSpaceShipx += spaceship.playerSpaceShipSpeed
        if keyPressed[pygame.K_UP] == True and spaceship.playerSpaceShipy >= spaceship.playerSpaceShipSpeed:
            spaceship.playerSpaceShipy -= spaceship.playerSpaceShipSpeed
        if keyPressed[pygame.K_DOWN] == True and spaceship.playerSpaceShipy < gameWindowHeight - spaceship.playerSpaceShipHeight - spaceship.playerSpaceShipSpeed:
            spaceship.playerSpaceShipy += spaceship.playerSpaceShipSpeed
        if keyPressed[pygame.K_SPACE] == True:
            bulletSoundEffect()
            if len(bulletList) < 25:
                bulletList.append(bulletClass(round(spaceship.playerSpaceShipx + spaceship.playerSpaceShipWidth // 2), spaceship.playerSpaceShipy))
        drawGameWindow()
    pygame.quit()
gameLoop()