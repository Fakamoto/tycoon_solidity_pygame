import pygame


def loop(player):
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((900, 800))

    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    background = GRAY

    font = pygame.font.SysFont(None, 48)

    game_over = False
    state = [0, 0, 0, 0]
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    player.buyLand()
                elif event.key == pygame.K_w:
                    player.buyCollector()
                elif event.key == pygame.K_e:
                    player.upgradeMultiplier()
                elif event.key == pygame.K_r:
                    game_over = True

        player.goldRefresh()
        state = player.display()

        screen.fill(background)
        screen.blit(font.render("If you manage to gain 100000 Gold", True, BLACK), (50, 0))
        screen.blit(font.render("and buy more than 10 Collectors you win", True, BLACK), (50, 30))
        screen.blit(font.render("Q:     Buy Land  -- Cost 1 Ether", True, BLACK), (50, 100))
        screen.blit(font.render("W:     Buy Collector  -- Cost 30 Gold", True, BLACK), (50, 150))
        screen.blit(font.render("E:     Buy Multiplier  -- Cost 300 Gold", True, BLACK), (50, 200))
        screen.blit(font.render("R:     Quit Game", True, BLACK), (50, 250))
        screen.blit(font.render(f"Ether Balance: {state[0]}", True, BLACK), (50, 400))
        screen.blit(font.render(f"Gold Balance: {state[1]}   ---   {state[2] * state[3]} Gold per second", True, BLACK), (50, 500))
        screen.blit(font.render(f"Number of Collectors: {state[2]}", True, BLACK), (50, 600))
        screen.blit(font.render(f"Collector Multiplier: {state[3]}x", True, BLACK), (50, 700))
        pygame.display.update()
        
        while player.win and not game_over:
            screen.fill(background)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        player.win = False
                    elif event.key == pygame.K_r:
                        game_over = True
            screen.blit(font.render("You Won!!!", True, BLACK), (50, 370))
            screen.blit(font.render("Q: To play again", True, BLACK), (50, 470))
            screen.blit(font.render("R: To exit", True, BLACK), (50, 570))
            pygame.display.update()
