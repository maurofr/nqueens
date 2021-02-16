import solution as sol
import turtle as t


def board(n):
    # Draws the grid of nxn squares
    for i in range(n + 1):
        brush.up()
        brush.goto(-20 * int(n/2), 20 * (i - int(n/2) - int(n % 2 != 0)))
        brush.down()
        brush.fd(20 * n)
    brush.right(90)
    for i in range(n + 1):
        brush.up()
        brush.goto(20 * (i - int(n/2)), 20 * int(n/2))
        brush.down()
        brush.fd(20 * n)


def draw(i, j):
    # Draws a circle (queen) in the square (i, j)
    brush.up()
    brush.goto(20 * (i - int(n/2)) + 5, 20 * (int(n/2) - j) - 10)
    brush.down()
    brush.begin_fill()
    brush.circle(5)
    brush.end_fill()


def solution(n):
    # Scans the solution and draws each queen
    T = sol.queens(n)
    for i in range(n):
        for j in range(n):
            if T[j][i] == 1:
                draw(i, j)


n = int(input())
brush = t.Turtle()
brush.speed(-1)
brush.hideturtle()
board(n)
solution(n)
t.done()
