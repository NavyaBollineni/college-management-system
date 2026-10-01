"""
CLI Formatting Utilities & Interactive Menus for Terminal Interface
"""

import sys

def print_banner(title, subtitle=None):
    width = 75
    print("\n" + "=" * width)
    print(f"{title.center(width)}")
    if subtitle:
        print(f"{subtitle.center(width)}")
    print("=" * width + "\n")

def print_section(title):
    width = 75
    print("\n" + "-" * width)
    print(f" ▶  {title.upper()}")
    print("-" * width)

def print_table(headers, rows):
    if not rows:
        print("  [No data records found]")
        return
    
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    # Header format string
    header_fmt = " | ".join(f"{{:<{col_widths[i]}}}" for i in range(len(headers)))
    divider = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

    print(" " + header_fmt.format(*headers))
    print(" " + divider)
    for row in rows:
        print(" " + header_fmt.format(*[str(v) for v in row]))
    print()

def get_menu_choice(options, prompt="Enter your choice"):
    print("\n" + "─" * 40)
    for key, label in options.items():
        print(f"  [{key}] {label}")
    print("─" * 40)

    while True:
        choice = input(f"{prompt} => ").strip()
        if choice in options:
            return choice
        print("  ⚠ Invalid choice! Please select a valid option from the menu.")

def prompt_input(prompt_msg, default=None, required=True):
    while True:
        if default:
            val = input(f"{prompt_msg} [{default}]: ").strip()
            if not val:
                return default
        else:
            val = input(f"{prompt_msg}: ").strip()
        
        if val or not required:
            return val
        print("  ⚠ Field cannot be empty. Please enter a valid value.")

def prompt_number(prompt_msg, num_type=int, min_val=None, max_val=None):
    while True:
        val_str = input(f"{prompt_msg}: ").strip()
        try:
            val = num_type(val_str)
            if min_val is not None and val < min_val:
                print(f"  ⚠ Value must be at least {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"  ⚠ Value must be at most {max_val}.")
                continue
            return val
        except ValueError:
            print(f"  ⚠ Please enter a valid numerical value.")
