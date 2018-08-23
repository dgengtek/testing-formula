# vim: ft=sls
{% from "testing/map.sls" import testing with context %}
Install package for testing:
  pkg.installed:
    - pkgs: {{ testing.packages }}
