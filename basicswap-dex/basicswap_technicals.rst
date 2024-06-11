==============
Under the Hood
==============
 
.. title::
     BasicSwap — Under the Hood

.. meta::
      
      :description lang=en: Dive deep into the underlying technology that enables BasicSwap DEX, the world's most secure and decentralized DEX. 
 
:term:`BasicSwap <BasicSwap>` is a cross-chain and highly secure :term:`DEX <DEX>` (decentralized exchange) that lets you trade cryptocurrencies without middleman interference using atomic swaps. Its distributed ledger technology enables users to place or accept swap offers without fees, promoting a free and open trading environment devoid of central points of failure.

:term:`BasicSwap <BasicSwap>` is crafted to uphold the highest standards of freedom in direct opposition to the growing threats to our sovereignty in the digital age. 

This page will break down, in detail, the key technical components that make BasicSwap the unique DEX that it is. Alternatively, you can familiarize yourself with BasicSwap's underlying technology and its considerations by consulting `this important definition page <https://basicswapdex.com/terms>`_.

----
 
.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2
 
----

Key Components
^^^^^^^^^^^^^^

:term:`BasicSwap <BasicSwap>` can be best understood as the decentralized version of the SWIFT messaging network; it sends and receives messages between two peers via the decentralized SMSG network for them to execute coin swaps together without any central party involvement. 

The coin swapping process itself is not conducted by :term:`BasicSwap <BasicSwap>`. Instead, it is handled by on-chain atomic swaps on the respective blockchains of the cryptocurrencies being exchanged. :term:`BasicSwap <BasicSwap>`'s role is to enable communication between swappers, allowing them to exchange the necessary information for atomic swaps and to publicly broadcast their offers without intermediaries.

Atomic Swaps
------------

:term:`BasicSwap <BasicSwap>` employs two distinct types of atomic swap protocols: HTLC ('Secret Hash') and PTLC ('Adaptor Signature'). These on-chain protocols facilitate the exchange of cryptocurrencies without the need for a trusted third party. HTLC uses hashed time-locked addresses, while PTLC utilizes adaptor signatures to execute swaps. 

Both protocols are open-source and have been developed by the broader cryptocurrency community, and are relatively narrow-scoped; they do not match orders between two users or provide any DEX framework. Instead, they just safely execute on-chain on the respective blockchains of the coins being exchanged, without third-party involvement.

.. seealso::

 - Atomic Swaps Explained - `Bitcoin Wiki <https://en.bitcoinwiki.org/wiki/Atomic_Swap>`_
 - Atomic Swap Protocol - `Decred-style <https://github.com/decred/atomicswap>`_
 - Atomic Swap Protocol - `Monero-style <https://eprint.iacr.org/2020/1126.pdf>`_     

Because of their narrow scope, atomic swap protocols need to be complemented by a decentralized messaging layer that relays imporant information and data between swappers to satisfy the conditions that enable swaps to securely take place. Without this messaging layer, it is impossible for a chain to move to the next steps of the process and know when to release swap transactions because it isn’t directly connected to the other blockchain it is interacting with.

In the case of :term:`BasicSwap <BasicSwap>`, that is where the decentralized :term:`SecureMessaging (SMSG)` network comes into play.

SecureMessaging (SMSG)
----------------------

:term:`BasicSwap <BasicSwap>` uses the open-source :term:`SecureMessaging (SMSG)` network, a decentralized and open-source data and messaging network (‘mixnet’) similar to BitMessage, to automate and simplify the process of exchanging swap data required for atomic swaps to take place between two peers. This network allows users to connect directly and share the necessary information securely, efficiently, and without intermediaries.

As such, all :term:`BasicSwap <BasicSwap>` users automatically operate as nodes within the :term:`SecureMessaging (SMSG)` network, making it entirely decentralized and autonomous. Messages, including swap data and network offers, are first end-to-end encrypted on the user’s local device, then broadcast through the network, and finally relayed and validated by all nodes to verify their authenticity against the network consensus and protect users' financial information against unauthorized access. 

This decentralized messaging network is essential in providing :term:`BasicSwap <BasicSwap>` with functionalities that atomic swaps alone cannot, such as its decentralized order book and the automation (from an end-user's perspective) of the intricate steps involved in executing a successful on-chain atomic swap.

As such, :term:`BasicSwap <BasicSwap>` functions similarly to a decentralized version of SWIFT, providing a messaging protocol that allows for peers to connect directly with each other with the purpose of executing atomic swaps without central points of failure using official coin cores (Bitcoin Core, Litecoin Core). 

:term:`BasicSwap <BasicSwap>` does not process, initiate, or execute swaps; it merely enables peers to communicate with each other and exchange the required information to simplify the process of using atomic swaps on the respective blockchains of the coins being swapped. In essence, :term:`BasicSwap <BasicSwap>` operates merely as a decentralized messaging protocol.

.. seealso::
 
 - Particl Wiki - `SecureMessaging P2P Network <https://particl.wiki/learn/marketplace/smsg/>`_


Adaptor Signatures
------------------

Whereas typical DEX platforms use either regular :term:`smart contracts <smart contract>` or HTLC atomic swaps, some cryptocurrencies like Bitcoin or Monero are not compatible with them. :term:`BasicSwap <BasicSwap>` uses adaptor signatures in these scenarios. 

Adaptor signatures are an off-chain form of smart contract that provide the flexibility needed to execute atomic swaps with non-programmable cryptocurrencies like Monero. They also provide more privacy than traditional HTLC atomic swaps by not inscribing an identical hash at a similar time on both participating blockchains of a swap.

.. seealso::
 
 - Whitepaper - `OtVES Signatures <https://raw.githubusercontent.com/LLFourn/one-time-VES/master/main.pdf>`_

----

.. seealso::

 - Blog Post - `BasicSwap The Fully Private Cross Chain DEX <https://particl.news/basicswap-the-fully-private-cross-chain-dex/>`_ 
 - Github - `BasicSwap <https://github.com/basicswap/basicswap>`_
 - BasicSwap Explained - :doc:`BasicSwap Explained <../basicswap-dex/basicswap_explained>`
 - BasicSwap Explained - :doc:`DEX Comparison <../basicswap-dex/basicswap_compared>`
