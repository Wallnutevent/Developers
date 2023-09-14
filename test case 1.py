import pygame

# Initialize the PyGame library
pygame.init()

# Set the dimensions of the game window
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the colors we will use
black = (0, 0, 0)
white = (255, 255, 255)

# Create a 3x3 grid of tiles
tiles = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]

# This variable will keep track of the current tile that is being moved
current_tile = None

# This loop will run until the user quits the game
while True:
    # Check for events
    for event in pygame.event.get():
        # If the user quits the game, quit the loop
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # If the user clicks the mouse, get the position of the click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Find the tile that was clicked
            for row in range(len(tiles)):
                for col in range(len(tiles[0])):
                    if mouse_x >= col * tile_width and mouse_x < (col + 1) * tile_width and \
                            mouse_y >= row * tile_height and mouse_y < (row + 1) * tile_height:
                        current_tile = tiles[row][col]

    # Clear the screen
    screen.fill(black)

    # Draw the tiles
    for row in range(len(tiles)):
        for col in range(len(tiles[0])):
            tile_x = col * tile_width
            tile_y = row * tile_height

            # If this is the current tile, draw it with a different color
            if tiles[row][col] == current_tile:
                pygame.draw.rect(screen, white, (tile_x, tile_y, tile_width, tile_height))
            else:
                pygame.draw.rect(screen, tiles[row][col], (tile_x, tile_y, tile_width, tile_height))

    # Update the display
    pygame.display.update()

    # Check if the puzzle is solved
    is_solved = True
    for row in range(len(tiles)):
        for col in range(len(tiles[0])):
            if tiles[row][col] != row * len(tiles[0]) + col + 1:
                is_solved = False
                break

    if is_solved:
        print("Congratulations! You solved the puzzle!")
        break

