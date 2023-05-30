===================
Using Trading Tools
===================

.. title::
   BasicSwap DEX Liquidity Tools Guide
   
.. meta::
   :description lang=en: Learn how to use the liquidity tools available for the BasicSwap DEX
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

The :guilabel:`createoffers.py` script lets you maintain your offer persistently up on the order book and dynamically manage its parameters.

Automatically Republish Offer and Adjust Prices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using :guilabel:`createoffers.py`, you can ensure that your offers stay persistently listed on the order book, with periodic price updates.

.. rst-class:: bignums

     #. Make sure your BasicSwap instance is up-to-date by closing it completely, running the following commands inside your :guilabel:`/docker` folder, and launching it back again.

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
		
		* :guilabel:`minrate`: The minimum rate under which the script should not accept an offer. This isn't the effective exchange rate, but rather the bare minimum you find tolerable. The script will not publish offers on the books below that value, effectively protecting you from unexpected and sudden liquidity spikes).
		
		* :guilabel:`ratetweakpercent`: How much percentage, below or above current market price (CoinGecko's API) you want to publish your orders on the book. By setting this as, for example, a value of guilabel:`5`, you're essentially listing offers at 5% above CoinGecko's stated market price. This lets you automate the publishing of profitable offers on the order book.
		
		* :guilabel:`amount_variable`: Either :guilabel:`True` or :guilabel:`False`, determines whether you want to allow people to take fractions of your offer (i.e., allow someone to swap 25 PART on your 100 PART offer, not just the full amount, by setting this to :guilabel:`True`).
		
		* :guilabel:`address`: Your swapping idendity/swap address. You can specify one, or leave as `-1` to generate a new random address everytime.
		
		* :guilabel:`name`: The name of your offer. Keep it as `offer 0`, `offer 1`, and so on.
		
		* :guilabel:`min_coin_from_amt`: The minimum number of coins a bid has to request for the script to automatically accept the offer. Keep in mind that each transaction costs on-chain transaction fees, so you may want to set that to a minimum that is at least higher than current on-chain fees.
		
		* :guilabel:`offer_valid_seconds`: The number of seconds your offer should stay up on the books, after which it will be republished, with a price update (if the script is still running by that time.) This can also be set globally rather than per order. For example, setting this as :guilabel:`3600` will make the script republish your offer every hour with a price update (current market price + :guilabel:`ratetweakpercent`).

		* :guilabel:`swap_type`: The script defaults to publishing offers using the more private :guilabel:`adaptor_sig` swap type, which requires the offering blockchain to contain a transaction malleability fix (i.e., Segwit). If that's not the case for your offer, you'll need to change this to * :guilabel:`secret_hash`. 

     	To save changes, press :kbd:`CTRL` + :kbd:`X`, then :kbd:`Y` + :kbd:`ENTER`.

     #. With BasicSwap running in the background, start the python script.

     	.. code-block:: bash

             python createoffers.py

        .. note::

		     The script needs to run continuously to be effective. Closing the terminal tab that runs it will shut it down. For this reason, we recommend executing the script using a background service system like `Byobu <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-byobu-for-terminal-management-on-ubuntu-16-04?>`_ or `screen <https://linuxize.com/post/how-to-use-linux-screen/>`_.