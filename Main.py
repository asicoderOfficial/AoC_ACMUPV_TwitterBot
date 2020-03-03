from LeaderboardsDB import create_db
# from LeaderboardsDB import insert_new_leaderboard
# from LeaderboardsDB import erase_contestant
# from LeaderboardsDB import update_db

from JsonParser import create_message
from JsonParser import get_json
from JsonParser import get_members

from Twitterer import leaderboard_tweet


def main():
    leaderboard_tweet()


if __name__ == "__main__":
    main()
