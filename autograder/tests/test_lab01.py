"""
test_lab01.py — Point-based auto-grader tests (20 points total)

Scoring:
- reverseList: 4 tests × 2 pts = 8 pts
- doubleIt:    5 tests (2+2+2+3+3) = 12 pts
TOTAL = 20 pts

These tests load the student's file from:
    submissions/<STUDENT_ID>/lab01.py
via the environment variable STUDENT_DIR (set by grade.py).
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from typing import Optional

import pytest


def load_student_lab01():
    student_dir = os.environ.get("STUDENT_DIR")
    assert student_dir, "STUDENT_DIR env var not set. grade.py should set it."

    lab_path = Path(student_dir) / "lab01.py"
    assert lab_path.exists(), f"Missing file: {lab_path}"

    spec = importlib.util.spec_from_file_location("student_lab01", lab_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _assert_sll_values(SinglyLinkedList, head: Optional[object], expected):
    assert SinglyLinkedList(head).to_list() == expected


# -------------------------
# reverseList (8 points)
# -------------------------

@pytest.mark.points(2)
def test_reverse_empty():
    m = load_student_lab01()
    assert m.reverseList(None) is None


@pytest.mark.points(2)
def test_reverse_single():
    m = load_student_lab01()
    ll = m.SinglyLinkedList.from_list([7])
    out = m.reverseList(ll.head)
    _assert_sll_values(m.SinglyLinkedList, out, [7])


@pytest.mark.points(2)
def test_reverse_multiple():
    m = load_student_lab01()
    ll = m.SinglyLinkedList.from_list([1, 2, 3, 4])
    out = m.reverseList(ll.head)
    _assert_sll_values(m.SinglyLinkedList, out, [4, 3, 2, 1])


@pytest.mark.points(2)
def test_reverse_two():
    m = load_student_lab01()
    ll = m.SinglyLinkedList.from_list([10, 20])
    out = m.reverseList(ll.head)
    _assert_sll_values(m.SinglyLinkedList, out, [20, 10])


# -------------------------
# doubleIt (12 points)
# -------------------------

@pytest.mark.points(2)
def test_double_zero():
    m = load_student_lab01()
    ll = m.SinglyLinkedList.from_list([0])
    out = m.doubleIt(ll.head)
    _assert_sll_values(m.SinglyLinkedList, out, [0])


@pytest.mark.points(2)
def test_double_no_carry():
    m = load_student_lab01()
    ll = m.SinglyLinkedList.from_list([1, 2, 3])  # 123 -> 246
    out = m.doubleIt(ll.head)
    _assert_sll_values(m.SinglyLinkedList, out, [2, 4, 6])


@pytest.mark.points(2)
def test_double_with_carry_middle():
    m = load_student_lab01()
    ll = m.SinglyLinkedList.from_list([4, 9, 5])  # 495 -> 990
    out = m.doubleIt(ll.head)
    _assert_sll_values(m.SinglyLinkedList, out, [9, 9, 0])


@pytest.mark.points(3)
def test_double_new_head_carry():
    m = load_student_lab01()
    ll = m.SinglyLinkedList.from_list([9, 9, 9])  # 999 -> 1998
    out = m.doubleIt(ll.head)
    _assert_sll_values(m.SinglyLinkedList, out, [1, 9, 9, 8])


@pytest.mark.points(3)
def test_double_longer_mix():
    m = load_student_lab01()
    ll = m.SinglyLinkedList.from_list([3, 6, 7, 9])  # 3679 -> 7358
    out = m.doubleIt(ll.head)
    _assert_sll_values(m.SinglyLinkedList, out, [7, 3, 5, 8])
