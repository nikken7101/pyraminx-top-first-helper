#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import itertools

all_turns = ["U", "U'", "L", "L'", "B", "B'", "R", "R'"]
faces = ["U", "L", "B", "R"]


class State:
    # See https://github.com/cubing/ksolve/blob/master/puzzles/Pyraminx.def for state definitions
    def __init__(self,
                 centers=np.array([0, 0, 0, 0], dtype='int8'),
                 ep=np.array([0, 1, 2, 3, 4, 5], dtype='int8'),
                 eo=np.array([0, 0, 0, 0, 0, 0], dtype='int8')):
        self.centers = centers
        self.ep = ep
        self.eo = eo

    def apply_single(self, move):
        centers = (self.centers + move.centers) % 3
        ep = self.ep[move.ep]
        eo = (self.eo[move.ep] + move.eo) % 2
        return State(centers, ep, eo)

    def apply(self, moves):
        ret = self
        for m in moves:
            ret = ret.apply_single(m)
        return ret

    def __repr__(self):
        return "centers: {}, ep: {}, eo: {}".format(self.centers, self.ep, self.eo)


class Pyraminx:
    _edges = {'U': [0, 1, 2],
              'L': [0, 3, 5],
              'R': [1, 3, 4],
              'B': [2, 4, 5]}

    _moves = {'U': State(np.array([1, 0, 0, 0], dtype='int8'),
                         np.array([1, 2, 0, 3, 4, 5], dtype='int8'),
                         np.array([0, 0, 0, 0, 0, 0], dtype='int8')),
              'L': State(np.array([0, 1, 0, 0], dtype='int8'),
                         np.array([5, 1, 2, 0, 4, 3], dtype='int8'),
                         np.array([0, 0, 0, 1, 0, 1], dtype='int8')),
              'R': State(np.array([0, 0, 1, 0], dtype='int8'),
                         np.array([0, 3, 2, 4, 1, 5], dtype='int8'),
                         np.array([0, 0, 0, 1, 1, 0], dtype='int8')),
              'B': State(np.array([0, 0, 0, 1], dtype='int8'),
                         np.array([0, 1, 4, 3, 5, 2], dtype='int8'),
                         np.array([0, 0, 0, 0, 1, 1], dtype='int8'))}

    for (face, move) in _moves.copy().items():
        inv_move = move.apply_single(move)
        _moves["{}'".format(face)] = inv_move

    def __init__(self, scramble):
        self.state = State()
        self.move(scramble)

    def __repr__(self):
        return self.state.__repr__()

    def move(self, moves):
        self.state = self.state.apply([self._moves[m] for m in moves if m in self._moves])
        return self

    def is_solved(self):
        solved = State()
        return ((self.state.centers == solved.centers).all() and
                (self.state.ep == solved.ep).all() and
                (self.state.eo == solved.eo).all())

    def is_center_solved(self):
        return (self.state.centers == 0).all()

    def is_oka_solved(self, face):
        if not self.is_center_solved():
            return False
        should_be_flipped = [(0, 3), (1, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
        edge_permutations = itertools.permutations(self._edges[face])
        for (e0, e1, e2) in edge_permutations:
            e0_solved = self.state.ep[e0] == e0 and self.state.eo[e0] == 0
            desired_flip = 1 if (e1, e2) in should_be_flipped or (e2, e2) in should_be_flipped else 0
            e1_solved = self.state.ep[e1] == e2 and self.state.eo[e1] == desired_flip
            if e0_solved and e1_solved:
                return True
        return False

    def is_keyhole_solved(self, face):
        if not self.is_center_solved():
            return False
        edge_pairs = itertools.permutations(self._edges[face], 2)
        for (e0, e1) in edge_pairs:
            e0_solved = self.state.ep[e0] == e0 and self.state.eo[e0] == 0
            e1_solved = self.state.ep[e1] == e1 and self.state.eo[e1] == 0
            if e0_solved and e1_solved:
                return True
        return False
