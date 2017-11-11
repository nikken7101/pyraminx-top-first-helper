#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, default_app
from bottle import request, template
from findkeyhole import findkeyhole
from findoka import findoka
from findbell import findbell
from pyraminx import all_turns


@route('/')
def demo():
    scramble = request.query.scramble
    scramble_seq = [x for x in scramble.split(" ") if x.upper() in all_turns]
    oka_solutions = findoka(scramble_seq)
    oka_solutions_texts = [(" ".join(turns) if len(turns) != 0 else "Solved!") + " ({} face)".format(face)
                           for turns, face in oka_solutions]
    kh_solutions = findkeyhole(scramble_seq)
    kh_solutions_texts = [(" ".join(turns) if len(turns) != 0 else "Solved!") + " ({} face)".format(face)
                          for turns, face in kh_solutions]
    bell_solutions = findbell(scramble_seq)
    bell_solutions_texts = [(" ".join(turns) if len(turns) != 0 else "Solved!") + " ({} face)".format(face)
                          for turns, face in bell_solutions]
    return template("demo",
                    scramble=" ".join(scramble_seq),
                    oka_solutions=oka_solutions_texts,
                    kh_solutions=kh_solutions_texts,
                    bell_solutions=bell_solutions_texts)

if __name__ == '__main__':
    run(host='0.0.0.0', port=51080, debug=True)
else:
    application = default_app()
