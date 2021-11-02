import pathlib
import basic_classes.colors as colors

# Screen Settings
FPS = 30
screen_width, screen_height = 900, 600
bg_color = colors.BLACK

start_moving_items = 10
max_moving_items = 200

# Ball Settings
min_radius = 20
max_radius = 100
min_speed = 1
max_speed = 15
pop_sound = pathlib.Path("assets", "pop.mp3")

_creation_new_item_interval = 2   # in seconds
creation_new_item_frames = _creation_new_item_interval * FPS # in frames

# Ring Settings
inner_radius_quotient = 0.4
wall_reflection_speed_min_biase = 1
wall_reflection_speed_max_biase = 7
point_increasing_quotient = 1.2
frame_speed_stochastic_change = 2
##speed_stochastic_quotient = 5


_speed_change_interval = 2   # in seconds
speed_change_frames = _speed_change_interval * FPS  # in frames
