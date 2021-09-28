===========
Buy Process
===========

.. title::
   Particl Marketplace Buy Process

.. meta::
   :description lang=en: Learn how the buyflow works on Particl Marketplace from a customer perspective.

The buying process of :term:`Particl Marketplace` gives you more privacy, security, and censorship resistance than any other online marketplace and is entirely free to use except for the tiny sub-cent transaction fees usually associated with :term:`cryptocurrency <Cryptocurrency>` transactions. The price to pay for these previously impossible benefits is that you are required to do things a bit differently than what you are used to.

Rest assured, it's not complicated at all. Just follow this quick user guide and you'll be up to speed in no time!

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2
   

Request Order
=============

.. hint::
  
    **Wallet Unlocking**

    To be able to progress through the purchasing process, your :term:`Particl Desktop` client needs to be unlocked. Failure to do so means that you won't be able to complete the required steps to submit and complete your order. Make sure the padlock icon at the top-right corner of the status bar is unlocked.

To purchase an item on :term:`Particl Marketplace`, you need to first submit an order request to the seller. Keep in mind that, after you do this, you still need to complete one additional step before your order is properly confirmed, so keep reading this user guide until the end!

**Add an item to your cart**


.. rst-class:: bignums

	#. Open :guilabel:`Market` -> :guilabel:`BROWSE` to find the item you want to purchase and click on it to expand its details.
	#. Click on the :guilabel:`Shipping & Escrow` tab within the listing's details to make sure the item is shipping in your country and you have enough PART :guilabel:`Anon` balance funds. You will find the number of PART required for the order within the :guilabel:`Total needed for order` column.
	#. Click on :guilabel:`Add to cart`. 

**Submit order request to the seller**


.. rst-class:: bignums

	#. Open :guilabel:`Market` -> :guilabel:`CART` to review the content of your cart and enter your shipping information. 
	#. Click the :guilabel:`Review & Submit this Order` button to review your order's details and click the :guilabel:`Confirm Order & Submit` to send the bid to the seller.
	#. Your order request has been submited to the seller, who still has to confirm your order.

.. hint::
	Save your shipping information into a user profile. That way you do not need to rewrite it with every order. To do so, check the :guilabel:`Save shipping profile` box before moving to the next step and give the profile a name.

Make Security Deposit
======================

Once the seller has confirmed your order, its status will change from :guilabel:`REQUESTING` to :guilabel:`ACCEPTED`; it's time to make your security deposit into the :doc:`two-party escrow smart-contract <../in-depth/indepth_escrow>`. The security deposit of any order is always equal to the value of what's being purchased, including shipping costs.

.. rst-class:: bignums

	#. Await the notification that the seller has accepted your order. 
	#. Open :guilabel:`Market` -> :guilabel:`PURCHASES` -> :guilabel:`Orders` and look for any order marked as :guilabel:`ACCEPTED`.
	#. Click on the order's tile to expand its details and click on the :guilabel:`Request Escrow`.
	#. You can provide and email address or a phone number to help the seller. This step is optional. 
	#. Confirm your security deposit by clicking on the :guilabel:`Confirm & Fund`.

.. hint::
	In the :guilabel:`Filter` section, you can check :guilabel:`Orders requiring attention` to only see orders that require your attention or filter them by status.

.. seealso::
  Have a look at :doc:`Two-party Escrow Explained <../in-depth/indepth_escrow>` to know all about it!

Order Status Verification
=========================

After locking your security deposit into the two-party escrow contract, all you need to do is wait to receive your item. 

At any point in time, you can verify the status of your order. Once the seller marks your order as shipped, he may send you a tracking number.

.. rst-class:: bignums

	#. Open :guilabel:`Market` -> :guilabel:`PURCHASES` -> :guilabel:`Orders` and find the order you want to monitor. Additional information, like a tracking number or notes, can be seen by clicking on the order's tile which gives you access to more details.

Receive Security Deposit Back
=============================

After receiving your order, it's very important to finalize the transaction on Particl Marketplace. That's how you get back your security deposit, without any fee, and release the payment to the seller.

.. rst-class:: bignums

	#. Wait for your package to arrive.
	#. Open :guilabel:`Market` -> :guilabel:`PURCHASES` -> :guilabel:`Orders`.
	#. Click on the order's tile to expand its details and click on the :guilabel:`Mark as delivered` button to complete the transaction and receive your security deposit back instantly.

.. attention::
	
	It is very important to come back to :term:`Particl Desktop` once you receive your order and mark it as complete. Without it, you won't recover your security deposit.

.. hint::
	In the :guilabel:`Filter by status` section, you can check :guilabel:`SHIPPING` to only see orders that have been shipped by sellers but haven't arrived your way yet.

.. include:: ../faq/faq_mp_customers_overview.rst.txt