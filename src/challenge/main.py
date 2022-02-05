# -*- coding: utf-8 -*-

"""
Test challenge.

This script will run asynchronous tasks
that displaying after a random amount of time (up to 5 seconds)
the name, the name of this job, the expected salary level after one year.

After performing all asynchronous tasks, the script should read stdin
and output the sha256 hash from the read data.
"""

import asyncio
import hashlib
import random
import sys
from typing import List, Set, Tuple

NAME = 'Evgeniy'
POSITION = 'Стажёр-программист Python / Python Developer Trainee'
SALARY = 275000
MIN_LAG = 0
MAX_LAG = 5

messages_list = [NAME, POSITION, SALARY]


async def print_message(message: str) -> None:
    """Print the message after a random delay.

    Args:
        message: Any string object.
    """
    rand_gen = random.SystemRandom()
    await asyncio.sleep(round(rand_gen.uniform(MIN_LAG, MAX_LAG), 3))
    sys.stdout.write('{0}\n'.format(message))


async def create_tasks(msg_list: list) -> Tuple[List[asyncio.Task], Set[asyncio.Task], Set[asyncio.Task]]:
    """Create task list and pend it to run concurrently.

    Args:
        msg_list: List of messages.

    Returns:
        tasks, done, pending: Tuple of list of Task objects,
        set of done Task objects and set of pending Task objects.
    """
    tasks = [asyncio.create_task(print_message(msg)) for msg in msg_list]
    done, pending = await asyncio.wait(tasks)
    return tasks, done, pending


def print_hash() -> str:
    """Read std input and print sha256 hash fom the given string."""
    input_string = sys.stdin.readline().strip()

    sha = hashlib.new('sha256')
    sha.update(input_string.encode('utf-8'))

    sys.stdout.write(sha.hexdigest())


if __name__ == '__main__':
    asyncio.run(create_tasks(messages_list))
    print_hash()
