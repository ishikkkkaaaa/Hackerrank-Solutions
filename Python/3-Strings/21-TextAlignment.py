# Replace all ______ with rjust, ljust or center.

thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
# replace  ______ To rjust |  ______ To  ljust
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
# replace ______ To center |  ______ To center
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
# replace ______ To center
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
# replace ______ To center |  ______ To center
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
# replace ______ To rjust |  ______ To ljust |  ______ To rjust
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c +
          (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
