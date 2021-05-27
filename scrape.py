from typing import Optional, Union
import io
import chess
import chess.pgn
from lxml import html
import requests


def get_pgn_from_chessgame_page(game_id: Union[int, str]) -> Optional[str]:
    url = f"https://www.chessgames.com/perl/chessgame?gid={game_id}"
    xpath = """//*[@id="olga-data"]/@pgn"""

    try:
        r = requests.get(url)
        tree = html.fromstring(r.content)
        pgn = tree.xpath(xpath)[0]
    # TODO: Add specific exceptions and handle each of them
    except:
        pgn = None

    return pgn


def pgn_to_game(pgn: str) -> Optional[chess.pgn.Game]:
    pgn_string_io = io.StringIO(pgn)
    game = chess.pgn.read_game(pgn_string_io)
    return game


def get_game_from_chessgame_page(game_id: Union[int, str]) -> Optional[chess.pgn.Game]:
    pgn = get_pgn_from_chessgame_page(game_id)
    game = pgn_to_game(pgn) if pgn else None
    return game


if __name__ == "__main__":
    g = get_game_from_chessgame_page(1706265)
