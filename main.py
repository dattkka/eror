import pygame
import random
pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')


start_background_img = pygame.image.load('startbc.jpg')
game_bc_img = pygame.image.load('bc.jpg')

start_btn_img = pygame.image.load('buttonstart.png')
exit_btn_img = pygame.image.load('exitimg.png')


btn_width, btn_height = 300, 150

start_btn_img = pygame.transform.scale(start_btn_img, (btn_width , btn_height))
exit_btn_img = pygame.transform.scale(exit_btn_img, (btn_width , btn_height))

start_btn_rect = start_btn_img.get_rect()
exit_btn_rect = exit_btn_img.get_rect()
start_btn_rect.center = (200, 200)
exit_btn_rect.center = (200, 350)
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play(-1)
bg_x = 0
running = True
running2 = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if exit_btn_rect.collidepoint(mouse_pos):
                running = False
            if start_btn_rect.collidepoint(mouse_pos):


                # Game dimensions
                WIDTH, HEIGHT = 400, 600

                # Bird dimensions
                BIRD_WIDTH, BIRD_HEIGHT = 20, 20

                # Pipe dimensions
                PIPE_WIDTH = 50
                PIPE_GAP = 200

                # Colors
                WHITE = (255, 255, 255)
                BLUE = (0, 0, 255)
                GREEN = (0, 255, 0)

                pygame.init()

                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                clock = pygame.time.Clock()
                class Bird:
                    def __init__(self):
                        self.x = 100
                        self.y = HEIGHT // 2
                        self.gravity = 0.5
                        self.velocity = 0

                    def flap(self):
                        self.velocity = -10

                    def update(self):
                        self.velocity += self.gravity
                        self.y += self.velocity

                    def draw(self):
                        pygame.draw.rect(screen, BLUE, (self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT))


                class Pipe:
                    def __init__(self, x, height):
                        self.x = x
                        self.height = height

                    def update(self):
                        self.x -= 3

                    def draw(self):
                        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))
                        pygame.draw.rect(screen, GREEN,
                                         (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP))


                bird = Bird()
                pipes = [Pipe(WIDTH + i * 300, random.randint(100, 400)) for i in range(3)]
                score = 0




                while running2:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            bird.flap()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            bird.flap()

                    bird.update()

                    for pipe in pipes:
                        pipe.update()
                        if pipe.x < PIPE_WIDTH:
                            pipes.remove(pipe)
                            pipes.append(Pipe(pipes[-1].x + 300, random.randint(100, 400)))
                        if bird.x + BIRD_WIDTH > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
                            if bird.y < pipe.height or bird.y + BIRD_HEIGHT > pipe.height + PIPE_GAP:
                                running2 = False
                            if bird.x > pipe.x + PIPE_WIDTH and bird.x < pipe.x + PIPE_WIDTH + 3:
                                score += 1

                    screen.blit(start_background_img, (bg_x, 0))
                    screen.blit(start_background_img, (bg_x + 400, 600))
                    bg_x -= 2

                    if bg_x == -400:
                        bg_x = 0
                    bird.draw()
                    for pipe in pipes:
                        pipe.draw()
                        pygame.display.flip()

                    # Display score
                    font = pygame.font.Font(None, 36)
                    score_text = font.render("Score: " + str(score), False, GREEN)
                    screen.blit(score_text, (10, 10))

                    pygame.display.flip()
                    clock.tick(60)
                pass
            pygame.display.flip()
        pygame.display.flip()



    screen.blit(start_background_img, (0, 0))
    screen.blit(start_btn_img, start_btn_rect)
    screen.blit(exit_btn_img, exit_btn_rect)


    pygame.display.flip()
pygame.quit()
