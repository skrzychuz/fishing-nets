class Settings():

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (231, 231, 231)
        self.font_color = (80, 80, 80)

        # Nets settings
        self.net_speed = 1.5
        self.net_width = 200
        self.net_height = 2
        self.net_color = 60, 60, 60
        self.net_limit = 10 # 100 (one hundred)

        # Fish
        self.rows_drop = 0

        # 1 for right, -1 left
        self.rows_direction = 1

        self.game_active = True

        self.scores = 0

        self.url = 'https://api.myjson.com/bins/z3kww'
        self.filename = 'data.json'
