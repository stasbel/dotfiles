"""Setup for pip package"""

from distutils import cmd as distutils_cmd
from distutils import log as distutils_log
import itertools
import os
from os import path
import subprocess
import sys

import setuptools

__line_width__ = 79
__version__ = '0.0.1'

# `test`: pytest + pytest plugins (sugar|xdist|cov|doctest)
# Functional testing.

# `lint`: vulture + flake8 (+plugins) + mypy
# Static code analyzers to prevent potential problems. Aims at affect AST.
# Plugins: pep8-naming + flake8-bugbear + flake8-docstrings + darglint \
# + flake8-pytest-style + flake8-eradicate + flake8-comprehensions \
# + flake8-logging-format + lake8-builtins
# (Optional): Other plugins.
# Depends on the project.
# (Optional): pylint
# Initial set of rules is too strict.
# (Optional): prospector
# Is not yet compatible with pure flake8.
# (Optional): xenon + cohesion
# Code quality metrics with possible thresholds.

# `format` (+fix): isort + black
# Popular wide-use code style formatters with autofixing. Doesn't affect AST.

# (Optional) `security`: safety + bandit + dodgy + dlint
# Seems to be more suitable for big projects where security checks make sense.

# (Optional) `docs`: doc8 + flake8-rst-docstrings
# Seems to be more suitable for big projects with urge for documentation.

_here = path.abspath(path.dirname(__file__))
with open(path.join(_here, 'README.md'), encoding='utf-8') as f:
    _long_description_lines = f.readlines()


class FormatCommand(distutils_cmd.Command):
    __AUTOPEP8_BASE = (
        'autopep8',
        '--aggressive',
        '--aggressive',
        '--aggressive',
        f'--max-line-length={__line_width__}',
    )
    __AUTOFLAKE_BASE = (
        'autoflake',
        '--expand-star-imports',
        '--remove-all-unused-imports',
        '--remove-unused-variables',
    )
    __ISORT_BASE = (
        'isort',
        '--force-single-line-imports',  # Force one import per line.
        # These two lines makes isort compatible with black.
        '--multi-line=3',
        '--trailing-comma',
        '--force-grid-wrap=0',
        '--use-parentheses',
        f'--line-width={__line_width__}',
    )
    __BLACK_BASE = (
        'black',
        '--skip-string-normalization',
        f'--line-length={__line_width__}',
    )
    description = 'Checks overall project code style.'
    user_options = [
        ('scope=', None, 'Folder of file to operate within.'),
        ('fix', None, 'True if tries to fix issues in-place.'),
    ]

    def __init__(self, dist):
        super().__init__(dist)

        # Nasty trick to look to formatters programs in python bin folder.
        os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable)

    def __call(self, command):
        command = list(command)

        self.announce(
            msg=f"Running command: '{str(' '.join(command))}'.",
            level=distutils_log.INFO,
        )

        return_code = subprocess.call(command)

        return return_code

    def _autopep8(self, scope, fix):
        command = list(self.__AUTOPEP8_BASE)

        if not fix:
            return 0

        command.append('--in-place')
        command.extend(['--recursive', scope])
        return self.__call(command)

    def _autoflake(self, scope, fix):
        command = list(self.__AUTOFLAKE_BASE)

        if fix:
            command.append('--in-place')
        else:
            command.append('--check')

        command.extend(['--recursive', scope])
        return self.__call(command)

    def _isort(self, scope, fix):
        command = list(self.__ISORT_BASE)
        if not fix:
            command.extend(['--check', '--diff'])

        command.extend(['-rc', scope])
        return self.__call(command)

    def _black(self, scope, fix):
        command = list(self.__BLACK_BASE)
        if not fix:
            command.extend(['--check', '--diff'])

        command.append(scope)
        return self.__call(command)

    def _pass(self):
        self.announce(msg='\033[32mPASS\x1b[0m', level=distutils_log.INFO)

    def _fail(self):
        self.announce(msg='\033[31mFAIL\x1b[0m', level=distutils_log.INFO)

    # noinspection PyAttributeOutsideInit
    def initialize_options(self):
        self.scope = '.'
        self.fix = ''

    def run(self):
        checkers = [self._isort]
        return_codes = []
        for checker in checkers:
            return_codes.append(checker(scope=self.scope, fix=self.fix))

        if sum(return_codes, 0) == 0:
            self._pass()
        else:
            self._fail()
            exit(max(return_codes))

    def finalize_options(self):
        pass


# TODO: Make versions range?
extras_require = dict(
    test=[
        'pytest==5.3.5',
        'pytest-sugar==0.9.2',
        'pytest-xdist==1.31.0',
        'pytest-cov==2.8.1',
        'pytest-doctest-ellipsis-markers==0.1.0',
    ],
    lint=[
        'vulture==0.24',
        'flake8==3.7.9',
        'mypy==0.761',
        'pydocstyle==5.0.2',
    ],
    format=['isort==4.3.21', 'black==19.10b0'],
)
extras_require['all'] = list(itertools.chain(extras_require.values()))

setuptools.setup(
    name='gadget',
    version=__version__,
    description=_long_description_lines[9],
    long_description='\n'.join(_long_description_lines),
    long_description_content_type='text/markdown',
    url='https://github.com/stasbel/gadget',
    author='Stanislav Beliaev',
    author_email='stasbelyaev96@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='yaml json config tool dict',
    packages=setuptools.find_packages(exclude=['tests', 'examples']),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=['PyYAML', 'frozendict'],
    extras_require=extras_require,
    cmdclass={'format': FormatCommand},
)

