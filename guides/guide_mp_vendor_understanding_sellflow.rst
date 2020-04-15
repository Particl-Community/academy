Selling Process
====================

The selling process of Particl's marketplace differs from traditional markets due to its decentralized nature. It grants you more privacy, security, censorship resistance, as well as costs you much lower fees. The price to pay to get these benefits is that you are required to do things a bit differently than what you are used to.

Rest assured, it's not complicated at all. Just follow this quick user guide and you'll be up to speed in no time!

The entire process of selling a product, from A to Z, can be seen in this walkthrough tutorial video.

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="390" src="https://www.youtube.com/embed/IC9yY3MThoo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2


Publish Items
------------------

.. attention::

   To put an item for sale on Particl, you need to have PART coins in your ``Public`` balance so that you can pay for the listing fees. You also need to have PART coins in your ``Anon`` balance so that you can make a security deposit (which is equal to the value of any item purchased by a buyer).

To make a sale on Particl, you need to first put your items up for sale. There are many ways to create listings on Particl and the right way for you to create listings depends on your requirements.

Publish a Single Item
~~~~~~~~~~~~~~~~~~~~~

If you want to only list a single item, then simply follow these steps.

Navigate to the right location
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Listings`` tab, and then on the ``Add new listing`` button.

Preparation for publishing
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Fill up all the text boxes with the information on your listing and upload a (or multiple) pictures of your product or service.
#. Review all of the information and when ready to publish your listing, click on the ``Save and Publish`` button.

Publishing a listing later
^^^^^^^^^^^^^^^^^^^^^^^^^^

After entering all the information, you can click on the ``Save`` button to save your listing information and publish it later instead of right now.

#. To publish a listing after it's been saved, navigate to the ``Listings`` tab of the ``SELL`` page.
#. Locate your saved listing (it will be marked as ``UNPUBLISHED``).
#. Click on its tile, and either edit it by clicking on the ``Edit listing`` button, or publish it by clicking the ``Publish`` button.
#. You can also delete the template if you do not have any use for it anymore by clicking on the red X icon (``Delete listing``).

Final publication
^^^^^^^^^^^^^^^^^
#. Unlock your wallet when prompted to.
#. Set the expiry time (the number of days your listings will be available) in the dropdown menu and click on ``Confirm & Publish``.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listing will be live on the Particl marketplace.

Publish Multiple Items at Once (CSV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are selling multiple items, then you may want to create a CSV inventory file and list all of your products at once. To do so, follow these simple steps.

Navigate to the right location
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Listings`` tab, and then on the ``Import listings`` button.

No CSV inventory file yet?
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Click on ``Download example CSV`` in the ``IMPORT SETTINGS`` section.
#. Save the CSV template on your computer.
#. Open it with a spreadsheet editor (i.e. Excel, LibreOffice, etc).
#. Add as many products as you want following the template's model.

Preparation for publishing
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In the ``SELECT IMPORT SOURCE`` section, select ``CSV file``.
#. Click on the ``CSV file to import`` line and import your CSV inventory file.
#. Click on the ``Load`` button to upload the file.
#. Review your import data and edit any listing, as needed, by first clicking on its tile and then by clicking on the ``Edit listing`` icon.
#. Click on the ``Continue`` button.
#. Set your shipping and expiration parameters, and then click on the ``Continue`` button.

Final publication
^^^^^^^^^^^^^^^^^
#. Unlock your wallet when prompted to.
#. Review the quoted fees and click on the ``Publish imported listings`` button. Careful, this is the final step, and you will be charged listing fees when clicking on that button.
#. Unlock your wallet when prompted to.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listings will be live on the Particl marketplace.

Import WooCommerce Inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are already selling online, more specifically on WooCommerce, then you can simply export your products into a Particl compatible CSV inventory file by following `this WooCommerce tutorial <https://docs.woocommerce.com/document/product-csv-importer-exporter/>`_. Once that is done, you can then easily import the CSV inventory file on Particl by following the simple steps that follow.

Navigate to the right location
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Listings`` tab, and then on the ``Import listings`` button.

Preparation for publishing
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   Until automatic fiat rates are supported on Particl, it is required to convert the quoted prices of your WooCommerce products into PART prices. If you want to sell your products for USD and the USD/PART price is $5, then simply type ``5``. Keep in mind these prices do not adjust automatically, which means you'll have to edit that line every time you re-publish your products.

#. In the ``SELECT IMPORT SOURCE`` section, select ``WooCommerce``.
#. Click on the ``Woocommerce export file`` line and import your WooCommerce CSV inventory file.
#. In the ``Fiat per PART rate`` line, enter the current PART price.
#. Click on the ``Load`` button to upload the file.
#. Review your import data and edit any listing, as needed, by first clicking on its tile and then by clicking on the ``Edit listing`` icon.
#. Click on the ``Continue`` button.
#. Set your shipping and expiration parameters, and then click on the ``Continue`` button.

Final publication
^^^^^^^^^^^^^^^^^
#. Unlock your wallet when prompted to.
#. Review the quoted fees and click on the ``Publish imported listings`` button. Careful, this is the final step, and you will be charged listing fees when clicking on that button.
#. Unlock your wallet when prompted to.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listings will be live on the Particl marketplace.s

Accept a Bid
---------------

.. attention::

	**For your Particl Desktop client to receive any bid from buyers, it needs to be unlocked**. New orders won't show up in your ``Orders`` page until you unlock your wallet using your password. To do so, simply click on the green lock icon at the top right corner of your client.

To initiate a marketplace transaction, you must first accept a bid on one of your listings. Accepting a bid indicates to your buyer that you are accepting his order. The buyer will then be required to lock the total payment amount (cost of the item + shipping) as well as his security deposit into a two-party escrow contract.

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. In the ``FILTER`` section, you can check  ``Orders requiring attention`` to only see orders that requires your attention or filter them by status.
#. Look for any new order marked as ``BIDDING``.
#. Click on the order's tile to expand its details and accept it by clicking on the ``Accept bid`` button.

Make the Security Deposit
---------------------------

.. note::

   Want to learn more about Particl's two-party deposit contract system and how it effectively keeps both parties safe without requiring any intermediary? Then just visit the :doc:Particl two-party escrow contract page <guides/guide_general_particl_balances>. to know all about it!

Once your buyer locks his funds into the two-party escrow, you will be prompted to also lock a security deposit equal to the value of your buyer's security deposit.

The two-party escrow contract ensures that neither you or the buyer can misbehave or act dishonestly. This is done by requiring both parties to "put skin in the game" by way of **security deposits that can only be refunded once both parties authorize the release of the funds**. The escrow contract is entirely autonomous, private by design, and doesn't require any intermediary such as an arbitrer or a support staff.

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. In the ``FILTER`` section, you can check  ``Orders requiring attention`` to only see orders that requires your attention or filter them by status.
#. Look for any order marked as ``ESCROW PENDING``.
#. Click on the order's tile to expand its details and make your security deposit by clicking on the ``Complete escrow`` button.

Package and Shipping an Order
-------------------------------

After making your security deposit into the two-party escrow contract, you will need to package and ship the order to your buyer.

#. Package and ship out your item. 
#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. In the ``FILTER`` section, you can check  ``Orders requiring attention`` to only see orders that requires your attention or filter them by status.
#. Look for any order marked as ``PACKAGING``.
#. Click on the order's tile to expand its details and click on the ``Mark as shipped`` button.
#. You can optionally enter a tracking number or note for your buyer, or can leave that space blank if not needed. 
#. Click on the ``Order shipped`` button to confirm that you have shipped the item. 

Receive and Verifying Payment
-------------------------------

Once your package is shipped, keep an eye out for your payment. Once your buyer receives its item and marks the transaction has complete, you will receive your security deposit back as well as the full payment for the order, at no fee.

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab.
#. In the ``FILTER BY STATUS`` section, you can check  ``Complete`` to only see orders that have been completed.
#. Click on the order's tile to expand its details and see the date and time it was completed.
#. Navigate to the ``HISTORY`` page and click on the `Received` tab.
#. Find the transaction based on the date and time at which point the order was completed to verify that you've succesfully received your payment.

Publish a Listing Again After it Expires
----------------------------------------

Re-publishing a listing after it expires requires you to go through the listing process once again. Simply follow these steps. 

Publish a Single Item
~~~~~~~~~~~~~~~~~~~~~

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Listings`` tab.
#. Find the listing you want to re-publish in the list of previously published listings. It should be marked as ```EXPIRED``.
#. Click its tile to expand it, and click on the ``Clone listing`` icon to clone it. This will bring you to its publishing page. 
#. Update its information and price, if needed, and click on the ``Save & Publish`` button.
#. Unlock your wallet when prompted to.
#. Set the expiry time (the number of days your listings will be available) in the dropdown menu and click on ``Confirm & Publish``.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listing will be live on the Particl marketplace.

Publish a WooCommerce or .CSV Inventory File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to publish a WooCommerce or .CSV inventory file again, simply go through the publishing process once again. 


Get a Sales Report for Tax Purposes
---------------------------------------

Due to the current stage of development of the Particl marketplace (Beta), an integrated tax reporting system isn't included yet but is planned to be added at a later time during the Beta phase of development. You can, however, manually inspect your transaction and order history at any point in time to get the data you need to report your taxes.

#. Navigate to the ``SELL`` page of the market menu on the left of your Particl Desktop client.
#. Click on the ``Orders`` tab
#. Find the orders you need and click on their tiles to get more details and data.
#. In the ``FILTER BY STATUS`` section, you can check  ``Complete`` to only see orders that have been completed.
#. Click on any order's tile to expand its details and see the date and time it was completed as well as the received PART payment for it.	
#. To calculate the payment of an order in your national currency, take note of the number of PART you've received as well as the date and time the order was completed. 
#. On a website that keeps track of PART's historical price data, get the proper national currency valuation of your payment at the time you've received it. CoinMarketCap is a good website where you can find that information, just `click on this link <https://coinmarketcap.com/currencies/particl/historical-data/>`_ to be taken directly to the historical data page for the PART coin.

Functionalities that will make tax reporting, order and transaction data exporting, and national currency calculations will be added at a later time during the Beta phase of development. To know what next features are planned for the marketplace, refer to `Particl's development roadmap <https://particl.io/roadmap>`_.

