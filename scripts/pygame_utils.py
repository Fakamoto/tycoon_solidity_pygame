import pygame


def loop(player):
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((1100, 1000))

    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    background = GRAY

    font = pygame.font.SysFont(None, 48)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player.buyLand()
                if event.key == pygame.K_2:
                    player.buyGold()
                if event.key == pygame.K_3:
                    player.buyDark()
                elif event.key == pygame.K_q:
                    player.buyGoldCollector()
                elif event.key == pygame.K_w:
                    player.buyDarkCollector()
                elif event.key == pygame.K_e:
                    player.upgradeMultiplier()
                elif event.key == pygame.K_r:
                    game_over = True

        player.balances()
        state = player.display()

        screen.fill(background)
        screen.blit(font.render("to win gain 100000 Gold and 10000 Dark", True, BLACK), (50, 0))
        screen.blit(font.render("buy +10 Collectors and +10 Dark Collectors", True, BLACK), (50, 50))
        screen.blit(font.render("1:     Buy Land  -- Cost 1 Ether", True, BLACK), (50, 100))
        screen.blit(font.render("2:     Buy Gold with Dark  -- Cost all your Dark", True, BLACK), (50, 150))
        screen.blit(font.render("3:     Buy Dark with Gold  -- Cost all your Gold", True, BLACK), (50, 200))
        screen.blit(font.render("Q:     Buy Collector  -- Cost 30 Gold", True, BLACK), (50, 250))
        screen.blit(font.render("W:     Buy Dark Collector  -- Cost 50 Dark", True, BLACK), (50, 300))
        screen.blit(font.render("E:     Buy Multiplier  -- Cost 300 Gold, 300 Dark", True, BLACK), (50, 350))
        screen.blit(font.render("R:     Quit Game", True, BLACK), (50, 400))
        screen.blit(font.render(f"Ether Balance: {state[0]}", True, BLACK), (50, 650))
        screen.blit(font.render(f"Gold Balance: {state[1]}   ---   {state[3] * state[5]} Gold per second", True, BLACK), (50, 700))
        screen.blit(font.render(f"Dark Balance: {state[2]}   ---   {(state[4] * state[5])/4} Dark per second", True, BLACK), (50, 750))
        screen.blit(font.render(f"Number of Collectors: {state[3]}", True, BLACK), (50, 800))
        screen.blit(font.render(f"Number of Dark Collectors: {state[4]}", True, BLACK), (50, 850))
        screen.blit(font.render(f"Multiplier: {state[5]}x", True, BLACK), (50, 900))
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
