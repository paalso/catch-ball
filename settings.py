import colors
import pathlib


# Screen Settings
FPS = 30
screen_width, screen_height = 900, 600
bg_color = colors.BLACK

max_moving_items = 7

# Ball Settings
min_radius = 100
max_radius = 100
min_speed = 1   # не нужно
max_speed = 1
pop_sound = pathlib.Path("assets", "pop.mp3")

# Ring Settings
inner_radius_quotient = 0.4
wall_reflection_speed_min_biase = 1
wall_reflection_speed_max_biase = 7
point_increasing_quotient = 1.2
speed_stochastic_quotient = 5
_speed_change_time = 2   # in seconds
speed_change_frames = _speed_change_time * FPS  # in seconds


