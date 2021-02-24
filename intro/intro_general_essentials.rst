===============
Operation Hints
===============

.. title::
   Particl Marketplace Operation Hints

.. meta::
   :description lang=en: Thing you should take into consideration if using Particl Marketplace.

The :term:`Particl Marketplace` is a decentralized marketplace, meaning that no third-party is required to do commerce. There's no marketplace company, e-commerce service provider, internet server, payment processor, or even bank involved. Transactions happen directly between trading partners.

That unlocks benefits not possible with traditional marketplaces, and it also means that the :term:`Particl Marketplace` behaves a bit differently. It is pretty easy to use, but there are a few things you need to consider before you get started. Let's go over them!

Find the deep-dive and technical explanation within :ref:`Particl Marketplace explained`.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Payment Processing
------------------

Instead of relying on 3rd party payment processors, bank transfers, or payment cards, :term:`Particl Marketplace` uses electronic currencies, commonly called :term:`cryptocurrency <Cryptocurrency>`. This enables near-free, near-instant currency transactions that cannot be held up, blocked, reversed, or delayed by any party.

Many different digital currencies can be used for payments on the :term:`Particl Marketplace`. The final settlement of payments is completed in "PART", Particl’s own :term:`cryptocurrency <Cryptocurrency>`. Mind the guide :doc:`Obtaining PART <../guides/guide_general_obtaining_part>`.

The in-depth guide :ref:`Currency (PART) Explained` will make you understand this electronic currency in full.

----

Fraud Protection
----------------

Every marketplace needs to have solutions in place to protect both its buyers and sellers from scammers.

On traditional marketplaces, this requires a third-party to hold payments on behalf of the involved parties. At the same time, a service is being provided, or a product is being shipped. This role is usually assumed by the marketplace operator itself (i.e. Amazon), a payment processor (i.e. Paypal, Visa), or third-party escrow services (i.e. bank). This “mediated” escrow solution works in most cases. There are a few downsides to it, such as higher costs due to the fees, biased decisions (such as the marketplace almost always ruling in favor of the buyer), deferred payouts, and nearly absent data security and user privacy for all users.

The :term:`Particl Marketplace` uses an entirely different approach. It secures transactions using a two-party escrow system that doesn’t require any third-party to be involved. 

The in-depth guide :ref:`Two-Party Escrow Explained` will give you deep knowledge about this unique selling proposition.

----

Phases of a Deal
----------------

.. figure:: ../_static/media/images/001_phases_of_a_deal.png
    :align: center
    :alt: Particl Marketplace's phases of a deal
    :target: ../_static/media/images/001_phases_of_a_deal.png

A buyer finds an item on :term:`Particl Marketplace` and decides to buy it. It starts with a request (bid) to the vendor if he is willing and able to sell it. If the vendor accepts, the buyer has to pay the item to the two-party escrow system, and both parties put collateral into the autonomous and free of charge two-party escrow system. The vendor sends out the package and marks the item as shipped. Once the package arrives and the customer is satisfied, they mark the order as completed. This mark signals the two-party escrow system to release the payment and collateral to the vendor. At the same time, the collateral for the customer gets released as well. The deal has concluded.

If any disruptions occur during trading, both parties will do their best to serve each other’s interests to recover the deposited collaterals. You find further information in the :ref:`Fraud protection` paragraph above. 

----


Community Markets
-----------------

By default, any participant of the :term:`Particl Marketplace` has access to the so-called :term:`Open Market`. It’s the always public market for a general-purpose where anyone can buy or sell anything. 

Additionally, there are infinite :term:`Community Markets <Community Market>` to be created with different states of accessibility. :term:`Community Markets <Community Market>` are private by default, and only those knowing about its access keys can join them. The :term:`Community Market <Community Market>` creator and owner can decide if publishing items on this market is limited to a group (storefront) or granted to anybody with access rights.

Additionally, a market owner has the right to promote their :term:`Community Markets <Community Market>` within the :term:`Market Browser` for a limited time in exchange for a small fee.

The use-case for the :term:`Community Markets <Community Market>` is versatile. A brand, categories of goods, or mindsets theme them. It is an ideal tool for creating markets that serve global or local communities, neighborhood co-operatives, VIP stores, pop-up stores, and pretty much anything you can imagine.

The user-guide :ref:`Markets & Storefronts` gives you insight how to manage them.

----

Crowd Moderation
----------------

Since the :term:`Particl Marketplace` relies on a distributed network that doesn't grant any special power to anyone, the moderation of its content needs to be done differently. After all, there is no support staff, moderator, or administrator that can single-handedly keep spam and undesirable content out of the marketplace. Instead, Particl relies on the “wisdom of the crowd” theory by giving every user the equal opportunity to flag and take off undesirable content. In other words, every user is a moderator.

Particl's marketplace moderation works using an upvote/downvote system. When you see a listing you think shouldn’t be on the marketplace, you can downvote and flag it as undesirable. 

The in-depth guide :ref:`Marketplace Moderation Explained` will give you deep knowledge about its mechanics.

----

Noteworthy Mentions
-------------------

There are various other considerations to keep in mind when using the :term:`Particl Marketplace`. What follows is a compilation of things to be aware of.

**Wallet Unlocking**

To receive orders or to complete order steps, the :term:`Particl Desktop` client needs to be unlocked. You will not receive any orders or get notifications on the progress of active orders if you keep your wallet locked. Mind the vault icon in the top-right status icons bar.

**Have Some Funds in Different Privacy States**

PART Coin has multiple privacy states by design. It is generally recommended to keep a few PART coins in both your :guilabel:`Public` and :guilabel:`Anon` balances. Indeed, holding some funds in those balances will allow you to use all the features offered to you by the :term:`Particl Marketplace` and accelerate the workflow.

The brief introduction :ref:`Types of balances` gives you insight on that matter.

**Loading and Syncing Times**

Because the :term:`Particl Marketplace`'s content is hosted on distributed Networks for payments and data-exchange, the marketplace may take a few minutes to sync. It may take even a few more minutes to fully load all marketplace's listings. This is to be normally expected and will get much faster as the Particl team improves the marketplace.

----

**Almost there**

Phew! Now you have quite an understanding of the :term:`Particl Marketplace`. In the next chapter, you can have a look at all of its funtions at once. 

Perhaps you want to skip that part and install it right away? Just head over to the :ref:`Installation Guides`.

---- 
