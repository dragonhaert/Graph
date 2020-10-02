from objects import *

if __name__ == '__main__':

    graph = GRAPH(window.width/2, 3*window.height/4)
    dx = 10

    for i in range(0, int(window.width*dx)):
        x = (i/dx - graph.position.X)

        def func(a):
            return (0.1*a)**3

        graph.seg(x, func(x), x + 1, func(x + 1), 'red', 3)

    running = True
    while running:
        graph.show()
        window.update()
        window.clear()

