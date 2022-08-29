from turtle import *

def dibujaTriangulo(tamanoBase, grado, tortuga):
    tortuga.hideturtle()
    if(grado<4):
        tortuga.speed(5)
    elif(grado<=7):
        tortuga.speed(500)
    elif(grado>=8):
        tortuga.speed(10000)

    tortuga.up()
    tortuga.goto(tamanoBase[0][0], tamanoBase[0][1])
    tortuga.down()
    tortuga.goto(tamanoBase[1][0], tamanoBase[1][1])
    tortuga.goto(tamanoBase[2][0], tamanoBase[2][1])
    tortuga.goto(tamanoBase[0][0], tamanoBase[0][1])

def obtenerMitad(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(tamanoBase, grado, tortuga):
    dibujaTriangulo(tamanoBase, grado, tortuga)
    if grado > 0:
        sierpinski([tamanoBase[0],
                        obtenerMitad(tamanoBase[0], tamanoBase[1]),
                        obtenerMitad(tamanoBase[0], tamanoBase[2])],
                   grado - 1, tortuga)
        sierpinski([tamanoBase[1],
                        obtenerMitad(tamanoBase[0], tamanoBase[1]),
                        obtenerMitad(tamanoBase[1], tamanoBase[2])],
                   grado - 1, tortuga)
        sierpinski([tamanoBase[2],
                        obtenerMitad(tamanoBase[2], tamanoBase[1]),
                        obtenerMitad(tamanoBase[0], tamanoBase[2])],
                   grado - 1, tortuga)

def main():
   tortuga = Turtle()
   ventana = Screen()
   ventana.title("Triángulo de Sierpiński")
   ventana.setup(650, 625, None, None)
   tamanoBase = [[-300, -150], [0, 300], [300, -150]]
   grado = int(textinput("Grado Triangulo", "Ingrese el grado del triángulo de Sierpiński a graficar: "))
   sierpinski(tamanoBase, grado, tortuga)
   ventana.exitonclick()

if(__name__ == "__main__"):
    main()