# vim: ft=sls
{% from "testing/map.sls" import testing with context %}

{{ salt.cp.cache_file(testing.download_url) }}
