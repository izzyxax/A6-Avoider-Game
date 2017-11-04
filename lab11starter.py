# Starter code for an adventure type game.
# University of Utah, David Johnson, 2017.
# This code, or code derived from this code, may not be shared without permission.

import sys, pygame, math

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_piskell_sprite(sprite_folder_name, number_of_frames):
    frame_counts = []
    padding = math.ceil(math.log(number_of_frames-1,10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding,'0') +".png"
        frame_counts.append(pygame.image.load(folder_and_file_name).convert_alpha())
                             
    return frame_counts

# The main loop handles most of the game    
def main():
                             
    # Initialize pygame                                 
    pygame.init()
   # The map tile width/height specifies how big the window is in tiles
    map_tile_width = 25
    map_tile_height = 25
    tile_size = 32 # the dimensions of the tile in pixels
    screen_size = width, height = (map_tile_width*tile_size, map_tile_height*tile_size)
    screen = pygame.display.set_mode(screen_size)
    print(screen_size)
    # Get a font
    myfont = pygame.font.SysFont("monospace", 24)

    # create the hero character
    hero = load_piskell_sprite("images/hero",12)
    hero_rect = hero[0].get_rect()
    hero_rect.center = (width/2, height/2)
    
    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    frame_count = 0;

    # variable to show if we are still playing the game
    playing = True

    # variable to show which way I am moving
    is_facing_right = True # False means left

    # Load a minimap
    world = pygame.image.load("images/labMap.png").convert_alpha()
    world_rect = world.get_rect()

    # Set the offset into the map
    mapx, mapy = (0,0)

    # Load the tiles
    sand = pygame.image.load("images/Sand.png").convert_alpha() # (206, 206, 46, 255)
    tile_rect = sand.get_rect()
    plains = pygame.image.load("images/Plains.png").convert_alpha() # (126, 206, 46, 255)
    swamp = pygame.image.load("images/Swamp.png").convert_alpha() # (14,64,14,255)
    dirt = pygame.image.load("images/Dirt.png").convert_alpha() # (117,94,21,255)
    water = pygame.image.load("images/water2.png").convert_alpha() # (0, 176, 255, 255)
    rocks = pygame.image.load("images/Rocky.png").convert_alpha() # (39, 39, 21, 255)

    # Loop while the player is still active
    while playing:
        # start the next frame
        screen.fill((100,120,120)) # some background color when there are no tiles
        
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            is_facing_right = False
            mapx += -1
        if keys[pygame.K_RIGHT]:
            is_facing_right = True
            mapx += 1
        if keys[pygame.K_UP]:
            mapy += -1
        if keys[pygame.K_DOWN]:
            mapy += 1

        if mapx < 0:
            mapx = 0
        if mapx > world.get_width() - 1 - (map_tile_width-1):
            mapx = world.get_width() - 1 - (map_tile_width-1)
        if mapy < 0:
            mapy = 0
        if mapy > world.get_height() - 1 - (map_tile_height-1):
            mapy = world.get_height() - 1 - (map_tile_height-1)
        # Draw the map
        for row in range(0,map_tile_height):
            for col in range(0,map_tile_width):
                tile_rect.topleft = col*tile_size, row*tile_size
                pixel_color= world.get_at((mapx + col, mapy + row))
                if pixel_color == (206,206,46,255):
                    tile_to_draw = sand
                if pixel_color == (126,206,46,255):
                    tile_to_draw = plains
                if pixel_color ==  (0, 176, 255, 255):
                    tile_to_draw = water
                if pixel_color == (117,94,21,255):
                    tile_to_draw = dirt
                if pixel_color == (14,64,14,255):
                    tile_to_draw = swamp
                if pixel_color == (39,39,21,255):
                    tile_to_draw = rocks
                screen.blit(tile_to_draw, tile_rect)#shows everything on screen
        # Draw the hero
        hero_sprite = hero[frame_count%len(hero)]
        if is_facing_right:
            hero_sprite = pygame.transform.flip(hero_sprite, True, False)
        screen.blit(hero_sprite, hero_rect)

        fps = clock.get_fps()
        # Render text to the screen
        label = myfont.render("FPS:" + str(int(fps)), True, (255,255,0))
        screen.blit(label, (20,20))

        # Bring drawn changes to the front
        pygame.display.update()

        frame_count += 1

        # 60 fps
        clock.tick(60)

    # loop is over    
    pygame.quit()
    sys.exit()




# Start the program
main()
