NSD
###

.. image:: https://travis-ci.org/adarnimrod/nsd.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/nsd

Provision an NSD authorative DNS server. By default the role has minimal
configuration. Overriding :code:`nsd_server_block` with a text block will
configure the :code:`server` clause of NSD, same for
:code:`nsd_remote_control_block` and the :code:`remote-control` block. Multiple
patterns, zones and keys are provided by overriding :code:`nsd_patterns`,
:code:`nsd_zones` and :code:`nsd_keys` respectively. Zone file templates can be
added by placing them in :code:`templates/nsd/zones` either inside the role or
relative to your playbook.

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
