# vim: ft=sls
{% set os_family = salt.grains.get("os_family") %}
{% set os = salt.grains.get("os") %}

{% if os_family == "" -%}
OS family is not supported:
  test.show_notification:
    - text: Formula is disabled
{% else -%}
include:
  - .install
  - .service
{% endif %}
