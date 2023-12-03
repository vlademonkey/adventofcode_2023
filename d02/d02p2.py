
import re

sum = 0
with open("input.txt") as fin:
    for line in fin:
        if line_match := re.match(r"^Game\s+(\d+):\s+(.+)", line):
            game_num = int(line_match.group(1))
            game_maxes = {"red":0, "green":0, "blue":0}
            games_list = re.split(";", line_match.group(2))
            for game in games_list:
                game_dict = {"red":0, "green":0, "blue":0}
                for game_match in re.finditer(r"(\d+)\s+(red|green|blue)", game):
                    game_dict[game_match.group(2)] += int(game_match.group(1))
                print(f"{game_dict=}")
                game_maxes["red"]   = max(game_maxes["red"], game_dict["red"])
                game_maxes["green"] = max(game_maxes["green"], game_dict["green"])
                game_maxes["blue"]  = max(game_maxes["blue"], game_dict["blue"])
            print(f"{game_maxes=}")
            sum += game_maxes["red"] * game_maxes["green"] * game_maxes["blue"]

print(sum)
