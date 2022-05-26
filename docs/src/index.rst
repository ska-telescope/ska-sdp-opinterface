SDP Operator interface
======================

The ``ska-sdp-opinterface`` repository contains a prototype which shows
some examples of a web-based interface which can view (and could, in the future, control)
the current live state of the SDP subsystem by means of the `SDP Configuration Database
<https://developer.skao.int/projects/ska-sdp-config/en/latest/>`_.
This illustrates some of the functionality which could
be expanded further in both monitoring and control of the
the SDP sub-system in a user-friendly and/or graphical manner.

This implementation is based on the Python `Flask <https://flask.palletsprojects.com/en/2.0.x/>`_
module and shows the following views

* Display of the current contents of the SDP Configuration library in a textual format
* Similar to the above but shown as a a `tree view` - where nodes in the tree can be expanded and this could be connected to additional functionality.
* A different `tree view` of the `SDP Scripts` contained in the database. Again the nodes can be expanded to show more detail.

.. toctree::
  :maxdepth: 1
  :caption: Using the Operator interface

  connecting
  list-view
  tree-view
  scripts-view


