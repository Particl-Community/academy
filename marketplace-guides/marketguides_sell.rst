===========
How to Sell
===========

.. title::
     Particl Marketplace - How to Sell

.. meta::
      
      :description lang=en: Learn everything there is to know about selling stuff on Particl’s online decentralized marketplace. It’s free, private, and unrestricted. 

Selling products and services on :term:`Particl Marketplace` gives you more privacy, security, and freedom than on any other online marketplace. It is also entirely free to use, except for a tiny sub-cent :term:`cryptocurrency <Cryptocurrency>` transaction fee, as well as a small anti-spam fee that is then redistributed to the network.

All these benefits are available through Particl Marketplace. And due to its unique decentralized architecture, the process of selling may be slightly different than what you’re used to. 

As we’ll see in this user guide, this process isn’t complicated at all. Simply read through it, and you’ll be up to full speed in no time!

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Publish Listings
----------------

.. attention::

   To list an item for sale on Particl Marketplace, you need to have PART coins in your :guilabel:`Public` (default) or :guilabel:`Anon` balance so that you can pay for listing fees. Funds in your :guilabel:`Anon` balance are also required to make security deposits into the two-party escrow smart contract.

The first step of selling on Particl is to first put an item up for sale on one of the available markets. There are many ways to create listings on Particl. The right way for you depends on your requirements.

----

.. container:: toggle

    .. container:: header

        **Publish a Single Item**

    Publish a Single Item
    ~~~~~~~~~~~~~~~~~~~~~

    If you only want to list a single item, then simply follow these steps.

    Create a listing template
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Inventory & Products` followed by the :guilabel:`New` button.
      #. Fill up all the text boxes with your listing information and upload one or more images of the product or service you intend to sell.

    If you want to publish now
    ^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. rst-class:: bignums

      #. Click on :guilabel:`Publish right away` tile to select on which market you want to publish your listing and set the correct category for your item.
      #. Click on the :guilabel:`Save and Publish` button and choose the duration time of your listing.
      #. Click on :guilabel:`Publish Listing`.

    .. hint::
      After one (1) blockchain confirmation (approximately 2 minutes), your listing will be live on the desired market(s).

    If you want to publish it later
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Instead of publishing your listing immediately, you can save its template for later. When creating your listing, instead of clicking on :guilabel:`Save and Publish`, you can click on the :guilabel:`Save` button to save your listing template for later.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Inventory & Products`, locate your saved listing, and click on its tile to expand its details. Its status will show as :guilabel:`Listing unpublished`.
      #. You can still edit the listing by clicking on the  :guilabel:`Edit` button or publish it by clicking the :guilabel:`Publish` icon (rocket).
      #. You can publish your listing in additional markets and storefronts by clicking on the green :guilabel:`Clone Product to Market` button and selecting which market (and category) you want to add your listing template to. 
      #. Choose the amount of time you want your listing to show up on the additional market and click on :guilabel:`Publish Listing`.

    .. hint::
      After one (1) blockchain confirmation (approximately 2 minutes), your listing will be live on the desired market(s).

    If you want to publish on multiple markets
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    You can also publish your listing on multiple markets and storefronts. This option is only available if you already possess publishing permissions on one or more markets.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Inventory & Products`, locate the listing you want to publish on multiple markets and click on its tile to expand its details.
      #. Click on the green :guilabel:`Clone Product to Market` button and select which market (and category) you want to publish your listing in. 
      #. Choose the amount of time you want your listing to show up on the market and click on :guilabel:`Publish Listing`.

    .. hint::
      After one (1) blockchain confirmation (approximately 2 minutes), your listing will be live on the desired market(s).

.. container:: toggle

    .. container:: header

        **Publish Multiple Items at Once**

    If you are selling multiple items, then you may want to create a CSV inventory file and list all of your products at once. This will save you valuable time as you won’t be required to manually list each item one by one. 

    Publishing multiple listings at once is separated into two steps: (1) creating listing templates and (2) publishing them.

    Create listing templates
    ^^^^^^^^^^^^^^^^^^^^^^^^

    The first step of the process is to import your inventory into :term:`Particl Desktop` using a CSV file and create a listing template for each item.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Inventory & Products`, followed by a click on the :guilabel:`Import` button.
      #. To process your inventory, import your CSV file by clicking on the :guilabel:`Choose file` button of the :guilabel:`IMPORT FROM CSV FILE` section and click on the :guilabel:`Process CSV import` button.
      #. One listing template per item will be created. Review each template and, if needed, click on their tiles to expand and edit their information.
      #. Click :guilabel:`Import & Save` to create your listing templates.

    .. tip::

     You can download a :file:`.csv` template file from the :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Inventory & Products` -> :guilabel:`Import` section after selecting :guilabel:`CSV file` as source. Follow the formatting of the template.


    Publish your listing templates
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The second step of the process is to publish the listing templates you've just created.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Inventory & Products` followed by a click on the :guilabel:`Batch (Re)publish...` button.
      #. Click :guilabel:`PUBLISH TO` to select in which markets you want to publish your listings.
      #. Click :guilabel:`PUBLISH DURATION` to select for how long you want your listings to be available.
      #. Click their :guilabel:`Publish` checkboxes or hit :guilabel:`Select all` in the :guilabel:`SELECT...` dropdown menu to individually choose the items you want to publish.  
      #. Click on :guilabel:`Publish selected products` and wait for :term:`Particl Desktop` to publish your listings. A progress bar at the bottom of the screen indicates the progress.

.. Import WooCommerce Inventory
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  If you are already selling online, more specifically on WooCommerce, then you can simply export your products into a Particl compatible CSV inventory file by following `this WooCommerce tutorial <https://docs.woocommerce.com/document/product-csv-importer-exporter/>`_. Once that is done, you can then easily import the CSV inventory file on Particl by following the simple steps that follow.

  Navigate to the right location
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. rst-class:: bignums

    #. Navigate to the :guilabel:`SELL` page of the market menu on the left of your :term:`Particl Desktop` client.
    #. Click on the :guilabel:`Listings` tab, and then on the :guilabel:`Import listings` button.

  Preparation for publishing
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    Until automatic fiat rates are supported on Particl, it is required to convert the quoted prices of your WooCommerce products into PART prices. If you want to sell your products for USD and the USD/PART price is $5, then simply type ``5``. Keep in mind these prices do not adjust automatically, which means you'll have to edit that line every time you re-publish your products.

  .. rst-class:: bignums

  #. In the :guilabel:`SELECT IMPORT SOURCE` section, select :guilabel:`WooCommerce`.
  #. Click on the :guilabel:`Woocommerce export file` line and import your WooCommerce CSV inventory file.
  #. In the :guilabel:`Fiat per PART rate` line, enter the current PART price.
  #. Click on the :guilabel:`Load` button to upload the file.
  #. Review your import data and edit any listing, as needed, by first clicking on its tile and then by clicking on the :guilabel:`Edit listing` icon.
  #. Click on the :guilabel:`Continue` button.
  #. Set your shipping and expiration parameters, and then click on the :guilabel:`Continue` button.

  Final publication
  ^^^^^^^^^^^^^^^^^

  .. rst-class:: bignums

  #. Unlock your wallet when prompted to.
  #. Review the quoted fees and click on the :guilabel:`Publish imported listings` button. Careful, this is the final step, and you will be charged listing fees when clicking on that button.
  #. Unlock your wallet when prompted to.
  #. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listings will be live on the :term:`Particl Marketplace'.

----

Sell and Process Orders
-----------------------

.. attention::

    For your :term:`Particl Desktop` client to receive any bid from buyers, it must be online and unlocked. New orders won't show up in your :guilabel:`Orders` or :guilabel:`Overview` until you unlock your wallet. To do so, click on the padlock icon in the status icons bar at the top right corner.

.. container:: toggle

    .. container:: header

        **Accept an Order**

    When a buyer wants to buy something you're selling, they'll first make an order request that you need to accept. Accepting an order indicates to your buyer that you are willing to process his order.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Orders` and check the :guilabel:`Orders requiring attention` checkbox to only see orders that require your attention or filter them by status.
      #. Look for any new order marked as :guilabel:`REQUESTING`.
      #. Click on the order's tile to expand its details and accept it by clicking on the :guilabel:`Accept order request` button.

.. container:: toggle

    .. container:: header

        **Make the Security Deposit**

    Once you accept your buyer's order, they will be required to send their payment as well as a security deposit into a :doc:`two-party escrow smart contract <../in-depth/indepth_escrow>`. After they do so, you will also be required to match that security deposit.

    .. seealso::
      Check out the :doc:`Two-party Escrow Explained <../in-depth/indepth_escrow>` page to know more about it!

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Orders` and check :guilabel:`Orders requiring attention` to only see orders that require your attention or filter them by status.
      #. Look for any order marked as :guilabel:`ESCROW`. Click on the order's tile to expand its details and make your security deposit by clicking on the :guilabel:`Complete escrow` button.
      #. In the window that appears, you can leave your buyer a note. This is optional. Confirm your security deposit by clicking on the :guilabel:`Confirm & Fund`.

.. container:: toggle

    .. container:: header

        **Package and Ship an Order**

    After making your security deposit into the two-party online escrow system, you now need to process, package, and ship your customer's order.

    .. rst-class:: bignums

      #. Package and ship out your item. 
      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Orders` and check :guilabel:`Orders requiring attention` to only see orders that require your attention or filter them by status.
      #. Look for any order marked as :guilabel:`PACKAGING`, click on the tile to expand its details, and click on the :guilabel:`Mark as shipped` button.
      #. In the window that appears, you can send your buyer a tracking number. This is optional and can be used to send other information as well (i.e., a download link). Confirm the order as shipped by clicking on :guilabel:`Yes, order is shipped`.

.. container:: toggle

    .. container:: header

        **Receive Payment**

    Once your package is shipped, keep an eye out for your payment. Once your buyer receives their order and marks the transaction as complete, you will receive your security deposit back as well as the full payment for the order at no fee.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`SELL` -> :guilabel:`Orders` and check :guilabel:`Orders requiring attention` to only see orders that require your attention or filter them by status.
      #. Check :guilabel:`COMPLETED` to only see orders that have been completed. Click on the order's tile to expand its details and see the date and time it was completed.

----

.. seealso::

 - FAQ - :doc:`Selling on Particl <../faq/faq_mp_general_overview>`
 - Marketplace Guides - :doc:`Install and Get Started <../marketplace-guides/marketguides_installation>`
 - Marketplace Guides - :doc:`Buy Stuff <../marketplace-guides/marketguides_buy>`
 - Github - `Particl Desktop <https://github.com/particl/particl-desktop>`_
 - Github - `Particl Core <https://github.com/particl/particl-core>`_
 - Unofficial Gateway - `Particl Store <https://particl.store/>`_
 - Unofficial Gateway - `Particl Marketplace Shop <http://particlmarketplace.shop/>`_
 - Particl Explained - :doc:`Two Party Escrow System <../particl-marketplace/marketplace_escrow>`