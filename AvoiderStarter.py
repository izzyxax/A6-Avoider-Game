# Starter code for an avoider game.
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

# This function moves rect slowly between start_pos and end_pos. The num_frame parameter
# says how many frames of animation are needed to do the bounce, so a bigger number means
# the rect moves slower. frame_count is the current overall frame count from the game.

#def bounce_rect_between_two_positions( rect, start_pos, end_pos, num_frame, frame_count ):
    if frame_count%num_frame < num_frame/2:
        new_pos_x = start_pos[0] + (end_pos[0] - start_pos[0]) * (frame_count%(num_frame/2))/(num_frame/2)
        new_pos_y = start_pos[1] + (end_pos[1] - start_pos[1]) * (frame_count%(num_frame/2))/(num_frame/2)
    else:
        new_pos_x = end_pos[0] + (start_pos[0] - end_pos[0]) * (frame_count%(num_frame/2))/(num_frame/2)
        new_pos_y = end_pos[1] + (start_pos[1] - end_pos[1]) * (frame_count%(num_frame/2))/(num_frame/2)

    rect.center = (new_pos_x, new_pos_y)

# The main loop handles most of the game    
def main():
                             
    # Initialize pygame                                 
    pygame.init()

    # Get a font
    myfont = pygame.font.SysFont("monospace", 24)

    # Load in the background image
    map = pygame.image.load("BG.png")

    # Store window width and height in different forms for easy access
    map_size = map.get_size()

    # The map rect is basically the whole screen, and we will draw to it to fill the background with the image
    map_rect = map.get_rect()
    
    # create the window the same size as the map image
    screen = pygame.display.set_mode(map_size)
        
    # The frame_count counts all the frames that have passed since the start of the game.
    # Look at the print statements in the loop to see how to use the count with a mod function
    # to get cycles of different lengths.
    frame_count = 0;

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # The game should not start until the start color is clicked. Until then game_started is False
    game_started = False

    # is_alive means that the game loop should continue. Winning or losing the game sets is_alive to False.
    is_alive = True

    #Hero: Load Hero/Getting Rect.
    hero = load_piskell_sprite("Hero",4)
    hero_rect = hero[0].get_rect()
    print(hero)
    #Enemy 1: Load Enemy/Getting Rect.
    enemy1 = load_piskell_sprite("Wagon",4)
    enemy1_rect = enemy1[0].get_rect()
    print(enemy1)

    #Speed Of Character: Higher the number faster it goes per pixel/square
    speed = 5

    #FPS for Sprite
    frame_number = 0





    # Loop while the player is still active
    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
            
        #Can't Spam Key Press it one by one: Hero Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero_rect.move_ip(-speed,0)
                    frame_number += 1
                if event.key == pygame.K_RIGHT:
                    hero_rect.move_ip(0,speed)
                    frame_number += 1
                if event.key == pygame.K_UP:
                    hero_rect.move_ip(0,speed)
                    frame_number += 1
                if event.key == pygame.K_DOWN:
                    hero_rect.move_ip(0,-speed)
                    frame_number += 1
            if frame_number >= len(hero):
                frame_number = 0
            
                    

        screen.blit(map, map_rect, hero, hero_rect)



#This Code uses a mouse as the character
        
        # This grabs the current color under the cursor from the screen. Note that anything
        # drawn on the screen before this statement adds to the color. I could have also
        # taken the color from the map if I just wanted that.

       # cursor_color = screen.get_at(pygame.mouse.get_pos())

        # Note that the color has 4 values - the 4th is alpha. If you want to compare colors
        # make sure that you compare all the values. An example would be
        # cursor_color == (255, 0, 0, 255)
        # to see if the cursor is over a pure red area.

        #print("Color:", cursor_color)




        # You may have sprites with different numbers of frames. We can make cycles
        # of different lengths by using mod on the frame_count. This is easier than
        # maintaining a different frame count variable for each different sprite.
        print("Cycle of length 3:", frame_count%3) # counts 0,1,2,0,1,2
        print("Cycle of length 4:", frame_count%4) # counts 0,1,2,3,0,1,2,3

        # Render text to the screen
        label = myfont.render("By: Isabella and Zach", True, (255,255,0))
        screen.blit(label, (607,800))
        
        # Bring drawn changes to the front
        pygame.display.update()

        # We are basically done this with frame of animation, so update the count.
        frame_count += 1

        # This tries to force the loop to run at 1/2 fps. The is artifically slow so the output above
        # can be inspected. You should change this speed. Something like 30 is more normal.
        clock.tick(0.5)

    # This happens once the loop is finished - the game is over.
    pygame.quit()
    sys.exit()


# Start the program
main()
