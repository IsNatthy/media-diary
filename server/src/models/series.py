# Modelo Series - Serie de TV, hereda de Content (campos: current_season, current_episode, total_episodes)

from app.src.models.content import Content

class Series(Content):
    def __init__(self, id, name, year, type, genre, state, current_season, current_episode, total_episodes):
        super().__init__(id, name, year, type="series", genre, state)
        self.current_season = current_season
        self.current_episode = current_episode
        self.total_episodes = total_episodes