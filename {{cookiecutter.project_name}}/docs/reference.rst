{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}
Reference
=========


{{ heading(cookiecutter.package_name) }}

.. automodule:: {{cookiecutter.package_name}}
   :members:
