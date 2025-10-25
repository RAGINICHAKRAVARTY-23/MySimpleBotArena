import sys
import time
import io
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

lyrics = [
    "Mur mon dusoukut",
    "Oxohay akolxore",
    "Mur sporxho mur akaxh",
    "Assei ekethore",
    "Mur mon mur bukut",
    "Likhe ekei akhore",
    "Mor mon mor sobie",
    "Anke ekei xanthore",
    "Mor mon dusoukut",
    "Oxohay akolxore",
    "Mor sporxho mor akaxh",
    "Ankei ekethore"
]

char_delays = [0.13,0.13,0.13,0.13,0.13,0.13,0.15,0.15,0.13,0.13,0.13,0.13]
line_delays = [1.8,1.8,1.8,1.8,1.8,1.8,2.0,2.0,1.8,1.8,1.8,1.8]

gradient_colors = [
    (255,150,150),
    (255,180,120),
    (255,220,120),
    (180,255,150),
    (120,255,220),
    (120,180,255),
    (180,120,255),
    (255,120,220),
    (255,150,150),
    (255,180,120),
    (255,220,120),
    (180,255,150)
]

def rgb_escape(r,g,b):
    return f"\033[38;2;{r};{g};{b}m"

def type_line(line, char_delay, line_delay, color):
    sys.stdout.write(rgb_escape(*color))
    for ch in line:
        if random.random() < 0.1:
            sys.stdout.write(f"*")
            sys.stdout.flush()
            time.sleep(char_delay / 2)
            sys.stdout.write("\b")
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write("\033[0m\n")
    time.sleep(line_delay)

def print_lyrics():
    for i, line in enumerate(lyrics):
        type_line(line, char_delays[i], line_delays[i], gradient_colors[i])
    sys.stdout.write(f"\n\033[1;38;2;255;100;255mZubeen Da — Tribute\033[0m\n\n")

if __name__ == "__main__":
    print_lyrics()
