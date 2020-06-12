{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}
Reference
=========

.. contents::
    :local:
    :backlinks: none


{{ heading(cookiecutter.package_name + ".__main__") }}

.. automodule:: {{cookiecutter.package_name}}.__main__
   :members:
