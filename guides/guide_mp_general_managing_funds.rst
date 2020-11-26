==============
Manage Funds
==============

In this section, you will learn how to manage your funds with Particl Desktop in preparation for buying and selling goods and services on Particl Marketplace.

.. meta::
   :description lang=en: Learn how to manage your funds with Particl Desktop.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

.. note::

	There are three different types of coin balances on Particl. Each of them serves a different function within the platform and carries their own level of transactional privacy.

	Learn about those different types with the :doc:`PART Cryptocurrency in-depth guide <../in-depth/indepth_part_coin>`

Needed Funds
============



PART funds needed for selling
-----------------------------

To sell products and services on Particl Marketplace, you'll need to have coins in both your :guilabel:`Public` balance and in your :guilabel:`Anon` balance.

PART funds needed for buying
----------------------------

To buy products and services on Particl Marketplace, you'll only need to have coins in your :guilabel:`Anon` balance. It is, however, quite useful to also have some coins in your :guilabel:`Public` balance as that will allow you to take part in the moderation process of the marketplace by flagging undesirable items. It'll also let you earn a bit of passive and dividend-like income through Particl's staking process.

Receive Coins 
==============

There are multiple ways you can fund your balance with PART coins.

From another PART address
-------------------------

You can receive PART coins coming from any wallet holding PART funds. This can be a personal wallet, a public exchange service provider, or a hardware wallet. 

.. rst-class:: bignums

	#. Navigate to the :guilabel:`Wallet` module of Particl Desktop by clicking on it from the outer menu at the very left of the client.
	#. Navigate to the :guilabel:`Receive` page.
	#. Choose if you want to receive :guilabel:`Public` or :guilabel:`Private` funds by clicking on the right tab on the page. Both the sender and receiver must agree on that (exchanges, for example, only support public transactions).
		- Optionally, create a :guilabel:`New address` below the :guilabel:`QR code` image.
		- Optionally, type a label into the :guilabel:`Label` field to identify this address with a specific purpose. 
	#. Click on the :guilabel:`Copy address` button to copy your address into your clipboard. 
	#. Send this address to another party so that they can send you PART coins or send some yourself from another Particl wallet.
	
.. tip::

	When posting the address from the clipboard to another party, **always** very and double-check the pasted address with the original. Make sure it is identical. **Remember:** *You are your own bank*.

From the in-app exchange module
-------------------------------

.. note::
   
   Particl's in-app swap engine is temporarily unavaible. We are working to get it back up as soon as possible!

The in-app exchange module allows you to obtain PART funds without the need to visit an external exchange. At a later stage this will be used as onramp and offramp for many different currencies including national currencies like the US Dollar or the Euro.

.. note::

	**Prerequisite:** Enable the desired exchange bot.

	#. Navigate to the :guilabel:`Bot Management` module.
	#. Choose an exchange and enable its bot by expanding its tile and then clicking on the :guilabel:`Enable bot` button.

.. rst-class:: bignums

	#. Navigate to the :guilabel:`Swap` module of Particl Desktop by clicking on it from the outer menu at the very left of the client the top left corner of the client.
	#. Click on the :guilabel:`Start new Exchange` button. 
	#. Type in the number of PART coins you want to receive in your public balance.
	#. Select the cryptocurrency you want to swap for PART coins, and then click on the :guilabel:`Next` button.
	#. Review the quote offered by the exchange, and then click on the :guilabel:`Next` button.
	#. Send your coins to the address provided and wait for the transaction to be completed. This can take several minutes depending on the exchange and the currency you trade for.

Convert Balances
================

Converting balances is needed if you want to switch and/or convert between the different PART privacy states mentioned in :doc:`PART Cryptocurrency in-depth guide <../in-depth/indepth_part_coin>`.

.. rst-class:: bignums

	#. Navigate to the :guilabel:`Wallet` module of Particl Desktop by clicking on it from the outer menu at the very left of the client.
	#. Navigate to the :guilabel:`Send / Convert` page of the wallet menu on the left of your Particl Desktop client.
	#. Click on the :guilabel:`Convert Public <-> Private` tab.
	#. In the :guilabel:`Pay From` section, select **the source** of funds you would like to convert.
	#. In the :guilabel:`Convert To` section, select **the destination** of funds you would like to recieve.
	#. Type in the number of coins you want to send to your other balance and click on the :guilabel:`Make payment` button.
		- Unlock your wallet when prompted to.
	#. Review the transaction details and click on the :guilabel:`Confirm & Send` button to confirm the transaction.
	#. Wait for twelve (12) confirmations (approximately 24 minutes) before the funds in the anon balance can be used without restriction.
		- You can track the status of this transaction in the :guilabel:`Overview` module under :guilabel:`Recent Transactions`
