# Adam Prieto
# Professor Jed Brown
# CSCI 5636 - Numerical Solutions to Partial Differential Equations
# December 2023

# Code Link: https://github.com/usnistgov/fipy/blob/master/examples/cahnHilliard/test.py

from __future__ import unicode_literals
from fipy.tests.doctestPlus import _LateImportDocTestSuite
import fipy.tests.testProgram

import time
from memory_profiler import profile


def _suite():
    return _LateImportDocTestSuite(docTestModuleNames = (
            'tanh1D',
            'mesh2D',
            'mesh3D',
            'sphere',
#             'mesh2DCoupled',  # FIXME: this test is [borked](https://github.com/usnistgov/fipy/issues/378)
        ), base = __name__)

if __name__ == '__main__':

    start_time = time.time()
    fipy.tests.testProgram.main(defaultTest='_suite')

    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time}sec")