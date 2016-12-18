NSD
###

.. image:: https://travis-ci.org/adarnimrod/nsd.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/nsd

Provision an NSD authorative DNS server. By default the role has minimal
configuration. You can add your own by overriding the default
:code:`nsd_config` dictionary with your own for configuration under the
:code:`server` block in :code:`nsd.conf`. For other blocks that can declared
multiple times (like the :code:`zone` block) add your own templates in the
:code:`templates/nsd/conf.d` directory either inside the role or next to your
playbook. Likewise, zone templates can be added by placing them in
:code:`templates/nsd/zones` (again either inside the role or relative to your
playbook).

Requirements
------------

See :code:`meta/main.yml` and assertions at the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Python 2.7 and either Docker or Vagrant and Virtualbox.
Install the Python dependencies, dependent roles and roles required for
testing:

.. code:: shell

    pip install -r tests/requirements.txt
    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles
    molecule dependency

To run the full test suite:

.. code:: shell

    pre-commit run --all-files
    molecule test --platform all

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
