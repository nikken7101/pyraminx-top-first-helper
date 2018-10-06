#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyraminx import Pyraminx, all_turns, faces
import queue
import sys


def find1flip(scramble):
    scrambled = Pyraminx(scramble)
    if scrambled.is_solved() or any([scrambled.is_1flip_solved(f) for f in faces]):
        return []
    q = queue.Queue()
    for m in all_turns:
        q.put([m])
    ret = []
    solution_length = 999
    while True:
        turns = q.get()
        if len(turns) > solution_length:
            break
        pyra = Pyraminx(scramble).move(turns)
        for face in faces:
            if pyra.is_1flip_solved(face):
                auf_ignored_turns = turns[:-1] if turns[-1][0] == face else turns
                ret.append((auf_ignored_turns, face))
                solution_length = len(turns)
        for m in all_turns:
            if turns[-1][0] != m[0]:
                q.put(turns + [m])
    return sorted(ret, key=lambda x: len(x[0]))


if __name__ == '__main__':
    answer = find1flip([x for x in sys.argv[1].split(" ") if x != ""])
    print("\n".join([" ".join(turns) + " ({} top)".format(face) for turns, face in answer]))
