=================
Apply for Listing
=================

.. title::
   BasicSwap DEX Coin Usage Guide
   
.. meta::
   :description lang=en: Add your coin to the BasicSwap DEX or apply for listing.
   :keywords lang=en: Particl, DEX, Trading, Exchange, Buy Crypto, Sell Crypto, Installation, Quickstart, Blockchain, Privacy, E-Commerce, multi-vendor marketplace, online marketplace

The :term:`BasicSwap DEX <BasicSwap>` lets you trade a range of cryptocurrencies in total privacy and without third-party assistance. And thanks to its open-source framework, anyone can add new coins to the DEX. 

This guide will show you how to add new coins to the BasicSwap DEX; either by manually integrating them or by submitting a coin listing application to the BasicSwap team.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

.. attention::

        BasicSwap is a cross-chain DEX that makes on-chain swaps. For this reason, each coin integration has to be worked out on a case-by-case basis. If you struggle to integrate a coin manually, consider submitting a listing application request. 

Manual Integration
==================

Thanks to its open-source nature, it is possible for anyone to submit their own coin integrations on Github. When successfully merged into the code, anyone with an up-to-date version of BasicSwap can then trade that new coin.

Requirements
------------

.. note::

        The following requirements are up-to-date with BasicSwap's latest version (|BS_version|).

Because BasicSwap is an entirely cross-chain DEX, there are basic requirements that a coin must possess to be readily integrated. 

**The blockchain...**

* Uses UTXO scripts
* Has CLTV or CSV
* Has Segwit enabled
* Works with watch-only addresses

Testing for Requirements
~~~~~~~~~~~~~~~~~~~~~~~~

In most cases, BasicSwap's requirements test script can help you quickly determine whether a coin can be readily integrated or not. 

If a coin does not pass the test or misses a few requirements, don't worry; it can probably still be integrated but may require the BasicSwap team to work on a custom integration framework. If that's your case, consider submitting a listing application request. 

.. rst-class:: bignums

        #. Install BasicSwap and ensure you are running the latest version (|BS_version|).
        #. Open the `basicswap` folder in a terminal.
        #. Navigate to where the test script is located.

               .. code-block:: bash

                      cd scripts
        #. Run the script by typing the following command while making sure to put the right destination folder for your coin's core.

               .. code-block:: bash

                      py requirements.python ~/Applications/particl/bin/particld -d

Integration Process
-------------------

If the coin you want to integrate meets all the requirements mentioned above, then there are good chances you will be able to add it to the DEX.

But remember, new coin integrations remain a case-by-case process that varies depending on what coin is being integrated.

With this in mind, you can check how other coins that may be similar to yours have been integrated into the DEX and derive your own process from these examples. Click on the numbers next to each coin's name to study their integration code.

 ===================================================================================================================================================================================================================================================================================================== =============== ================== ======= ====== ========= ======================= 
  Coin                                                                                                                                                                                                                                                                                                  UTXO Scripts    Bitcoin Version    CLTV    CSV    Segwit    Watch-only Addresses   
 ===================================================================================================================================================================================================================================================================================================== =============== ================== ======= ====== ========= ======================= 
  Bitcoin                                                                                                                                                                                                                                                                                               Yes             24.0               Yes     Yes    Yes       Yes                    
  Monero                                                                                                                                                                                                                                                                                                No              —                  —       —      —         —                      
  Litecoin                                                                                                                                                                                                                                                                                              Yes             0.21               Yes     Yes    Yes       Yes                    
  Dash (`1 <https://github.com/tecnovert/basicswap/commit/7298867e18efbaf1a6630769da651084ea8e954c>`_, `2 <https://github.com/tecnovert/basicswap/commit/4866ff4db89593472d21261ebbbb6a87e3f1f922>`_, `3 <https://github.com/tecnovert/basicswap/commit/aa14da27af33b5b02845d6c87e32b46e57d741a4>`_)    Yes             —                  Yes     Yes    No        Yes                    
  Firo (`1 <https://github.com/firoorg/firo>`_)                                                                                                                                                                                                                                                          Yes             —                  Yes     Yes    No        Yes                    
  PIVX (`1 <https://github.com/tecnovert/basicswap/commit/d74699992be727ea4bb6df0871da5983ef775566>`_)                                                                                                                                                                                                  Yes             —                  Yes     No     No        Yes                    
  Particl                                                                                                                                                                                                                                                                                               Yes             24.0               Yes     Yes    Yes       Yes                    
 ===================================================================================================================================================================================================================================================================================================== =============== ================== ======= ====== ========= ======================= 

Apply for a Listing
===================

Alternatively, you can send us a `listing application <https://basicswapdex.com/apply>`_. This is a great option if your coin does not meet most of the requirements or if you would rather focus your development resources elsewhere.

Please note, however, that on top of adding new coins, we are also constantly working on tackling our roadmap; improving and growing BasicSwap in the process. For this reason, we cannot guarantee a swift integration for all applicants. 

To submit a listing application for your coin, follow this link: https://BasicSwapDEX.com/apply

.. tip::

        To bump the priority of your application, consider pledging a donation to our open-source developers as part of your application.

----

.. seealso::

 - BasicSwap Explained - :doc:`BasicSwap Explained <../basicswap-dex/basicswap_explained>`
 - BasicSwap Guides - :doc:`Install BasicSwap <../basicswap-guides/basicswapguides_installation>`
 - BasicSwap Guides - :doc:`Update BasicSwap <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Route BasicSwap Through Tor <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Make an Offer <../basicswap-guides/basicswapguides_make>`
 - BasicSwap Guides - :doc:`Take an Offer <../basicswap-guides/basicswapguides_take>`
