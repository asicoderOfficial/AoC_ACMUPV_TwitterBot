import requests

LEADERBOARD_ID = "547238"
LEADERBOARD_URL = "https://adventofcode.com/2019/leaderboard/private/view/{}".format(LEADERBOARD_ID)
SESSION_ID = "53616c7465645f5f22b2b896b560d2780f9554714e5519c7107568dd4cede343bee4ba9603e6e7f886d284d678fdf899"


def get_json():
    r = requests.get(
        "{}.json".format(LEADERBOARD_URL),
        cookies={"session": SESSION_ID}
    )
    if r.status_code != requests.codes.ok:
        print("Error retrieving leaderboard")
        exit(1)

    members = get_members(r.json()["members"])
    message = create_message(members)


def create_message(members):
    message = "Hello!\nThis is the actual leaderboard:\n"
    for username, score, stars in members:
        message += "*{}* {} Points, {} Stars\n".format(username, score, stars)

    message += "\n<{}|View Online Leaderboard>".format(LEADERBOARD_URL)

    return message


def get_members(members_of_json):
    members = [(m["name"], m["local_score"], m["stars"]) for m in members_of_json.values()]

    members.sort(key=lambda s: (-s[1], -s[2]))

    return members
