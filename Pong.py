# Pong in Python, simple solution for simple game

import turtle       # import biblioteki turle, lepsza niz pygames do takich prostych gierek


# Load config from file
f = open('conf.txt', 'r')
conf = f.read()
f.close()
x = int(conf.split(';')[1])          # wazne parametry konfiguracyjne to sa kolejne liczby nieparzyste, w pliku conf sa one oddzielone srednikiem
y = int(conf.split(';')[3])
diff = int(conf.split(';')[5])
diff = diff / 10

# Main window
window = turtle.Screen()        #tworzenie glownego okna gry
window.title("PING PONG")
window.bgcolor("black")
window.setup(width=x, height=y)
window.tracer(0)

# Paddle A                      # jest to lewna kolumna
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")        #ksztal
paddle_a.color("white")         #kolor
paddle_a.shapesize(stretch_wid=y/120, stretch_len=1)        #rozciagniecie kwadratu, tak aby stal sie prostokatem
paddle_a.penup()
paddle_a.goto(-x/2 + 50, 0)
# Paddle B                      #prawa kolumna
paddle_b = turtle.Turtle()
paddle_b.speed(0)               #analogicznie
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=y/120, stretch_len=1)
paddle_b.penup()
paddle_b.goto(x/2 - 50, 0)
paddle_b.k = 0
# Ball                          #pilka
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")            #podobnie jak z kolumnami
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2                   #tutaj parametry dx i dy odpowiadaja za przemieszczanie sie, mozliwe ze na roznych komputerach predkosc bedzie inna przy tych samych parametrach
ball.dy = 0.2
ball.temp1 = 0                  # wartosci tymczasowe potrzebne do funkcji pause
ball.temp2 = 0

# score
score = turtle.Turtle()         # tablica wynikow
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, y/2 - 40)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))
score.a = 0                     #wynik gracza 1, a ponizej gracza 2
score.b = 0


# Functions


def paddle_a_up():              #sa tutaj 4 funkcje do poruszania kolumnami, najpierw 2 dla gracza 1, a pozniej dla gracza 2
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up(x,y):               #metoda onclick() dziala tylko jak przyjmie argument w postaci funckji z dwoma argumentami
    y = paddle_b.ycor()
    y += 20
    if paddle_b.k == 0:
        paddle_b.sety(y)


def paddle_b_down(x,y):             #dlatego te dwie funkcje dla gracza 2, ktory steruje za pomoca myszki posiadaja dwa nieuzywane argumenty
    y = paddle_b.ycor()             # modern problems require modern solutions
    y -= 20
    if paddle_b.k == 0:
        paddle_b.sety(y)


def set_speed1():                   #9 funkcji do ustawiania predkosci
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 0.2
    ball.dy = 0.2
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def set_speed2():
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 0.4
    ball.dy = 0.4
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def set_speed3():
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 0.6
    ball.dy = 0.6
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def set_speed4():
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 0.8
    ball.dy = 0.8
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def set_speed5():
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 1
    ball.dy = 1
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def set_speed6():
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 1.2
    ball.dy = 1.2
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def set_speed7():
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 1.4
    ball.dy = 1.4
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def set_speed8():
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 1.6
    ball.dy = 1.6
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def set_speed9():
    tempx = ball.dx
    tempy = ball.dy
    ball.dx = 1.8
    ball.dy = 1.8
    if tempx < 0:
        ball.dx *= -1
    if tempy < 0:
        ball.dy *= -1


def computer():
    if paddle_b.k == 0:
        paddle_b.k = 1
    else:
        paddle_b.k = 0


def comp_mov():
    y = paddle_b.ycor()

    if ball.dx > 0:
        if paddle_b.ycor() > ball.ycor():
            paddle_b.sety(y - diff)
        else:
            paddle_b.sety(y + diff)
    elif paddle_b.ycor() != 0:
        if paddle_b.ycor() > 0:
           paddle_b.sety(y - diff)
        if paddle_b.ycor() < 0:
            paddle_b.sety(y + diff)


def reset():            # funkcja ustawiajaca oba wyniki na 0
    score.a = 0
    score.b = 0
    score.clear()       # czyscimy tablice wynikow, bez tego cyfry (bo tylko one sie zmieniaja) nachodzily by na siebie
    score.write("Player 1: {}  Player 2: {}".format(score.a, score.b), align="center", font=("Courier", 24, "normal"))      # zapisujemy zmieniony wynik


def pause():                    # funkcja sluzaca do paouzowania rozgrywki
    if ball.dx != 0:            # jesli predkosc nie jest rowna zero, czyli pilka sie porusza
        ball.temp1 = ball.dx    # to do zmienych czasowcyh przpisujemy predkosci tej pilki, tak zeby miec je pozniej z czego odzyskac
        ball.temp2 = ball.dy
        ball.dx = 0             # a predkosc ustawiamy na zero
        ball.dy = 0
    else:
        ball.dx = ball.temp1    # a jak pilka nie porusza sie to poprostu przypisujemy jej taka predkosc jaka miala przed pauza
        ball.dy = ball.temp2

# Keybord binding


window.listen()
window.onkeypress(paddle_a_up, "Up")        # strzalka w gore
window.onkeypress(paddle_a_down, "Down")    # strzalka w dol
window.onscreenclick(paddle_b_up, 1)        # lpm
window.onscreenclick(paddle_b_down, 3)      # ppm
window.onkeypress(reset, "r")
window.onkeypress(pause, "p")
window.onkeypress(computer, "k")
window.onkeypress(set_speed1, "1")
window.onkeypress(set_speed2, "2")
window.onkeypress(set_speed3, "3")
window.onkeypress(set_speed4, "4")
window.onkeypress(set_speed5, "5")
window.onkeypress(set_speed6, "6")
window.onkeypress(set_speed7, "7")
window.onkeypress(set_speed8, "8")
window.onkeypress(set_speed9, "9")



# Main game loop

while True:
    window.update()
    # movement

    ball.setx(ball.xcor() + ball.dx)                # poruszaja pilka w pionie i poziomie
    ball.sety(ball.ycor() + ball.dy)                # dzieki czemu wyglada to na plynny ruch

    if paddle_b.k == 1:
        comp_mov()
    # borders
    if ball.ycor() > y/2 - 10:                           # tutaj sa nasze granice, jesli pilka je napotka
        ball.sety(y/2 - 10)                              # to zmieniamy jej kierunek ruchu
        ball.dy *= -1
    if ball.ycor() < -y/2 + 10:
        ball.sety(-y/2 + 10)
        ball.dy *= -1
    if ball.xcor() > x/2 - 10:
        ball.goto(0, 0)
        ball.dx *= -1
        score.a += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score.a, score.b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -x/2 + 10:
        ball.goto(0, 0)
        ball.dx *= -1
        score.b += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score.a, score.b), align="center", font=("Courier", 24, "normal"))
    # Collision
    if (ball.xcor() > x/2 - 60 and ball.xcor() < x/2 - 50) and (ball.ycor() < paddle_b.ycor() + y/12 and ball.ycor() > paddle_b.ycor() - y/12):
        ball.setx(x/2 - 60)
        ball.dx *= -1
    if (ball.xcor() < - x/2 + 60 and ball.xcor() > - x/2 + 50) and (ball.ycor() < paddle_a.ycor() + y/12 and ball.ycor() > paddle_a.ycor() - y/12):
        ball.setx(- x/2 + 60)
        ball.dx *= -1


