import shutil
from art import *

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def colorize_art(art, color):
    colored_art = ""
    for line in art.split('\n'):
        colored_art += color + line + RESET + "\n"
    return colored_art

def combine_ascii_art(art1, art2):
    lines1 = art1.split('\n')
    lines2 = art2.split('\n')

    max_lines = max(len(lines1), len(lines2))
    lines1 += [''] * (max_lines - len(lines1))
    lines2 += [''] * (max_lines - len(lines2))

    combined_art = '\n'.join([line1 + '  ' + line2 for line1, line2 in zip(lines1, lines2)])
    return combined_art

def center_align_pattern(pattern, width):
    lines = pattern.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def center_align_art(ascii_art):
    terminal_width, _ = shutil.get_terminal_size()
    lines = ascii_art.split('\n')
    centered_lines = [line.center(terminal_width) for line in lines]
    return '\n'.join(centered_lines)

def logo_text(str1, str2, color1=GREEN, color2=YELLOW):
    ascii_art1 = text2art(str1)
    ascii_art2 = text2art(str2)

    if color1.upper()=="RED" and color2.upper()=="RED":
        color1=RED
        color2=RED
        colored_art1 = colorize_art(ascii_art1, color1)
        colored_art2 = colorize_art(ascii_art2, color2)
        combined_art = combine_ascii_art(colored_art1, colored_art2)
        print(center_align_art(combined_art))
        
    else:
    
        colored_art1 = colorize_art(ascii_art1, color1)
        colored_art2 = colorize_art(ascii_art2, color2)

        combined_art = combine_ascii_art(colored_art1, colored_art2)
        columns, _ = shutil.get_terminal_size()
        centered_ascii_art = center_align_pattern(combined_art, columns)

        print(centered_ascii_art)
