'''
Every drawn point has to be drawn at a distance of r from the center.
We already know r. We also know that we should not leave holes in the circle. Therefore we need to draw something for every 0 <= x <= r if we consider a quarter of a circle.
That leaves us with calculating y. We can calculate y using the Pythagorean theorem as the distance between the center (0/0) and (x/y) has to be r:

a² + b² = c²
x² + y² = r²
y² = r² - x²
y = sqrt(r² - x²)
Using x and y we can draw points for all four quarters of the circle:

draw_point(a + x, b + y)
draw_point(a + x, b - y)
draw_point(a - x, b + y)
draw_point(a - x, b - y)
Now our drawing will look like this:

   #####
  #     #
 #       #


#         #


 #       #
  #     #
   #####
To fill the missing spaces we can just redraw everything while swapping x and y:

   #####
  #     #
 #       #
#         #
#         #
#         #
#         #
#         #
 #       #
  #     #
   #####
'''

def draw_circle(a: int, b: int, r: int) -> None:
    grid = [[' '] * (a + r + 1) for _ in range(b + r + 1)]
    
    def draw_point(x: int, y: int) -> None:
        grid[y][x] = '#'
            
    r_squared = r**2
    
    for x in range(r + 1):
        y = round((r_squared - x**2)**0.5)
        
        draw_point(a + x, b + y)
        draw_point(a + y, b + x)
        draw_point(a + x, b - y)
        draw_point(a + y, b - x)
        draw_point(a - x, b + y)
        draw_point(a - y, b + x)
        draw_point(a - x, b - y)
        draw_point(a - y, b - x)
        
    for row in grid:
        print(''.join(row))

print(draw_circle(5, 5, 5))