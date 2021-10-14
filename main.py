namespace SpriteKind {
    export const GolfBall = SpriteKind.create()
    export const Hole = SpriteKind.create()
}
scene.onHitTile(SpriteKind.GolfBall, 0, function (sprite) {
    golfball.stopDart()
})
let golfball: Dart = null
tiles.setTilemap(tilemap`level1`)
scene.setTile(14, img`
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    e e e e e e e e e e e e e e e e 
    `, true)
scene.setBackgroundColor(7)
golfball = darts.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . 1 1 1 1 1 . . . . . . 
    . . . . 1 1 1 1 1 1 1 . . . . . 
    . . . 1 1 1 1 1 1 1 1 1 . . . . 
    . . . 1 1 1 1 1 1 1 1 1 . . . . 
    . . . 1 1 1 1 1 1 1 1 1 . . . . 
    . . . 1 1 1 1 1 1 1 1 1 . . . . 
    . . . . 1 1 1 1 1 1 1 . . . . . 
    . . . . . 1 1 1 1 1 . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.GolfBall, 25, 110)
golfball.setTrace()
golfball.controlWithArrowKeys()
let hole = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . 2 . . . . . . . 
    . . . . . . . 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . 2 2 2 2 . . . . . . . 
    . . . . 2 2 2 2 2 . . . . . . . 
    . . . 2 2 2 2 2 2 . . . . . . . 
    . . . . . . . . 1 . . . . . . . 
    . . . . . . . . 1 . . . . . . . 
    . . . . . . . . 1 . . . . . . . 
    . . . . . . . . 1 . . . . . . . 
    . . . . . . 1 1 1 1 1 . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Hole)
hole.setPosition(960, 105)
scene.cameraFollowSprite(golfball.sprite)
