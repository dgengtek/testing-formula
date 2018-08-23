#!/bin/env python3
"""
"""
################################################################################
# functions preceded with an _ are not loaded

# use decorator for dependency loading
"""
from salt.utils.decorators import depends

HAS_DEP = False
try:
    import dependency_that_sometimes_exists
    HAS_DEP = True
except ImportError:
    pass

@depends(HAS_DEP)
def foo():
    return True
"""
# printout configuration
"""
When writing a module the __outputter__ dictionary can be declared in the module. 
The __outputter__ dictionary contains a mapping of function name to Salt Outputter.

__outputter__ = {
    'run': 'txt'
}

This will ensure that the text outputter is used.
"""

# use depends decorator to include only if dependency exists
"""
@depends('dependency_that_sometimes_exists')
def foo():
    '''
    Function with a dependency on the "dependency_that_sometimes_exists" module,
    if the "dependency_that_sometimes_exists" is missing this function will not exist
    '''
    return True
"""
# use fallback function to run if not exists
"""
def _fallback():
    '''
    Fallback function for the depends decorator to replace a function with
    '''
    return '"dependency_that_sometimes_exists" needs to be installed for this function to exist'

@depends('dependency_that_sometimes_exists', fallback_function=_fallback)
def foo():
    '''
    Function with a dependency on the "dependency_that_sometimes_exists" module.
    If the "dependency_that_sometimes_exists" is missing this function will be
    replaced with "_fallback"
    '''
    return True

"""
################################################################################

import logging

log = logging.getLogger(__name__)

# Define the module's virtual name
__virtualname__ = 'ftesting'


def __virtual__():
    '''
    '''
    return __virtualname__
