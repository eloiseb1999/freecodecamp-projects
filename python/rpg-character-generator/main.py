def create_character(name, strength, intelligence, charisma):
    # Validations: Name
    if not isinstance(name, str):
        return 'The character name should be a string'
    if len(name) == 0:
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    # Validations: Types
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'

    # Validations: Ranges
    if any(s < 1 for s in (strength, intelligence, charisma)):
        return 'All stats should be no less than 1'
    if any(s > 4 for s in (strength, intelligence, charisma)):
        return 'All stats should be no more than 4'

    # Validations: Points Sum
    if sum([strength, intelligence, charisma]) != 7:
        return 'The character should start with 7 points'

    # Character Sheet Generation
    def format_line(label, value):
        full_dots = '●' * value
        empty_dots = '○' * (10 - value)
        return f"{label} {full_dots}{empty_dots}"

    character_sheet = (
        f"{name}\n"
        f"{format_line('STR', strength)}\n"
        f"{format_line('INT', intelligence)}\n"
        f"{format_line('CHA', charisma)}"
    )

    return character_sheet
