def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    stats = [strength, intelligence, charisma]
    if not all(isinstance(s, int) for s in stats):
        return "All stats should be integers"
    if not all(s >= 1 for s in stats):
        return "All stats should be no less than 1"
    if not all(s <= 4 for s in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"

    full_dot = "●"
    empty_dot = "○"

    def make_line(abbr, value):
        return f"{abbr} {full_dot * value}{empty_dot * (10 - value)}"

    return "\n".join([
        name,
        make_line("STR", strength),
        make_line("INT", intelligence),
        make_line("CHA", charisma)
    ])