#pygame assignment
#%%
Group mate = Rachel
#%%
1. What is pygame? Can you modify its source code?
- pygame (the library) is a Free and Open Source python programming language library for making multimedia applications like games
- yes you can
#%%
2. What is Rectangle? How do you create a rectangle? (give sample code)
- Rectangle areas where the area inside can be manipulated
- cat.getRect()
#%%
3. Can you play music with pygame? (give sample code)
- yes you can
- pygame.mixer.init()
  pygame.mixer.music.load('filename')
  pygame.mixer.music.play()
#%%
4. A lot of games involve timer in its gameplay. How do you create a timer from round start to round finish? (give sample code)
- clock = pygame.time.clock()
  clock.tick()
  print(clock.get_time())
#%%
5. What is sprite and groups? When do you use it? (give sample code)
- sprite is a base class for objects in the game
- groups is a thing that stores a sprites
- when you want to group a bunch of objects into a single entity
- class Player(Sprite):
	def __init__(self,game):
		super().__init__()
		self.player = Player(self)
		self.players = pygame.sprite.group()
#%%
6. What is collision detection? Why is it important? (give sample code)
- collision detection is a code to detect if there is a collision between two objects
- because many game mechanics needed something to trigger a command when an object hit something
- if object.rect.colliderect(sprite.rect):
	return True
#%%
7. How do you display image in pygame? What is the function of blit? (give sample code)
- screen.blit(object)
- to show the object on the screen
#%%
8. How do you tell a bunch of sprites to update and draw at (almost) the same time? (give sample code)
- 
  all_sprites = pygame.sprite.group()
  all_sprites.draw()
#%%
10. What is game physics? Why is it important?
- game physics is how the object inside the game behave (movement,etc)
- it is important because it affects how the game works

#%%
11. How do you display text in pygame? (give sample code)
- text = font.render('test', False, (0,0,0))
  screen.blit(text(0,0))
#%%
12. How do you move a sprite / image in pygame? (give sample code)
class Broccoli(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

while True:
    Broccoli.rect.move_ip(0,1)

#%%
13. How do you fill a color of a surface? (give sample code)
- image = pygame.Surface((20,20))
  image.fill(RED)
#%%
14. You have a player sprite. How do you randomize its position in a screen? (give sample code)
- class Player(Sprite):
	def __init(self,game):
		super().__init__()
  		self.rect.x = randint(0,self.screen_rect.right-self.rect.width)
  		self.rect.y = randint(0,self.screen_rect.bottom-self.rect.height)
#%%
15. Did you notice there are no number 9? (Y/N) 
- N
#%%