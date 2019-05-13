import re
import sys
import fileinput

from sys import argv
from functools import partial
from contextlib import contextmanager


class InvalidArgumentLength(Exception):
    pass


print_ = partial(print, f'{__file__}:')


@contextmanager
def cli_exception_handler():
    try:
        yield

    except Exception as ex:
        print_(repr(ex))
        exit(1)

    else:
        exit(0)


if ('__main__' == __name__):
    with cli_exception_handler():
        if (1 == len(argv)):
            raise InvalidArgumentLength('Please pass the processing target as the first argument to this script.')

        pattern = re.compile(r'\.\. include:: (?P<filename>.*)\n')
        file_input_ = partial(fileinput.input, inplace=True)
        # stdout_ = sys.stdout
        with file_input_() as handle:
            for line in handle:
                match = pattern.fullmatch(line)
                # print(match, file=stdout_)
                if match:
                    with open(match.group('filename'), mode='rt') as include_handle:
                        print(include_handle.read())
                else:
                    print(line, end='')