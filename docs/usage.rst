========
Examples
========

To simply run using default the configuration, use:

.. code-block:: bash

    pytest --stats-d tests/


If there is a need to configure where to sent results to other than `localhost:8125`, use:

.. code-block:: bash

    pytest --stats-d --stats-host http://myserver.com --stats-port 3000 tests/


You can also prefix your results if you plan on having multiple projects sending results to the same server:

.. code-block:: bash

    pytest --stats-d --stats-prefix myproject test/