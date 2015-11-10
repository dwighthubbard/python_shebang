#!/usr/bin/env python
"""
Create a simple python script with a shebang line that points to python_shebang
and execute it via os.system.  If things work properly we will see the output
of the script.
"""

#Copyright (c) 2014-2015 Yahoo! Inc. All rights reserved.
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. See accompanying LICENSE file.
import unittest
import tempfile
import os


test_scripts = {
    'simple': """#!/usr/bin/env {}
from __future__ import print_function
import sys
print('Python ok')
print(sys.version)
""",
    'virtualenv': """#!/usr/bin/env {}
from __future__ import print_function
import os
if 'VIRTUAL_ENV' in os.environ.keys():
    print('Virtualenv ok')
"""
}


def which(filename):
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, filename)):
                return os.path.join(path, filename)


class UnitTest(unittest.TestCase):
    script_file = None

    def setUp(self):
        # Create a tempfile with a script that uses our shebang handler
        self.python_shebang_location = which('python_shebang')

    def test_run_from_shell_simple(self):
        with tempfile.NamedTemporaryFile(mode='w+b') as script_file:
            os.fchmod(script_file.fileno(), 0o700)
            script_file.write(test_scripts['simple'].format(self.python_shebang_location).encode('utf-8'))
            script_file.flush()
            with os.popen(script_file.name, 'r') as command_handle:
                result = command_handle.read()
            self.assertIn('Python ok', result)

    def test_run_from_shell_virtualenv(self):
        with tempfile.NamedTemporaryFile(mode='w+b') as script_file:
            os.fchmod(script_file.fileno(), 0o700)
            script_file.write(test_scripts['virtualenv'].format(self.python_shebang_location).encode('utf-8'))
            script_file.flush()
            with os.popen(script_file.name, 'r') as command_handle:
                result = command_handle.read()
            self.assertIn('Virtualenv ok', result)


if __name__ == "__main__":
    unittest.main()