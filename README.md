# ping_pong

This code is a Python script for creating a simple "Ping-Pong" game using the Turtle graphics library. Here's a description of the main components and functionality of the code:

Screen Setup: The code creates a graphical window using Turtle. It sets the title, background color, and dimensions of the screen.

Paddles: Two paddles, one on the left (red) and one on the right (blue), are created using Turtle. These paddles can be moved up and down by the players to hit the ball.

Ball: A ball is created as a black circular shape using Turtle. It's initialized with a starting position at the center of the screen and given initial velocity components (dx and dy) to move diagonally.

Score: The score for both players is displayed at the top of the screen using Turtle. The maximum score required to win the game is set to 5, but this can be adjusted.

Paddle Movement Functions: There are four functions for moving the paddles up and down in response to user key presses. These functions update the y-coordinates of the paddles.

Key Bindings: Key bindings are set up to associate specific keys with paddle movements. The "r" and "c" keys control the left paddle (up and down, respectively), while the "Up" and "Down" arrow keys control the right paddle.

Game Over Handling: The game has a flag called game_over to indicate whether the game is over or not. If the game is over, it displays a "Game Over" message and provides options to replay or quit the game.

Main Game Loop: The code enters a main game loop that continually updates the game's state. In this loop, it checks for collisions with the screen borders, updates the score when a player scores a point, and checks for collisions between the ball and paddles.

Replay and Quit Functions: The code defines two functions, replay_game and quit_game, which are used when the game is over. replay_game resets the game, and quit_game closes the Turtle graphics window and exits the game.

The game loop continues to run indefinitely, and players can control the paddles to hit the ball. When one of the players reaches the specified maximum score, the game will end, and they have the option to replay or quit.

It's worth noting that the code defines the replay and quit functions within the main loop, which may not be the best practice for code organization. It's typically better to define these functions outside of the game loop.
