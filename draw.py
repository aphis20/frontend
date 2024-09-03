import turtle as t

def draw_planet(distance, radius, color):
    t.penup()
    t.goto(distance, -radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_solar_system():
    t.speed(0)  # Fastest drawing speed
    t.bgcolor("black")
    
    # Draw the Sun
    draw_planet(0, 60, "yellow")

    # Draw Mercury
    draw_planet(100, 10, "gray")

    # Draw Venus
    draw_planet(150, 15, "orange")

    # Draw Earth
    draw_planet(200, 20, "blue")

    # Draw Mars
    draw_planet(250, 15, "red")

    # Draw Jupiter
    draw_planet(350, 40, "brown")

    # Draw Saturn
    draw_planet(450, 35, "gold")
    
    # Draw Uranus
    draw_planet(550, 30, "lightblue")
    
    # Draw Neptune
    draw_planet(650, 30, "darkblue")

    t.hideturtle()

# Setup turtle screen
t.setup(width=800, height=600)
t.title("Solar System")
t.bgcolor("black")

# Draw the solar system
draw_solar_system()

# Finish
t.done()
