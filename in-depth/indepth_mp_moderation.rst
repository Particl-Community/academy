================================
Marketplace Moderation Explained
================================

Like on any online marketplace or platform, there needs to be a way for its content to be moderated. Sure, Particl is unstoppable, uncensorable, and it can't ban users. But leaving the platform without any sort of moderation mechanism would create an unspeakable number of problems.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Have a look at the outcomes before starting to dig into the deep details.

**Benefits**

- Moderation system based on direct democracy.
- Provably fair and accurate governance. 
- No pre-defined ban on certain products and services.
- Entirely distributed, doesn't require any user with special permissions.

**Considerations**

- Because there is no way to enforce any pre-defined bans on a distributed network, you may encounter products you do not like from time to time. It is important that you flag these products if you believe they shouldn't be on the marketplace.
- For your coins to count as votes, they need to be held in your :guilabel:`Public` balance. Coins held in your :guilabel:`Anon` balance don't work with the voting mechanism.

Since Particl is a distributed marketplace, there is no one in possession of any special account that would give them more power and privileges than others. That means no support staff, no moderator, no admin, no nothing there to keep spam and undesirable content away. For this reason, the moderation of the marketplace's content needs to be done differently. 

Instead of giving moderating powers to a few group of "trusted" individuals, it gives it back to everyone. Indeed, Particl's moderation system is heavily inspired by the concept of the "wisdom of the crowd" which stipulates that, typically, decisions taken collectively by large groups of people are more informed than if taken by a limited group of individuals. 

That, of course, is probably not applicable to all spheres of life, but when it comes to moderating a global and distributed marketplace, it's a perfect way to reach a fair and globally agreeable consensus and take personal or geographical bias out of the equation. :term:`Particl Marketplace` truly is the first global marketplace environment.

How Does it Work? 
-----------------

Ultimately, Particl's moderation system is very similar to Reddit's popular upvote and downvote system. On Reddit, each thread and post can be upvoted or downvoted by the community. Any Reddit user can cast a vote (an upvote or a downvote) which either adds or substract a "point". Once a post reaches a negative threshold of points, meaning that a much greater number of people have downvoted the post compared to the number of people who've upvoted it, it gets automatically hidden and placed at the bottom of the list.

On Particl, listings are moderated the same way threads and posts are on Reddit. The big difference is that instead of counting votes on a "one user equals one point basis", it does it on a "one coin equals one point basis". When a listing reaches a negative threshold of points, it gets delisted and taken off the marketplace completely. 

Flagging
~~~~~~~~

If you find a listing that you think shouldn't be on the marketplace, you can flag it for removal. This immediately takes it off your instance of the marketplace and moves it to the *Reported Listings* page where other people will now be able to upvote or downvote it. You won't see that listing on the marketplace anymore, but others still do and can purchase it up until the point when that listing accumulates enough downvotes.

Upvoting and downvoting
~~~~~~~~~~~~~~~~~~~~~~~

If you navigate to the *Reported Listings* page, you'll find all the listings that have been flagged by other people. You'll also find any listing that you've previously flagged and that have not yet received enough downvotes to be completely taken off the marketplace.

It is also where you can cast upvotes and downvotes for listings that have been flagged by other people. When you cast a vote, it adds or substracts a number of points equal to the number of PART coins you hold in your public balance. 

When a reported listing reaches a number of points lower than the minimum allowed by the network, it gets completely taken off Particl for everyone, even for those who've never seen the listing in the first place. This delisting process also permanently deletes a listing from the *Reported Listings* page. 

Adjustable thresholds
~~~~~~~~~~~~~~~~~~~~~

The delisting threshold is the agreed upon point requirement for a listing to remain on the marketplace. When a listing accumulates more downvotes than the agreed upon threshold, it gets deleted from the marketplace for everyone.

This threshold is adjustable and collectively agreed upon by the community. It's also possible to manually change the delisting threshold of your own client by modifying the correct :term:`Particl Desktop` configuration file on your computer. This doesn't affect the threshold of other people, but it can allow you to make quick changes, if needed, without having to wait for a new :term:`Particl Desktop` client update to change the threshold.

The delisting threshold is currently set at |Threshold|, which means a listing has to get a moderation score (upvote/downvote ratio) of |Threshold| to be taken off the Particl network.

Benefits
--------

Provably fair
~~~~~~~~~~~~~

Particl's moderation system is powered by blockchain technology which makes it provably fair. It cannot be tricked and creates an equal level playing field for everyone. The system makes it impossible for anyone to fraudulently inflate their voting power. It is pure, unadultered direct democracy in action.

No pre-defined restrictions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Particl is a completely distributed network. For this reason, it cannot effectively enforce any restriction on products or services being offered, unlocking the full potential of *free market* on a global scale. The marketplace's moderation policies are solely based on the votes of its users. 

Free to use
~~~~~~~~~~~

Typically, online marketplaces include the costs of moderating their platform into the sales commission paid by sellers. That's because moderating a marketplace is costly and requires quite a bit of logistics. Staff needs to be hired, policies need to be drafted along with a legal team, and etc. 

Particl's moderation system doesn't need to deal with that at all. It is completely distributed and autonomous. And although it requires coins to flag listings and vote on them, it doesn't cost anything at all. Not even the usual :term:`cryptocurrency <Cryptocurrency>` transaction fee!

Coins as voting tickets?
------------------------

To understand why Particl uses coins to count votes and not the number of users that vote, you have to remember that it never ever knows anything about any of its users in the first place.

To game the moderation system, it would be very easy to create an infinite number of Particl identities and cast multiple upvotes or downvotes to certain listings. No one would ever know about it and there'd be no way for Particl to detect that dishonest behavior.

PART coins, on the other hand, are the perfect voting tickets. They can't be faked, created out of thin air, or be duplicated. There is a fixed number of them in circulation and they grant everyone with an equal opportunity to either increase or decrease their total voting power. The more PART coins you hold, the greater your voting power becomes.

This system also prevents outside influence from outside parties by ensuring that only those real stake in the network can have a say over its moderation policies.

Game-Theory
~~~~~~~~~~~

Using coins as voting tickets also involves a bit of game theory which solidifies the system. By definition, game theory simply refers to the `study of mathematical models of strategic interaction among rational decision-makers <https://en.wikipedia.org/wiki/Game_theory>`_. In the case of a distributed and open moderation system, it is how people can be forced into behaving rationally.

To understand why that is, we have to keep in mind that a PART coin is a unit of digital currency with a value that fluctuates depending on many factors. This includes the amount of activity on the marketplace, but also its user growth, general appeal to other people, financial market speculation, and etc.

Generally speaking, moderating the marketplace irrationally (i.e. sellers dishonestly flagging each other's listings or leaving immoral listings on it) directly leads to less people using the marketplace. And when less people use the marketplace, the value of the PART coin itself can have a hard time going up, just like the size of the :doc:`dividend-like staking rewards <../in-depth/indepth_staking>` it pays as well.

For this reason, Particl users are directly and financially incentivized to keep the platform as clean and fairly moderated as possible.

Keep in Mind
------------

- Because there is no way to enforce any pre-defined bans on a distributed network, you may encounter listings that you don't like from time to time. It is important that you flag these products if you believe they shouldn't be on the marketplace.
- For your coins to count as votes, they need to be held in your :guilabel:`Public` balance. Coins held in your Anon balance won't count towards moderation votes.

----

.. seealso::

 Other sources for useful or more in-depth information:

 - Particl Wiki - `Community governance <https://particl.wiki/learn/marketplace/governance/>`_
 - Particl News Blog - `Particl Explained – Decentralized Marketplace Moderation <https://particl.news/particl-explained-decentralized-marketplace-moderation-7daa3c75d5b2/>`_ 
 - Particl News Blog - `Particl – Community Crowdfunding System <https://particl.news/new-community-crowdfunding-system-f31f54231982/>`_ 
 