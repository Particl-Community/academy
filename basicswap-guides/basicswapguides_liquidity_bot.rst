==============================
Automated Market Making Script
==============================

.. title::
   BasicSwap DEX Liquidity Tools Guide
   
.. meta::
   :description lang=en: Learn how to use the automated market making tool available for the BasicSwap DEX
   :keywords lang=en: Particl, DEX, Trading, Exchange, Buy Crypto, Sell Crypto, Installation, Quickstart, Blockchain, liquidity, Privacy, E-Commerce, multi-vendor marketplace, online marketplace

You can use a variety of tools to help you provide liquidity and manage positions more easily on :term:`BasicSwap DEX <BasicSwap>`. This guide walks you through all the instructions to make full use of them.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

.. attention::

     Certain liquidity tools may link to external services, potentially diminishing your privacy depending on their usage. As a result, they are presently provided as optional companion scripts requiring independent operation. 

     Aspects of these tools that don't establish connections with third-parties are anticipated to be incorporated into the central BasicSwap protocol in the future.

Offer Management
================

By default, :term:`BasicSwap` allows offers to be published on the order book for a maximum of 48 hours. This is due to the nature of the :term:`SecureMessaging` (SMSG) networking protocol used to propagate offers on the network.

The :guilabel:`createoffers.py` script enables you to keep your offers consistently on the order book, while also dynamically managing their parameters.

Automatically Republish Offer and Adjust Prices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using :guilabel:`createoffers.py`, you can ensure that your offers stay persistently listed on the order book, with periodic price updates.

.. rst-class:: bignums

     #. Navigate to your /docker folder and make sure that your BasicSwap instance is :doc:`up-to-date <../basicswap-guides/basicswapguides_installation>`.

     	.. code-block:: bash

             git pull
             docker-compose build

     #. Navigate to your :guilabel:`/scripts` folder.

     #. Enable the script's configuration file by renaming it :guilabel:`createoffers.json`.

     	.. code-block:: bash

             cp template_createoffers.json createoffers.json

     #. Open the :guilabel:`createoffers.json` file in a text editor.

     	.. code-block:: bash

             nano createoffers.json

     #. Edit the file and set the correct parameters by modifying the following values to your preferences.

        	* :guilabel:`coin_from`: The coin you want to send. 
		
		* :guilabel:`coin_to`: The coin you want to receive in exchange of your :guilabel:`coin_from`.
		
		* :guilabel:`amount`: The number of :guilabel:`coin_from` coins you want to offer on the books.
		
		* :guilabel:`minrate`: This refers to the lowest acceptable rate under which the script should not consider an offer. Note that this isn't the effective exchange rate, but merely the absolute minimum rate you deem acceptable. The script will refrain from publishing offers on the books that fall below this value, thereby offering protection against sudden and unexpected liquidity spikes.
		
		* :guilabel:`ratetweakpercent`: This parameter specifies the percentage above or below the current market price (as reported by CoinGecko's API) at which you want to list your orders. For instance, if you set this to a value of 5, your offers will be listed at 5% above the market reported price. This feature automates the process of listing profitable offers on the order book.
		
		* :guilabel:`amount_variable`: Either :guilabel:`True` or :guilabel:`False`, determines whether you permit your offer to be partially fulfilled. For example, if you enable this option (set it to :guilabel:`True`), someone could fulfill just 25 PART of your 100 PART offer instead of the entire amount.
		
		* :guilabel:`address`: This refers to your swap identity or swap address. You have the option to specify one (this would be a Particl address from your BasicSwap Particl wallet), or if you prefer, you can set this to -1, which will prompt the system to generate a new random address each time your offer is updated.
		
		* :guilabel:`name`: The name of your offer. Keep it as `offer 0`, `offer 1`, and so on.
		
		* :guilabel:`min_coin_from_amt`: This refers to the smallest amount of coins a bid must request for the script to automatically accept the offer. Remember that each transaction incurs on-chain transaction fees. Thus, it may be beneficial to set this value higher than the current on-chain fees.
		
		* :guilabel:`offer_valid_seconds`: This parameter determines the duration (in seconds) for which your offer will remain on the books. After this time has elapsed, your offer will be re-published with a price adjustment, provided the script is still in operation. For instance, setting it to :guilabel:`3600` will prompt the script to re-publish your offer every hour with a revised price (current market price + :guilabel:`ratetweakpercent`). This parameter can be set universally instead of on a per-order basis.

		* :guilabel:`swap_type`: The script defaults to publishing offers using the more private :guilabel:`adaptor_sig` swap type, which requires the offering blockchain to contain a transaction malleability fix (i.e., Segwit). If that's not the case for your offer, you'll need to change this to :guilabel:`secret_hash`. 

     	To save changes, press :kbd:`CTRL` + :kbd:`X`, then :kbd:`Y` + :kbd:`ENTER`.

     #. With BasicSwap running in the background, start the python script.

     	.. code-block:: bash

             python createoffers.py

        .. note::

		     The script needs to run continuously to take effect. Closing the terminal tab that runs it will terminate it. For this reason, we recommend executing the script using `Byobu <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-byobu-for-terminal-management-on-ubuntu-16-04?>`_ or `screen <https://linuxize.com/post/how-to-use-linux-screen/>`_.
