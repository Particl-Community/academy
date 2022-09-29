======================
Privacy Specifications
======================

.. title::
   PART Coin Privacy Specs

.. meta::
      
      :description lang=en: Learn more about Particl’s modern and flexible privacy coin PART.

PART is a solid privacy coin with a high level of flexibility and :term:`smart contract <smart contract>` interactivity. It doesn’t just allow you to transact person-to-person with anyone else; it also lets you do it completely anonymously, preserving the privacy of your financial data from the rest of the world. 

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 3

----

Transactional Privacy
*********************

PART has an adjustable level of privacy and lets you choose between three different types of transactions (public, blind, and anon), each with its own purpose, cost, and level of anonymity.

+----------------------------------+---------------------------------------------+
| **Adjustable Level of Privacy**  | Yes, 3 levels                               |
+----------------------------------+---------------------------------------------+
| **Privacy Protocols**            | Confidential Transactions (CT) and RingCT   |
+----------------------------------+---------------------------------------------+
| **Bulletproofs**                 | Enabled                                     |
+----------------------------------+---------------------------------------------+
| **Stealth Addresses**            | Yes                                         |
+----------------------------------+---------------------------------------------+
| **Ring Signatures**              | Yes                                         |
+----------------------------------+---------------------------------------------+
| **Taproot**                      | Yes                                         |
+----------------------------------+---------------------------------------------+

PART has three different types of transactions, each with its own use cases, cost, level of privacy, type of balance, and settings. All three types are available on :term:`Particl Desktop` where you can easily convert your coins from one kind of balance to another.

----

Public transactions
===================

+-----------+------------------------------+-----------------------+---------------------+
| **Cost**  | **Participants Information** | **Amount Transacted** | **Type of Balance** |                                   
+-----------+------------------------------+-----------------------+---------------------+
| Very low  | Public                       | Public                | Public              |                                   
+-----------+------------------------------+-----------------------+---------------------+

Public transactions let you make Bitcoin-like pseudonymous blockchain transactions. These transactions are the most affordable ones to make and the simplest to integrate into other platforms. For this reason, they are the most widely supported type of transaction by exchanges and third-party services.

Additionally, public transactions can only be sent to public balances, which is also the only type of balance that can stake. Visit the :doc:`Staking Guide <../part-guides/partguides_staking>` for more information on this topic.

Use Cases
^^^^^^^^^

- Send and receive pseudonymous payments on a public blockchain;
- Earn PART coins in dividend-like payments via staking;
- Pay for listing fees on the marketplace;
- Promote user markets and storefronts on the Market Browser;
- Moderate the :term:`Particl Marketplace`;
- Use smart contracts;
- Trade on :term:`BasicSwap <BasicSwap>` DEX;
- Vote on community proposals (DAO).

----

Blind transactions
==================

+-----------+------------------------------+-----------------------+-------------------------+
| **Cost**  | **Participants Information** | **Amount Transacted** | **Type of Balance**     |                                   
+-----------+------------------------------+-----------------------+-------------------------+
| Low       | Public                       | Hidden                | Blind (private address) |                                   
+-----------+------------------------------+-----------------------+-------------------------+

Confidential Transactions
^^^^^^^^^^^^^^^^^^^^^^^^^

Blind transactions offer a significant step-up in privacy. Based on the work of the open-source `Elements Project <https://elementsproject.org/features/confidential-transactions/investigation>`_, they let you make confidential transactions that keep the value of the payment private between only you and the other party you're transacting with.

The identity of the participants (their PART address) is still publicly displayed on the blockchain, but no one else can determine how many coins were transacted.

The Confidential Transactions protocol is entirely trustless, meaning that it doesn’t require any trusted setup and doesn’t require the assistance of any intermediary to process transactions.

To prove and ensure that amounts being sent and received are correct and not fraudulent, the protocol uses rangeproof.

Rangeproofs
^^^^^^^^^^^

A rangeproof is a cryptographic protocol used to **verify that a payment amount is positive or zero without actually revealing the amount transferred in the transaction**. 

Without rangeproofs, the amounts in a transaction could be set so large that it would be considered a negative number, thus allowing coins to be generated out of thin air. An attacker could add a negative amount output and another different output, generating extra coins. The negative output would make the commitments still sum to zero.

The downside with rangeproofs is that they are quite heavy on the blockchain. Their size scales linearly with the number of outputs in a transaction and the bits in the proof’s range. In fact, due to their heavy nature, rangeproofs take up the majority of a blinded transaction’s size.

Bulletproofs
^^^^^^^^^^^^

Bulletproofs is a new generation of rangeproofs that scale logarithmically rather than linearly. In its `whitepaper <https://eprint.iacr.org/2017/1066.pdf>`_, they are referred to as non-interactive zero-knowledge short proofs. 

More simply, they are a groundbreaking improvement over regular rangeproofs as they reduce their size by around ~70%. And, because rangeproofs make up for the majority of a blind transaction's size, it, in turn, reduces transaction fees and the space they take on the blockchain by the same ratio.

.. seealso::

 * Particl's Bulletproofs audit - `Report by Quarkslab <https://blog.quarkslab.com/resources/2019-07-05-audit-particl-bulletproof-mlsag/particl_audit_report.pdf>`_
 * Confidential Transactions whitepaper - `Confidential Transactions investigation <https://elementsproject.org/features/confidential-transactions/investigation>`_
 * Bulletproofs whitepaper - `Bulletproofs <https://eprint.iacr.org/2017/1066.pdf>`_ 

Use Cases
^^^^^^^^^

- Send and receive payments without disclosing the value transferred;
- Hide amounts sent to smart contracts;
- Trade on :term:`BasicSwap <BasicSwap>` DEX.

----

Anon transactions
=================

+-----------+------------------------------+-----------------------+------------------------+
| **Cost**  | **Participants Information** | **Amount Transacted** | **Type of Balance**    |                                   
+-----------+------------------------------+-----------------------+------------------------+
| Moderate  | Hidden                       | Hidden                | Anon (private address) |                                   
+-----------+------------------------------+-----------------------+------------------------+

By adding “ring signatures” to blind transactions (RingCT), you obtain anon PART transactions. This is the most private type of transaction on Particl and makes transactions completely untraceable. All of the transaction data (values transferred and addresses of the participants) is anonymously written on the blockchain, making it impossible for anyone not involved with a transaction to see its details.

Anon transactions can be made more or less anonymous by manually adjusting the number of ring signatures included in transactions. The more private a transaction is, the more expensive it is to send.

Ring Signatures (MLSAG)
^^^^^^^^^^^^^^^^^^^^^^^

Multilayered Linkable Spontaneous Ad-Hoc Group Signatures (MLSAG), or ring signatures, is the Ring part of RingCT. It is **a type of digital signature that is performed by many outputs at once within a given group of RingCT outputs** (represented by Anon balances on Particl Desktop). It is then impossible for any outside observer to tell which of the participating outputs within that signature is the output actually sending out the transaction.

`Wikipedia describes ring signatures as follows <https://en.wikipedia.org/wiki/Ring_signature>`_: *“A ring signature is a type of digital signature that can be performed by any member of a group of users that each have keys. Therefore, a message signed with a ring signature is endorsed by someone in a particular group of people. One of the security properties of a ring signature is that it should be computationally infeasible to determine which of the group members’ keys was used to produce the signature.”*.

In RingCT’s case, the digital signature used to execute a transaction could have originated from any member of the ring group. Users put some of their funds within an Anon balance. Funds held within an Anon balance are used to execute RingCT transactions. Before a transaction is executed, the protocol anonymously signs it by **using other RingCT outputs as decoys** and produces a signature that, when verified, looks like it could have been initiated by any of the owners of the RingCT outputs used by the ring group. **It is not possible to know who really made the transaction because it could be anyone that has an output that’s being used by the ring group as a decoy**.

**This effectively anonymizes all values contained within a transaction**. It also arms transacting parties with a very strong plausible deniability.

.. seealso::

 * Particl's MLSAG audit - `Report by Quarkslab <https://blog.quarkslab.com/resources/2019-07-05-audit-particl-bulletproof-mlsag/particl_audit_report.pdf>`_
 * RingCT whitepaper - `Ring Confidential Transactions <https://eprint.iacr.org/2015/1098.pdf>`_

Use Cases
^^^^^^^^^

- Send and receive anonymous and untraceable payments;
- Pay for goods and services on :term:`Particl Marketlace`;
- Pay for listing fees on :term:`Particl Marketplace`;
- Promote user markets and storefronts on the Market Browser;
- Use smart contracts anonymously;
- Enter into two-party escrow agreements without sharing any information with any third-party;
- Receive staking rewards anonymously.

To learn more about the technology powering PART’s privacy capabilities, refer to the Particl Blockchain — Privacy section of the whitepaper.

----

Stealth Addresses
=================

Particl allows anyone to use stealth addresses instead of regular, public addresses. Stealth addresses are one-time addresses that increase privacy because **only the owner of a stealth address can tell if an output belongs to it or not**. What is meant by “one-time address” is that a stealth address can receive payments many times, but each time, it generates a new ‘one-time address’ for that output/transaction.

Without knowing the private key of an address, an observer won’t be able to link and guess which outputs match which stealth address. This helps in protecting the identity of the receiver of a transaction.

On their own, stealth addresses probably aren’t enough to protect transaction information from any well-funded and motivated observer (i.e., a state actor), but when combined with stronger privacy protocols such as Confidential Transactions or RingCT, it provides yet another layer of privacy for the user.

As it currently stands, blind and anon transactions can only be sent to stealth addresses.

----

Privacy-first Smart Contracts
*****************************

One of the reasons we rarely see privacy-preserving smart contracts is that they require coins to have programmable outputs. After all, a smart contract is very much akin to a distributed program. Unfortunately, outputs are not programmable in most privacy coins, such as Monero, Zcash, and others.

That is also the case with Particl’s anon transactions, which use RingCT. However, the uniqueness of the Particl ecosystem still allows for them to be used in smart contracts, granting them the same level of anonymity as when making anon transactions.

Because blind transactions (CT) have programmable outputs and can be used in smart contracts, RingCT transactions can be attached to their outputs.

In fact, **a RingCT output is converted to a CT output, which forms the inputs of a given smart contract. When the smart contract is ready to release funds to a particular address, it is directly released into a RingCT output**. In other words, incoming and outgoing smart contract payments can be made using anon transactions, but the coins are temporarily converted into blind outputs while the smart contract manages them.

**This makes Particl smart contracts completely anonymous**.

----

.. seealso::

 * PART Guides - :doc:`Send, Receive, and Convert PART <../part-guides/partguides_sendreceiveconvert>`
 * PART Guides - :doc:`Particl Desktop Wallet <../part-guides/partguides_desktop>`
 * PART Guides - :doc:`Buy and Sell PART <../particl-blockchain/blockchain_buysell>`