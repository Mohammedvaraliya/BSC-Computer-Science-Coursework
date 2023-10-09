import pygame
import random

# Screen
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("T109 Mohammed Varaliya")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Character
character_size = 50
character_speed = 5
character = pygame.Rect(width // 2 - character_size // 2, height - character_size,
                        character_size, character_size)

# Bullets (triangles) properties
bullet_size = 10
bullets = []

# Enemy (circle) properties
enemy_radius = 20
enemies = []

# Initialize score
score = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()


if __name__ == "__main__":

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(character.centerx - bullet_size // 2, character.top,
                                        bullet_size, bullet_size)
                    bullets.append(bullet)

        # Move bullets
        for bullet in bullets:
            bullet.y -= 10
            if bullet.top < 0:
                bullets.remove(bullet)

        # Spawn enemies
        if random.randint(1, 100) <= 2:
            enemy_x = random.randint(enemy_radius, width - enemy_radius)
            enemy = pygame.Rect(enemy_x - enemy_radius, 0, enemy_radius * 2, enemy_radius * 2)
            enemies.append(enemy)

        # Move enemies
        for enemy in enemies:
            enemy.y += 5
            if enemy.top > height:
                enemies.remove(enemy)

        # Move character
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.x -= character_speed
        if keys[pygame.K_RIGHT]:
            character.x += character_speed

        # Check for collisions
        for bullet in bullets:
            for enemy in enemies:
                if bullet.colliderect(enemy):
                    score += 1
                    bullets.remove(bullet)
                    enemies.remove(enemy)

        # Check for character collision with enemies
        for enemy in enemies:
            if character.colliderect(enemy):
                running = False

        # Clear the screen
        screen.fill(white)

        # Draw bullets
        for bullet in bullets:
            pygame.draw.polygon(screen, blue, [(bullet.left, bullet.bottom), (bullet.centerx,
                                                                        bullet.top), (bullet.right, bullet.bottom)])

        # Draw character
        pygame.draw.rect(screen, red, character)

        # Draw enemies
        for enemy in enemies:
            pygame.draw.circle(screen, red, enemy.center, enemy_radius)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, red)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Limit frame rate to 60 FPS
        clock.tick(60)

    # Game over display
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, red)
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 -
                                game_over_text.get_height() // 2))
    pygame.display.flip()

    # Wait for a few seconds before closing the game
    pygame.time.wait(3000)

    # Clean up
    pygame.quit()