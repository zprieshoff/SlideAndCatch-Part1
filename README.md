# (lab) Slide and Catch Part 1

This is a simple slide and catch game with an arcade/pixel space theme. Users constrol the space ship using the left and right arrow keys to catch the following fuel canisters. fuel canisters fall at random speeds and from random locations.

# Sprite Details

## Fuel Sprite
* **Class name:** "Fuel"
* **Image:** "fuel.png"
* **Size:** 30x30
* **Sprite Type:** Can be a BasicSprite because of its simple motion but it is a SuperSprite.
* **Being Born:** Spawned at the top of the screen at random locations.
* **Dying:** Doesn't necessary die or get destroyed, when it makes contact with the user its location is simply reset.
* **Movement:** Starting from the top of the screen, the sprite(s) fall to the bottom of the screen.
* **Control:** Controlled by the computer.
* **Motion:** Almost like gravity, constantly moving to the bottom of the screen at random speeds.
* **Off-Stage** Sprites are never really off the screen/stage.
* **Collision:** When they makes contact with the user, its location is reset to a random location at the top of the screen.

## Ship Sprite
* **Class name:** "Ship"
* **Image:** "spaceship.png"
* **Size:** 50x40
* **Sprite Type:** Can be a BasicSprite because of its simple motion but it is a SuperSprite. Would need to be a SuperSprite if more complex motions or maybe abilities are added.
* **Being Born:** Spawned in the middle at the bottom of the screen. Same spot everytime.
* **Dying:** Doesn't die or get destroyed, this mechanic can be added later if lives and enemey sprites or things you need to avoid are added.
* **Movement:** Starting from the bottom middle of the screen, the user moves the sprite left and right at a set speed.
* **Control:** Controlled by the user pressing left and right arrow keys.
* **Motion:** Horizontal movement with screen boundaries so that the sprite doesn't go off screen
* **Off-Stage** Sprite is never really off the screen/stage.
* **Collision:** When it makes contact with the fuel sprite only the fuel sprite is affected. Later will add a points system.

## UI Components
* **Pre-game Explanation:** Currently there is no pre-game. Later will add an interactive menu with buttons like "Play" or "Quit".
* **Gameplay Feedback:** Currently there is no in-game feedback. Later will add a points system that is linked to a timer. If the user doesn't get X amount of points in X amount of time they lose. A message like "Lost in space!" could be displayed if they lose, and maybe "Your journey continues!" if they win.
* **Needed UI Components:** Text for the users score, maybe a fuel meter that will act as the countdown.
* **Mechanics Update:** These components would have to be updated in real time during gameplay, every X seconds the fuel meter drops by one. Every time the user catches fuel their score will go up and fuel meter will raise by one.
* **UI Placement:** Score could be at the top of the screen, and the fuel meter at the side. These shouldn't block gameplay.

## Game States
* **States:** Currently there is only a playing state. Later will have a Start Menu, playing, and a Game Over Menu.
* **Transfer Between States:** Currently there is no transfer. The player can play the game and that is it. Later, the transitions will look like *Start Menu* > *Playing Game* by pressing the start key, which will probably be space. In game it will look like *Playing Game* > *Game Over/Retry* > *Start Menu* to go from the Game Over Menu to the Start Menu the user would be prompted with a "Replay" option, this key could either be space to keep it consistent or r for replay.
* **Communication Between States:** The users top score could be passed through the states to have a "High score" mechanic.
* **Game Ending:** Currently the game can only end by the user manually closing out of the pygame window. Later will have a mechanic to end the game when the fuel meter is empty, then the user can press a key to quit the game. This key could be q.

## Sound Effects
* **Needed Sound Effects:** Game Start, Collecting fuel "powerup.wav", Game Over. Already have collecting fuel sound, its annoying but good so turn your volume down.
* **Sound Playback:** Game Start sound would be played when the user presses space while in the Start Menu State. Collecting fuel sound is already played when the user collects fuel. Game Over sound would be played when the users fuel meter goes down, then if the user chooses to replay the Game Start sound can be played again.
* **Sound Code Placement:** Should be in event handling sections for their causes.

## Background Image
* **Image:** There is a background image that represents a pixel space theme.
* **Where?:** I created the image myself.
* **Visability:** The gameplay can still be clearly seen because the sprites are brightly color and the background image is dark.

## Intellectual Property
* **Fuel:** Image taken from pixelart https://www.pixilart.com/draw/gas-can-0d8faf0067e0f64
* **Ship:** Image made by me using pixilart
* **Collecting Fuel:** Sound taken from Freesound https://freesound.org/people/Romeo_Kaleikau/sounds/588251/
