#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, default_app
from bottle import request, template
from findall import findall
from pyraminx import all_turns


@route('/')
def demo():
    scramble = request.query.scramble
    scramble_seq = [x for x in scramble.split(" ") if x.upper() in all_turns]
    print("Scramble: " + " ".join(scramble_seq))
    if not scramble_seq:
        return template("demo",
                        scramble="",
                        oka_solutions=[],
                        kh_solutions=[],
                        bell_solutions=[],
                        oneflip_solutions=[],
                        intuitive_solutions=[])
    solutions = findall(scramble_seq)
    oka_solutions_texts = [(" ".join(turns) if len(turns) != 0 else "Solved!") + " ({} top)".format(face)
                           for turns, face, method in solutions if method == "oka"]
    kh_solutions_texts = [(" ".join(turns) if len(turns) != 0 else "Solved!") + " ({} top)".format(face)
                          for turns, face, method in solutions if method == "keyhole"]
    bell_solutions_texts = [(" ".join(turns) if len(turns) != 0 else "Solved!") + " ({} top)".format(face)
                            for turns, face, method in solutions if method == "bell"]
    oneflip_solutions_texts = [(" ".join(turns) if len(turns) != 0 else "Solved!") + " ({} top)".format(face)
                               for turns, face, method in solutions if method == "1flip"]
    intuitive_solutions_texts = [(" ".join(turns) if len(turns) != 0 else "Solved!") + " ({} top)".format(face)
                                 for turns, face, method in solutions if method == "intuitive"]
    return template("demo",
                    scramble=" ".join(scramble_seq),
                    oka_solutions=oka_solutions_texts,
                    kh_solutions=kh_solutions_texts,
                    bell_solutions=bell_solutions_texts,
                    oneflip_solutions=oneflip_solutions_texts,
                    intuitive_solutions=intuitive_solutions_texts)


if __name__ == '__main__':
    run(host='0.0.0.0', port=51080, debug=True)
else:
    application = default_app()
