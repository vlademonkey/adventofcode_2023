
import re

sum = 0
with open("input.txt") as fin:
    for line in fin:
        if line_match := re.match(r"^Game\s+(\d+):\s+(.+)", line):
            game_num = int(line_match.group(1))
            game_valid = True
            games_list = re.split(";", line_match.group(2))
            for game in games_list:
                game_dict = {"red":0, "green":0, "blue":0}
                for game_match in re.finditer(r"(\d+)\s+(red|green|blue)", game):
                    game_dict[game_match.group(2)] += int(game_match.group(1))
                print(f"{game_dict=}")
                if game_dict["red"] > 12 or game_dict["green"] > 13 or game_dict["blue"] > 14:
                    game_valid = False
            if game_valid:
                sum += game_num

print(sum)
