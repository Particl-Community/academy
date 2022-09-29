======================
Privacy Specifications
======================

|PM| takes security and privacy very seriously. Its protocol and application are built from the ground up in a way that never creates any useful data about you, your identity, or your assets. When no data exists, it cannot be collected, analyzed, shared, or leaked.

This page dives into some of the critical components of the marketplace and details how they’re designed to preserve your privacy by default.

.. title::
   Particl Marketplace Explained

.. meta::
   :description lang=en: Learn more about Particl’s decentralized online marketplace and its privacy-first approach.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Marketplace Content
~~~~~~~~~~~~~~~~~~~

When you upload content like images online, it often contains sensitive data about you - data like where the picture was taken (geo-location) or what device was used to take the picture. This is a big privacy issue that can lead to catastrophic data leaks, such as unwillingly revealing the GPS location of your home or work environment.

To protect you from this, Particl Marketplace encrypts and strips every image of its metadata before broadcasting it to the rest of the network. This makes it impossible for anyone to collect any useful information about user-uploaded images.

Two-Party Online Escrow System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually, when a transaction goes wrong and needs to be resolved by a third-party, marketplaces and payment processors act as the deciding factor by issuing a resolution. They have the final say in who should get the money when a conflict arises. They can also ban users, force refunds, etc.

This puts your data and your online privacy at risk because, while a third-party can protect you from scammers, it also gains full access to all of your information.

To offer the same kind of protection without impeding your online privacy, Particl uses a two-party escrow system that uses autonomous blockchain :term:`smart contracts <Smart Contract>` and anonymous :term:`cryptocurrency` transactions. No entity other than the one you're transacting with can gain access to your information. No digital footprint is generated.

Secure Messaging
~~~~~~~~~~~~~~~~

On traditional marketplaces, all your communications with buyers and sellers are stored, monitored, and analyzed by the marketplace itself. This, as you might expect, exposes a great deal of information about you and your business activities. It opens the door wide open for anyone, authorized or not, to collect that information and use it for a variety of reasons, some entirely detrimental to you, such as copying your successful products. 

Particl makes sure to put that issue to rest by relying on a completely :term:`decentralized <Decentralization>` messaging network: :term:`SecureMessaging (SMSG)`. It encrypts, end-to-end, all the messages you send to other users and automatically delivers them to the intended recipient. Only the people you're sending a message to can open and read it. It cannot be intercepted and decrypted by anyone else.

Private Transactions
~~~~~~~~~~~~~~~~~~~~

Sending payments online is usually anything but private. You typically require the use of a payment processor (i.e., Paypal), a bank, or a financial institution. In all cases, it exposes the full details of your transactions and financial data not only to these providers, but also to their partners and other affiliated entities.

That’s why Particl Marketplace forces all transactions between a buyer and a seller to be anonymous by default. Using Anon transactions, the information of the transaction’s participants and the transferred amount are never made public and are encrypted by default. This unique Particl feature ensures that all marketplace trades are anonymous by default without the user requiring to take extra precautions.

Network Connection
~~~~~~~~~~~~~~~~~~

To further hide one’s usage of Particl Marketplace, it is possible and, in many cases, recommended, to route its connection through the Tor network. 
The Tor network is a free and open-source network that enables anonymous online communication. It protects your digital privacy by anonymizing your IP address. It does so by routing your connection through a vast and global network of volunteers. Tor’s intended use is to protect your personal privacy as well as your freedom and ability to conduct confidential communication. 
When enabled on Particl, it makes your :term:`node <node>`’s IP address entirely anonymous and makes it impossible for an outside party to determine that you’re even using Particl.

----

.. seealso::

 - Marketplace Explained - :doc:`Particl Marketplace Explained <../particl-marketplace/marketplace_explained>`
 - Particl Explained - :doc:`Privacy Specifications <../particl-blockchain/blockchain_privacy>`