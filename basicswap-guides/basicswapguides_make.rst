===============
Create an Offer
===============

.. title::
   BasicSwap DEX Trading Guide
   
.. meta::
   :description lang=en: Learn how to trade safely and in privacy using BasicSwap DEX.
   :keywords lang=en: Particl, DEX, Trading, Exchange, Buy Crypto, Sell Crypto, Installation, Quickstart, Blockchain, Privacy, E-Commerce, multi-vendor marketplace, online marketplace

:term:`BasicSwap DEX <BasicSwap>` is a cross-chain and privacy-centric DEX (decentralized exchange) that lets you trade cryptocurrencies without middleman interference. 

One of its particularities is the presence of a distributed order book that lets you make or take offers without third-party involvement. 

This guide will walk you through the full process of making an offer and placing it on the books.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Create an Offer
===============

.. rst-class:: bignums

     #. In BasicSwap, click on the blue :guilabel:`New Offer` button.

     #. Enter the coin and amounts you want to send in :guilabel:`You Send`.

     #. Enter the coin and amounts you want to get in exchange in :guilabel:`You get`. 

         .. note::

             You can see the most recent rates by clicking on the :guilabel:`Check Current Rates` button at the bottom of the page.

     #. Select your offer preferences.

         * **Lock Rate**: Automatically adjusts the :guilabel:`You Get` value based on the rate you've entered. Without it, the rate value is automatically adjusted based on the number of coins you put in :guilabel:`You Get`.
         * **Amount Variable**: Allow bids with a different amount to the offer.
         * **Rate Variable**: Allow bids with a different rate to the offer.

     #. Click on the blue :guilabel:`Continue` button to progress to the next step.

Setup Offer Preferences
=======================

.. rst-class:: bignums

     #. Determine how long you want your coins to be listed on the order book by adjusting the :guilabel:`Offer valid (hrs)` value.

     #. Set the contract lock time by adjusting the :guilabel:`Contract Locked (Mins)` value. This is the timer that determines whether a swap has failed or not. When a swap fails for any reason, both participants are refunded their coins.

     #. Choose whether you want to auto-accept bids on your offer or not. :guilabel:`Accept All` will accept all bids automatically, while :guilabel:`Accept Known` will only accept bids from other traders you've swapped with in the past.

          .. attention::

               When you successfully complete a swap, your offer does not automatically disappear from the books. Keep that in mind when setting an offer as either :guilabel:`Accept All` or :guilabel:`Accept Known`.

     #. Click on the blue :guilabel:`Continue` button to progress to the next step.

Confirm the Offer
=================

.. rst-class:: bignums

     #. Review your order information and click on the blue :guilabel:`Confirm Offer` button if satisfied.

See my Active Offers
====================

.. rst-class:: bignums

     #. Review the current and previous orders you've placed on BasicSwap's order book by navigating to the :guilabel:`Your Offers` tab. 

Accept a Bid
============

If your offer is set to accept all bids automatically, you don’t need to do anything. Swaps will happen automatically whenever someone picks up your offer.

If you've set your offer to only accept bids from known peers or not automatically accept any offer at all, you need to look out for incoming bids and accept them.

.. rst-class:: bignums

     #. Navigate to the :guilabel:`Bids Received` tab. If you receive bids, they will show up here. 

     #. When you receive a bid, click on its :guilabel:`BID ID` to open its details.

     #. Review the bid's information and click on :guilabel:`Accept Bid` if you want to initiate the swap.

     #. The rest of the process is entirely automatic. Just wait a few minutes and the swap will complete. 

.. tip::

     You can follow a swap's progress from the :guilabel:`Events` section of its bid page. 

----

.. seealso::

 - BasicSwap Explained - :doc:`BasicSwap Explained <../basicswap-dex/basicswap_explained>`
 - BasicSwap Guides - :doc:`Install BasicSwap <../basicswap-guides/basicswapguides_installation>`
 - BasicSwap Guides - :doc:`Update BasicSwap <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Take an Offer <../basicswap-guides/basicswapguides_take>`
