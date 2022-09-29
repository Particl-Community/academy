==================
Content Moderation
==================

.. title::
   Particl Marketplace Moderation

.. meta::
   :description lang=en: Learn more about Particl Marketplace’s community-powered and privacy-oriented moderation system.

Like any online marketplace or platform, there needs to be a way for its content to be moderated. As we’ve seen, Particl’s entirely distributed structure means it is unstoppable, uncensorable, and unable to ban users. However, leaving the platform without any sort of moderation mechanism would open up the possibility for an unspeakable number of problems to make their way through.

That’s why Particl contributors have designed a completely decentralized and adjustable moderation system that filters content without discriminating against specific products or users.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Power and Control to the People
-------------------------------

Because Particl is a distributed marketplace, there are no moderation staff, moderators, or accounts with special permissions to keep the marketplace clean from undesirable content. This means that the moderation of the marketplace's content needs to be done differently than what we typically see on other e-commerce platforms. 

Instead of giving moderating powers to a few groups of "trusted" individuals, Particl’s moderation system gives it back to every single user. This is an efficient way to reach a fair and globally agreeable consensus and take personal or geographical biases out of the equation.

Benefits
~~~~~~~~

.. container:: toggle

    .. container:: header

        **Provably Fair**

    Particl's moderation system is powered by tamper-proof blockchain technology, which makes it provably fair. No party, including a marketplace operator itself, can unilaterally censor users or content. This system represents the closest form of direct democracy possible with today's technology.

.. container:: toggle

    .. container:: header

        **No Censorship nor Bans**

    Particl's modular ecosystem is blank and requires direct input from users for products to be voted out. In other words, it cannot and does not enforce any restrictions on products or services being offered, unlocking the full potential of the global *free market* without interference. 

.. container:: toggle

    .. container:: header

        **Incurs no Cost**

    Typically, online marketplaces include the costs of moderating their platform into the sales commission paid by sellers as part of their service fees. That's they require staff and legal teams. Particl's moderation system is entirely non-custodial and autonomous, meaning that it runs at no cost to anyone. 


How Does it Work? 
-----------------

In comparison, Particl's moderation system is similar to Reddit's well-known upvote and downvote system. On Reddit, each thread and post can be upvoted or downvoted by the community. Any Reddit user can cast a vote (an upvote or a downvote) that adds or subtracts a "point". Once a post reaches a certain negative threshold of points, meaning that a much greater number of people have downvoted the post compared to the number of people who've upvoted it, it gets automatically hidden and placed at the bottom of the list.

On Particl, listings and markets are moderated in a similar fashion. A big difference is that instead of counting votes on a "one user equals one point basis", it does it on a "one coin equals one point basis". When a listing or market reaches a certain negative threshold of points, meaning that it is generally deemed undesirable, it is hidden from view and becomes inaccessible unless the removal threshold is modified locally by the user or turned off entirely. 

Flagging
~~~~~~~~

If you find a listing that you think shouldn't be on the marketplace, you can flag it for removal. This immediately takes it off your local instance of the marketplace, casts an equal number of downvotes as the number of coins on your public PART balance, and moves it to the *Reported Listings* page where others can now upvote or downvote it. While you won't see a listing you’ve flagged on your local copy of the marketplace, it will still show up on others as long as it does not cross the removal threshold.

Upvoting and downvoting
~~~~~~~~~~~~~~~~~~~~~~~

If you navigate to the *Reported Listings* page, you’ll find all the listings that other people have flagged. You’ll also find any listing you’ve previously flagged that has not yet received enough downvotes to be completely filtered off the marketplace by the moderation system.

It is also where you can cast upvotes and downvotes for listings that other people have flagged. When you cast a vote, it adds or subtracts a number of points equal to the number of PART coins you hold in your public balance.

Adjustable removal threshold
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The removal threshold is the agreed-upon point requirement for a listing to remain on the marketplace. When a listing accumulates more downvotes than that threshold, it gets filtered off for everyone using the default values of the moderation system.

However, this threshold is user-adjustable at the local level and can be modified by editing a marketplace configuration file. While doing this doesn't affect the removal threshold of other people, it allows you to see, on your local version of the marketplace, listings that have received more downvotes than the default removal threshold. In the same way, it also allows you to make your filtering parameters more sensitive and filter off listings even before they reach the default removal threshold. 

In other words, it gives you full control over your e-commerce experience while avoiding outright censorship and still providing a decent level of moderation to keep the user experience viable for most people.

At this time, the delisting threshold is currently set at |Threshold|, which means a listing has to get a moderation score (upvote/downvote ratio) of |Threshold| to be taken off the Particl network.

Why use coins as voting tickets?
--------------------------------

To understand why Particl uses coins to count votes and not the number of users that vote, you have to remember that the protocol never knows anything about any of its users in the first place. 

To game the moderation system, it would be very easy to create an infinite number of Particl identities and cast multiple upvotes or downvotes to certain listings. No one would ever know about it, and there'd be no way for Particl to detect this dishonest and fraudulent behavior.

PART coins, on the other hand, are the perfect voting tickets. They can't be faked, created out of thin air, or duplicated. There is a fixed number of them in circulation, and they grant everyone an equal opportunity to either increase or decrease their total voting power. The more PART coins you hold, the greater your voting power becomes.

This system also prevents outside influence from outside parties by ensuring that only those with real stakes in the network can have a say over its moderation policies.

Game-Theory
~~~~~~~~~~~

Using coins as voting tickets also involves a bit of game theory which solidifies the system. By definition, game theory simply refers to the `study of mathematical models of strategic interaction among rational decision-makers <https://en.wikipedia.org/wiki/Game_theory>`_. In the case of a distributed and open moderation system, it is how people can be forced into behaving rationally.

To understand why that is, we have to keep in mind that a PART coin is a unit of digital currency with a value that fluctuates depending on many factors. This includes the amount of activity on the marketplace, but also its user growth, general appeal to other people, financial market speculation, reputation, etc.

Generally speaking, moderating the marketplace irrationally (i.e., sellers dishonestly flagging each other's listings or leaving immoral listings on it) directly leads to fewer people using the marketplace. And when fewer people use the marketplace, the PART coin itself can reduce in value, just like the size of the dividend-like staking rewards it pays as well.

For this reason, Particl users are directly and financially incentivized to keep the platform as clean and fairly moderated as possible.

Considerations
--------------

- Because there is no way to enforce any predefined bans on a distributed network, you may encounter listings that you don't like from time to time. It is important that you flag these products if you believe they shouldn't be on the marketplace.
- For your coins to count as votes, they need to be held in your :guilabel:`Public` balance. Coins held in your Blind or Anon balance cannot count towards moderation votes.
- If you don’t like how the community moderates the marketplace, you can always tweak your removal threshold for more lenient or sensitive parameters.

----

.. seealso::

 - Marketplace Explained - :doc:`Particl Marketplace Explained <../particl-marketplace/marketplace_explained>`
 - PART Guides - :doc:`Send, Receive and Convert PART <../part-guides/partguides_sendreceiveconvert>`
 - Marketplace Guides - :doc:`Install and Get Started <../marketplace-guides/marketguides_installation>` 