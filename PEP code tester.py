from pylint.lint import Run
from pylint.reporters.text import TextReporter

with open("report.log", "w") as f:
    reporter = TextReporter(f)
    Run(["test.py"], reporter=reporter, do_exit=False)