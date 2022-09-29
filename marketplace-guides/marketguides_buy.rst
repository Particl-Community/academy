==========
How to Buy
==========

.. title::
   Particl Marketplace - How to Buy

.. meta::
   :description lang=en: Learn everything there is to know about buying stuff on Particl’s online decentralized marketplace. It’s free, private, and unrestricted. 

Buying products and services on :term:`Particl Marketplace` gives you more privacy, security, and freedom than on any other online marketplace. It is also entirely free to use, except for tiny sub-cent :term:`cryptocurrency <Cryptocurrency>` transaction fees. 

All these benefits are available through Particl Marketplace. And due to its unique decentralized architecture, the process of shopping online may be slightly different than what you’re used to. 

As we’ll see in this user guide, this process isn’t complicated at all - you’ll be up to speed in no time!

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Purchase an Item
----------------

.. attention::

   To purchase an item on Particl Marketplace, you need to have PART coins in your :guilabel:`Public` (default) or :guilabel:`Anon` balance.

.. container:: toggle

    .. container:: header

        **Place an Order**

    .. attention::
      
        **Wallet Unlocking**

        To be able to progress through the steps of the purchasing process, your :term:`Particl Desktop` client needs to be unlocked. Failure to do so means that you won't be able to complete the required steps to submit and complete your order. Make sure the padlock icon at the top-right corner of the status bar is unlocked.

    To purchase an item on :term:`Particl Marketplace`, you must first submit an order request to the seller. Keep in mind that, after you do this, you will still need to complete one additional step before your order is properly confirmed!

    **Add an item to your cart**


    .. rst-class:: bignums

        #. Open :guilabel:`Market` -> :guilabel:`BROWSE` to find the item you want to purchase and click on it to expand its details.
        #. Click on the :guilabel:`Shipping & Escrow` tab within the listing's details to ensure the item ships to your country and that you have enough PART in your :guilabel:`Anon` balance. You will find the total number of PART required to send the order request within the :guilabel:`Total needed for order` column.
        #. Click on :guilabel:`Add to cart`. 

    **Submit order request to the seller**


    .. rst-class:: bignums

        #. Open :guilabel:`Market` -> :guilabel:`CART` to review the content of your cart and enter your shipping information. 
        #. Click the :guilabel:`Review & Submit this Order` button to review your order's details, and click the :guilabel:`Confirm Order & Submit` to send the bid to the seller.
        #. Your order request has been submitted to the seller. Now we wait for his confirmation.

    .. hint::
        Save your shipping information into a user profile. That way, you do not need to rewrite it with every order. To do so, check the :guilabel:`Save shipping profile` box before moving to the next step and give the profile a name.

.. container:: toggle

    .. container:: header

        **Make Security Deposit**

    Once the seller has confirmed your order, its status will change from :guilabel:`REQUESTING` to :guilabel:`ACCEPTED`; it's time to make your security deposit into the :doc:`two-party escrow smart contract <../in-depth/indepth_escrow>`.

    .. rst-class:: bignums

        #. Await the notification that the seller has accepted your order. 
        #. Open :guilabel:`Market` -> :guilabel:`PURCHASES` -> :guilabel:`Orders` and look for any order marked as :guilabel:`ACCEPTED`.
        #. Click on the order's tile to expand its details and click on :guilabel:`Request Escrow`.
        #. You can provide an email address or a phone number to help the seller and shipping provider. This step is optional. 
        #. Confirm your security deposit by clicking on the :guilabel:`Confirm & Fund`.

    .. hint::
        In the :guilabel:`Filter` section, you can check :guilabel:`Orders requiring attention` to only see orders that require your attention or filter them by status.

    .. seealso::
      Check out the :doc:`Two-party Escrow Explained <../in-depth/indepth_escrow>` page to know more about it!

.. container:: toggle

    .. container:: header

        **Verify Order Status**

    After locking your security deposit into the two-party escrow contract, you now need to wait for your package to arrive, after which you’ll be required to mark the transaction as complete to receive your security deposit back.

    Once the seller marks your order as shipped, he may send you a tracking number through the private Chat function of your specific order.

    .. rst-class:: bignums

        #. Open :guilabel:`Market` -> :guilabel:`PURCHASES` -> :guilabel:`Orders` and find the order you want to monitor. Additional information, like a tracking number or notes, can be seen by clicking on the order's tile.

.. container:: toggle

    .. container:: header

        **Finalize Order and Get Security Deposit Back**

    After receiving your order, it's crucial to finalize the transaction on Particl Marketplace. That is how you get back your security deposit, and release the payment to the seller.

    .. rst-class:: bignums

        #. Wait for your package to arrive.
        #. Open :guilabel:`Market` -> :guilabel:`PURCHASES` -> :guilabel:`Orders`.
        #. Click on the order's tile to expand its details, and click on the :guilabel:`Mark as delivered` button to complete the transaction and receive your security deposit back instantly.

    .. attention::
        
        It is crucial to return to :term:`Particl Desktop` once you receive your order and mark it as complete. Without it, you won't recover your security deposit.

    .. hint::
        In the :guilabel:`Filter by status` section, you can check :guilabel:`SHIPPING` to only see orders that have been shipped by sellers but haven't arrived your way yet.

Contact a Seller
----------------

.. container:: toggle

    .. container:: header

        **Resolve Order Issues**

    If you encounter an issue during your order or want to contact your seller, you can use the marketplace's dedicated messaging system. Messages are sent through the :term:`SecureMessaging <SecureMessaging (SMSG)>` P2P network (SMSG). All direct messages are end-to-end encrypted and anonymous by default. 

    .. rst-class:: bignums
 
            #. Open :guilabel:`Market` -> :guilabel:`PURCHASES` -> :guilabel:`Orders` and find the order you have an issue with. 
            #. Open up the order's chat function and send a message to the seller.

.. container:: toggle

    .. container:: header

        **Ask a Question Before Buying**

    Each listing has a public chat section where you can leave questions for the seller to respond to. Questions and answers published in the chat section of listings are public and visible to everyone else.

    .. attention::
        
        Do not include any personal information in the public chat of a listing. What you write here is visible to everyone on the network.

    .. rst-class:: bignums
 
            #. Open :guilabel:`Market` -> :guilabel:`BROWSE` and click on the listing you have a question about to open up its modal. 
            #. Click on the :guilabel:`CHAT` tab to open up the listing's public chat section.
            #. Accept Particl Desktop's warning message — **do NOT** type any sensitive information in the public chat.
            #. Type your question and click :guilabel:`Send` button.

----

.. seealso::

 - FAQ - :doc:`Buying on Particl <../faq/faq_mp_general_overview>`
 - Marketplace Guides - :doc:`Install and Get Started <../marketplace-guides/marketguides_installation>`
 - Marketplace Guides - :doc:`Sell Stuff <../marketplace-guides/marketguides_sell>`
 - Github - `Particl Desktop <https://github.com/particl/particl-desktop>`_
 - Github - `Particl Core <https://github.com/particl/particl-core>`_
 - Unofficial Gateway - `Particl Store <https://particl.store/>`_
 - Unofficial Gateway - `Particl Marketplace Shop <http://particlmarketplace.shop/>`_
 - Particl Explained - :doc:`Two Party Escrow System <../particl-marketplace/marketplace_escrow>`