=========================
Currency (PART) Explained
=========================

.. meta::
      
      :description lang=en: Deep dive explanation of Particl's privacy coin PART.

PART is the untraceable :term:`cryptocurrency <Cryptocurrency>` of the :term:`Particl Blockchain`; a :term:`blockchain <Blockchain>` based on the Bitcoin code on which several privacy and utility technologies have been added. It enables you to do independent, secure, borderless, and private payments without requiring any third-party like a bank or a payment processor.

PART is also the settlement currency of the :term:`Particl Marketplace`. Regardless of the currency used by the buyer to initiate a transaction, all payments on the marketplace are ultimately converted into PART before the :doc:`escrow stage <../in-depth/indepth_escrow>`.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

What are cryptocurrencies?
--------------------------

:term:`Cryptocurrencies <Cryptocurrency>` are digital units of currency. They can be transferred person-to-person without requiring any third-party (like a bank or a payment processor) to facilitate transactions. They enable near-free, near-instant, and borderless currency transactions that cannot be held up, blocked, reversed (chargebacks), or delayed by any party.

**What are their benefits?**

- They can be used anywhere in the world, at any time (100% uptime).
- Transactions are near-free; usually just a few cents or even less per transaction.
- Transactions are near-instant; usually takes a few seconds or minutes for payments to be fully settled.
- Transactions cannot be reversed (no chargebacks).
- You keep complete control of your financial data.

**A few things to keep in mind...**

- Payments are sent to unique cryptographic addresses similar to bank account numbers.
- Once you send a payment, you cannot modify or cancel it. Always double-check the payment details before making a transaction.
- You and only you are responsible for the security of your funds. They cannot be retrieved if you lose your password(s) or control over your wallets(s).
- The price of almost any cryptocurrency is volatile by nature and based on the concept of supply and demand.

Blockchain Specifications
-------------------------

PART is the :term:`cryptocurrency <Cryptocurrency>` of the :term:`Particl blockchain <Particl Blockchain>`. It is a secure and confidential currency specifically designed to power e-commerce and financial platforms. It uses several security, cryptographic, and privacy-preserving protocols to make sure none of your personal information and data can be collected when transacting on the :term:`Particl Marketplace <Particl Marketplace>`. 

PART has been released back in 2017 and is based on the latest version of the Bitcoin code (currently |BTC Version|). The Particl codebase contains many modern-day improvements and additional features not present in the Bitcoin code. This makes it a faster, more private, and more flexible version of Bitcoin.

+--------------------------+-----------------------------------------------------------+
| **Native Blockchain**    | Particl                                                   |
+--------------------------+-----------------------------------------------------------+
| **Blockchain Codebase**  | |PART Version|                                            |
+--------------------------+-----------------------------------------------------------+
| **Codebase Origin**      | |BTC Version|                                             |
+--------------------------+-----------------------------------------------------------+
| **Block Time**           | 120 seconds (5x faster than Bitcoin)                      |
+--------------------------+-----------------------------------------------------------+
| **Block Size**           | 2 MB (2x more capacity than Bitcoin)                      |
+--------------------------+-----------------------------------------------------------+
| **Consensus Mechanism**  | Particl Proof-of-Stake (:term:`PPoS`)                     |
+--------------------------+-----------------------------------------------------------+
| **Circulating Supply**   | |Coin supply| (100%)                                      |
+--------------------------+-----------------------------------------------------------+
| **Inflation Rate**       | 8% per year (4% to stakers, 4% to decentralized treasury) |
+--------------------------+-----------------------------------------------------------+
| **Segwit**               | Enabled                                                   |
+--------------------------+-----------------------------------------------------------+
| **Lightning Network**    | Enabled                                                   |
+--------------------------+-----------------------------------------------------------+
| **Atomic Swaps**         | Enabled  (Particl DEX coming soon)                        |
+--------------------------+-----------------------------------------------------------+

Staking Specifications
----------------------     

Particl uses the :doc:`Particl Proof-of-Stake <../in-depth/indepth_staking>` (:term:`PPoS`) consensus mechanism. It pays back interest in dividend-like payments to stakers in exchange for securing the network. :term:`PPoS` offers many secure staking options that let you easily and quickly earn rewards without any of the security or financial risks typically associated with staking.

:term:`PPoS` is also what Particl's :ref:`community governance system <Community Governance Explained>` uses to let you cast votes on proposals.

Cold staking protocol
=====================

Particl's cold staking protocol allows you to securely delegate your staking power to a staking-only node that contains no coin. This lets your earn interest payments (:ref:`staking rewards <What's a staking reward?>`) on your PART coins, even if they're stored offline. 

It enables true and secure staking on cold wallets, hardware devices (i.e., Ledger Nano), mobile wallets, cloud servers, or even just a piece of paper. Staking-only nodes do not have access to the coins they are staking, meaning they are hackproof.

Cold staking pools
==================

You can join a cold staking pool to team up with other stakers and combine your staking powers. This leads to more frequent rewards in exchange for a small fee paid to the pool operator. Cold staking pools are ideal if you have a smaller balance or don't want to manage a staking node yourself.  

On-chain voting right
=====================

Particl's :ref:`community governance <Community Governance Explained>` is powered by :term:`PPoS`. By staking, you can :ref:`vote on community proposals <Voting on Proposals>` using your staking power as voting power. When voting on a proposal, any block you stake during the voting period will cast a vote. The more blocks you stake during a proposal's voting period, the more votes you cast.

+-----------------------------+------------------------+
| **Staking Revenue**         | 4% to ~8% per year     |
+-----------------------------+------------------------+
| **Cold Staking**            | Yes                    |
+-----------------------------+------------------------+
| **Staking Pools**           | Yes                    |
+-----------------------------+------------------------+
| **Hardware Staking**        | Yes                    |
+-----------------------------+------------------------+
| **Multi-Signature Staking** | Yes                    |
+-----------------------------+------------------------+
| **Mobile Staking**          | Yes                    |
+-----------------------------+------------------------+
| **Nb. of Coins to Stake**   | >0                     |
+-----------------------------+------------------------+
| **Masternodes**             | No                     |
+-----------------------------+------------------------+
| **Coin Maturity**           | 225 blocks (~8 hours)  |
+-----------------------------+------------------------+

Privacy Specifications
----------------------  

PART is a modern-day :term:`cryptocurrency <Cryptocurrency>` and the logical evolution to Bitcoin. It doesn't just allow you to transact person-to-person with anyone else; it also does it in a way that doesn't permanently share all of your financial data with the rest of the world. 

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
| **Taproot**                      | Yes (Taproot-ready as of Particl Core 0.21+)|
+----------------------------------+---------------------------------------------+

PART has three different types of transactions, each with its own purpose, cost, level of privacy, type of balance, and settings. All three types are available on :term:`Particl Desktop`, where you can easily convert your coins from one kind of balance to another. 

Public transactions
===================

- **Cost:** Very low
- **Privacy:** Public; transacted amounts and the identity of the participants are permanently written on the blockchain and publicly displayed. Identical to Bitcoin transactions.
- **Type of balance:** Public

Public transactions let you make Bitcoin-like public transactions. These transactions are the most affordable ones to make and the simplest to integrate into other platforms. For this reason, they are the most widely supported type of transactions by exchanges and third-party services.

Additionally, public transactions can only be sent to public balances, which is also the only type of balance that can stake. For this reason, coins held in public balances act as "voting tickets" in Particl's :ref:`community governance system <Community Governance Explained>`. Visit the :doc:`Staking <../in-depth/indepth_staking>` in-depth guide for more information on this topic.

**What can you do with public transactions?**

- Send and receive public payments.
- Earn PART coins in dividend-like payments by staking.
- Pay for listing fees on the marketplace.
- Promote user markets and storefronts on the Market Browser.
- Moderate the :term:`Particl Marketplace`.
- Use smart-contracts. 

Blind transactions
==================

- **Cost:** Low
- **Privacy:** Confidential; the identity of the participants is publicly displayed on the blockchain, but transacted amounts are kept anonymous.
- **Type of balance:** Blind (Private)

Blind transactions offer a significant step-up in privacy. Based on the work of the open-source `Elements Project <https://elementsproject.org/features/confidential-transactions/investigation>`_, they let you make confidential transactions that keep the value of the payment private between only you and the other party you're transacting with. 

The identity of the participants (their PART address) is still publicly displayed on the blockchain, but it's impossible for anyone else to determine how many coins were transacted. 

**What can you do with blind balances and transactions?**

- Send and receive payments without disclosing the value transferred.
- Use confidential smart-contracts.

Anon transactions
=================

- **Cost:** Moderate
- **Privacy:** Anonymous; both the transacted amounts and the identity of the participants are anonymous. No date is publibly displayed on the blockchain.
- **Type of balance:** Anon (Private)

By adding “ring signatures” to blind transactions (RingCT), you obtain anon transactions. This is the most private type of transaction on Particl and makes them completely untraceable. All of the transaction data (values transferred and addresses of the participants) is anonymously written on the blockchain, making it impossible for anyone not involved with a transaction to see its details.

Anon transactions can be made more or less anonymous by manually adjusting the number of ring signatures included in transactions. The more private an anon transaction is, the more expensive it is to send. 

**What can you do with anon balances and transactions?**

- Send and receive anonymous and untraceable payments.
- Pay for goods and services on :term:`Particl Marketplace`.
- Pay for listing fees on :term:`Particl Marketplace`.
- Use anonymous smart-contracts.
- Enter into two-party escrow agreements without sharing any information with any third-party.
- Receive :ref:`staking rewards <What's a staking reward?>` anonymously. 

Read the :doc:`Funds, Coins, and Balances <../guides/guide_mp_general_managing_funds>` user guide for more information on how to make different types of transactions.

Marketplace Payments and Settlements
------------------------------------

The PART coin is the settlement layer of :term:`Particl Marketplace`. Although you can initiate transactions using other cryptocurrencies (i.e., Bitcoin), all marketplace payments are converted into PART :ref:`before the seller receives a bid from a buyer <Technicals of a Buy Flow>`.

All :term:`Particl Marketplace` transactions are settled in PART because of the :doc:`two-party escrow system <../in-depth/indepth_escrow>`. It works using an anonymous escrow smart-contract on the :term:`Particl Blockchain`, and for this reason, needs to use the blockchain's native coin. 

One of the results of settling all marketplace transactions in PART is that a fair number of coins are constantly locked in escrow, away from circulation. This directly leads to a reduction in the circulating PART supply on trading markets while naturally stimulating its demand. This creates a positive feedback that takes coins more coins out of circulation and creates more demand at the same time the more the people use :term:`Particl Marketplace`.

.. note::
 Although paying for an order on :term:`Particl Marketplace` is done manually using an in-app swap module, a more automatic mechanism is planned for later during the Beta phase of development.

----

.. seealso::

 Other sources for useful or more in-depth information:

 - Particl Academy - Explained :doc:`Staking <../in-depth/indepth_staking>`
 - Particl Academy - Guide :doc:`Staking and Voting <../guides/guide_mp_general_enable_staking>`
 - Particl Academy - Guide :doc:`Funds, Coins, and Balances <../guides/guide_mp_general_managing_funds>`
 - Particl Academy - Guide :doc:`Obtaining PART <../guides/guide_general_obtaining_part>`
 - Particl Wiki - `PART coin frequently asked questions <https://particl.wiki/support/faq/part-coin/>`_
 - Particl Website - `PART coin specifications <https://particl.io/coin-specifications>`_
 - Particl Website - `PART coin exchanges <https://particl.io/part-exchanges/>`_
 - Particl Website - `Particl user guides <https://particl.io/user-guides/>`_
 - CoinGecko - `Particl on CoinGecko <https://www.coingecko.com/en/coins/particl>`_
 - CoinMarketCap - `Particl on CoinMarketCap <https://coinmarketcap.com/currencies/particl>`_
