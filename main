import pygame
import minesweeper as ms

number_colors = {
    1: (0, 0, 255),
    2: (0, 128, 0),
    3: (255, 0, 0),
    4: (128, 0, 128),
    5: (128, 0, 0),
    6: (64, 224, 208),
    7: (0, 0, 0),
    8: (128, 128, 128)
}
def drawGame(screen, board, checked, flagged, first):
    flag = pygame.image.load("img/flag.png")
    flag = pygame.transform.scale(flag, (800//len(board)-5, 800//len(board)-5))
    if first:
        board = board[1:len(board)-1]
        for i in range(len(board)):
            board[i] = board[i][1:len(board[i])-1]
    for i in range(len(board)):
        for j in range(len(board[i])):
            pygame.draw.rect(screen, (169,169,169), (i * 800//len(board), j*800//len(board), 800//len(board)-2.5, 800//len(board)-2.5), border_radius=2)
    if not first:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if checked[i][j] and not flagged[i][j]:
                    pygame.draw.rect(screen, (255, 255, 255), (i * 800//len(board), j*800//len(board), 800//len(board)-2.5, 800//len(board)-2.5), border_radius=2)
                    if board[i][j] != '*' and board[i][j] != 0:
                        font = pygame.font.SysFont('Arial', 88-5*len(board), bold=True)
                        text_surface = font.render(str(board[i][j]), True, number_colors[board[i][j]])
                        screen.blit(text_surface, dest=(i * 800//len(board)+(800//len(board))//3, j*800//len(board)+(800//len(board))//3))
                    if board[i][j] == '*':
                        screen.blit(flag, dest=(i * 800//len(board), j*800//len(board)))
                if flagged[i][j]:
                    screen.blit(flag, (i * 800//len(board), j*800//len(board)))

pygame.init()
pygame.display.set_caption("Minesweeper")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
difficulty = 0
screen = pygame.display.set_mode((800, 800))
start = True
first_click = True
lost = False
running = True
won = False
ecolor = (200, 240, 250)
mcolor = (173, 216, 230)
hcolor = (173, 216, 230)

while running:
    if start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] < 485 and event.pos[0] > 320 and event.pos[1] < 435 and event.pos[1] > 390:
                    game = ms.MineSweeper(difficulty)
                    start = False
                if event.pos[0] < 485 and event.pos[0] > 320 and event.pos[1] < 375 and event.pos[1] > 330:
                    difficulty = 1
                    ecolor = (173, 216, 230)
                    mcolor = (200, 240, 250)
                    hcolor = (173, 216, 230)
                if event.pos[0] < 305 and event.pos[0] > 140 and event.pos[1] < 375 and event.pos[1] > 330:
                    difficulty = 0
                    ecolor = (200, 240, 250)
                    mcolor = (173, 216, 230)
                    hcolor = (173, 216, 230)
                if event.pos[0] < 665 and event.pos[0] > 500 and event.pos[1] < 375 and event.pos[1] > 330:
                    difficulty = 2
                    ecolor = (173, 216, 230)
                    mcolor = (173, 216, 230)
                    hcolor = (200, 240, 250)
                
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (173, 216, 230), (320, 390, 165, 45), border_radius=20)
        font = pygame.font.SysFont('Arial', 25)
        text_surface = font.render("Click to start", True, (0, 0, 0))
        screen.blit(text_surface, dest=(330, 400))

        pygame.draw.rect(screen, mcolor, (320, 330, 165, 45), border_radius=20)
        text_surface = font.render("Medium", True, (0, 0, 0))
        screen.blit(text_surface, dest=(355, 340))

        pygame.draw.rect(screen, ecolor, (140, 330, 165, 45), border_radius=20)
        text_surface = font.render("Easy", True, (0, 0, 0))
        screen.blit(text_surface, dest=(190, 340))

        pygame.draw.rect(screen, hcolor, (500, 330, 165, 45), border_radius=20)
        text_surface = font.render("Hard", True, (0, 0, 0))
        screen.blit(text_surface, dest=(555, 340))

        font = pygame.font.SysFont('Arial', 75)
        text_surface = font.render("Minesweeper", True, (0, 0, 0))
        screen.blit(text_surface, dest=(175, 100))
        pygame.display.flip()

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if first_click:
                        game.check_square(event.pos[0]//(800//(len(game.board)-2)), event.pos[1]//(800//(len(game.board)-2)))
                        first_click = False

                    else:
                        if game.check_square(event.pos[0]//(800//len(game.board)), event.pos[1]//(800//len(game.board))) == '*':
                            lost = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    game.flag_square(event.pos[0]//(800//len(game.board)), event.pos[1]//(800//len(game.board)))
        if not won and not lost:
            screen.fill((0, 0, 0))
            drawGame(screen, game.board, game.checked, game.flagged, first_click)
            won = game.did_win()
            

        pygame.display.flip()

        if lost:
            screen.fill((255,255,255))
            font = pygame.font.SysFont('Arial', 75)
            text_surface = font.render("You lost", True, (0, 0, 0))
            screen.blit(text_surface, dest=(250, 100))
            pygame.display.flip()

        if won:
            screen.fill((255,255,255))
            font = pygame.font.SysFont('Arial', 75)
            text_surface = font.render("You won", True, (0, 0, 0))
            screen.blit(text_surface, dest=(250, 100))
            pygame.display.flip()



pygame.quit()