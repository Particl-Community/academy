
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

This area shows some sample texts. Or an internal link to a certain page like the Introduction Page of Particl Marketplace n other than that we have some roles like *emphasis* **strong** ``literal`` and so on. It is even possible to reference a link: `Make me laugh`_

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

Video
-----

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="400" src="https://www.youtube.com/embed/sUodtqG8DUs" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

Images
------

.. figure:: media/images/canvas_w_logo.png
    :align: center
    :figwidth: 100%
    :figheight: 350px
    :target: media/images/canvas_w_logo.png

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


Codeblock
-----------

.. code-block:: none

    $ cd ~/myproject
    $ foo bar
    > kill -9

.. code-block:: bash

    $ cd ~/.particl
    $ rm *

Tabs
----

Grouped tabs
^^^^^^^


.. tabs::

   .. group-tab:: Linux

      Linux Line 1

   .. group-tab:: Mac OSX

      Mac OSX Line 1

   .. group-tab:: Windows

      Windows Line 1

.. tabs::

   .. group-tab:: Linux

      Linux Line 1
      Linux Line 2

   .. group-tab:: Mac OSX

      Mac OSX Line 1
      Mac OSX Line 2

   .. group-tab:: Windows

      Windows Line 1
      Mac OSX Line 2


Normal tabls
^^^^

.. tabs::
	 .. tab:: Windows

	    c:\foo\bar.bat

	 .. tab:: Mac

	    cd ~
	    ls -la
	    whoami

	 .. tab:: Linux

	    cd ~
	    ls -la
	    uname -a

