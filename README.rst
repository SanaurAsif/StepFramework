Step Framework
===============

.. contents::
   :local:

Introduction
------------

`Step Framework <https://github.com/SanaurAsif/Step>`_ |r| is a generic open source
automation framework for run tests as steps. It has simple plain
text syntax and it can be extended easily with generic and custom libraries.

Step Framework is operating system and application independent. It is
implemented using `Python <http://python.org>`_ which is also the primary
language to extend it. The framework has a rich ecosystem around it consisting
of various generic libraries and tools that are developed as separate projects.

Step Framework project is hosted on GitHub_ where you can find source code,
an issue tracker, and some further documentation.

Step Framework development is sponsored by non-profit `Root Of Cyber
<https://t.me/RootOfCyber>`_. If you are using the framework
and benefiting from it, consider joining the foundation to help maintaining
the framework and developing it further.

.. _GitHub: https://github.com/SanaurAsif/Step


Installation
------------

If you already have Python_ with `pip <https://pip.pypa.io>`_ installed,
you can simply run::

    pip install git+https://github.com/SanaurAsif/Step


Example
-------

Step is a simple example test case for testing login to some system.
You can find more examples with links to related demo projects from
https://github.com/SanaurAsif/Step.

.. code:: stepframework

    *** Continous ***
    Log to console    time

    *** Settings ***
    Documentation     A test suite with a single test for valid login.
    ...
    ...               This test has a workflow that is created using keywords in
    ...               the imported resource file.
    Resource          login.resource

    *** Test Cases ***
    Valid Login
        Open Browser To Login Page
        Input Username    demo
        Input Password    mode
        Submit Credentials
        Welcome Page Should Be Open
        [Teardown]    Close Browser

Usage
-----

Tests (or tasks) are executed from the command line using the ``rocx``
command or by executing the ``rocx`` module directly like ``python -m rocx`` .

The basic usage is giving a path to a test (or task) file as an
argument with possible command line options before the path::

    rocx test.step
    rocx --variable BROWSER:Firefox --outputdir results path/to/tests/test.step



Support and Contact
-------------------

- `Slack <https://t.me/RootOfCyber>`_
- `Forum <https://t.me/ROCX_Group>`_
- `Developer <https://web.facebook.com/sanaur.asif.72>`_ on Facebook

Contributing
------------

Interested to contribute to Step Framework? Great! In that case it is a good
start by looking at the full code. If you interested submit your pull requests.


License and Trademark
---------------------

Step Framework is open source software provided under the `Apache License 2.0`__.
Step Framework documentation and other similar content use the
`Creative Commons Attribution 3.0 Unported`__ license. Most libraries and tools
in the ecosystem are also open source, but they may use different licenses.

Step Framework trademark is owned by `Root Of Cyber`_.

__ http://apache.org/licenses/LICENSE-2.0
__ http://creativecommons.org/licenses/by/3.0

.. |r| unicode:: U+00AE