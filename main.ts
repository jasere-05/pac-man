namespace SpriteKind {
    export const bonus = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    Pac_man,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite2, otherSprite2) {
    if (kill == false) {
        dead = false
        pause(400)
        dead = true
        info.changeLifeBy(-1)
    } else {
        sprites.destroy(sprite2)
        info.changeScoreBy(5)
        gost += -1
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.bonus, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    kill = true
    stars += -1
    pause(6000)
    kill = false
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    Pac_man,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
info.onScore(100, function () {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.confetti)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    Pac_man,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    Pac_man,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite3, otherSprite3) {
    sprites.destroy(otherSprite3)
    info.changeScoreBy(10)
})
let fruit: Sprite = null
let bon: Sprite = null
let stars = 0
let Pac_man: Sprite = null
let kill = false
let dead = false
class ActionKind {
    static Walking: number
    private ___Walking_is_set: boolean
    private ___Walking: number
    get Walking(): number {
        return this.___Walking_is_set ? this.___Walking : ActionKind.Walking
    }
    set Walking(value: number) {
        this.___Walking_is_set = true
        this.___Walking = value
    }
    
    static Idle: number
    private ___Idle_is_set: boolean
    private ___Idle: number
    get Idle(): number {
        return this.___Idle_is_set ? this.___Idle : ActionKind.Idle
    }
    set Idle(value: number) {
        this.___Idle_is_set = true
        this.___Idle = value
    }
    
    static Jumping: number
    private ___Jumping_is_set: boolean
    private ___Jumping: number
    get Jumping(): number {
        return this.___Jumping_is_set ? this.___Jumping : ActionKind.Jumping
    }
    set Jumping(value: number) {
        this.___Jumping_is_set = true
        this.___Jumping = value
    }
    
    public static __initActionKind() {
        ActionKind.Walking = 0
        ActionKind.Idle = 1
        ActionKind.Jumping = 2
    }
    
}
ActionKind.__initActionKind()
let gost = 5
dead = true
kill = false
Pac_man = sprites.create(img`
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
    `, SpriteKind.Player)
info.setLife(5)
Pac_man.setPosition(170, 170)
scene.cameraFollowSprite(Pac_man)
scene.setBackgroundColor(15)
tiles.setCurrentTilemap(tilemap`level1`)
controller.moveSprite(Pac_man, 100, 100)
pause(5000)
let ft1 = sprites.create(img`
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
    `, SpriteKind.Enemy)
ft1.setPosition(170, 170)
let ft2 = sprites.create(img`
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
    `, SpriteKind.Enemy)
ft2.setPosition(170, 170)
let ft3 = sprites.create(img`
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
    `, SpriteKind.Enemy)
ft3.setPosition(170, 170)
let ft4 = sprites.create(img`
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
    `, SpriteKind.Enemy)
ft4.setPosition(170, 170)
let ft5 = sprites.create(img`
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
    `, SpriteKind.Enemy)
ft5.setPosition(170, 170)
game.onUpdate(function () {
    if (kill == false) {
        if (dead == true) {
            ft1.follow(Pac_man, 60)
            ft2.follow(Pac_man, 80)
            ft3.follow(Pac_man, 40)
            ft4.follow(Pac_man, 30)
            ft5.follow(Pac_man, 50)
        } else {
            ft1.follow(Pac_man, 0)
            ft2.follow(Pac_man, 0)
            ft3.follow(Pac_man, 0)
            ft4.follow(Pac_man, 0)
            ft5.follow(Pac_man, 0)
        }
    } else {
        ft1.follow(Pac_man, -40)
        ft2.follow(Pac_man, -10)
        ft3.follow(Pac_man, -40)
        ft4.follow(Pac_man, -30)
        ft5.follow(Pac_man, -20)
    }
})
game.onUpdate(function () {
    if (gost == 0) {
        game.gameOver(true)
        game.setGameOverEffect(true, effects.confetti)
    }
})
game.onUpdate(function () {
    if (kill == false) {
        ft1.setImage(img`
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
            `)
        ft2.setImage(img`
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
            `)
        ft3.setImage(img`
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
            `)
        ft4.setImage(img`
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
            `)
        ft5.setImage(img`
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
            `)
        controller.moveSprite(Pac_man, 100, 100)
    } else {
        ft1.setImage(img`
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
            `)
        ft2.setImage(img`
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
            `)
        ft3.setImage(img`
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
            `)
        ft4.setImage(img`
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
            `)
        ft5.setImage(img`
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
            `)
    }
    controller.moveSprite(Pac_man, 130, 130)
})
game.onUpdateInterval(15000, function () {
    if (stars == 0) {
        bon = sprites.create(img`
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
            `, SpriteKind.bonus)
        tiles.placeOnRandomTile(bon, assets.tile`transparency16`)
        stars += 1
    }
})
game.onUpdateInterval(10000, function () {
    fruit = sprites.create(img`
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
        `, SpriteKind.Food)
    tiles.placeOnRandomTile(fruit, assets.tile`transparency16`)
})
