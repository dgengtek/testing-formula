# vim: ft=sls

{% import_yaml "testing/defaults.yaml" as defaults %}

{% import_yaml "testing/os_family_map.yaml" as os_family_map %}
{% import_yaml "testing/os_map.yaml" as os_map %}

{% set os_family_map = salt['grains.filter_by'](os_family_map, grain="os_family") %}
{% set os_map = salt['grains.filter_by'](os_map , grain="os") %}

{## Merge the flavor_map to the default settings ##}
{% do defaults.update(os_family_map) %}
{% do defaults.update(os_map) %}

{% set testing = salt['pillar.get'](
        'testing',
        default=defaults,
        merge=True
    )
%}
