# Modelo Series - Serie de TV, hereda de Content (campos: current_season, current_episode, total_episodes)
from sqlalchemy import Column, Integer, ForeignKey
from src.models.content import Content

class Series(Content):
    __tablename__ = "series"

    id = Column(Integer, ForeignKey("contents.id"), primary_key=True)
    current_season = Column(Integer, default=1)
    current_episode = Column(Integer, default=1)
    total_episodes = Column(Integer, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "series",
    }

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "currentSeason": self.current_season, # Frontend expects camelCase
            "currentEpisode": self.current_episode,
            "totalEpisodes": self.total_episodes
        })
        return data