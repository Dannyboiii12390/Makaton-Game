import pygame as py
import classes
py.init()

LIGHT_BLUE = (52, 180, 235)

def drawGameScreen(scr, matchHB, swapHB, imageHB, meaningHB, imageBox, k, score, questionsAnswered): #will update the screen
    global LIGHT_BLUE
    #redraws the backround
    scr.setbg()

    matchHB.draw(scr)
    swapHB.draw(scr)
    imageHB.draw(scr)
    meaningHB.draw(scr)

    imageBox.draw(scr,k)

    swapHB.text(scr,"SWAP", scr.width//9, 6.4*scr.height//10 )
    matchHB.text(scr,"MATCH",9*scr.width//10-scr.width//2.875, 6.4*scr.height//10)
    meaningHB.text(scr, imageBox.correct, 9*scr.width//10-scr.width//2.875, 2.5*scr.height//10)

    # questions answered correctly in the middle of the screen
    font = py.font.SysFont("Helvetica", 45)

    #initialising the start game text
    scoreText= font.render('SCORE', True, LIGHT_BLUE)
    scoreText_rect = scoreText.get_rect(center = (scr.width//2,scr.height//2))
    scoreText_rect[1] -= scoreText.get_rect()[3]

    # initialising the quit game text
    showScoreText = font.render(str(score), True, LIGHT_BLUE)
    showScoreText_rect = showScoreText.get_rect(center = (scr.width//2,scr.height//2))

    #loads score text onto screen to show user their current score
    scr.WINDOW.blit(scoreText, (scoreText_rect[0], scoreText_rect[1]))
    scr.WINDOW.blit(showScoreText, (showScoreText_rect[0],showScoreText_rect[1]))

    #initialising the start game text
    questionsAnweredText= font.render('ANSWERED', True, LIGHT_BLUE)
    questionsAnweredText_rect = questionsAnweredText.get_rect(center = (scr.width//2, scr.height//2))
    questionsAnweredText_rect[1] -= 3*(questionsAnweredText.get_rect()[3])

    # initialising the quit game text
    showQuestionsAnweredText = font.render(str(questionsAnswered), True, LIGHT_BLUE)
    showQuestionsAnweredText_rect = showQuestionsAnweredText.get_rect(center = (scr.width//2,scr.height//2))
    showQuestionsAnweredText_rect[1] -= 2*(showQuestionsAnweredText.get_rect()[3])

    #shows user how many questions have been answered
    scr.WINDOW.blit(questionsAnweredText, (questionsAnweredText_rect[0], questionsAnweredText_rect[1]))
    scr.WINDOW.blit(showQuestionsAnweredText, (showQuestionsAnweredText_rect[0], showQuestionsAnweredText_rect[1]))

    py.display.update()

def setup(): # initialize the class objects
    
    with open("settings.txt") as f:
        a = f.readline()
        b,c = a.split(":")
        width, height = c.split(",")
        width, height = int(width), int (height)

        a = f.readline()
        b,FPS = a.split(":")
        FPS = int(FPS)
        
        c = f.readline()
        d,numRounds = c.split(":")
        numRounds = int(numRounds)


    #instantiates the screen object
    scr = classes.Screen(width, height)
    
    #creates a clock to set a frame limit
    clock = py.time.Clock()
    
    
    score = questionsAnswered = 0
    

    #creates the hit box for the boxes
    matchHB = classes.hitBox((9*scr.width//10)-(scr.width//3), 7*scr.height//10, scr.width//3, scr.height//7) 
    swapHB = classes.hitBox(scr.width//10, 7*scr.height//10, scr.width//3, scr.height//7) 
    imageHB = classes.hitBox(scr.width//10, scr.height//10, scr.width//3, scr.height//2) 
    meaningHB = classes.hitBox((9*scr.width//10)-(scr.width//3), scr.height//10, scr.width//3, scr.height//2)
    
    imageBox = classes.imgBox(scr.width//10, scr.height//10, scr.width//3, scr.height//2)
    
    return FPS, clock, scr, matchHB, swapHB, imageHB, meaningHB, imageBox, score, questionsAnswered, numRounds

def main(): # main function
    FPS, clock, scr, matchHB, swapHB, imageHB, meaningHB, imageBox, score, questionsAnswered, numRounds = setup()
    k = 0
    run = True
    click = False
    while run:
        
        if questionsAnswered >= numRounds:
            run = False

        clock.tick(FPS)
        mx,my = py.mouse.get_pos()
        
        if click:
            if swapHB.HB.collidepoint((mx,my)):
                k = swapHB.clicked()
            
            if matchHB.HB.collidepoint((mx,my)):
                if imageBox.checkCorrect(k):
                    score +=1
                questionsAnswered += 1
                k = swapHB.clicked()
                imageBox.randImgs()
        
        click = False

        for event in py.event.get():
            #did the user click the close window button
            if event.type == py.QUIT:
                run = False

            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    run = False

            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


            drawGameScreen(scr, matchHB, swapHB, imageHB, meaningHB, imageBox, k, score, questionsAnswered)


if __name__ == '__main__': # starts the program
    main()