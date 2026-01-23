from turtle import Screen
from snake_main import snake_move
from food import Food
from scoreboard import Scoreboard


scr = Screen()
scr.setup(600, 600)
scr.bgcolor("black")
scr.tracer(0)


snake = snake_move()
food = Food()
score = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_is_on = True

def game():
    global game_is_on

    if not game_is_on:
        return

    snake.move()
    scr.update()

    
    if snake.head.distance(food) < 8:
        food.refresh()
        snake.extend()
        score.increase_score()

    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_is_on = False
        score.game_over()
        return

    
    for segment in snake.list_turtle[2:]:
        if snake.head.distance(segment) < 6:
            game_is_on = False
            score.game_over()
            return

    scr.ontimer(game, 100)

game()
scr.exitonclick()
