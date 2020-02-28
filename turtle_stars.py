import turtle

st = turtle.Turtle()
turtle.bgcolor("cyan") #or st.getscreen().bgcolor("cyan")
st.speed(30)
st.color("red", "yellow")
def draw_star(st, l):
    for i in range(5):
        st.forward(l)
        st.left(216)
    st.penup()
    st.left(10)
    st.forward(10)
    st.pendown()
st.begin_fill()
for i in range(36):
    draw_star(st, 10)
st.end_fill()
turtle.done()