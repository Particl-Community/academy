Essentials
==========

|PM| is a decentralized marketplace, meaning that no third-party is required to facilitate transactions. There's no marketplace company, e-commerce service provider, internet server, payment processor, or even bank involved. Transactions happen directly between you and the other person. 

While that unlocks many benefits not possible with traditional marketplaces, it also means that |PM| behaves a bit differently. Don’t worry. It is pretty easy to use, but there are a few things you need to consider before you get started. Let’s go over them!

Find the deep-dive and technical explanation within :ref:`Particl Marketplace explained`.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Cryptocurrency Transactions
---------------------------

Instead of relying on payment processors, bank transfers, or payment cards, Particl Marketplace works using cryptocurrencies. Cryptocurrencies are digital units of currency that can be transferred person-to-person without requiring a third-party to facilitate transactions. It enables near-free, near-instant currency transactions that cannot be held up, blocked, reversed, or delayed by any party. While many different digital currencies can be used on |PM|, all marketplace transactions are ultimately settled in PART, Particl’s native cryptocurrency.

The in-depth guide :ref:`PART Cryptocurrency` will make you understand it in detail.

**Benefits**

- Can be used anywhere in the world at any time.
- No downtime.
- Near-free transactions, usually a few cents or less per transaction.
- Near-instant, usually takes around 2 minutes to be fully settled.
- Full control over your financial privacy.
- Cannot be reversed (no chargebacks).

**Considerations**

- Payments are sent to cryptocurrency addresses, not emails or bank accounts.
- Payments are not reversible. Once you sent a payment, you cannot modify or cancel it.
- You and only you are responsible for the security of your funds. They cannot be retrieved if you lose access to your wallet or get hacked. 
- The price of cryptocurrencies (i.e. PART, BTC) changes based on supply and demand.

The Two-party Escrow
--------------------

Every marketplace needs to have solutions in place to protect both its buyers and sellers from scammers.

On traditional marketplaces, this requires a third-party to hold payments on behalf of the involved parties. At the same time, a service is being provided, or a product is being shipped. This role is usually assumed by the marketplace operator itself (i.e. Amazon), a payment processor (i.e. Paypal, Visa), or third-party escrow services (i.e. bank). This “mediated” escrow solution works in most cases. There are a few downsides to it, such as higher costs due to the fees, biased decisions (such as the marketplace almost always ruling in favor of the buyer), and nearly absent data security and user privacy for all users.

|PM| uses an entirely different approach. It secures transactions using a two-party escrow system that doesn’t require any third-party to be involved. To keep transacting parties honest with each other, it leverages smart-contracts and the Mutually Assured Destruction game-theory. Here, both parties must make an equal security deposit to be held as collateral into an escrow smart-contract. Because the security deposits can only be refunded once, both parties agree that a transaction has been completed satisfactorily. Users are financially incentivized to remain honest with each other and mutually work on resolutions if needed.

The in-depth explanation of the topic :ref:`Two-Party Escrow` will give you deep knowledge.

**Benefits**

- Free of charge
- Full data security and user privacy.
- Available 24/7.
- Infinitely scalable, can support as many transactions as users create. 

**Considerations**

- Security deposits are equal to the full cost of the purchased item + shipping.
- The PART coin value changes based on supply and demand, the value of the security deposit may fluctuate while in escrow. 
- Sellers need to make a security deposit equal to that of their buyer's, so they require a PART balance to sell on the marketplace.

The Marketplace Moderation
--------------------------

Since |PM| relies on a distributed network that doesn't grant any special power to anyone, the moderation of its marketplace's content needs to be done differently. After all, there is no support staff, moderator, or administrator that can single-handedly keep spam and undesirable content out of the marketplace. Instead, Particl relies on the “wisdom of the crowd” theory by giving every user the equal opportunity to flag and take off undesirable content. In other words, every user is a moderator.

Particl's marketplace moderation works using an upvote/downvote system. When you see a listing you think shouldn’t be on the marketplace, you can downvote and flag it as undesirable. When a listing gets too many downvotes compared to the number of upvotes, it gets taken off the marketplace entirely. The downvote ratio can be set up by the community. And because it is impossible for the network to determine the number of true users, due to the decentralized and private nature of Particl, it counts votes on a one-coin-equals-one-vote basis. That way, the system cannot be cheated, and only those with a stake in the network can get involved with its moderation system.

The in-depth explanation of the topic :ref:`Marketplace Moderation` will give you deep knowledge.

**Benefits**

- Moderation system based on direct democracy.
- Provably fair and accurate governance. 
- No pre-defined ban on certain products and services.
- Entirely distributed, doesn't require any user with special permissions.

**Considerations**

- Because there is no way to enforce any pre-defined bans on a distributed network, you may encounter products you do not like from time to time. It is important that you flag these products if you believe they shouldn't be on the marketplace.
- For your coins to count as votes, they need to be held in your :guilabel:`Public` balance. Coins held in your :guilabel:`Anon` balance don't work with the voting mechanism.

Other Considerations
--------------------

There are various other considerations to keep in mind when using |PM|. What follows is a compilation of some of the most important ones to be aware of.

**Wallet unlocking**

To receive an order or complete order steps, your Particl Desktop client needs to be unlocked. You will not receive any order or get notified on the progress of active orders if you keep your wallet locked. 

**Keep Some Funds in Your Balances**

PART Coin has multiple privacy states by design. It is generally recommended to keep a few PART coins in both your :guilabel:`Public` and :guilabel:`Anon` balances. Indeed, holding some funds in those balances will allow you to use all the features offered to you by |PM| and benefit from the full experience.

The in-depth explanation is within :ref:`Types of balances`

**Syncing Times**

Because the marketplace's content is hosted on the SMSG portion of the :term:`Particl Network`, the marketplace may take a few minutes to sync. It may take even a few more minutes to fully load all marketplace's listings. This is to be normally expected and will get much faster as the Particl team improves the marketplace.

This is, unfortunately, a small price to pay to get all the awesome benefits offered by Particl's distributed network such as near-zero fees and rock solid security. But rest assured, these are also roadmap items the Particl team plans on tackling as it moves through the Beta phase of development.