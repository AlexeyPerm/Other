from typing import List


def checkio(game_result: List[str]) -> str:
    for k in game_result:
        if k[0] == k[1] == k[2] and k[0] != ".":
            return k[0]

    for l in zip(game_result[0], game_result[1], game_result[2]):
        if len(set(l)) == 1 and '.' not in l:
            return l[0]

    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != "." or \
            game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[2][0] != ".":
        return game_result[1][1]
    return 'D'


if __name__ == '__main__':
    checkio([".O.", "...", "..."])