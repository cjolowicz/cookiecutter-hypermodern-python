{%- macro heading(text) -%}
## {{text}}
{%- endmacro -%}
# Reference

{{ heading(cookiecutter.package_name) }}

```{eval-rst} 
.. automodule:: {{cookiecutter.package_name}}
   :members:
```
