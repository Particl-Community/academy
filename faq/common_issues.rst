Common Issues
=============

.. note::

   The Particl Academy is up-to-date with Particl's latest version, |PD version|. 

   Got any issue not mentioned here? Then **let us know** about it so that we can help you out and update the Particl Academy!

General
-------

.. container:: toggle

    .. container:: header

        **Time offset warning icon (top right corner of Particl Desktop)**

    This warning simply means your computer is synced to a different time than the Particl network. Usually, this doesn't cause any noticeable issue, but when the offset gets too big, it can cause errors in the propagation of SMSG messages (listings, escrow, etc).

    .. tabs::
	 .. group-tab:: Windows

	 	#. Download timesync tool
	 	#. etc

	 .. group-tab:: Mac  

	 	#. ? 

	 .. group-tab:: Linux  

	 	#. ? 

.. container:: toggle

    .. container:: header

        **Coins not showing up when importing 24-word passphrase**

    - Make sure you are using |PD version|. 
    - Make sure you haven't made any **typo** in any of the 24 words.
    - Enter your seed's password, if you have any.
    - Try only entering your 24-word passphrase, **without** any password.
    - If all else fails, do a hard reset of Particl.

.. container:: toggle

    .. container:: header

        **Particl is indefinitely loading a wallet and not starting up**

    - Make sure you are using |PD version|. 
    - Close Particl Desktop and reopen it.

.. container:: toggle

    .. container:: header

        **Number of coins not showing up in private balances and transaction history**

    When you hold coins in either blind or anon balances, the balances aren't displayed on your Particl Desktop until you unlock it with your password. This is a security measure designed to keep your private balances private from prying eyes.

Marketplace
-----------

.. container:: toggle

    .. container:: header

        **I can't find the marketplace on Particl Desktop**

    - Make sure you are using |PD version|. 

.. container:: toggle

    .. container:: header

        **No listing is showing up on the marketplace (empty marketplace)**

    - Make sure you are using |PD version|. 
    - Leave Particl Desktop open for a few minutes so that it can sync the blockchain and load the market data. This can take several minutes and tends to take longer on slow internet connections.
    - Reset your market database by deleting your ``particl-market`` folder. Keep in mind this is a last resort solution. It will permanently remove all your market-related data as current orders, listings, order history, and etc. **Make sure that you do not have any active order before doing this step.**

    .. tabs::
	 .. group-tab:: Windows

	 		**Particl-market folder location**

	 	``%userprofile%\AppData\Roaming\particl-market``

	 .. group-tab:: Mac  

	 		**Particl-market folder location**

	 	``~/Library/Application Support/particl-market``

	 .. group-tab:: Linux  

	 		**Particl-market folder location**

	 	``~/.particl-market``

.. container:: toggle

    .. container:: header

        **I can't publish a listing**

    - Make sure you are using |PD version|. 
    - Make sure you have enough PART in your public balance to cover for the listing fees.


.. container:: toggle

    .. container:: header

        **"Message did not send" error when trying to list multiple items at once**

    - Scroll down to the bottom of the page and republish the listings that couldn't be sent in a SMSG message. You may need to repeat that step a few times until all items are published.

.. container:: toggle

    .. container:: header

        **The escrow process is jammed. Neither the buyer or seller can progress further**

    In rare occasions, the SMSG network can encounter message propagation issues. This can lead in issues such as the escrow not progressing further even when both transacting parties complete the escrow steps. To fix that issue, you can manually resend messages to the other party.

    .. tabs::
	 .. group-tab:: As the seller

	 	#. Find the order you want to fix in the ``Orders`` tab of the ``SELL`` page.
	 	#. Note down the order's ID.
	 	#. Open the Debug console window by clicking on its icon at the top right corner of your Particl Desktop client.
	 	#. Click on the ``Market`` tab and enter the following command by replacing ``<ID>`` by the order ID you've just noted down.
	 		``orderitem history <id>``
	 	#. This will give you a lot of data about the order. Copy everything and paste it into text document to better search for the data you need to continue further. 
	 	#. Note down the ``<msgid>`` values you need for the next step.
	 		- If your buyer has successfully locked its funds in escrow but you're not getting that notification and can't progress further, then you need to note down 2 ``msgid`` values: **MPA_COMPLETE** and **MPA_SHIP**.
	 		- If you've sent the item to your buyer but he hasn't received that notification and can't confirm that he has received the item, then you only need to note down the **MPA_SHIP** ``<msgid>`` value.
	 	#. Run the following command(s) in Particl Desktop's Debug window for each ``<msgid>`` value you've noted down (**MPA_COMPLETE** first, then **MPA_SHIP**).
	 		``smsg resent <msgid>``

	 .. group-tab:: As the buyer 

	 	#. Find the order you want to fix in the ``Orders`` tab of the ``PURCHASE`` page.
	 	#. Note down the order's ID.
	 	#. Open the Debug console window by clicking on its icon at the top right corner of your Particl Desktop client.
	 	#. Click on the ``Market`` tab and enter the following command by replacing ``<ID>`` by the order ID you've just noted down.
	 		``orderitem history <id>``
	 	#. This will give you a lot of data about the order. Copy everything and paste it into text document to better search for the data you need to continue further. 
	 	#. Note down the ``<msgid>`` values you need for the next step.
	 		- If you have successfully locked your funds (payment + security deposit) in escrow but the seller isn't getting that notification and can't progress further, then you need to note down the ``msgid`` value of **MPA_LOCK**.
	 		- If you've received the item but can't confirm the order as completed, then contact the seller and ask them to complete resend **MPA_SHIP** (instructions located in the *As the seller* tab of this page) value.
	 	#. Run the following command in Particl Desktop's Debug window by replacing ``<msgid>`` with the value of **MPA_LOCK**.
	 		``smsg resent <msgid>``
    
In-App Exchange
---------------

.. container:: toggle

    .. container:: header

        **I can't find any exchange to swap crypto for PART coins**

    - Make sure you are using |PD version|. 
    - TBD by new structure.

.. container:: toggle

    .. container:: header

        **Certain cryptocurrencies are not available to swap for PART coins**

    Not all cryptocurrencies are currently accepted on Particl. To request a coin to be added, fill up **this listing form**.