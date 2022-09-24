"""
A recursive solver for the Tower of Hanoi.

For n disks, it takes a minimum of 2n – 1 moves to solve.

For manual testing:
python hanoi_tower.py
"""

import sys


TOTAL_DISKS = 6
TOWERS = {
    'A': list(reversed(range(1, TOTAL_DISKS+1))),
    'B': [],
    'C': [],
}


def print_disk(disk_num: int) -> None:
    """Print disk."""

    empty_space = ' ' * (TOTAL_DISKS - disk_num)

    if disk_num == 0:
        # Draw the pole.
        print(f'{empty_space}||{empty_space}', end='')
    else:
        # Draw disk.
        disk_space = '@' * disk_num
        disk_label = str(disk_num).rjust(2, '_')
        print(f'{empty_space}{disk_space}{disk_label}{disk_space}{empty_space}', end='')


def print_towers() -> None:
    """Print all hanoi towers."""

    for lvl in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if lvl >= len(tower):
                print_disk(0)
            else:
                print_disk(tower[lvl])

        print()

    # Print tower labels (A, B, C).
    empty_space = ' ' * (TOTAL_DISKS)
    print(
        f'{empty_space} A{empty_space}{empty_space} B{empty_space}{empty_space} C')


def move_one_disk(start_tower: str, end_tower: str) -> None:
    """Move top disk from start_tower to end_tower."""

    disk = TOWERS[start_tower].pop()
    TOWERS[end_tower].append(disk)


def solve(number_of_disks: int, start_tower: str, end_tower: str, tmp_tower: str) -> None:
    if number_of_disks == 1:
        move_one_disk(start_tower, end_tower)
        print_towers()
        return
    else:
        solve(number_of_disks - 1, start_tower, tmp_tower, end_tower)
        move_one_disk(start_tower, end_tower)
        print_towers()

        solve(number_of_disks - 1, tmp_tower, end_tower, start_tower)
        return


if __name__ == '__main__':
    from doctest import testmod
    testmod()

    option = input('Enter i to enable interactive mode: ').strip()

    if option != 'i':
        print_towers()
        solve(TOTAL_DISKS, 'A', 'B', 'C')
    else:
        while True:
            print_towers()
            print(
                'Enter letter of start tower and the end tower. (A, B, C) Or q to quit.')
            move = input().upper()
            if move == 'q':
                sys.exit()
            elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
                move_one_disk(move[0], move[1])
