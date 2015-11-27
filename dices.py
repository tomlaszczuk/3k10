from random import randint
import click

def throw(numbers, dice):
    results = []
    for i in range(numbers):
        results.append(str(randint(1, dice)))
    return results


def print_results(results):
    print("\n".join(results))


@click.command(help='Usage example: throw 3d10')
@click.argument('roll', default='d6')
def thr(roll):
    results = ["Bad expression (it should be something like 3d10) Dice must be > 0"]
    if roll.count('d') != 1:
        print_results(results)
        return
    try:
        dice = int(roll.split('d')[1])
        if roll.split('d')[0] == '':
            results = throw(1, dice)
        else:
            results = throw(int(roll.split('d')[0]), dice)
    except ValueError:
        pass
    finally:
        print_results(results)
