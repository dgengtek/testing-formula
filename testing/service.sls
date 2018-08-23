# vim: ft=sls
{% from "testing/map.sls" import testing with context %}

Start testing service:
  service.running:
    - name: {{ testing.service.name }}
    - enable: True
