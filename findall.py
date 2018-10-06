#!/usr/bin/env python
# -*- coding: utf-8 -*-
import queue
import sys

from pyraminx import Pyraminx, all_turns, faces

opposite_face = {
    "U": "D",
    "R": "L",
    "L": "R",
    "B": "F"
}


def findall(scramble):
    def get_solved_info(turns):
        pyra = Pyraminx(scramble).move(turns)
        ret = []
        for face in faces:
            is_oka_solved = pyra.is_oka_solved(face)
            is_keyhole_solved = pyra.is_keyhole_solved(face)
            is_bell_solved = pyra.is_bell_solved(face)
            is_1flip_solved = pyra.is_1flip_solved(face)
            is_intuitive_solved = pyra.is_intuitive_solved(face)
            is_v_solved = pyra.is_v_solved(face)
            if (is_oka_solved or is_keyhole_solved or is_bell_solved or
                    is_1flip_solved or is_intuitive_solved or is_v_solved):
                auf_ignored_turns = turns[:-1] if len(turns) > 1 and turns[-1][0] == face else turns
                if is_oka_solved:
                    ret.append((auf_ignored_turns, face, "oka"))
                if is_keyhole_solved:
                    ret.append((auf_ignored_turns, face, "keyhole"))
                if is_bell_solved:
                    ret.append((auf_ignored_turns, face, "bell"))
                if is_1flip_solved:
                    ret.append((auf_ignored_turns, face, "1flip"))
                if is_intuitive_solved:
                    ret.append((auf_ignored_turns, face, "intuitive"))
                if is_v_solved:
                    ret.append((auf_ignored_turns, opposite_face[face], "v-first"))
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
    print("\n".join([" ".join(turns) + " ({}, {} method)".format(face, method) for turns, face, method in answer]))
