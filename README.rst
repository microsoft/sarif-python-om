sarif-om
========

Python classes for the SARIF 2.1.0 object model

Usage
=====
::

    pip install sarif-om

    import sarif_om

Description
===========

This module contains classes for the object model defined by the
`Static Analysis Results Interchange Format (SARIF) Version 2.1.0 <https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01>`_ file format,
an `OASIS <https://www.oasis-open.org>`_ `Committee Specification <https://www.oasis-open.org/news/announcements/static-analysis-results-interchange-format-sarif-v2-1-0-from-the-sarif-tc-is-an-a>`_.

To learn more about SARIF and find resources for working with it, you can visit the `SARIF Home Page <http://sarifweb.azurewebsites.net/>`_.

The source code is available at https://github.com/microsoft/sarif-python-om.

How to use
==========

.. code-block:: python

    from sarif_om import SarifLog, Run, Tool, ToolComponent, Result, Message


    sarif_log = SarifLog(
        version="2.1.0",
        runs=[
            Run(
                tool=Tool(
                    driver=ToolComponent(
                        name="My Static Analyzer",
                        version="1.0.0",
                    )
                ),
                results=[
                    Result(
                        rule_id="R001",
                        message=Message(text="Use of uninitialized variable 'x'"),
                    )
                ],
            )
        ],
    )

    print(sarif_log)

To serialize it to plain dict or JSON:

.. code-block:: python

    from sarif_om import to_dict, to_json

    print(to_json(sarif_log))
    print(to_dict(sarif_log))

To deserialize dict/JSON data to ``sarif_om.SarifLog``:

.. code-block:: python

    import json
    from sarif_om import from_dict, from_json


    sarif_log_dict = {
        "runs": [
            {
                "tool": {"driver": {"name": "My Static Analyzer", "version": "1.0.0"}},
                "results": [
                    {
                        "message": {"text": "Use of uninitialized variable 'x'"},
                        "ruleId": "R001",
                    }
                ],
            }
        ],
        "version": "2.1.0",
    }

    print(from_dict(sarif_log_dict))
    print(from_json(json.dumps(sarif_log_dict)))

Generation
==========

The classes in this module were generated from the `SARIF JSON schema <https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01/schemas/sarif-schema-2.1.0.json>`_
by the `jschema-to-python <https://github.com/microsoft/jschema-to-python>`_ code generator,
using the final SARIF standard JSON schema file ``sarif-schema-2.1.0.json`` and the code generation hints file ``code-gen-hints.json``
at the root of the GitHub repo, with the following command line::

    pip install jschema-to-python

    py -m jschema_to_python
        --schema-path sarif-schema-2.1.0.json
        --module-name sarif_om
        --output-directory sarif_om
        --root-class-name SarifLog
        --hints-file-path code-gen-hints.json
        --force
        -vv

Contributing
============

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the `Microsoft Open Source Code of Conduct <https://opensource.microsoft.com/codeofconduct>`_.
For more information see the `Code of Conduct FAQ <https://opensource.microsoft.com/codeofconduct/faq>`_ or
contact `opencode@microsoft.com <mailto:opencode@microsoft.com>`_ with any additional questions or comments.
