## Starter code for an avoider game.
# University of Utah, David Johnson, 2017.
# This code, or code derived from this code, may not be shared without permission.
import sys, pygame, math, time

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_piskell_sprite(sprite_folder_name, sprite_name ,number_of_frames):
    frame_counts = []
    padding = math.ceil(math.log(number_of_frames-1,10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/" + sprite_name + str(frame) + ".png"
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
    myfont = pygame.font.SysFont("monospace", 12)
    death_font = pygame.font.SysFont("monospace", 32)

    # Load in the background image
    world = pygame.image.load("BG.png")
    world2 = pygame.image.load("BG2.png")
    #Big_rect = world.get_rect()

    # Store window width and height in different forms for easy access
    world_size = world.get_size()
    world2_size = world2.get_size()
    

    # The map rect is basically the whole screen, and we will draw to it to fill the background with the image
    world_rect = world.get_rect()
    world2_rect = world2.get_rect()
    
    # create the window the same size as the map image
    screen = pygame.display.set_mode(world_size)
    screen2 = pygame.display.set_mode(world2_size)

    
    # The frame_count counts all the frames that have passed since the start of the game.
    # Look at the print statements in the loop to see how to use the count with a mod function
    # to get cycles of different lengths.
    frame_count = 0;

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # The game should not start until the start color is clicked. Until then game_started is False
    game_started = False

    map_tile_width = 30
    map_tile_height = 20
    tile_size = 32
    screen_size = width, height = (map_tile_width*tile_size, map_tile_height*tile_size)

    #Hero: Load Hero/Getting Rect.
    hero = load_piskell_sprite("Hero", "sprite_",4)
    hero_rect = hero[0].get_rect()

    #Enemy 1: Load Enemy/Getting Rect.
    enemy1 = load_piskell_sprite("Wagon","sprite_",4)
    enemy1_rect = enemy1[0].get_rect()
    y1 = enemy1_rect.midleft = (0,400)
    #print(enemy2)
    enemy2 = load_piskell_sprite("Wagon","sprite_",4)
    enemy2_rect = enemy2[0].get_rect()
    y2 = enemy2_rect.midleft = (-100, 400)
    #print(enemy3)
    enemy3 = load_piskell_sprite("Wagon","sprite_",4)
    enemy3_rect = enemy3[0].get_rect()
    y3 = enemy3_rect.midleft = (0, 700)
    #print(enemy4)
    enemy4 = load_piskell_sprite("Wagon","sprite_",4)
    enemy4_rect = enemy4[0].get_rect()
    y4 = enemy4_rect.midleft = (-90, 500)
    #print(enemy5)
    enemy5 = load_piskell_sprite("Wagon","sprite_",4)
    enemy5_rect = enemy5[0].get_rect()
    y5 = enemy5_rect.midleft = (-180, 500)
    #print(enemy6)
    enemy6 = load_piskell_sprite("Wagon","sprite_",4)
    enemy6_rect = enemy6[0].get_rect()
    y6 = enemy6_rect.midleft = (0, 600)
    #print(enemy7)
    enemy7 = load_piskell_sprite("Wagon","sprite_",4)
    enemy7_rect = enemy7[0].get_rect()
    y7 = enemy7_rect.midleft = (-80, 600)
    #print(enemy8)
    enemy8 = load_piskell_sprite("Wagon","sprite_",4)
    enemy8_rect = enemy8[0].get_rect()
    y8 = enemy8_rect.midleft = (-200, 600)
    #print(enemy9)
    enemy9 = load_piskell_sprite("Wagon","sprite_",4)
    enemy9_rect = enemy9[0].get_rect()
    y9 = enemy9_rect.midleft = (-400, 500)
    #print(enemy10)
    enemy10 = load_piskell_sprite("Wagon","sprite_",4)
    enemy10_rect = enemy10[0].get_rect()
    y10 = enemy10_rect.midleft = (-400, 480)
    #Speed Of Character: Higher the number faster it goes per pixel/square
    speed = 5

    #FPS for Sprite
    frame_number = 0

    #Colours
    black = (0,0,0)
    yellow = (255,255,0)
    red = (255,0,0)
    white = (255,255,255)
    green = (200,100,100)

    
   #Collision
 #   def pixel_collision(sprite,sprite_rect, image, color):
 #       #Figure out where the upper left corner or the sprite_rect is
 #       x_offset, y-offset = sprite_rect.topleft
 #       for row_pos in range(sprite.get_height()):
 #           for col_pos in range(sprite.get_width()):
 #               if sprite.get_at((col_pos, row_pos)) == image.get_at(col_pos + x_offset,row_pos + y_offset):
 #                   return True #found collision
 #       return False
    quit_game = False
    while quit_game == False:
        
        # is_alive means that the game loop should continue. Winning or losing the game sets is_alive to False.
        is_alive = True
        lives = 3
        
        #print(hero)
        hero_rect.midbottom = (500,800)
        # Level 1
        level_one = True
        while level_one == True and quit_game == False:
            # Check events by looping over the list of events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                
            #Can't Spam Key Press it one by one: Hero Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero_rect.move_ip(-speed,0)
                    frame_number += 1
                if event.key == pygame.K_RIGHT:
                    hero_rect.move_ip(speed,0)
                    frame_number += 1
                if event.key == pygame.K_UP:
                    hero_rect.move_ip(0,-speed)
                    frame_number += 1
                if event.key == pygame.K_DOWN:
                    hero_rect.move_ip(0,speed)
                    frame_number += 1
                if frame_number >= len(hero):
                    frame_number = 0

            enemy1_rect.move_ip(speed + 7,0)
            if (enemy1_rect.x > width):
                enemy1_rect.center = y1
            enemy2_rect.move_ip(speed + 7,0)
            if (enemy2_rect.x > width):
                enemy2_rect.center = y2
            enemy3_rect.move_ip(speed + 10,0)
            if (enemy3_rect.x > width):
                enemy3_rect.center = y3
            enemy4_rect.move_ip(speed + 6,0)
            if (enemy4_rect.x > width):
                enemy4_rect.center = y4
            enemy5_rect.move_ip(speed + 6,0)
            if (enemy5_rect.x > width):
                enemy5_rect.center = y5
            enemy6_rect.move_ip(speed + 9,0)
            if (enemy6_rect.x > width):
                enemy6_rect.center = y6
            enemy7_rect.move_ip(speed + 9,0)
            if (enemy7_rect.x > width):
                enemy7_rect.center = y7
            enemy8_rect.move_ip(speed + 9,0)
            if (enemy8_rect.x > width):
                enemy8_rect.center = y8
            enemy9_rect.move_ip(speed + 7,0)
            if (enemy9_rect.x > width):
                enemy9_rect.center = y9           
            enemy10_rect.move_ip(speed + 7,0)
            if (enemy10_rect.x > width):
                enemy10_rect.center = y10           
            #Map 1
            screen.blit(world, world_rect)
            
            #Hero_Blit
            screen.blit(hero[frame_number%len(hero)], hero_rect)

            #Enemy Blit
            screen.blit(enemy1[frame_number%len(enemy1)], enemy1_rect)
            #Enemy 2 Blit
            screen.blit(enemy2[frame_number%len(enemy2)], enemy2_rect)
            #Enemy 3 Blit
            screen.blit(enemy3[frame_number%len(enemy3)], enemy3_rect)
            #Enemy 4 Blit
            screen.blit(enemy4[frame_number%len(enemy4)], enemy4_rect)
            #Enemy 5 Blit
            screen.blit(enemy5[frame_number%len(enemy5)], enemy5_rect)
            #Enemy 6 Blit
            screen.blit(enemy6[frame_number%len(enemy6)], enemy6_rect)
            #Enemy 7 Blit
            screen.blit(enemy7[frame_number%len(enemy7)], enemy7_rect)
            #Enemy 8 Blit
            screen.blit(enemy8[frame_number%len(enemy8)], enemy8_rect)
            #Enemy 9 Blit
            screen.blit(enemy9[frame_number%len(enemy9)], enemy9_rect)
            #Enemy 10 Blit
            screen.blit(enemy10[frame_number%len(enemy10)], enemy10_rect)
        
            #Temp line for beta reference
            #pygame.draw.line(screen,(200,100,100),(0,375),(width,375))

            py_Line = (hero_rect.x,375)
            if tuple(hero_rect) < py_Line:
                win = death_font.render("Success!", True, red)
                screen.blit(win,((width/4)+50,height/2))
                level_one =  False
                
            #Collision
            if hero_rect.colliderect(enemy1_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy2_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy3_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy4_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy5_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy6_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy7_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy8_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy9_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy10_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            # You may have sprites with different numbers of frames. We can make cycles
            # of different lengths by using mod on the frame_count. This is easier than
            # maintaining a different frame count variable for each different sprite.
            #print("Cycle of length 3:", frame_count%3) # counts 0,1,2,0,1,2
            #print("Cycle of length 4:", frame_count%4) # counts 0,1,2,3,0,1,2,3

            # Render text to the screen
            #Checks For Hero's Life Counter BUT needs an actual Counter
            if lives == 3:
                My_Life_Counter = myfont.render("Lives: 3", True, red)
            if lives == 2:
                My_Life_Counter = myfont.render("Lives: 2", True, red)
            if lives == 1:
                My_Life_Counter = myfont.render("Lives: 1", True, red)
            if lives == 0:
                My_Life_Counter = myfont.render("Lives:0", True, red)
                is_alive = False
                level_one = False
                screen.blit(dead,((width/4)+50,height/2))
                
            label = myfont.render("By: Isabella and Zach", True, yellow)
            dead = myfont.render("You Are Dead", True, red)
            screen.blit(label, (607,800))
            screen.blit(My_Life_Counter,(10,10))
            # Bring drawn changes to the front
            pygame.display.update()

            # We are basically done this with frame of animation, so update the count.
            frame_count += 1

            # This tries to force the loop to run at 1/2 fps. The is artifically slow so the output above
            # can be inspected. You should change this speed. Something like 30 is more normal.
            clock.tick(60)
        time.sleep(5)
        lives = 3
        hero_rect.midbottom = (500,800)
        #level 2
        level_two = True
        while level_two == True and quit_game == False:
            # Check events by looping over the list of events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                
            #Can't Spam Key Press it one by one: Hero Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero_rect.move_ip(-speed,0)
                    frame_number += 1
                if event.key == pygame.K_RIGHT:
                    hero_rect.move_ip(speed,0)
                    frame_number += 1
                if event.key == pygame.K_UP:
                    hero_rect.move_ip(0,-speed)
                    frame_number += 1
                if event.key == pygame.K_DOWN:
                    hero_rect.move_ip(0,speed)
                    frame_number += 1
                if frame_number >= len(hero):
                    frame_number = 0

            enemy1_rect.move_ip(speed + 7,0)
            if (enemy1_rect.x > width):
                enemy1_rect.center = y1
            enemy2_rect.move_ip(speed + 7,0)
            if (enemy2_rect.x > width):
                enemy2_rect.center = y2
            enemy3_rect.move_ip(speed + 10,0)
            if (enemy3_rect.x > width):
                enemy3_rect.center = y3
            enemy4_rect.move_ip(speed + 6,0)
            if (enemy4_rect.x > width):
                enemy4_rect.center = y4
            enemy5_rect.move_ip(speed + 6,0)
            if (enemy5_rect.x > width):
                enemy5_rect.center = y5
            enemy6_rect.move_ip(speed + 9,0)
            if (enemy6_rect.x > width):
                enemy6_rect.center = y6
            enemy7_rect.move_ip(speed + 9,0)
            if (enemy7_rect.x > width):
                enemy7_rect.center = y7
            enemy8_rect.move_ip(speed + 9,0)
            if (enemy8_rect.x > width):
                enemy8_rect.center = y8
            
            #Map 2
            screen2.blit(world2, world_rect)
            
            #Hero_Blit
            screen2.blit(hero[frame_number%len(hero)], hero_rect)

            #Enemy Blit
            screen2.blit(enemy1[frame_number%len(enemy1)], enemy1_rect)
            #Enemy 2 Blit
            screen2.blit(enemy2[frame_number%len(enemy2)], enemy2_rect)
            #Enemy 3 Blit
            screen2.blit(enemy3[frame_number%len(enemy3)], enemy3_rect)
            #Enemy 4 Blit
            screen2.blit(enemy4[frame_number%len(enemy4)], enemy4_rect)
            #Enemy 5 Blit
            screen2.blit(enemy5[frame_number%len(enemy5)], enemy5_rect)
            #Enemy 6 Blit
            screen2.blit(enemy6[frame_number%len(enemy6)], enemy6_rect)
            #Enemy 7 Blit
            screen2.blit(enemy7[frame_number%len(enemy7)], enemy7_rect)
            #Enemy 7 Blit
            screen2.blit(enemy8[frame_number%len(enemy8)], enemy8_rect)
            
            #Temp line for beta reference
            #pygame.draw.line(screen,(200,100,100),(0,445),(width,445))

            py_Line = (hero_rect.x,445)
            if tuple(hero_rect) < py_Line:
                win = death_font.render("Success!", True, red)
                screen.blit(win,((width/4)+50,height/2))
                level_two = False

                
            #Collision
            if hero_rect.colliderect(enemy1_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy2_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy3_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy4_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy5_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy6_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy7_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)
            if hero_rect.colliderect(enemy8_rect):
                lives -= 1
                hero_rect.midbottom = (500,800)

            # You may have sprites with different numbers of frames. We can make cycles
            # of different lengths by using mod on the frame_count. This is easier than
            # maintaining a different frame count variable for each different sprite.
            #print("Cycle of length 3:", frame_count%3) # counts 0,1,2,0,1,2
            #print("Cycle of length 4:", frame_count%4) # counts 0,1,2,3,0,1,2,3

            # Render text to the screen
            #Checks For Hero's Life Counter BUT needs an actual Counter
            if lives == 3:
                My_Life_Counter = myfont.render("Lives: 3", True, red)
            if lives == 2:
                My_Life_Counter = myfont.render("Lives: 2", True, red)
            if lives == 1:
                My_Life_Counter = myfont.render("Lives: 1", True, red)
            if lives == 0:
                My_Life_Counter = myfont.render("Lives:0", True, red)
                is_alive = False
                level_two = False
                level_one = True
                screen2.blit(dead,((width/4)+50,height/2))
                
            label = myfont.render("By: Isabella and Zach", True, yellow)
            dead = death_font.render("You Are Dead", True, red)
            screen2.blit(label, (607,800))
            screen2.blit(My_Life_Counter,(10,10))
            # Bring drawn changes to the front
            pygame.display.update()

            # We are basically done this with frame of animation, so update the count.
            frame_count += 1

            # This tries to force the loop to run at 1/2 fps. The is artifically slow so the output above
            # can be inspected. You should change this speed. Something like 30 is more normal.
            clock.tick(60)
            
    time.sleep(5)#added so that the You are dead or Success appears

    # This happens once the loop is finished - the game is over.
    pygame.quit()
    sys.exit()


# Start the program
main()
