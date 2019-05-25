# Move a ball

        ###################################################
        # Student should add code where relevant to the following.

        import simplegui


        # Define globals - Constants are capitalized in Python
        HEIGHT = 400
        WIDTH = 400
        RADIUS_INCREMENT = 5
        ball_radius = 20

        # Draw handler
        def draw(canvas):
        canvas.draw_circle([WIDTH // 2, HEIGHT // 2], ball_radius, 1,
        "White", "White")

        # Event handler for buttons
        def increase_radius():
        global ball_radius
        ball_radius += RADIUS_INCREMENT

        def decrease_radius():
        global ball_radius
        if ball_radius > RADIUS_INCREMENT:
        ball_radius -= RADIUS_INCREMENT


        # Create frame and assign callbacks to event handlers
        frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
        frame.set_draw_handler(draw)
        frame.add_button("Increase radius", increase_radius)
        frame.add_button("Decrease radius", decrease_radius)


        # Start the frame animation
        frame.start()

------------------------------------------------------------------
        # Move a ball

        ###################################################
        # Student should add code where relevant to the following.


        import simplegui

        # Define globals - Constants are capitalized in Python
        HEIGHT = 400
        WIDTH = 400
        RADIUS_INCREMENT = 5
        ball_radius = 20

        # Draw handler
        def increase_radius():
        global ball_radius
        ball_radius += RADIUS_INCREMENT
        return ball_radius

        def decrease_radius():
        global ball_radius, RADIUS_INCREMENT
        if ball_radius <= RADIUS_INCREMENT:
        print "Ball radius (" + str(ball_radius) + ") is less or equal than increment (" + str(RADIUS_INCREMENT) + "): can't decrease"
        elif ball_radius > RADIUS_INCREMENT:
        ball_radius -= RADIUS_INCREMENT
        return ball_radius
        else:
        print "decrease_radius sees smth invalid"





        def draw(canvas):
        canvas.draw_circle([200, 200], ball_radius, 2, "Green", "Orange")


        # Event handlers for buttons


        # Create frame and assign callbacks to event handlers
        frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
        frame.set_draw_handler(draw)
        frame.add_button("Increase radius", increase_radius)
        frame.add_button("Decrease radius", decrease_radius)


        # Start the frame animation
        frame.start()