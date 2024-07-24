# James Stimac 24-7-2024
import pygame, asyncio

#pygame setup
pygame.init()
#set display size
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

async def main():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #reset screen before next frame
        screen.fill("green")

        #main game render
        
        #flip() display to put work on screen
        pygame.display.flip()

        clock.tick(60) #limits fps
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())