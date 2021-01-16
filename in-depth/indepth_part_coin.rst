=========================
Currency (PART) Explained
=========================

Although you can use many different coins to pay for products and services on :term:`Particl Marketplace`, all payments are ultimately converted and settled in PART. 

PART is an untraceable :term:`cryptocurrency` that can be sent to anyone, anywhere in the world, without the need for any third-party to facilitate transactions. It is a secure :term:`cryptocurrency` that is similar to Bitcoin, but packed with more functionality to help you preserve your financial privacy from prying eyes.

**Cryptocurrencies in general**

:term:`Cryptocurrencies` are digital units of a currency that can be transferred person-to-person without requiring a third-party (payment processor) to facilitate transactions. It enables near-free, near-instant currency transactions that cannot be held up, blocked, reversed, or delayed by any party.

**Benefits**

- Can be used anywhere in the world at any time.
- No downtime.
- Near-free transactions, usually a few cents or less per transaction.
- Near-instant, usually takes around 2 minutes to be fully settled.
- Full control over your financial privacy.
- Cannot be reversed (no chargebacks).

**Considerations**

- Payments are sent to special addresses similar to bank accounts.
- Once you sent a payment, you cannot modify or cancel it.
- You and only you are responsible for the security of your funds. They cannot be retrieved if you lose control over your wallets. 
- The price of cryptocurrencie's majority changes based on supply and demand.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Blockchain Specifications
-------------------------

PART is the :term:`cryptocurrency` of the :term:`Particl Blockchain`. It is a secure and confidential currency specifically designed to power eCommerce and marketplaces. It uses several security, encryption, and privacy protocols to make sure none of your personal information and data can be collected when transacting on the marketplace. 

PART has been released back in 2017 and is based on the Bitcoin code. Unlike Bitcoin, many modern day improvements have been added to the code, making it faster, more private, and more flexible.

+--------------------------+------------------------------------------+
| **Native blockchain**    | Particl                                  | 
+--------------------------+------------------------------------------+
| **Blockchain Codebase**  | |BTC Version|                            |
+--------------------------+------------------------------------------+
| **Block Time**           | 120 seconds (5x faster than Bitcoin)     | 
+--------------------------+------------------------------------------+
| **Block Size**           | 2 MB (2x more capacity than Bitcoin)     |
+--------------------------+------------------------------------------+
| **Consensus Mechanism**  | Particl Proof-of-Stake (PPoS)            |
+--------------------------+------------------------------------------+
| **Circulating Supply**   | |Coin supply| (100%)                     |
+--------------------------+------------------------------------------+
| **Inflation Rate**       | 2% per year                              |
+--------------------------+------------------------------------------+
| **Segwit**               | Enabled                                  |
+--------------------------+------------------------------------------+
| **Lightning Network**    | Enabled                                  |
+--------------------------+------------------------------------------+
| **Atomic Swaps**         | Enabled                                  |
+--------------------------+------------------------------------------+

Staking Specifications
----------------------     

Particl uses the Particl Proof-of-Stake (PPoS) consensus mechanism which pays back interest in dividend-like payments to stakers in exchange for securing the network. PPoS offers many secure staking options that lets you effortlessly reap the benefits of staking without any of its typical security risks.

In particular, Particl's cold staking mechanism allows you to earn an interest on the PART coins you own even when they're stored offline. That also includes funds stored on a cold wallet, a hardware device (i.e. Ledger Nano), a phone, a cloud server, or even just a piece of paper. Cold staking also lets you earn rewards more often by teaming up with other stakers. This is done by joining a staking pool. 

+-----------------------------+------------------------+
| **Staking Revenue**         | 2% to ~5% per year     |
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
| **Masternode**              | No                     |
+-----------------------------+------------------------+
| **Coin Maturity**           | 225 blocks (~8 hours)  |
+-----------------------------+------------------------+

Privacy Specifications
----------------------  

PART is a modern day :term:`cryptocurrency`. It doesn't just allow you to transact person-to-person with anyone else, it also does it in a way that doesn't permanently share all of your financial data with the rest of the world. It has an adjustable level of privacy and lets you choose between three different types of transactions (public, blind, and anon), each with their own purpose, cost, and level of privacy.

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
| **Taproot**                      | Yes (Particl Core 0.21+)                    |
+----------------------------------+---------------------------------------------+

Types of balances
^^^^^^^^^^^^^^^^^

On Particl, there are three different types of balance, each with their own purpose, cost, level of privacy, and settings. All three types of balance are available on :term:`Particl Desktop` and you can easily convert coins from one type of balance to another by reading the :doc:`Manage Funds user guide <../guides/guide_mp_general_managing_funds>`.

Public Balance
~~~~~~~~~~~~~~

- **Cost:** Extremely low
- **Privacy:** Fully transparent and auditable, transacting amounts and parties are publicly displayed on the blockchain

Public balances let you make Bitcoin-like public transactions. These transactions are the most affordable ones to make, but they're also the most simple ones to support and integrate. For this reason, they are the most widely supported type of transaction by exchanges and third-party services. 

**What can you do with public balances and transactions?**

- Send and receive payments.
- Earn PART coins by staking the coins in your public balance.
- Pay for listing fees on the marketplace.
- Promote user markets and storefronts on the Market Browser.
- Participate in the marketplace's moderation system.
- Use smart-contracts.
- Receive regular staking rewards.

Blind Balance
~~~~~~~~~~~~~

- **Cost:** Low
- **Privacy:** Confidential, transacting amounts are not publicly displayed

Blind balances offer a significant step-up in privacy. Based on the work of the open-source `Elements Project <https://elementsproject.org/features/confidential-transactions/investigation>`_, they let you make blinded transactions that keep the value of the payment private between you and the other party you're transacting with. Who's participating in a blinded transaction is still publicly displayed on the blockchain, but it's impossible for anyone not involved in a given transaction to see what the value of its payment is. 

**What can you do with blind balances and transactions?**

- Send and receive confidential payments.
- Use confidential smart-contracts.
- Receive confidential staking rewards.

Anon Balance
~~~~~~~~~~~~

- **Cost:** Moderate
- **Privacy:** Anonymous, transacting amounts and the identity of parties are hidden

By adding "ring signatures" to blind balances, you obtain anon balances, the highest level of privacy on Particl. Not only does it make transactions confidential, it makes them entirely untreaceable. What this means is that both the transacting amounts and the parties involved with a given transaction remain anonymous. Who you transact with and how much you're transacting can only be known by you and that other person.

**What can you do with anon balances and transactions?**

- Send and receive untraceable transactions.
- Pay for goods and services on :term:`Particl Marketplace`.
- Pay for listing fees on the marketplace.
- Use anonymous smart-contracts.
- Participate in two-party escrow transactions without sharing your information to any third-party.
- Receive anonymous staking rewards.

.. seealso::

 Other sources for useful or more in-depth information:

 - Particl Wiki - `PART coin frequently asked questions <https://particl.wiki/support/faq/part-coin/>`_
 - Particl Website - `PART coin specifications <https://particl.io/coin-specifications>`_
 - Particl Website - `PART coin exchanges <https://particl.io/part-exchanges/>`_
 - Particl Website - `Particl user guides <https://particl.io/user-guides/>`_
