let Pac_man = sprites.create(img`
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
Pac_man.setPosition(135, 130)
scene.cameraFollowSprite(Pac_man)
scene.setBackgroundColor(15)
tiles.setCurrentTilemap(tilemap`level1`)
controller.moveSprite(Pac_man, 100, 100)
