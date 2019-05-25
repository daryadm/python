# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False


class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5, 5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
# soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def draw(self, canvas):
        if self.thrust == False:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]],
                              self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel
        self.vel[0] *= 0.97
        self.vel[1] *= 0.97

        forward_vector = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0] += forward_vector[0] * 0.08
            self.vel[1] += forward_vector[1] * 0.08
        else:
            pass
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def to_left(self):
        self.angle_vel -= 0.05

    def to_right(self):
        self.angle_vel += 0.05

    def thrust_on(self):
        self.thrust = True
        ship_thrust_sound.play()

    def thrust_off(self):
        self.thrust = False
        ship_thrust_sound.rewind()

    def shoot(self):
        global a_missile, missile_group
        forward_vector = angle_to_vector(self.angle)
        cannon_pos0 = self.pos[0] + self.radius * forward_vector[0]
        cannon_pos1 = self.pos[1] + self.radius * forward_vector[1]
        missile_vel0 = self.vel[0] + forward_vector[0] * 5
        missile_vel1 = self.vel[1] + forward_vector[1] * 5
        a_missile = Sprite([cannon_pos0, cannon_pos1], \
                           [missile_vel0, missile_vel1], \
                           self.angle, 0, \
                           missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        if self.animated:
            current_index = self.age * self.image_size[0] // 1
            current_center = [self.image_center[0] + current_index, self.image_center[1]]
            canvas.draw_image(self.image, \
                              current_center, \
                              self.image_size, \
                              self.pos, \
                              self.image_size, \
                              self.angle)

        else:
            canvas.draw_image(self.image, \
                              self.image_center, \
                              self.image_size, \
                              self.pos, \
                              self.image_size, \
                              self.angle)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age += 1
        if self.age < self.lifespan:
            return False
        else:
            return True

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def get_vel(self):
        return self.vel

    def get_angle(self):
        return self.angle

    def get_angle_vel(self):
        return self.angle_vel

    def collide(self, other_object):
        if dist(other_object.get_position(), \
                self.get_position()) \
                < (other_object.get_radius() + self.get_radius()):
            return True
        else:
            return False


def keydown(key):
    if simplegui.KEY_MAP["up"] == key:
        my_ship.thrust_on()
    elif simplegui.KEY_MAP["left"] == key:
        my_ship.to_left()
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.to_right()
    elif simplegui.KEY_MAP["space"] == key:
        my_ship.shoot()


def keyup(key):
    if simplegui.KEY_MAP["left"] == key:
        my_ship.to_right()
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.to_left()
    elif simplegui.KEY_MAP["up"] == key:
        my_ship.thrust_off()


def click(pos):
    global started, score, lives, time
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
    score = 0
    lives = 3
    time = 0
    soundtrack.play()


def group_collide(group, other_object):
    global explosion_group
    remove_from_group = set([])
    group_copy = set(group)
    for e in group_copy:
        if e.collide(other_object):
            new_explosion = Sprite(e.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound)
            explosion_group.add(new_explosion)
            remove_from_group.add(e)
    group.difference_update(remove_from_group)
    if len(group) < len(group_copy):
        return True


def group_group_collide(group1, group2):
    group1_copy = set(group1)
    #    remove_from_group = set([])
    num_group_collisions = 0
    for m in group1_copy:
        if group_collide(group2, m):
            group1.discard(m)
            num_group_collisions += 1
    return num_group_collisions


def process_sprite_group(group, canvas):
    group_copy = set(group)
    remove_from_group = set([])
    for s in group_copy:
        s.draw(canvas)
        if s.update():
            remove_from_group.add(s)
        else:
            s.update()
    group.difference_update(remove_from_group)


def draw(canvas):
    global time, lives, score, started, rock_group, explosion_group

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text("Score: " + str(score), [WIDTH - 150, 50], 24, "White")
    canvas.draw_text("Lives: " + str(lives), [WIDTH - 148, 75], 24, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    #    a_rock.draw(canvas)
    #    a_missile.draw(canvas)

    # update ship and sprites
    my_ship.update()
    #    a_rock.update()
    #    a_missile.update()
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)

    if group_group_collide(rock_group, missile_group):
        score += 1

    if group_collide(rock_group, my_ship):
        lives -= 1
        new_explosion = Sprite(my_ship.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound)
        explosion_group.add(new_explosion)

    if lives == 0:
        rock_group = set([])
        started = False
        soundtrack.rewind()

    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())


# timer handler that spawns a rock
def rock_spawner():
    global rock_group, started, score
    #    pos[0] = random.randrange(WIDTH)
    #    pos[1] = random.randrange(HEIGHT)
    #    vel[0] = random.randrange(-1,1)
    #    vel[1] = random.randrange(-1,1)
    #    ang_vel = random.randrange(10)/10
    if score >= 20:
        score_tenths = score // 10
        vel = [random.randrange(-5, 5) / 10.0 * score_tenths, \
               random.randrange(-5, 5) / 10.0 * score_tenths]
    else:
        vel = [random.randrange(-5, 5) / 10.0, \
               random.randrange(-5, 5) / 10.0]
    a_rock = Sprite([random.randrange(WIDTH), \
                     random.randrange(HEIGHT)], \
                    vel, 5, random.choice([-1, 1]) * \
                    random.randrange(-50, 50) / 1000.0, \
                    asteroid_image, asteroid_info)
    if len(rock_group) <= 12 and started == True \
            and dist(a_rock.get_position(), my_ship.get_position()) >= my_ship.get_radius() + 10:
        rock_group.add(a_rock)
    else:
        pass


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
# a_rock = Sprite([WIDTH / 4, HEIGHT / 4], [-1, 1], 0, 0, asteroid_image, asteroid_info)
rock_group = set([])
# a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [0,0], 0, 0, missile_image, missile_info, missile_sound)
missile_group = set([])
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()