#!/usr/bin/env python

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        suffix = self._task.args.get('suffix')
        varname = self._task.args.get('var_name')

        merged = {}
        for var in (v for v in task_vars.keys() if v.endswith(suffix)):
            merged.update(task_vars[var])

        return dict(
            ansible_facts={varname: self._templar.template(merged)},
            changed=False
        )
