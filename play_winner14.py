import pygame
import turtle
import time
import random

pygame.init()
#music
music=pygame.mixer.Sound("Sounds\\game_music.wav")
music.play(-1) 
food_eat=pygame.mixer.Sound("Sounds\\food_eat.wav")
game_over=pygame.mixer.Sound("Sounds\\game_over.wav")

def main_game():
    delay = 0.1
    # Score
    score = 0
    high_score = 0
    level=1
    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game by ADITYA and DEVANSHU")
    wn.bgpic('Images\\backpic2.gif')
    wn.setup(width=600, height=600)
    wn.tracer(0) # Turns off the screen updates

    print('which head you want? 1 or 2')
    a = input()
    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    if a == '1':
        wn.addshape('Images\\snake_head.gif')
        turtle.shape('Images\\snake_head.gif')
        head.shape('Images\\snake_head.gif')
    if a == '2':
        wn.addshape('Images\\snake_head2.gif')
        turtle.shape('Images\\snake_head2.gif')
        head.shape('Images\\snake_head2.gif')

    #head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"


    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(200,200)

    #Body of Snake
    segments = []

    # Snake Obstacle
    #if 
    obstacle=turtle.Turtle()
    obstacle.penup()
    obstacle.speed()
    wn.addshape('Images\\brick.gif')
    turtle.shape('Images\\brick.gif')
    obstacle.shape("Images\\brick.gif")
    #obstacle.shape("square")
    #obstacle.color('black')
    obstacle.goto(40,40)
    obstacle.pendown()

    obs2=turtle.Turtle()
    obs2.penup()
    obs2.speed(0)
    wn.addshape('Images\\brick.gif')
    turtle.shape('Images\\brick.gif')
    obs2.shape("Images\\brick.gif")
    #obs2.shape("square")
    #obs2.color("black")
    c2,d2=1,1

    obs3=turtle.Turtle()
    obs3.penup()
    obs3.speed(0)

    wn.addshape('Images\\brick.gif')
    turtle.shape('Images\\brick.gif')
    obs3.shape("Images\\brick.gif")
    #obs3.shape("square")
    #obs3.color("black")
    c3,d3=1,1

    obs4=turtle.Turtle()
    obs4.penup()
    obs4.speed(0)
    wn.addshape('Images\\brick.gif')
    turtle.shape('Images\\brick.gif')
    obs4.shape("Images\\brick.gif")
    x4=random.randint(-299,299)
    y4=random.randint(-299,299)
    c4,d4=1,1

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("circle")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0 Level: 1", align="center", font=("Courier", 20, "normal"))

    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction =="down" and head.direction =="left":
            x=head.xcor()
            y=head.ycor()
            head.setx(x+5)
            head.sety(y+5)
            
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # Main game loop
    while True:
        wn.update()
        

        if level ==2 and c2>=d2:
            x2=random.randint(-299,299)
            y2=random.randint(-299,299)
            obs2.penup()
            obs2.goto(x2,y2)
            d2+=1
        
        if level == 3 and c3>=d3:
            x3=random.randint(-299,299)
            y3=random.randint(-299,299)
            obs3.penup()
            obs3.goto(x3,y3)
            d3+=1
        
        if level == 4 and c4>=d4:
            x4=random.randint(-299,299)
            y4=random.randint(-299,299)
            obs4.penup()
            obs4.goto(x4,y4)
            d4+=1


        # Check for a collision with the border
        if head.distance(obs3)<20 and level>=3:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            wn.addshape('Images\\game_over.gif')
            turtle.shape('Images\\game_over.gif')
            wn.update()
            pygame.mixer.pause()    
            game_over.play()    
            time.sleep(3.2)
            turtle.shape("blank")
            wn.update()
            pygame.mixer.unpause()
            wn.bgpic('Images\\backpic.gif')
            delay = 0.1
            pen.clear()
            obs3.reset(),obs2.reset(),obs4.reset()
            c2=d2
            c3=d3
            c4=d4
            pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))
            
            
        
        if head.distance(obs4)<20 and level>=4:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            wn.addshape('Images\\game_over.gif')
            turtle.shape('Images\\game_over.gif')
            wn.update()
            pygame.mixer.pause()    
            game_over.play()    
            time.sleep(3.2)
            turtle.shape("blank")
            wn.update()
            pygame.mixer.unpause()
            wn.bgpic('Images\\backpic.gif')
            # Reset the delay
            delay = 0.1
            pen.clear()
            obs3.reset(),obs2.reset(),obs4.reset()
            c2=d2
            c3=d3
            c4=d4
            pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))
            

        if head.distance(obs2)<20 and level>=2:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            wn.addshape('Images\\game_over.gif')
            turtle.shape('Images\\game_over.gif')
            wn.update()
            pygame.mixer.pause()    
            game_over.play()    
            time.sleep(3.2)
            turtle.shape("blank")
            wn.update()
            obs2.hideturtle()
            pygame.mixer.unpause()
            wn.bgpic('Images\\backpic.gif')
            # Reset the delay
            delay = 0.1
            pen.clear()
            obs3.reset(),obs2.reset(),obs4.reset()
            c2=d2
            c3=d3
            c4=d4
            pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))
            
        
        if head.distance(obstacle)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            wn.addshape('Images\\game_over.gif')
            turtle.shape('Images\\game_over.gif')
            wn.update()
            pygame.mixer.pause()    
            game_over.play()    
            time.sleep(3.2)
            turtle.shape("blank")
            wn.update()
            pygame.mixer.unpause()
            wn.bgpic('Images\\backpic.gif')
            score = 0
            level = 1
            # Reset the delay
            delay = 0.1
            pen.clear()
            obs3.reset(),obs2.reset(),obs4.reset()
            c2=d2
            c3=d3
            c4=d4 
            pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))
            

        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            wn.addshape('Images\\game_over_brick.gif')
            turtle.shape('Images\\game_over_brick.gif')
            wn.update()
            pygame.mixer.pause()    
            game_over.play()    
            time.sleep(3.2)
            turtle.shape("blank")
            wn.update()
            pygame.mixer.unpause()
            obs3.reset(),obs2.reset(),obs4.reset()
            c2=d2
            c3=d3
            c4=d4     
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            level = 1

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal")) 


        # Check for a collision with the food
        color_set={"red", "green", "yellow",'violet','blue','black','magenta','pink','grey'}
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)
            #plays the sound
            food_eat.play()
            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            for i in color_set:    
                new_segment.color(i)
                new_segment.penup()
                segments.append(new_segment)

            # Shorten the delay
            delay -= 0.01

            # Increase the score
            score += 10
            if score%20==0:
                level+=1

            if score > high_score:
                high_score = score
            
            pen.clear()
            pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal")) 
    
        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    
        
        if level == 1:
            wn.bgpic('Images\\backpic2.gif')
        if level == 2:
            wn.bgpic('Images\\backpic.gif')
        if level == 3:
            wn.bgpic('Images\\backpic3.gif')
        if level == 4:
            wn.bgpic('Images\\backpic4.gif')
        if level == 5:
            wn.bgpic('Images\\backpic5.gif')

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
                wn.addshape('Images\\game_over_snake.gif')
                turtle.shape('Images\\game_over_snake.gif')
                wn.update()
                pygame.mixer.pause()    
                game_over.play()    
                time.sleep(3.2)
                turtle.shape("blank")
                wn.update()
                pygame.mixer.unpause()
                wn.bgpic('Images\\backpic2.gif')
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
            
                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0
                level = 1
                # Reset the delay
                delay = 0.1
            
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))

        time.sleep(delay)
wn = turtle.Screen()
wn.title("Snake Game by ADITYA and DEVANSHU")
wn.bgpic('Images\\Home.gif')
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates
wn.listen()
wn.onkeypress(main_game, "space")
wn.mainloop()