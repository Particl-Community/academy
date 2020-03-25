Selling Process
====================

The selling process of Particl's marketplace differs from traditional markets due to its decentralized nature. It grants you more privacy, security, censorship resistance, as well as costs you much lower fees. The price to pay to get these benefits is that you are required to do things a bit differently than what you are used to.

The entire process of selling a process, from A to Z, can be seen on this walkthrough tutorial video.

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="390" src="https://www.youtube.com/embed/sUodtqG8DUs" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Managing Your Balances
----------------------

.. note::

   There is much more to learn about Particl balances, their functions, as well as their levels of privacy. Head to the **:doc:Particl balances page <guides/guide_general_particl_balances>** right away to know all about it!

There are three different types of coin balances on Particl. Each of them serves a different function within the platform and carries their own level of transactional privacy.

To sell products and services on Particl, you'll need to have coins in both your ``Public`` balance and in your ``Anon`` balance.

Receiving Coins in a Public Balance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to the ``RECEIVE`` page of the wallet menu on the left of your Particl Desktop client.
#. Click on the ``Copy address`` button to copy your public address in your clipboard.
#. Send it to another party so that they can send your PART coins or send some yourself from another Particl wallet.

.. tip::
   
   You can also receive PART coins on your public balance by exchanging Bitcoin and other currencies right from the Particl Desktop client?

   #. Navigate to the ``BOT MANAGEMENT`` page of the wallet menu on the left of your Particl Desktop client.
   #. Choose an exchange and enable its bot by expanding its tile and then clicking on the ``Enable bot`` button.
   #. Navigate to the ``EXCHANGE`` page of the wallet menu on the left of your Particl Desktop client.
   #. Click on the ``Start new Exchange`` button. 
   #. Type in the number of PART coins you want to receive in your public balance.
   #. Select the cryptocurrency you want to swap for PART coins, and then click on the ``Next`` button.
   #. Review the quote offered by the exchange, and then click on the ``Next`` button.
   #. Send your coins to the address provided and wait for the transaction to be completed. This can take several minutes depending on the exchange.

Converting Public Balances to Anon 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to the ``SEND / CONVERT`` page of the wallet menu on the left of your Particl Desktop client.
#. Click on the ``Convert Public <-> Private`` tab.
#. In the ``PAY FROM`` section, select ``Public``.
#. In the ``CONVERT TO`` section, select ``Anon``.
#. Type in the number of coins you want to send to your anon balance and click on the ``Make payment`` button.
#. Unlock your wallet when prompted to.
#. Review the transaction details and click on the ``Confirm & Send`` button to confirm the transaction.
#. Wait for twelve (12) confirmations (approximately 24 minutes) before the funds in the anon balance can be used.

Publishing Items
------------------

.. attention::

   To put an item for sale, you need to have PART coins in your public balance to pay for the listing fees and you need the an anon balance at the same size of the item being sold and shipped.

Publishing a Single Item
~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the right location
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Listings`` tab, and then on the ``Add new listing`` button.

Preparation for publishing
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Fill up all the text boxes with the information on your listing and upload a (or multiple) pictures of your product or service.
#. Review all of the information and when ready to publish your listing, click on the ``Save and Publish`` button.

.. tip::
	**Publish later**

	Alternatively, you can click on the ``Save`` button to save your listing information and publish it later.

	- To publish your listing later, you will have to navigate to the ``listing`` tab of the ``sell`` page.
	- Locate your saved listing (it will be marked as ``UNPUBLISHED``).
	- Click on its tile, and either edit it by clicking on the ``Edit listing`` button, or publish it by clicking the ``Publish`` button.
	- You can also delete the template if you do not have any use for it anymore by clicking on the red X icon (``Delete listing``).

Final Publication
^^^^^^^^^^^^^^^^^
#. Unlock your wallet when prompted to.
#. Set the expiry time (the number of days your listings will be available) in the dropdown menu and click on ``Confirm & Publish``.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listing will be live on the Particl marketplace.

Importing WooCommerce Inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attention::

	To import your WooCommerce products on Particl's marketplace, you need to first export your WooCommerce inventory on a compatible .csv file following `this tutorial <https://docs.woocommerce.com/document/product-csv-importer-exporter/>`_.

Navigate to the right location
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Listings`` tab, and then on the ``Import listings`` button.

Preparation for publishing
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In the ``SELECT IMPORT SOURCE`` section, select ``WooCommerce``.
#. Click on the ``Woocommerce export file`` line and import your WooCommerce CSV inventory file.
#. In the ``Fiat per PART rate`` line, enter the current PART price.

.. note::
   **Why is this needed?**

   Until automatic fiat rates are supported on Particl, this step is required to convert the quoted prices of your WooCommerce products into PART prices. If you want to sell your products for USD and the USD/PART price is $5, then simply type ``5``. Keep in mind these prices are not currently dynamic, which means you'll have to edit that line every time you re-publish your products.

#. Click on the ``Load`` button to upload the file.
#. Review your import data and edit any listing, as needed, by first clicking on its tile and then by clicking on the ``Edit listing`` icon.

.. note::

	If there is an error in your WooCommerce CSV inventory file or if any information is missing, the client will notify you about it before publishing. You can also opt to not publish certain listings by unchecking their ``Publish`` checkboxes.

#. Click on the ``Continue`` button.
#. Set your shipping and expiration parameters, and then click on the ``Continue`` button.

Final Publication
^^^^^^^^^^^^^^^^^
#. Unlock your wallet when prompted to.
#. Review the quoted fees and click on the ``Publish imported listings`` button. Careful, this is the final step, and you will be charged listing fees when clicking on that button.
#. Unlock your wallet when prompted to.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listings will be live on the Particl marketplace.s

Importing CSV Inventory File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the right location
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Listings`` tab, and then on the ``Import listings`` button.

Preparation for publishing
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In the ``SELECT IMPORT SOURCE`` section, select ``CSV file``.
#. Click on the ``CSV file to import`` line and import your CSV inventory file.

.. note::
	**No CSV file yet?**

   - Click on ``Download example CSV`` in the ``IMPORT SETTINGS`` section.
   - Save the CSV template on your computer.
   - Open it with a spreadsheet editor (i.e. Excel, LibreOffice, etc).
   - Add as many products as you want following the template's model.

#. Click on the ``Load`` button to upload the file.
#. Review your import data and edit any listing, as needed, by first clicking on its tile and then by clicking on the ``Edit listing`` icon.

.. note::

	If there is an error in your CSV inventory file or if any information is missing, the client will notify you about it before publishing. You can also opt to not publish certain listings by unchecking their ``Publish`` checkboxes.

#. Click on the ``Continue`` button.
#. Set your shipping and expiration parameters, and then click on the ``Continue`` button.

Final Publication
^^^^^^^^^^^^^^^^^
#. Unlock your wallet when prompted to.
#. Review the quoted fees and click on the ``Publish imported listings`` button. Careful, this is the final step, and you will be charged listing fees when clicking on that button.
#. Unlock your wallet when prompted to.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listings will be live on the Particl marketplace.

Accepting a Bid
---------------

.. attention::

	For your Particl Desktop client to receive bids from buyers, it needs to be unlocked. New orders won't show up in your ``Orders`` page until you unlock your wallet using your password. To do so, simply click on the green lock icon at the top right corner of your client.

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. In the ``FILTER`` section, you can check  ``Orders requiring attention`` to only see orders that requires your attention or filter them by status.
#. Look for any new order marked as ``BIDDING``.
#. Click on the order's tile to expand its details and accept it by clicking on the ``Accept bid`` button.

Making a Security Deposit
---------------------------

.. note::

   Want to learn more about Particl's novel dual deposit escrow system and how it keeps both parties safe without the use of any third-party? Just follow this link and get to know it all!

After accepting a bid, Particl will prompt your buyer to lock both the payment for the item and a security deposit equal to the same value of the item and the shipping costs into a two-party escrow system. Once that is done, your Particl Desktop client will also prompt you to lock a security deposit of the same value into the escrow system.

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. In the ``FILTER`` section, you can check  ``Orders requiring attention`` to only see orders that requires your attention or filter them by status.
#. Look for any order marked as ``ESCROW PENDING``.
#. Click on the order's tile to expand its details and make your security deposit by clicking on the ``Complete escrow`` button.

Packaging and Shipping an Order
-------------------------------

After making your security deposit into the escrow smart-contract, you will need to package and ship the order to your buyer.

#. Package and ship out your item. 
#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. In the ``FILTER`` section, you can check  ``Orders requiring attention`` to only see orders that requires your attention or filter them by status.
#. Look for any order marked as ``PACKAGING``.
#. Click on the order's tile to expand its details and click on the ``Mark as shipped`` button.
#. You can optionally enter a tracking number or note for your buyer, or can leave that space blank if not needed. 
#. Click on the ``Order shipped`` button to confirm that you have shipped the item. 

Receiving and Verifying Payment
-------------------------------

Once your package is shipped, keep an eye out for your payment. Once the buyer receives the item and confirms the transaction has been completed satisfactorily, he will mark the transaction as complete. This will send you back, at no fee, your security deposit as well as the full payment for the order.

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. In the ``FILTER`` section, you can check  ``Complete`` in the ``FILTER BY STATUS`` section to only see orders that have been completed.
#. Click on the order's tile to expand its details and see the date and time it was completed.
#. Navigate to the ``HISTORY`` page and click on the `Received` tab.
#. Find the transaction based on the date and time at which point the order was completed to verify that you've succesfully received your payment.

Getting a Sales Report for Tax Purposes
---------------------------------------

Due to the current stage of development of the Particl marketplace (Beta), an integrated tax reporting system isn't included yet but is planned to be added at a later time during the Beta phase of development. You can, however, manually inspect your transaction and order history at any point in time to get the data you need to report your taxes.

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. Find the orders you need and click on their tiles to get more details and data.
#. In the ``FILTER`` section, you can check  ``Complete`` in the ``FILTER BY STATUS`` section to only see orders that have been completed.
#. Click on any order's tile to expand its details and see the date and time it was completed as well as the received PART payment for it.	
#. To calculate the payment of an order in your national currency, take note of the number of PART you've received as well as the date and time the order was completed. 
#. On a website that keeps track of PART's historical price data, get the proper national currency valuation of your payment at the time you've received it. CoinMarketCap is a good website where you can find that information, just **[click on this link](https://coinmarketcap.com/currencies/particl/historical-data/)** to be taken directly to the historical data page for the PART coin.

Functionalities that will make tax reporting, order and transaction data exporting, and national currency calculations will be added at a later time during the Beta phase of development. To know what next features are planned for the marketplace, refer to **[Particl's development roadmap](https://particl.io/roadmap)**.