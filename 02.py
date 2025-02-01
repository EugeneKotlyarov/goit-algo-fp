import turtle


def pifagor_tree(branch_length, t, angle, depth):
    if depth == 0:
        return
    else:
        t.forward(branch_length)
        t.right(angle)
        pifagor_tree(0.8 * branch_length, t, angle, depth - 1)
        t.left(2 * angle)
        pifagor_tree(0.8 * branch_length, t, angle, depth - 1)
        t.right(angle)
        t.backward(branch_length)


def main():
    depth = int(input("Вкажіть глибину рекурсії (ціле число): "))
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("black")
    t.color("green")
    # трошки прискоримость при збільшенні глибини
    t.speed(int(5 * depth / 3))
    t.width(2)
    t.left(90)
    pifagor_tree(100, t, 25, depth)
    screen.exitonclick()


if __name__ == "__main__":
    main()
