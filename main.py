from turtle import Screen
from snake import Snake
from score import Score
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

game_on = True

snake_jogui = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake_jogui.up, 'Up')
screen.onkey(snake_jogui.down,'Down')
screen.onkey(snake_jogui.left,'Left')
screen.onkey(snake_jogui.right,'Right')


while game_on:
    screen.update()
    time.sleep(.1)

    snake_jogui.move()

    #collition with food
    if snake_jogui.head.distance(food) < 15:
        food.refresh()
        snake_jogui.extend()
        score.new_score()

    #collition with wall
    if snake_jogui.head.xcor() > 280 or snake_jogui.head.xcor() < -280 or \
            snake_jogui.head.ycor() > 280 or snake_jogui.head.ycor() < -280:
        score.game_over()
        game_on = False

    #collition with own tail
    for segment in snake_jogui.segments[1:]:
        if snake_jogui.head.distance(segment) < 10:
            score.game_over()
            game_on = False


screen.exitonclick()