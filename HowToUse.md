# How to use it #

First install the Pygments library.

easy\_install Pygments

Put the syntax\_highlight folder somewhere in your PYTHONPATH.

Add it to your INSTALLED\_APPS in settings.py for your project.

The application currently consists only of 4 template tags. To use them in your templates you need to load the 'syntax' template library.

{%load syntax%}

1. {%highlight code syntax%}

Outputs html representation of higlighted code without linenumbers.

2. {%highlight\_table code syntax%}

Outputs html representation of highlighted code in a table with 2 columns, the first of which contains the line numbers. This can be layed out incorrectly by some browsers if no css reset is used. The demo project uses the YUI css reset library.

3. {%highlight\_inline code syntax%}

Outputs html representation of higlighted code with linenumbers embedded in the pre tags next to the code.


In the above 3 tags the syntax variable is optional, and the library will try to guess the correct lexer if it is ommited. The arguments may be eyther string literals or template variables.

4. {%highlight\_css style%}

Outputs needed css to colorize the output the first 3 tags produce. Style is optional and if it is ommited the 'default' pygments style will be used. Style can also be a string literal or a template context variable.



See the included demo project for details of what syntaxes and styles are supported and how to use the library.