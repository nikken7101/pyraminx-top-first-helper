#!/usr/bin/env python
# -*- coding: utf-8 -*-
import queue
import sys

from pyraminx import Pyraminx, all_turns, faces


def findall(scramble):
    def get_solved_info(turns):
        pyra = Pyraminx(scramble).move(turns)
        ret = []
        for face in faces:
            is_oka_solved = pyra.is_oka_solved(face)
            is_keyhole_solved = pyra.is_keyhole_solved(face)
            is_bell_solved = pyra.is_bell_solved(face)
            if is_oka_solved or is_keyhole_solved or is_bell_solved:
                auf_ignored_turns = turns[:-1] if len(turns) > 1 and turns[-1][0] == face else turns
                if is_oka_solved:
                    ret.append((auf_ignored_turns, face, "oka"))
                if is_keyhole_solved:
                    ret.append((auf_ignored_turns, face, "keyhole"))
                if is_bell_solved:
                    ret.append((auf_ignored_turns, face, "bell"))
        return ret

    solved_info = get_solved_info([])
    if solved_info:
        return solved_info

    q = queue.Queue()
    for m in all_turns:
        q.put([m])

    ret = []
    default_solution_length = 4
    while not q.empty():
        turns = q.get()
        solved_info = get_solved_info(turns)
        if solved_info:
            ret += solved_info
        if len(turns) < default_solution_length:
            for m in all_turns:
                if turns[-1][0] != m[0]:
                    q.put(turns + [m])
    return sorted(ret, key=lambda x: len(x[0]))


if __name__ == '__main__':
    answer = findall([x for x in sys.argv[1].split(" ") if x != ""])
    print("\n".join([" ".join(turns) + " ({} face, {} method)".format(face, method) for turns, face, method in answer]))