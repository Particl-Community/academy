=======================
Markets and Storefronts
=======================

.. title::
   Particl Markets Explained

.. meta::
   :description lang=en: Learn more about deploying and owning online markets and shops on the Particl network. It's free, unrestricted, maintenance-free!

Particl's marketplace dApp is more than just a single large marketplace; it is a vast network of markets and storefronts created by other users. Each market can be deployed privately or shared publicly with the rest of the network.

This guide will explain in great detail everything you need to know about joining and creating markets on the Particl network.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

What is a "Particl market"?
---------------------------

.. note::

   To simplify the terminology, "markets" and "storefronts" may both be referred to as “markets”.

On Particl Marketplace, you can create your own markets and storefronts or join a wide variety of user-generated ones. 

The only difference between a market and a storefront is user permissions. On a market, anyone with access to it can buy or sell anything. On a storefront, only those with seller permissions can. 

User Permissions
****************

When it comes to market permissions, there are two key concepts to keep in mind: the access key and the publish key.

 * **Access Key —** Sometimes referred to as "access code", it lets you join a market or storefront.

 * **Publish Key —** Sometimes referred to as "seller code", it lets you sell items on a storefront.

When a market is created, anyone that joins it can buy and sell stuff on it. 

Storefronts, on the other hand, does not automatically grant seller permissions to everyone that joins. Instead, they require possession of a separate publish key. Only those with access to the storefront AND its seller code are allowed to sell. 

Data Encryption
***************

Market-specific data, like listing content and images, is encrypted and stored on the privacy-first :term:`SecureMessaging <SecureMessaging (SMSG)>` P2P network (SMSG). It is then relayed to other peers of the network without leaking the information to unauthorized parties.

To understand why, it must be understood that **a Particl market is, essentially, a combination of public and private keys**. 

When creating a market, a public key and private key (the access key/code) are generated. By default, the market and its content are encrypted, but possession of the market's private key (the access code) essentially decrypts its content and gives you access to it.

So while SMSG :term:`nodes <node>` may relay data from markets they do not have access to, it is impossible for them to determine the content of the data messages they're circulating. 

Market Browser
--------------

The Market Browser lets you explore and join markets that have been publicly shared by other users of the network. It also allows you to manually join markets using access and publish keys or create one of your own. 

If you see markets or storefronts that you deem undesirable, you can flag them for removal, just like with listings.

----

.. seealso::

 - Marketplace Guides - :doc:`Install and Get Started <../marketplace-guides/marketguides_installation>`
 - Marketplace Guides - :doc:`Sell Stuff <../marketplace-guides/marketguides_sell>`
 - Marketplace Guides - :doc:`Buy Stuff <../marketplace-guides/marketguides_buy>`
 - Unofficial Gateway - `Particl Store <https://particl.store/>`_
 - Unofficial Gateway - `Particl Marketplace Shop <http://particlmarketplace.shop/>`_
 - Marketplace Explained - :doc:`Content Moderation <../particl-marketplace/marketplace_escrow>`
 - Marketplace Explained - :doc:`Two Party Escrow System <../particl-marketplace/marketplace_escrow>`
 - Marketplace Explained - :doc:`Privacy Specifications <../particl-marketplace/marketplace_privacy>`