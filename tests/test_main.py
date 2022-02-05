# -*- coding: utf-8 -*-

"""
Tests fo main.py.

This script will run tests for main.py
"""

import asyncio
import hashlib
import io

import pytest

from src.challenge.main import create_tasks
from src.challenge.main import print_hash
from src.challenge.main import print_message

MSG = 'Hello world'


@pytest.mark.asyncio
async def test_print_message(capsys):
    """print_message() should print the passed message."""
    await print_message(MSG)
    captured = capsys.readouterr()

    assert captured.out == 'Hello world\n'


@pytest.mark.asyncio
async def test_create_tasks_list():
    """tasks from create_tasks() should contain Task instances."""
    tasks_lst, done_set, pending_set = await create_tasks([MSG])

    assert isinstance(tasks_lst[0], asyncio.Task)


@pytest.mark.asyncio
async def test_create_tasks_pending():
    """create_tasks() should complete all tasks."""
    tasks_lst, done_set, pending_set = await create_tasks([MSG])

    assert not pending_set


def test_print_hash(monkeypatch, capsys):
    """print_hash() should print sha256 hash fom the given string."""
    sha_test = hashlib.new('sha256')
    sha_test.update(MSG.encode('utf-8'))

    monkeypatch.setattr('sys.stdin', io.StringIO(MSG))
    print_hash()
    captured = capsys.readouterr()

    assert captured.out == sha_test.hexdigest()
