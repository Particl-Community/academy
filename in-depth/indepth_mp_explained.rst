=============================
Particl Marketplace Explained
=============================

**This article is a technical explanation for the more curious minds.**

.. meta::
      
      :description lang=en: Deep dive explanation of Particl's blockchain e-commerce solution yielding fair market conditions. Simply put, it's the most secure and private online marketplace on the web.

With the award-winning :term:`Particl Marketplace`, you transform today’s e-commerce into a free, secure, cost-efficient, and trustworthy environment where you can enjoy true free market conditions. How this all comes together is explained in this section. 

.. admonition:: Understanding the Basics of Particl Maketplace

   - Particl Academy - Intro :doc:`Uncompromising, What You Get <../intro/intro_general_particlmarketplace>`
   - Particl Academy - Intro :doc:`Target Audiences <../intro/intro_general_target_audiences>`
   - Particl Academy - Intro :doc:`Particl Marketplace Brief Overview <../intro/intro_marketplace_brief_overview>`

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Characteristics
---------------

While the :term:`Particl Marketplace` is an easy-to-use e-commerce platform, what happens in the background is relatively complex and employs several brand new technologies. There's no server, central database, or employees working at keeping the marketplace up and running. Instead, it relies on an intricate combination of distributed technologies developed, maintained, and run by a vast and global network of participants.

* **Autonomous** — runs by itself and requires no human intervention
* **Secure** — has the highest level of digital security provided by trustless encryption
* **Private** — no data or personal information is ever collected about you
* **Resilient** — can’t be censored or shut down by anyone
* **Censorship-proof** — no predefined rules or policies, and no ban on items
* **Near-zero fee** — only pay the bare minimum for the network to run by itself

These advantages are only possible thanks to the particularly :term:`decentralized <Decentralization>` nature of the :term:`Particl Marketplace`.

----

Technicals in a Nutshell
------------------------

:term:`Particl Marketplace` is an application on the :term:`Particl Desktop` client. It uses Particl's :ref:`Open Market Protocol (OMP)` to connect and interact with the :term:`Particl Network`. That's the backbone for the :term:`decentralized <Decentralization>` payments, communications, security, and privacy capabilities of the marketplace. 

The :term:`Particl Network` is a combination of the :term:`Particl Blockchain` and the :term:`SecureMessaging (SMSG)`. 

The blockchain executes and verifies all financial transactions using its native and untraceable currency; :ref:`PART <Currency (PART) Explained>`. All transactions on the :term:`Particl Marketplace` are private and confidential by default.

On the other end, the :term:`SecureMessaging (SMSG)` protocol processes all the non-financial data related to the :term:`decentralized <Decentralization>` marketplace and securely broadcasts it to the rest of the network using military-grade encryption. 

The :term:`Particl Network` is entirely trustless and requires no third-party to function.

----

The Front-End 
-------------

The front-end part of any application or platform refers to what a user directly interacts with. It is, more directly, the graphical inteface. 

Particl Desktop & Marketplace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:term:`Particl Desktop` is the front-end application of the :term:`Particl Network`; it allows you to connect directly with the underlying platform code in a graphical, user-friendly, and easy to use fashion.

If you want to sell or purchase an item on :term:`Particl Marketplace`, browse listings and markets, leave a comment, or any other similar action, you inevitably need to use :term:`Particl Marketplace`; the front-end application of Particl to do so. It is what what makes all the code appear in a visual manner.

.. note::

   A web and a mobile version of :term:`Particl Marketplace` are planned to be released later on and will play a key role in making the platform more accessible and convenient to use.

.. note:: 
   
   :term:`Particl Desktop` and :term:`Particl Marketplace` are ever-ongoing works in progress. Every day, they get better, easier to use, and more accessible for all. Exciting new projects and features constantly emerge to help the :term:`Particl ecosystem <Particl Ecosystem>` thrive. 

.. seealso::

 - Particl Academy - :doc:`All Functions <../intro/intro_general_functions>`
 - Github - `Particl Desktop <https://github.com/particl/particl-desktop>`_


The Backend 
-----------

The back-end of any application or platform refers to the part that is not directly accessed by the user, typically responsible for storing and manipulating data. These are the various protocols, including the :term:`Particl Blockchain`, that are used to bring the :term:`Particl ecosystem` to life. 


The Open Market Protocol (OMP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :term:`Open Market Protocol (OMP)` is the back-end protocol that makes :term:`Particl Marketplace` possible. It is the framework that defines how marketplace transactions, orders, listings, and other key e-commerce functionalities are to be processed by the :term:`SecureMessaging (SMSG)` network and the :term:`Particl Blockchain`. It is the “glue” that sticks everything together. 

If :term:`Particl Desktop` is what people use to access :term:`Particl Marketplace` (the front-end), the OMP is what makes it possible in the background (the back-end).

.. seealso::

 - Particl Wiki - `Open Market Protocol <https://particl.wiki/learn/marketplace/open-market-protocol/>`_
 - Particl Wiki - `SecureMessaging <https://particl.wiki/learn/marketplace/smsg/>`_
 - Github - `Particl Market <https://github.com/particl/particl-market>`_
 - Github - `OMP Lib <https://github.com/particl/omp-lib>`_
 - Github - `Particl RPC Documentation <https://particl.github.io/rpc-docs/>`_

The Particl Blockchain
~~~~~~~~~~~~~~~~~~~~~~

The :term:`Particl Blockchain` is a decentralized, immutable, and censorship-proof ledger. It is based on the Bitcoin technology and has been carefully enhanced by the Particl team to provide a more robust level of privacy by using a combination of industry-leading privacy technologies. 

The :term:`Particl Blockchain` processes and validates payments between two users without requiring any third-party such as a bank or a payment processor.

The PART Coin
^^^^^^^^^^^^^

PART is the :term:`cryptocurrency <Cryptocurrency>` of the :term:`Particl blockchain <Particl Blockchain>`. It is a secure and confidential currency designed specifically to power e-commerce and online marketplaces. It uses several security, encryption, and privacy protocols to make sure none of your personal information and data can be collected when transacting on the :term:`cryptocurrency <Particl Marketplace>`. 

.. seealso::

 - Github - `Particl Core <https://github.com/particl/particl-core>`_
 - Block Explorer - `Insight <https://explorer.particl.io>`_
 - Particl Academy - :doc:`Blockchain Specifications <../in-depth/indepth_part_coin>`
 - Particl Academy - :doc:`PART Coin <../in-depth/indepth_part_coin>`

The SecureMessaging (SMSG protocol)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SecureMessaging (SMSG protocol) is a :term:`decentralized <Decentralization>` storage network (DSN) to store and transfer data between nodes in a privacy-preserving manner. It enables a private and secure environment for e-commerce and communications between users. 

SMSG powers the Particl Marketplace without bloating the blockchain with excessive data and without leaving any permanent record.

* note about its developent future with the "note" box

.. seealso::

 - Github - `Particl Core <https://github.com/particl/particl-core>`_
 - Particl Wiki - `SecureMessaging <https://particl.wiki/learn/marketplace/smsg/>`_

The Data Storage Network (DSN)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* What it does
* Why is it there
* Inspiration from glossary and wiki
* Backlink from glossary

.. seealso::

 - Github - `Particl Core <https://github.com/particl/particl-core>`_
 - Particl Wiki - `Data Storage Network <https://particl.wiki/learn/marketplace/data-storage-network/>`_

Trustless Setup
---------------

* What makes it a trustless setup
* Why is it important

Technicals of a Buy-Flow
------------------------

* What's happening (signaling,smart-contracts,communications of/between protocols) in the background at each stage. 1.,2.,3.

Payments and Settlement-layer
-----------------------------

* unsure if this should be placed here, since this shall be true to any dapp on Particl. Could have a better fit on the "PART Explained" page.
* Why is it the settlement-layer
* What is it used for
* What does it mean economically (supply reduction, etc.)
* Inspiration from glossary
* Link to the "PART Coin explained" with the "see also" box
* Link to the "fund,coins,balances" with the "see also" box
* Link to the "obtain part" with the "see also" box
* Link to the "CMC Page" with the "see also" box
* note about its developent future (ideal situation where a user can pay in any currency and the conversion happens on the fly in the background) with the "note" box