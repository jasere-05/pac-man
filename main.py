class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
@namespace
class SpriteKind:
    bonus = SpriteKind.create()

def on_up_pressed():
    animation.run_image_animation(Pac_man,
        [img("""
                . . . f f . . . . f . . . . 
                        . . f 5 5 f . . f 5 f . . . 
                        . f 5 5 5 f . . f 5 5 f . . 
                        . f 5 5 5 5 f f 5 5 5 5 f . 
                        f 5 5 5 5 5 f f 5 5 5 5 f . 
                        f 5 1 1 f 5 f f 5 5 5 5 5 f 
                        f 5 f f f 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 f . . . 
                        . . . f f f 5 5 f f . . . . 
                        . . . . . . f f . . . . . .
            """),
            img("""
                . . . . . . f f . . . . . . 
                        . . . f f f 5 f f f . . . . 
                        . . f 5 5 5 5 f 5 5 f . . . 
                        . f 5 5 5 5 5 f 5 5 5 f . . 
                        . f 5 5 5 5 5 f 5 5 5 5 f . 
                        f 5 5 5 5 5 5 f 5 5 5 5 f . 
                        f 5 1 1 f 5 f f 5 5 5 5 5 f 
                        f 5 f f f 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 f . . . 
                        . . . f f f 5 5 f f . . . .
            """)],
        500,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite, otherSprite):
    global kill, stars
    sprites.destroy(otherSprite)
    kill = True
    stars += -1
    pause(6000)
    kill = False
sprites.on_overlap(SpriteKind.player, SpriteKind.bonus, on_on_overlap)

def on_left_pressed():
    animation.run_image_animation(Pac_man,
        [img("""
                . . . . f f f f f . . . . . 
                        . . f f 5 5 5 5 5 f f . . . 
                        . f 5 5 5 1 f 5 5 5 5 f . . 
                        f 5 5 5 5 1 f 5 5 5 5 5 f . 
                        f 5 5 5 5 f f 5 5 5 5 5 f . 
                        . f f 5 5 5 5 5 5 5 5 5 f . 
                        . . . f f f 5 5 5 5 5 5 5 f 
                        . . . f f f 5 5 5 5 5 5 5 f 
                        . f f 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 f . . . 
                        . . . f f 5 5 5 f f . . . . 
                        . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . f f f f f . . . . 
                        . . . f f 5 5 5 5 5 f f . . 
                        . . f 5 5 5 1 f 5 5 5 5 f . 
                        . f 5 5 5 5 1 f 5 5 5 5 5 f 
                        . f 5 5 5 5 f f 5 5 5 5 5 f 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 f 5 5 5 5 5 5 5 
                        f f f f f f f 5 5 5 5 5 5 5 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f 
                        . . f 5 5 5 5 5 5 5 5 5 f . 
                        . . . f 5 5 5 5 5 5 5 f . . 
                        . . . . f f 5 5 5 f f . . . 
                        . . . . . . f f f . . . . .
            """)],
        500,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_score():
    game.game_over(True)
    game.set_game_over_effect(True, effects.confetti)
info.on_score(100, on_on_score)

def on_right_pressed():
    animation.run_image_animation(Pac_man,
        [img("""
                . . . . . f f f f f . . . . 
                        . . . f f 5 5 5 5 5 f f . . 
                        . . f 5 5 5 5 f 1 5 5 5 f . 
                        . f 5 5 5 5 5 f 1 5 5 5 5 f 
                        . f 5 5 5 5 5 f f 5 5 5 5 f 
                        . f 5 5 5 5 5 5 5 5 5 f f . 
                        f 5 5 5 5 5 5 5 f f f . . . 
                        f 5 5 5 5 5 5 5 f f f . . . 
                        . f 5 5 5 5 5 5 5 5 5 f f . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f 
                        . . f 5 5 5 5 5 5 5 5 5 f . 
                        . . . f 5 5 5 5 5 5 5 f . . 
                        . . . . f f 5 5 5 f f . . . 
                        . . . . . . f f f . . . . .
            """),
            img("""
                . . . . f f f f f . . . . . 
                        . . f f 5 5 5 5 5 f f . . . 
                        . f 5 5 5 5 f 1 5 5 5 f . . 
                        f 5 5 5 5 5 f 1 5 5 5 5 f . 
                        f 5 5 5 5 5 f f 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        5 5 5 5 5 5 5 f 5 5 5 5 5 f 
                        5 5 5 5 5 5 5 f f f f f f f 
                        f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 f . . . 
                        . . . f f 5 5 5 f f . . . . 
                        . . . . . f f f . . . . . .
            """)],
        500,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    global dead, gost
    if kill == False:
        dead = False
        pause(400)
        dead = True
        info.change_life_by(-1)
    else:
        sprites.destroy(sprite2)
        info.change_score_by(5)
        gost += -1
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_down_pressed():
    animation.run_image_animation(Pac_man,
        [img("""
                . . . . . . f f . . . . . . 
                        . . . . f f 5 5 f f f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 5 5 5 f f f 5 f 
                        f 5 5 5 5 5 f f 5 f 1 1 5 f 
                        . f 5 5 5 5 f f 5 5 5 5 5 f 
                        . f 5 5 5 5 f f 5 5 5 5 f . 
                        . . f 5 5 f . . f 5 5 5 f . 
                        . . . f 5 f . . f 5 5 f . . 
                        . . . . f . . . . f f . . .
            """),
            img("""
                . . . . f f 5 5 f f f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 f 
                        f 5 5 5 5 5 5 5 5 f f f 5 f 
                        f 5 5 5 5 5 f f 5 f 1 1 5 f 
                        . f 5 5 5 5 f 5 5 5 5 5 5 f 
                        . f 5 5 5 5 f 5 5 5 5 5 f . 
                        . . f 5 5 5 f 5 5 5 5 5 f . 
                        . . . f 5 5 f 5 5 5 5 f . . 
                        . . . . f f f 5 f f f . . . 
                        . . . . . . f f . . . . . .
            """)],
        500,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap3(sprite3, otherSprite3):
    sprites.destroy(otherSprite3)
    info.change_score_by(10)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

bon: Sprite = None
fruit: Sprite = None
avoid: Sprite = None
Pac_man: Sprite = None
kill = False
dead = False
gost = 5
dead = True
kill = False
Pac_man = sprites.create(img("""
        . . . . . f f f f f . . . . 
            . . . f f 5 5 5 5 5 f f . . 
            . . f 5 5 5 5 f 1 5 5 5 f . 
            . f 5 5 5 5 5 f 1 5 5 5 5 f 
            . f 5 5 5 5 5 f f 5 5 5 5 f 
            . f 5 5 5 5 5 5 5 5 5 f f . 
            f 5 5 5 5 5 5 5 f f f . . . 
            f 5 5 5 5 5 5 5 f f f . . . 
            . f 5 5 5 5 5 5 5 5 5 f f . 
            . f 5 5 5 5 5 5 5 5 5 5 5 f 
            . . f 5 5 5 5 5 5 5 5 5 f . 
            . . . f 5 5 5 5 5 5 5 f . . 
            . . . . f f 5 5 5 f f . . . 
            . . . . . . f f f . . . . .
    """),
    SpriteKind.player)
info.set_life(5)
Pac_man.set_position(170, 170)
scene.camera_follow_sprite(Pac_man)
scene.set_background_color(15)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
controller.move_sprite(Pac_man, 100, 100)
pause(5000)
ft1 = sprites.create(img("""
        . . . . f f 1 1 1 1 f f . . . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . . f 1 1 1 1 1 1 1 1 f . . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d d d 1 1 1 1 d d d f . 
            . . f b d b f d d f b d b f . 
            . . f c d c f 1 1 f c d c f . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . f f f c d b 1 b d f f f f 
            f c 1 1 1 c b f b f c 1 1 1 c 
            f 1 b 1 b 1 f f f f 1 b 1 b 1 
            f b f b f f f f f f b f b f b 
            . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . .
    """),
    SpriteKind.enemy)
ft1.set_position(170, 170)
ft2 = sprites.create(img("""
        . . . . f f 1 1 1 1 f f . . . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . . f 1 1 1 1 1 1 1 1 f . . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d d d 1 1 1 1 d d d f . 
            . . f b d b f d d f b d b f . 
            . . f c d c f 1 1 f c d c f . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . f f f c d b 1 b d f f f f 
            f c 1 1 1 c b f b f c 1 1 1 c 
            f 1 b 1 b 1 f f f f 1 b 1 b 1 
            f b f b f f f f f f b f b f b 
            . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . .
    """),
    SpriteKind.enemy)
ft2.set_position(170, 170)
ft3 = sprites.create(img("""
        . . . . f f 1 1 1 1 f f . . . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . . f 1 1 1 1 1 1 1 1 f . . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d d d 1 1 1 1 d d d f . 
            . . f b d b f d d f b d b f . 
            . . f c d c f 1 1 f c d c f . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . f f f c d b 1 b d f f f f 
            f c 1 1 1 c b f b f c 1 1 1 c 
            f 1 b 1 b 1 f f f f 1 b 1 b 1 
            f b f b f f f f f f b f b f b 
            . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . .
    """),
    SpriteKind.enemy)
ft3.set_position(170, 170)
ft4 = sprites.create(img("""
        . . . . f f 1 1 1 1 f f . . . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . . f 1 1 1 1 1 1 1 1 f . . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d d d 1 1 1 1 d d d f . 
            . . f b d b f d d f b d b f . 
            . . f c d c f 1 1 f c d c f . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . f f f c d b 1 b d f f f f 
            f c 1 1 1 c b f b f c 1 1 1 c 
            f 1 b 1 b 1 f f f f 1 b 1 b 1 
            f b f b f f f f f f b f b f b 
            . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . .
    """),
    SpriteKind.enemy)
ft4.set_position(170, 170)
ft5 = sprites.create(img("""
        . . . . f f 1 1 1 1 f f . . . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . . f 1 1 1 1 1 1 1 1 f . . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d 1 1 1 1 1 1 1 1 d f . 
            . . f d d d 1 1 1 1 d d d f . 
            . . f b d b f d d f b d b f . 
            . . f c d c f 1 1 f c d c f . 
            . . . f b 1 1 1 1 1 1 b f . . 
            . . f f f c d b 1 b d f f f f 
            f c 1 1 1 c b f b f c 1 1 1 c 
            f 1 b 1 b 1 f f f f 1 b 1 b 1 
            f b f b f f f f f f b f b f b 
            . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . .
    """),
    SpriteKind.enemy)
ft5.set_position(170, 170)
stars = 0

def on_on_update():
    if kill == False:
        if dead == True:
            ft1.follow(Pac_man, 60)
            ft2.follow(Pac_man, 80)
            ft3.follow(Pac_man, 40)
            ft4.follow(Pac_man, 30)
            ft5.follow(Pac_man, 50)
        else:
            ft1.follow(Pac_man, 0)
            ft2.follow(Pac_man, 0)
            ft3.follow(Pac_man, 0)
            ft4.follow(Pac_man, 0)
            ft5.follow(Pac_man, 0)
    else:
        ft1.follow(Pac_man, -50)
        ft2.follow(Pac_man, -10)
        ft3.follow(Pac_man, -40)
        ft4.follow(Pac_man, -30)
        ft5.follow(Pac_man, -20)
game.on_update(on_on_update)

def on_on_update2():
    if gost == 0:
        game.game_over(True)
        game.set_game_over_effect(True, effects.confetti)
game.on_update(on_on_update2)

def on_on_update3():
    if kill == False:
        ft1.set_image(img("""
            ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
        """))
        ft2.set_image(img("""
            ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
        """))
        ft3.set_image(img("""
            ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
        """))
        ft4.set_image(img("""
            ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
        """))
        ft5.set_image(img("""
            ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
        """))
        controller.move_sprite(Pac_man)
        ft1.set_bounce_on_wall(False)
        ft2.set_bounce_on_wall(False)
        ft3.set_bounce_on_wall(False)
        ft4.set_bounce_on_wall(False)
        ft5.set_bounce_on_wall(False)
    else:
        ft1.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c c c . . . . 
                        . . . . . . c c d d d d c . . . 
                        . . . . . c c c c c c d c . . . 
                        . . . . c c 4 4 4 4 d c c . . . 
                        . . . c 4 d 4 4 4 4 4 1 c . c c 
                        . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
                        . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
                        f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                        f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
                        f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
                        . f 4 4 4 4 1 c 4 f 4 d f f f f 
                        . . f f 4 d 4 4 f f 4 c f c . . 
                        . . . . f f 4 4 4 4 c d b c . . 
                        . . . . . . f f f f d d d c . . 
                        . . . . . . . . . . c c c . . .
        """))
        ft2.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c c c . . . . 
                        . . . . . . c c d d d d c . . . 
                        . . . . . c c c c c c d c . . . 
                        . . . . c c 4 4 4 4 d c c . . . 
                        . . . c 4 d 4 4 4 4 4 1 c . c c 
                        . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
                        . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
                        f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                        f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
                        f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
                        . f 4 4 4 4 1 c 4 f 4 d f f f f 
                        . . f f 4 d 4 4 f f 4 c f c . . 
                        . . . . f f 4 4 4 4 c d b c . . 
                        . . . . . . f f f f d d d c . . 
                        . . . . . . . . . . c c c . . .
        """))
        ft3.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c c c . . . . 
                        . . . . . . c c d d d d c . . . 
                        . . . . . c c c c c c d c . . . 
                        . . . . c c 4 4 4 4 d c c . . . 
                        . . . c 4 d 4 4 4 4 4 1 c . c c 
                        . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
                        . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
                        f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                        f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
                        f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
                        . f 4 4 4 4 1 c 4 f 4 d f f f f 
                        . . f f 4 d 4 4 f f 4 c f c . . 
                        . . . . f f 4 4 4 4 c d b c . . 
                        . . . . . . f f f f d d d c . . 
                        . . . . . . . . . . c c c . . .
        """))
        ft4.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c c c . . . . 
                        . . . . . . c c d d d d c . . . 
                        . . . . . c c c c c c d c . . . 
                        . . . . c c 4 4 4 4 d c c . . . 
                        . . . c 4 d 4 4 4 4 4 1 c . c c 
                        . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
                        . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
                        f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                        f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
                        f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
                        . f 4 4 4 4 1 c 4 f 4 d f f f f 
                        . . f f 4 d 4 4 f f 4 c f c . . 
                        . . . . f f 4 4 4 4 c d b c . . 
                        . . . . . . f f f f d d d c . . 
                        . . . . . . . . . . c c c . . .
        """))
        ft5.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c c c . . . . 
                        . . . . . . c c d d d d c . . . 
                        . . . . . c c c c c c d c . . . 
                        . . . . c c 4 4 4 4 d c c . . . 
                        . . . c 4 d 4 4 4 4 4 1 c . c c 
                        . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
                        . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
                        f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
                        f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
                        f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
                        . f 4 4 4 4 1 c 4 f 4 d f f f f 
                        . . f f 4 d 4 4 f f 4 c f c . . 
                        . . . . f f 4 4 4 4 c d b c . . 
                        . . . . . . f f f f d d d c . . 
                        . . . . . . . . . . c c c . . .
        """))
        ft1.set_bounce_on_wall(True)
        ft2.set_bounce_on_wall(False)
        ft3.set_bounce_on_wall(False)
        ft4.set_bounce_on_wall(False)
        ft5.set_bounce_on_wall(False)
        controller.move_sprite(Pac_man, 130, 130)
game.on_update(on_on_update3)

def on_on_update4():
    global avoid
    avoid = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
game.on_update(on_on_update4)

def on_update_interval():
    global fruit
    fruit = sprites.create(img("""
            . . . . . . . . . . . 6 6 6 6 6 
                    . . . . . . . . . 6 6 7 7 7 7 8 
                    . . . . . . 8 8 8 7 7 8 8 6 8 8 
                    . . e e e e c 6 6 8 8 . 8 7 8 . 
                    . e 2 5 4 2 e c 8 . . . 6 7 8 . 
                    e 2 4 2 2 2 2 2 c . . . 6 7 8 . 
                    e 2 2 2 2 2 2 2 c . . . 8 6 8 . 
                    e 2 e e 2 2 2 2 e e e e c 6 8 . 
                    c 2 e e 2 2 2 2 e 2 5 4 2 c 8 . 
                    . c 2 e e e 2 e 2 4 2 2 2 2 c . 
                    . . c 2 2 2 e e 2 2 2 2 2 2 2 e 
                    . . . e c c e c 2 2 2 2 2 2 2 e 
                    . . . . . . . c 2 e e 2 2 e 2 c 
                    . . . . . . . c e e e e e e 2 c 
                    . . . . . . . . c e 2 2 2 2 c . 
                    . . . . . . . . . c c c c c . .
        """),
        SpriteKind.food)
    tiles.place_on_random_tile(fruit, assets.tile("""
        transparency16
    """))
game.on_update_interval(10000, on_update_interval)

def on_update_interval2():
    global bon, stars
    if stars == 0:
        bon = sprites.create(img("""
                . . . . . . . . . . . . . . . 
                            . . . . . . . b . . . . . . . 
                            . . . . . . b d b . . . . . . 
                            . . . . . . c d c . . . . . . 
                            . . . . . . c 5 c . . . . . . 
                            . . . . . c d 5 d c . . . . . 
                            . . b c c d 5 5 5 d c c b . . 
                            . b d d 5 5 5 5 5 5 5 d d b . 
                            . . b c c d 5 5 5 d c c b . . 
                            . . . . . c d 5 d c . . . . . 
                            . . . . . . c 5 c . . . . . . 
                            . . . . . . c d c . . . . . . 
                            . . . . . . b d b . . . . . . 
                            . . . . . . . b . . . . . . . 
                            . . . . . . . . . . . . . . .
            """),
            SpriteKind.bonus)
        tiles.place_on_random_tile(bon, assets.tile("""
            transparency16
        """))
        stars += 1
game.on_update_interval(10000, on_update_interval2)
