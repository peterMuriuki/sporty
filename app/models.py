from sqlalchemy import Column, Integer, TIMESTAMP, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os

database_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'files', 'database', 'eanmble.db'))
engine = create_engine('sqlite:///' + database_dir)
session = Session(bind=engine)


BASE = declarative_base()


class Team(BASE):
    """Represents the data that will be saved about a specific team

    a representation of the aspects that are most important in this preliminary
    survey, this aspects will be added to the data csv file
    """
    __tablename__ = 'Teams'

    id = Column(Integer, primary_key=True)
    time = Column(Integer)
    team_name = Column(String)
    country = Column(String)
    league = Column(String)
    goals_conceded = Column(Integer)
    goals_scored = Column(Integer)
    logo = Column(String)
    flagged = Column(Integer, default=0)
    # types of checkers that we will be using: over, under, win, loss, draw,
    over = Column(Boolean)
    under = Column(Boolean)
    win = Column(Boolean)
    draw = Column(Boolean)
    loss = Column(Boolean)


    def __init__(self, team_name, time, country_name, league_name, goals_scored, goals_conceded):

        if type(country_name) is not str:
            raise TypeError('The Country_Name')
        self.country = country_name

        if not isinstance(team_name, str):
            raise TypeError('The Team_name is not a String')
        self.team_name = team_name

        if not isinstance(league_name, str):
            raise TypeError('unrecognized format for league name')
        self.league = league_name

        if not isinstance(goals_conceded, int) or not isinstance(goals_scored, int):
            raise TypeError('Unrecognized format for both goals scored and goals conceded')
        self.goals_conceded = goals_conceded
        self.goals_scored = goals_scored

        self.time = time

    def __repr__(self):
        """formats a string into an arbitrary string presentation"""
        return '<{}{}{}{}{}{}{}>'.format(self.id, self.team_name, self.time, self.country,
                                self.league, self.goals_scored, self.goals_conceded)