
testpage
==============

This page is for testing purposes.

Links
-----
* `rst manual <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
* `Learn everything and see examples <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_

.. note::
	
	#. Best practice is to `open Getting Started <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_ to see how things shall look like in the end. 
	#. If you found your example click on ``Edit on Gitub`` in the top right corner. 
	#. Finally click the ``raw`` version with github to see how the markup was realized.

---

Testing ground
--------------

this is the area to play around with reStructuredText.


Headings
--------------

This area shows some sample texts. Or an internal link to a certain page like the Introduction Page of Particl Marketplace n other than that we have some roles like *emphasis* **strong** ``literal`` and so on. It is even possible to reference a link: `Make me laugh`_:

First heading
==============

Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Second heading
--------------

Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Third heading
^^^^^^^^^^^^^
Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. _Make me laugh: https://www.youtube.com/watch?v=hY7m5jjJ9mM

Boxes
--------------

.. note::
	
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. tip::
	
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. danger::
	
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. attention::
	
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Tables
--------------

Even csv tables can be put in.

Simple
^^^^^^^
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

Grid
^^^^^^^
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

CSV
^^^^

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"


Lists
--------------

Nested Normal 
^^^^^^^^^^^^^
* sadipscing elitr
* magna aliquyam erat, sed diam
	* with nesting
	* if you like
* ipsum dolor sit

Manual 
^^^^^^^^^^^^^
1. sadipscing elitr
2. magna aliquyam erat, sed diam 
3. ipsum dolor sit

Automatic 
^^^^^^^^^^^^^
#. sadipscing elitr
#. magna aliquyam erat, sed diam
#. ipsum dolor sit

Normal 
^^^^^^^^^^^^^
- sadipscing elitr
- magna aliquyam erat, sed diam
- ipsum dolor sit


Prompts & blocks
-----------

.. prompt:: 
	bash $

    cd whatever/you/like
    rm foo

.. sample::
	It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

.. code-block:: none

    $ cd ~/myproject
    $ foo bar
    > kill -9

.. highlight:: c
	highlighting for c

.. highlight:: bash
	bash here

.. highlight:: guess
	lets the lexer identify the code

.. code-block:: sourcecode
	this is a source code

Tabs
------

Testing tabs here

.. tabs::
 .. code-tab:: windows Windows

    cd ..

    format c:
    And now go back to work    

 .. code-tab:: Mac

    cd ~

    rm *
    And now go back to work
