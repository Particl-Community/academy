==============
Under the Hood
==============
 
.. title::
     BasicSwap — Under the Hood

.. meta::
      
      :description lang=en: Discover the technology that powers the BasicSwap decentralized DEX. Unrestricted crypto trading in complete privacy. 
 
:term:`BasicSwap <BasicSwap>` is a cross-chain and privacy-centric :term:`DEX <DEX>` (decentralized exchange) that lets you trade cryptocurrencies without middleman interference. 

Its user-friendly interface allows users to easily benefit from its groundbreaking benefits, but what makes them possible in the first place is rather complex and intricate. 

This page will break down, in detail, the key technical components that live under the hood and make BasicSwap the unique DEX that it is.

----
 
.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2
 
----

Similarly to the Particl Marketplace, :term:`BasicSwap <BasicSwap>` relies on an intricate combination of distributed technologies developed, maintained, and run by a vast and global network of participants.

Key Components
^^^^^^^^^^^^^^

Three key technologies make BasicSwap the powerhouse that it is: the SecureMessaging (SMSG) protocol, scriptless scripts technology, and the more widely-known ‘atomic swaps’ protocol.
 
Atomic Swaps
------------

Atomic swaps have been around for quite some time and are an important part of many DEX platforms currently available. They allow for swapping digital assets between two users in a peer-to-peer fashion, assuming that the logistical requirements behind executing such a swap exist.

The atomic swap technology is, in and of itself, a relatively narrow-scoped protocol; it does not match orders between two users or provide any DEX framework. Instead, it just safely swaps assets and does so very securely.

.. seealso::

 - Atomic Swaps Explained - `Bitcoin Wiki <https://en.bitcoinwiki.org/wiki/Atomic_Swap>`_
 - Atomic Swap Protocol - `Decred-style <https://github.com/decred/atomicswap>`_
 - Atomic Swap Protocol - `Monero-style <https://eprint.iacr.org/2020/1126.pdf>`_     

That’s why it needs to be complemented by a common and decentralized channel in which the information related to a swap is transferred between two parties — often across two entirely different chains. Without this added layer, it is impossible for a chain to know when to release the swap in question because it isn’t directly connected to the other blockchain.

In the case of BasicSwap and the wider Particl ecosystem, that is where the distributed :term:`SecureMessaging (SMSG)` network comes into play.

SecureMessaging (SMSG)
----------------------

SecureMessaging (SMSG) is Particl’s own custom-built and unique P2P messaging network that stands at the very core of its ecosystem. Inspired by the BitMessage protocol, the SMSG network is a mixnet that acts as a decentralized storage network (DSN). It stores and transfers data across :term:`nodes <node>` in a privacy-preserving manner, encrypted from end to end (E2EE), and without requiring the use of any central server.

This decentralized technology is essential in providing the BasicSwap DEX with functionality that atomic swaps alone cannot, such as an order book and order matching system, transferring swap data between two different blockchains, etc.

When running a BasicSwap client, you are also automatically running an SMSG node along with it. 
DEX and swap-related data are transferred between users through the SMSG network. BasicSwap nodes then receive this data and let other users interact with it using scriptless scripts. This creates an all-in-one DEX that works entirely without third-parties and in total privacy. 

.. seealso::
 
 - Particl Wiki - `SecureMessaging P2P Network <https://particl.wiki/learn/marketplace/smsg/>`_


Scriptless Scripts
------------------

Whereas typical DEX platforms use traditional :term:`smart contracts <smart contract>`, some cryptocurrencies like Monero are not compatible with them. BasicSwap uses scriptless scripts in these scenarios. 
Scriptless scripts are an off-chain form of smart contract that provides more privacy and scalability than their on-chain counterparts. On BasicSwap, they are used to safely spend Monero coin outputs collaboratively and without third-party involvement.

Indeed, when swapping assets on BasicSwap, the participants' coins are sent to a scriptless chain and into an address created from the sum of their private keys. 

The only way to spend that output requires participants to cooperate through One-Time Verifiably Encrypted Signatures (OtVES). OtVES allows for the safe and trustless exchange of digital signatures without requiring a trusted party to serve as an adjucator. The one-time property of OTVES ensures both participants can get the decryption key they need to process through the process of swapping their coins.

.. seealso::
 
 - Whitepaper - `OtVES Signatures <https://raw.githubusercontent.com/LLFourn/one-time-VES/master/main.pdf>`_

 
Other Notable Protocols
^^^^^^^^^^^^^^^^^^^^^^^

Tor Network
-----------

The Tor network is a free and open-source network that enables anonymous online communication. It protects your digital privacy by anonymizing your IP address. It does so by routing your connection through a vast and global network of volunteers. Tor’s intended use is to protect your personal privacy as well as your freedom and ability to conduct confidential communication. 

When enabled on BasicSwap, it makes your node’s IP address entirely anonymous and makes it impossible for an outside party to determine that you’re even using the DEX.

.. note::

 - BasicSwap Guides - :doc:`Enable Tor <../basicswap-guides/basicswapguides_installation>`

Taproot Forward Compatibility
-----------------------------

Taproot is a new protocol improvement enabled on Particl that adds the ability to script more advanced logic and condition-based requirements into Bitcoin-style scripts, allowing for more advanced smart contracts to happen on the Particl Blockchain.

When combined with scriptless scripts and the SMSG network, it makes possible complex privacy-first dApps (i.e., BasicSwap) that carry a much lesser degree of risk compared to complex turing-complete smart contracts.

Additionally, Taproot’s off-chain nature, as well as its ability to aggregate multiple signatures, keys, and scripts significantly improves the level of privacy of the blockchain’s smart contracts and dApps by transforming complex condition-based transactions into standard-looking transactions. This preserves the fungibility and financial information of coins transferred through Particl smart contracts and dApps.

At the time of this writing, Taproot isn’t yet added to BasicSwap but is expected to make its way onto it at some point during the open beta as the DEX is forward-compatible with it. This will make swaps on BasicSwap indistinguishable from standard blockchain transactions, significantly improving the privacy of its users.

----

.. seealso::

 - Blog Post - `BasicSwap The Fully Private Cross Chain DEX <https://particl.news/basicswap-the-fully-private-cross-chain-dex/>`_ 
 - Github - `BasicSwap <https://github.com/tecnovert/basicswap>`_
 - BasicSwap Explained - :doc:`BasicSwap Explained <../basicswap-dex/basicswap_explained>`
 - BasicSwap Explained - :doc:`DEX Comparison <../basicswap-dex/basicswap_compared>`
 - BasicSwap Guides - :doc:`How to Use <../basicswap-guides/basicswapguides_usage>` 