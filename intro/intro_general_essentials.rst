Essentials
==========

Particl is a **decentralized marketplace**, meaning there is not a single middleman or third-party getting in the middle of any transaction that happens between you and a buyer or seller. 

While that unlocks a ton of benefits not possible with traditional marketplaces, it also means that **Particl behaves a bit differently**. Don't worry, it's actually pretty easy to use, but there are a few things you need to consider and be aware of before you get started. Let's go over them!

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Basic Mechanics & Features
--------------------------

Particl does not rely on servers, payment processors, or any other central point of control. Instead, it entirely runs on a distributed, global network of nodes kept online by Particl users. It is a hybrid of P2P and blockchain technologies, meaning that it uses a few different protocols to enable its unique features.

- The **Particl blockchain** for sending and receiving currency transactions without involving any payment processor.

- The **SMSG network** for distributing and storing non-transactional data such as the marketplace's listings and markets, their descriptions, images, messages, and etc.

- The **Tor network** for keeping your digital network identity (your IP address) private when using Particl.

Because its network is autonomous and isn't operated by a single entity, the marketplace has a few features that behave differently than what you would expect on traditional online marketplaces. Let's have a look at these differences.

Cryptocurrency Transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An obvious difference between traditional online marketplaces and Particl is how you make payments. Instead of relying on payment processors, bank transfers, or payment cards, Particl works using cryptocurrencies. 

Cryptocurrencies are digital units of currency that can be transfered person-to-person without requiring a third-party to facilitate transactions. It enables near-free, near-instant currency transactions that cannot be held up, blocked, reversed, or delayed by any party.

While Particl accepts many different cryptocurrencies for payments, all marketplace transactions are ultimately settled in PART, Particl's native cryptocurrency.

Benefits
^^^^^^^^

- Available **anywhere in the world** at any time.
- **No downtime**.
- **Near-free** transactions, usually a few cents or less per transaction.
- **Near-instant**, usually takes around 2 minutes to be fully settled.
- Full control over your **financial privacy**.
- Cannot be held up, blocked, reversed, or delayed by any party.
- **Chargeback-proof** payment solution for merchants.

Need to keep in mind
^^^^^^^^^^^^^^^^^^^^

- Payments are sent to cryptocurrency addresses, not emails or bank accounts.
- Payments are **not reversible**. Once you send a payment, you cannot modify or cancel it.
- Payments information can be **seen by anyone** unless you send funds using **private transactions**.
- You and only you are responsible for the **security of your funds**. They cannot be retrieved if you lose access to your wallet or get hacked. 
- The value of cryptocurrencies (i.e. PART, BTC) is **not stable** and changes based on supply and demand.
- You and only you are responsible for properly following the requirements (i.e. filing taxes) and guidelines of your jurisdiction and the ones you're doing business in. 


Two-party Escrow
~~~~~~~~~~~~~~~~

Another big difference between traditional marketplaces and Particl is how transactions between two parties are secured. In fact, scammers are rampant all over the internet, and every marketplace needs to have solutions in place to protect both its buyers and sellers from malicious actors. 

On traditional marketplaces, this requires a third-party to hold payments on behalf of the involved parties while a service is being provided or while a product is being shipped. This role is usually assumed by the marketplace operator itself (i.e. Amazon), a payment processor (i.e. Paypal, Visa), or third-party escrow services (i.e. a bank). 

While this "mediated" escrow solution works in most cases, there are a few downsides to it such as **higher costs** due to the fees, **biased decisions** (such as the marketplace almost always ruling in favor of the buyer), as well as **reduced data security** and **user privacy** for all. 

Instead, Particl uses a two-party escrow system that doesn't require any third-party to be involved. To keep transacting parties honest with each other, it leverages smart-contracts and the Mutually Assured Destruction game-theory.

Particl's two-party escrow system, which is **fully autonomous**, requires both parties to make an equal **security deposit** into an escrow smart-contract before initiating a transaction. Because the security deposits can only be refunded once both parties agree that a transaction has been completed satisfactorily, no party is incentivized in misbehaving as that would directly result in a financial loss.

Benefits
^^^^^^^^

- **Free to use**, no fee other than the usual cryptocurrency transaction fee.
- More **data security** and **user privacy**.
- Available **24/7**.
- **Infinitely scalable**, can support as many transactions as users create. 

Need to keep in mind
^^^^^^^^^^^^^^^^^^^^

- Escrowed transactions are currently **mandatory** on all marketplace transactions.
- Security deposits are always **equal to the full cost of the purchased item + shipping**.
- Security deposits and payments for products are always **settled in PART**.
- Escrowed transactions **may take a few days to complete** depending on shipping times. The faster a product arrives to its destination, the quicker the buyer can mark the transaction as complete.
- Because **the price of the PART coin changes over time**, the fiat valuation (i.e. USD, EUR) of the funds received once an escrow smart-contract is completed **may be different** than what it was once the transaction was initiated. 
- Sellers also need to make a security deposit, meaning they, too, need to have a few PART coins to accept orders. 

Marketplace Moderation
~~~~~~~~~~~~~~~~~~~~~~

Since Particl is a distributed network that doesn't grant any special power to anyone, the moderation of its marketplace's content needs to be done differently. After all, there is no support staff, moderator, or administrator that can single-handedly keep spam and undesirable content out of the marketplace.

Instead, Particl relies on the "wisdom of the crowd" by **giving every user the equal opportunity to flag and take off undesirable content**. In other words, every user is a moderator. 

Particl's marketplace moderation works using an **upvote/downvote system**. When you see a listing you think shouldn't be on the marketplace, you can flag it as undesirable so that others can vote on it. When a listing gets too many downvotes compared to the number of upvotes, it gets taken off the marketplace entirely. The value of this "downvote threshold" is determined by the Particl community and can be adjusted if needed. 

And because it is impossible for the network to determine the number of true users, it counts votes on a **one-coin-equals-one-vote** basis. That way, only those with a stake in the network can get involved with its moderation system.

Benefits
^^^^^^^^

- Moderation system based on **direct democracy**.
- **Provably fair** and accurate governance. 
- **No pre-defined ban** on certain products and services.
- Votes are **free**.
- Entirely **distributed**, doesn't require any user with special permissions.

Need to keep in mind
^^^^^^^^^^^^^^^^^^^^

- Because there is no way to enforce any pre-defined bans on a distributed network, **you may encounter products you do not like from time to time**. It is important that you flag these products if you believe they shouldn't be on the marketplace.
- Taking a listing off the marketplace is **as fast as other users are** to cast their votes.
- For your coins to count as votes, they need to be held in your ``Public`` balance. Coins held in your ``Anon`` balance won't count towards moderation votes.

Multi-Currency Support
~~~~~~~~~~~~~~~~~~~~~~

On Particl, you can use many different cryptocurrencies to either pay for products on the marketplace or top up your Particl wallet with PART coins. However, it's important to note that **all non-PART transactions are ultimately settled as PART transactions** so the escrow smart-contracts can be funded.

For example, let's say you pay for a product using **Bitcoin**. You would first need to go through the checkout process and confirm your order. Then, your Particl Desktop client would give you a Bitcoin address to send your payment. Once it is sent, Particl would then **automatically swap** your BTC for PART and fund the escrow smart-contract created for your order.

Multi-currency support is currently provided by a few in-app bots connected to external exchanges. It will eventually be possible to swap other cryptocurrencies for PART without requiring any middleman by using in-app "atomic swap" exchanges.

Benefits
^^^^^^^^

- Allows you to pay for products and services using your favorite cryptocurrency.
- **No account** required, no KYC.
- Your IP address remains **private**.
- Allows you to top up your Particl acccount without leaving the wallet.

Need to keep in mind
^^^^^^^^^^^^^^^^^^^^

- Particl's multi-currency support currently relies on third-party swap services (i.e. SimpleSwap, StealthEx).
- Third-party swap services likely **track transactions** going through their systems.  
- Third-party swap services charge a **transaction fee** for their services.
- While buyers can use their favorite cryptocurrency, sellers can currently only **receive payments in PART**. 

Other Considerations
---------------------

There are various other considerations to keep in mind when using Particl. What follows is a compilation of some of the most important ones to be aware of.

Don't Forget to Unlock Your Wallet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**To receive an order or complete order steps, your Particl Desktop client needs to be unlocked.** You will not receive any order or get notified on the progress of active orders if you keep your wallet locked. 

Completing an order on Particl's marketplace requires you and the other party you're transacting with to manually do a few steps. Every time you complete a step, a P2P message is generated and then sent to the other party's client indicating that it is their turn to act. But for the other party's client to be able to unlock and interpret the message, it needs to be unlocked first. 

Keep Some Funds in Your Balances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is generally recommended to keep a few PART coins in both your ``Public`` and ``Anon`` balances. Indeed, holding *some* funds in those balances will allow you to use all the features offered to you by Particl and benefit from the full experience.

Public balance
^^^^^^^^^^^^^^

- Send public transactions.
- Earn dividend-like staking rewards.
- Flag, upvote, and downvote listings.
- Pay for listing fees and earn a portion of all the fees paid to the network by other users..
- Create and vote on community proposals.

Anon balance
^^^^^^^^^^^^

- Send untraceable transactions.
- Pay for products and services on the marketplace.
- Make escrow security deposits. 

Syncing Times
~~~~~~~~~~~~~

Because the marketplace's content is hosted on a distributed network (SMSG) instead of a cluster of servers, the marketplace may appear slower than a typical website. For example, it may take a few minutes for the blockchain network to sync. It may take even a few more minutes to fully load all marketplace's listings.

This is, unfortunately, a small price to pay to get all the awesome benefits offered by Particl's distributed network such as near-zero fees and rock solid security. But rest assured, these are also roadmap items the Particl team plans on tackling as it moves through the Beta phase of development.