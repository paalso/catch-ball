import pathlib
import basic_classes.colors as colors

# Screen Settings
FPS = 30
screen_width = 1200
screen_height = int(screen_width / 1.5)
menu_width, menu_height = 400, 300
bg_color = colors.DARK_GREY
info_text_color = colors.AZURE
info_text_size = int(0.05 * screen_height)
padding = 20

game_results = pathlib.Path("data", "results.csv")
endgame_imgs = {
    "win": pathlib.Path("assets", "win.jpg"),
    "fail": pathlib.Path("assets", "fail.jpg"),
}
endgame_sounds = {
    "win": pathlib.Path("assets", "win.mp3"),
    "fail": pathlib.Path("assets", "fail.mp3"),
}
endgame_msgs = {
    "win":
        "You've won!\n" + \
        "Your final score is {}\n" + \
        "You are awesome!",
    "fail":
        "You've failed!\n" + \
        "Your final score is {}\n" + \
        "Goodbye, loser!",

}
endgame_delay = 7000    # in milliseconds
# msg_font = None
endgame_msg_position = \
        0.05 * screen_width, 0.05 * screen_height,
endgame_msg_size = int(0.07 * screen_height)
endgame_msg_color = colors.BROWN

# Game Settings
game_duration = 20  # in seconds
start_moving_items = 10
max_moving_items = 200
finish_early_bonus_factor = 1.2
extra_click_cost = 1

# Ball Settings
min_radius = 30
max_radius = 100
min_speed = 1
max_speed = 8
pop_sound = pathlib.Path("assets", "pop.mp3")

_creation_new_item_interval = 2   # in seconds
creation_new_item_frames = _creation_new_item_interval * FPS # in frames

# Ring Settings
min_inner_radius_factor = 0.25
max_inner_radius_factor = 0.45
wall_reflection_speed_min_biase = 1
wall_reflection_speed_max_biase = 7
point_increasing_factor = 1.2
frame_speed_stochastic_change = 2

_speed_change_interval = 2   # in seconds
speed_change_frames = _speed_change_interval * FPS  # in frames
