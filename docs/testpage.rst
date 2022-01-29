========
Testpage
========

This page is for testing purposes. It showcases the reStructuredText markup with its rendered and raw versions for different formats and usecases. 

.. admonition:: See also

   * Sphinx Docs `Sphinx Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
   * Sphinx Docs `TOC <https://www.sphinx-doc.org/en/master/usage/index.html>`_

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 4

Metadata Test
=============

Each page should have its own metadata to have a descent intro on the searchengines and if links are shared.

.. code-block:: rst

    .. meta::
      
      :description lang=en: Particl Marketplace is censorship-resistant eCommerce built on blockchain technology and respects your privacy.


Headings Test
=============

This area shows some sample texts. Or an internal link to a certain page like the :doc:`Particl Support Page <../faq/get_support>` n other than that we have some roles like *emphasis* **strong** ``literal`` and so on. It is even possible to reference a link: `Make me laugh`_ or to reference to a heading on this page like :ref:`Video` or :ref:`Images` but you can also reference another page :doc:`like this <../intro/intro_general_particlmarketplace>`

First heading
=============

Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Second heading
--------------

Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Third heading
~~~~~~~~~~~~~

Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Fourth heading
""""""""""""""

Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. _Make me laugh: https://www.youtube.com/watch?v=hY7m5jjJ9mM

.. code-block:: rst

    Headings
    --------

    This area shows some sample texts. Or an internal link to a certain page like the :ref:`Particl Support Page <../faq/get_support>` n other than that we have some roles like *emphasis* **strong** ``literal`` and so on. It is even possible to reference a link: `Make me laugh`_

    ==============
    Document title
    ==============

    use only once in a document

    First heading
    -------------

    Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

    Second heading
    ~~~~~~~~~~~~~~

    Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

    Third heading
    ^^^^^^^^^^^^^
    Bodytext Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

    .. _Make me laugh: https://www.youtube.com/watch?v=hY7m5jjJ9mM

.. code-block:: rst

    1.  ==========  for the first  level
    2.  ----------  for the second level
    3.  ~~~~~~~~~~  for the third  level
    4.  """"""""""  for the fourth level
    5.  ''''''''''
    6.  ^^^^^^^^^^
    7.  ##########
    8.  **********

Achievements Test
=================

An achievement can be placed below a task that has been completed.

.. rst-class:: achievement

  Congratulations! You have installed Particl Marketplace.

.. code-block:: rst

  .. rst-class:: achievement

  Congratulations! You have installed Particl Marketplace.

Bigmessage
==========

A bigmessage can be placed where it is really needed.

.. rst-class:: bigmessage

  bigmessage! Get it while it's hot.

.. code-block:: rst

  .. rst-class:: bigmessage

  bigmessage! Get it while it's hot.

Glossary Test
=============

We have now a glossary file ":doc:`../glossary`" which should be populated with definitions. Then we can reference these definitions like this -> :term:`Sphinx` or :term:`FooBarLoo as I want<Sphinx>`.

.. code-block:: rst

  We have now a glossary file :doc:`glossary` which should be populated with definitions. Then we can reference these definitions like this -> :term:`Sphinx`.

  You can link to a term in the glossary while showing different text in the topic by including the term in angle brackets. For example:

  :term:`FooBarLoo as I want<Sphinx>`  

Text Roles
==========

Abbriviation 
------------

If the role content contains a parenthesized explanation, it will be treated specially: it will be shown in a tool-tip in HTML, and output only once in LaTeX.

:abbr:`LIFO (last-in, first-out)`

.. code-block:: rst

    :abbr:`LIFO (last-in, first-out)`

File Path
---------

Using a file path

:file:`/etc/passwd`

.. code-block:: rst

    :file:`/etc/passwd`

Keystrokes
----------

Mark a sequence of keystrokes

:kbd:`cmd` + :kbd:`s` || :kbd:`cmd+s` followed by :kbd:`y`

.. code-block:: rst

    :kbd:`cmd` + :kbd:`s` || :kbd:`cmd+s` followed by :kbd:`y`

GUI Labels
----------

Using GUI Labels

:guilabel:`&Cancel`, :guilabel:`O&k`, :guilabel:`&Reset`, :guilabel:`FAQ`

.. code-block:: rst

    :guilabel:`&Cancel`, :guilabel:`O&k`, :guilabel:`&Reset`, :guilabel:`FAQ`

inline code
-----------

:code:`$result = $a + 23;`

.. code-block:: rst

    :code:`$result = $a + 23;`

Menu Selection
--------------

If you want to describe a menu path

:menuselection:`Start --> Programs`

.. code-block:: rst

  :menuselection:`Start --> Programs`

Subscript and Superscript 
-------------------------

:subscript:`subscripted`

:superscript:`superscripted`

.. code-block:: rst

    :subscript:`subscripted`
    :superscript:`superscripted`

External Links
==============

* `External inline link <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
* External referenced link `The reference`_.

.. _The reference: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html

.. code-block:: rst

  * `External inline link <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
  * `External referenced link `The reference`_.

  .. _The reference: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html

Internal Links
==============

* Learn how to :ref:`link to a different section within this document<Tables>`.

.. code-block:: rst

  * Learn how to :ref:`link to a different section within this document<Tables>`.
  .. Mind the non existent gap between the last word and the 

To support cross-referencing to arbitrary locations in **any** document, the standard reST labels are used. For this to work label names **must be unique** throughout the entire documentation. 

* I reference to a page under :menuselection:`guides --> guide_general_enable_tor.rst` :ref:`Enable Tor on Particl Desktop`

.. code-block:: rst

  * I reference to a page under :menuselection:`guides --> guide_general_enable_tor.rst` :ref:`Enable Tor on Particl Desktop`
  
  Additionally there is the possibility to define manual reference labels.

  .. _my-reference-label:

  Section to cross-reference
  --------------------------

  This is the text of the section.

  It refers to the section itself, see :ref:`my-reference-label`.

  The referencing works over the whole tree which means targeting at any page as long the reference label is unique.

**Cross-referencing documents** There is also a way to directly link to documents. Link to the specified document; the document name can be specified in absolute or relative fashion:

* :menuselection:`faq --> common_issues.rst` as relative path :doc:`link text <../faq/common_issues>`.
* :menuselection:`faq --> common_issues.rst` as absolute path :doc:`link text </faq/common_issues>`.

.. code-block:: rst

 * :menuselection:`faq --> common_issues.rst` as relative path :doc:`link text <_templates/../faq/common_issues>`.
 * :menuselection:`faq --> common_issues.rst` as absolute path :doc:`link text </faq/common_issues>`.


Download Links
==============

See :download:`this image </_static/images/particl-logo-green.png>`.

.. code-block:: rst

  See :download:`this image </_static/images/particl-logo-green.png>`.

Video
=====

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="390" src="https://www.youtube.com/embed/IC9yY3MThoo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

.. code-block:: rst

      .. raw:: html

          <div style="text-align: center; margin-bottom: 2em;">
          <iframe width="100%" height="390" src="https://www.youtube.com/embed/IC9yY3MThoo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
          </div>


Images
======

.. figure:: /_static/media/images/canvas_w_logo.png
    :align: center
    :alt: Particl Logo on a dark canvas
    :target: /_static/media/images/canvas_w_logo.png

.. code-block:: rst

      .. figure:: /_static/media/images/canvas_w_logo.png
          :align: center
          :alt: Particl Logo on a dark canvas
          :target: /_static/media/images/canvas_w_logo.png

Boxes
=====

.. note::
	
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. tip::
	
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. danger::
	
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. attention::
	
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. seealso::
  
  Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. hint::
  
  Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. important::
  
  Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

.. admonition:: Further technical documentation

  You can make up your own admonition too.

.. code-block:: rst

      .. note::
  
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

      .. tip::
  
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

      .. danger::
  
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

      .. attention::
  
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

      .. warning::
  
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

      .. hint::
  
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

      .. important::
  
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

      .. admonition:: Further technical documentation

        You can make up your own admonition too.

Tables
======

Even csv tables can be put in.

Simple
------

A simple Table 


=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

.. code-block:: rst

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

Grid
----
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

.. code-block:: rst

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | ...        | ...      |          |
    +------------------------+------------+----------+----------+


CSV
---

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

.. code-block:: rst

    .. csv-table:: Frozen Delights!
       :header: "Treat", "Quantity", "Description"
       :widths: 15, 10, 30
    
       "Albatross", 2.99, "On a stick!"
       "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
       crunchy, now would it?"
       "Gannet Ripple", 1.99, "On a stick!"


Lists
=====

Big fat looking list
--------------------

.. rst-class:: bignums-xxl

1. **Do this and that.**

    * And FooBar of course. 
    * If you know what I mean.
    * Whatever

2. Two

   .. code-block:: php

    $a = 'hello';
    $b = 'something';

.. code-block:: rst

    .. rst-class:: bignums-xxl

        1. **Do this and that.**
        
            * And FooBar of course. 
            * If you know what I mean.
            * Whatever
        
        2. Two
        
           .. code-block:: php
        
            $a = 'hello';
            $b = 'something';


Nested Normal 
-------------
* sadipscing elitr
* magna aliquyam erat, sed diam
	* with nesting
	* if you like
* ipsum dolor sit

.. code-block:: rst

    * sadipscing elitr
    * magna aliquyam erat, sed diam
      * with nesting
      * if you like
    * ipsum dolor sit

Manual 
------
1. sadipscing elitr
2. magna aliquyam erat, sed diam 
3. ipsum dolor sit

.. code-block:: rst

    1. sadipscing elitr
    2. magna aliquyam erat, sed diam 
    3. ipsum dolor sit

Automatic 
---------
#. sadipscing elitr
#. magna aliquyam erat, sed diam
#. ipsum dolor sit

.. code-block:: rst

    #. sadipscing elitr
    #. magna aliquyam erat, sed diam
    #. ipsum dolor sit

Normal 
------
- sadipscing elitr
- magna aliquyam erat, sed diam
- ipsum dolor sit

.. code-block:: rst

    - sadipscing elitr
    - magna aliquyam erat, sed diam
    - ipsum dolor sit


Codeblocks
==========

No special highlighting 
-----------------------

.. code-block:: none

    $ cd ~/myproject
    $ foo bar
    > kill -9

.. code-block:: rst

    .. code-block:: none
    
        $ cd ~/myproject
        $ foo bar
        > kill -9

Bash highlighting
-----------------

.. code-block:: bash

    $ cd ~/.particl
    $ rm *

.. code-block:: rst

    .. code-block:: bash
    
        $ cd ~/.particl
        $ rm *

HTML highlighting
-----------------

.. code-block:: html

   <h1>code block example</h1>
   <p>Paragraph Text</p>

.. code-block:: rst

    .. code-block:: html
    
       <h1>code block example</h1>
       <p>Paragraph Text</p>

Tabs
====

Grouped tabs
------------

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


.. code-block:: rst

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


Normal tabs
-----------

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

.. code-block:: rst

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


Toggles
=======

Toggle items can be used for FAQ like content. 

.. container:: toggle

    .. container:: header

        **I am a header. Why is particl the best marketplace in the world?**

    Because Particl is the best thing you will every see in your entire life. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    And because of **THIS**

.. container:: toggle

    .. container:: header

        **I am a second header. Why is particl the best marketplace in the world?**

    Because Particl is the best thing you will every see in your entire life. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    And because of **THIS**

.. container:: toggle

    .. container:: header

        **I am a second header. Why is particl the best marketplace in the world?**

    Because Particl is the best thing you will every see in your entire life. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    And because of **THIS**

.. container:: toggle

    .. container:: header

        **I am a second header. Why is particl the best marketplace in the world?**

    Because Particl is the best thing you will every see in your entire life. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    And because of **THIS**

.. code-block:: rst

    .. container:: toggle
    
        .. container:: header
    
            **I am a header. Why is particl the best marketplace in the world?**
    
        Because Particl is the best thing you will every see in your entire life. Lorem ipsum dolor sit amet,     consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    
        And because of **THIS**
    
    .. container:: toggle
    
        .. container:: header
    
            **I am a second header. Why is particl the best marketplace in the world?**
    
        Because Particl is the best thing you will every see in your entire life. Lorem ipsum dolor sit amet,     consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    
        And because of **THIS**

Including files
===============

We are able to include files and render them locally. This is very helpful for the FAQ sections as we are able to deliver the FAQ additionally at the place where it might be needed. For the nature that faq do have a repetitve character in certain sections we do not need to write them again and they are always up to date. The naming is important to prevent double rendering.

.. include:: /faq/faq_testpage.rst.txt

.. code-block:: rst

    .. include:: /faq/faq_testpage.rst.txt

Epilogs
=======

I am a text and int the middle of it I put a link |Courage Cat| out of the epilog. Guess what |PM| is? 

epilog data is put into :file:`conf.py`

.. code-block:: rst

  I am a text and int the middle of it I put a link |Courage Cat| out of the epilog. Guess what |PM| is?
