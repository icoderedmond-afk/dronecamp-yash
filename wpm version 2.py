import curses
import time
import random

# Sample target sentences
SENTENCES = [
    "The quick brown fox jumps over the lazy dog",
    "Which is better? Messi or Ronaldo? Minecraft or Roblox.",
    "Why did monkeys turn into humans? I don\'t know.",
    "Do you like bloxd.io? I do..... a bit."
]

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test 2!\n")
    stdscr.addstr("Press any key to begin...")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    # Overlay user's typed characters with green/red coloring
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def load_text():
    return random.choice(SENTENCES)

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)  # Don't block terminal waiting for input

    while True:
        # Calculate time elapsed and dynamic WPM
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / 5) / (time_elapsed / 60))

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Check if user completed the sentence
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # Handle user input
        try:
            key = stdscr.getkey()
        except:
            continue

        # Ordinal 27 is the Escape key
        if ord(key) == 27:
            break

        # Handle Backspace
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    # Define text colors: Pair 1 = Green, Pair 2 = Red, Pair 3 = White
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press ESC to quit or any key to try again.")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

# curses.wrapper handles terminal initialization and cleanup automatically
curses.wrapper(main)
