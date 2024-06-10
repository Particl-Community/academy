====================
Manage Enabled Coins
====================

.. title::
   BasicSwap DEX Coin Management Guide
   
.. meta::
   :description lang=en: Learn how to manage enabled coins on BasicSwap DEX.
   :keywords lang=en: Particl, DEX, Trading, Exchange, Buy Crypto, Sell Crypto, Installation, Quickstart, Blockchain, Privacy, E-Commerce, multi-vendor marketplace, online marketplace

:term:`BasicSwap DEX <BasicSwap>` is a non-custodian DEX (decentralized exchange), meaning that you remain in full control of your coins at every step.

This aspect of BasicSwap significantly improves your security and privacy, but it also means that you need to maintain a full node of every coin you've enabled.

This guide will walk you through everything you need to know about managing coins on BasicSwap.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

.. note::

      While BasicSwap currently requires that you run full coin nodes locally at this beta stage, we are working on solutions to allow for light services and alternative gateways (i.e., web and third-party integrations).

Enable Coins
============

Only Particl is enabled by default on BasicSwap. That's because the DEX leverages the :term:`SecureMessaging (SMSG)` network to function, which runs parallel to the Particl blockchain.

If you want to enable other coins such as Bitcoin, Litecoin, or even Monero, follow the steps detailed in the :doc:`Enable or Disable Coins guide <../basicswap-guides/basicswapguides_addremovecoins>`.

Monitor Sync Status
===================

When running a full BasicSwap node, you also host coin nodes (i.e., a Bitcoin node) locally on your device.

You can check the sync status of each coin node by following these steps.

.. rst-class:: bignums

    #. On BasicSwap, navigate to the Wallets section by clicking on the blue :guilabel:`Wallets` button.

    #. Each coin will display a progress bar that shows the sync progress.

    #. You can also verify that each node is connected to its respective network by ensuring that it is marked as :guilabel:`Updating` next to the coin's core version. 

Manage Wallets (Deposit/Withdraw)
=================================

You can manage various coin-related options directly from BasicSwap. Typically, most settings are made available on a per-coin basis (some coins have unique features that you'll find here), but that's also where you'll find the option to deposit and withdraw coins.

.. rst-class:: bignums

    #. On BasicSwap, navigate to the Wallets section by clicking on the blue :guilabel:`Wallets` button.

    #. Each coin has an associated :guilabel:`Manage` button. Click on it to open a coin's settings.

    #. In the coin's :guilabel:`Manage` page, you'll find various coin-specific options (i.e., balance conversion for PART) and the ability to deposit and withdraw coins.

.. note::

    Specifically for PIVX, Dash, and Firo, you may need to click on the :guilabel:`Reseed wallet` button **after the blockchain is fully synced** to enable deposits and withdrawals.

----

.. seealso::

 - BasicSwap Explained - :doc:`BasicSwap Explained <../basicswap-dex/basicswap_explained>`
 - BasicSwap Guides - :doc:`Install BasicSwap <../basicswap-guides/basicswapguides_installation>`
 - BasicSwap Guides - :doc:`Update BasicSwap <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Make an Offer <../basicswap-guides/basicswapguides_make>`
 - BasicSwap Guides - :doc:`Take an Offer <../basicswap-guides/basicswapguides_take>`
