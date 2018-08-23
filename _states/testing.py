#!/bin/env python3
"""
"""
import logging


################################################################################
# call states with __states__["nameofstate.function"](parameter1,p2,p3,kwargs)
# ret = __states__['file.managed'](name='/tmp/myfile', source='salt://myfile')

# call salt functions with __salt__["nameofmodule.function"](p1,p2,kwargs)
"""
name: The same value passed to the state as "name".

changes: A dict describing the changes made.

Each thing changed should be a key, with its value being another
dict with keys called "old" and "new" containing the old/new values.
For example, the pkg state's changes dict has one key for each
package changed, with the "old" and "new" keys in its sub-dict containing
the old and new versions of the package. For example, the final changes
dictionary for this scenario would look something like this:

ret['changes'].update({'my_pkg_name': {'old': '',
                                   'new': 'my_pkg_name-1.0'}})

result: A tristate value. True if the action was successful,
False if it was not, or None if the state was run in test mode, test=True,
and changes would have been made if the state was not run in test mode.
live mode 	test mode
no changes 	True 	True
successful changes 	True 	None
failed changes 	False 	None

Note

Test mode does not predict if the changes will be successful or not.

comment: A string containing a summary of the result.


The return data can also, include the pchanges key, this stands for
predictive changes. The pchanges key informs the State system what
changes are predicted to occur.

Note

States should not return data which cannot be serialized such as frozensets.

################################################################################
# Return comment of changes if test.
if __opts__['test']:
    ret['result'] = None
    ret['comment'] = 'State Foo will execute with param {0}'.format(bar)
    return ret


"""


"""
# required return data
"""
################################################################################

# write to minion logs
logger = logging.getLogger(__name__)

__virtualname__ = 'ftesting'


def __virtual__():
    return __virtualname__


def _error(ret, err_msg):
    ret['result'] = False
    ret['comment'] = err_msg
    return ret


def _del_key(k, kwargs):
    if k in kwargs:
        del kwargs[k]
        return True
    return False


def _kw_set_default(k, kwargs, default):
    if k not in kwargs:
        kwargs[k] = default


def simple_example(name, source, **kwargs):
    return
    return_dict = {
        "name": name,
        "changes": {},
        "result": True,
        "comment": "",
    }
    return_dict["changes"].update(header=__salt__["file.prepend"](filename,
        header))
    _kw_set_default("sfn", kwargs, "")
    _kw_set_default("ret", kwargs, return_dict)
    _kw_set_default("source", kwargs, None)
    _kw_set_default("contents", kwargs, None)
    _kw_set_default("source_sum", kwargs, {})
    _kw_set_default("user", kwargs, "root")
    _kw_set_default("group", kwargs, "root")
    _kw_set_default("mode", kwargs, "0755")
    _kw_set_default("saltenv", kwargs, "base")
    _kw_set_default("backup", kwargs, "")
    if __opts__["test"]:
        return return_dict

    return __salt__["file.manage_file"](**kwargs)


# implement logic in a salt execution module and call here with
# __salt__["module.function"]
def notafunction():
    # required dict to return
    return_dict = {
           "name": "name",
           "changes": {},
           "result": True,
           "comment": "",
            }

    if __opts__["test"]:
        return_dict["result"] = None
        return_dict["comment"] = "comment here about what whill change"
        return return_dict

    # execute changes now

    return return_dict


# used for requisite
# needs to have same parameters and return same structured dict
def mod_watch():
    # required dict to return
    return_dict = {
           "name": "name",
           "changes": {},
           "result": True,
           "comment": "",
            }

    if __opts__["test"]:
        return_dict["result"] = None
        return_dict["comment"] = "comment here about what whill change"
        return return_dict

    # execute changes now

    return return_dict


def mod_init(low):
    """
    must be named this way
    mod_init(low)
    used for setting up an environment for the state module
    requires low state data(dict)

    must return a bool
    return true if setup was sucessfull, will not run next time on state execution
    return false to run next time

    Refresh the package database here so that it only needs to happen once
    """
    if low['fun'] == 'installed' or low['fun'] == 'latest':
        rtag = __gen_rtag()
        if not os.path.exists(rtag):
            open(rtag, 'w+').write('')
        return True
    else:
        return False


