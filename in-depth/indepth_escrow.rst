Two-Party Escrow
================

To secure transactions and force you and the person you're transacting with to stay honest, Particl uses a unique *two-party escrow* system. It is free to use and entirely autonomous, but it's probably a bit different than what you've used in the past. 

This in-depth guide will explain everything you need to know about this unique escrow model so that it won't be any mystery to you anymore!

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

The Issue With Typical Resolution Centers
--------------------------------------

Traditional marketplaces, just like any company that processes payments, need to provide some form of security to the person that sends the payment and the one that receives it. This is commonly accomplished by having the funds held into an escrow account controlled by an impartial third-party (the escrow agent).

When two parties transact on a marketplace, a third-party (the escrow agent) holds the payment until the transaction is completed. That role is typically assumed by the marketplace itself (i.e. Amazon), a payment processor (i.e. Paypal, Visa), or third-party escrow services (i.e. a bank or a financial institution). 

The introduction of an impartial third-party in the middle of all transactions allows disputes and issues to be settled, but it also causes a lot of friction and introduces a few issues. These can become pretty troublesome, especially if the third-party in charge of the escrow account isn't as impartial or honest as it should. 

High escrow fee
^^^^^^^^^^^^^^^

No service provided is ever provided for free. That's also the case with the escrow services provided by online marketplaces. Running escrow services can be costly for a company. They need to hire staff, deploy a secure system to secure the funds, define clear and rigid policies, have the legal team look over everything, and etc. This is why they always charge an escrow fee. On some online marketplaces, they'll clearly tell you the escrow fees, but it's usually just added to the final commission taken by the marketplace everytime you or a vendor makes a sale.

Incorrect resolutions
^^^^^^^^^^^^^^^^^^^^^

Decisions rendered by an escrow agent usually follow a very rigid set of resolution policies rather than being settled on a case-by-case basis. This, of course, allows a great number of issues to be resolved in a fast and efficient way, but it also brushes over a lot of cases that should probably be looked into more deeply.

Fraud and abuse
^^^^^^^^^^^^^^^

Knowing that escrow agents typically don't process issues on a case-by-case basis, scammers have perfected the art of abusing escrow resolution policies and tricking escrow agents. Even on very popular platforms like eBay or Paypal, "escrow scams" are rampant and successfully steals thousands upon thousands of dollars every single day from people around the world.

One of the best example of an escrow scam is with the infamous but very prominent "return scam". Let's say you put up an item worth $1,000 for sale online. The scammer will buy it from you, pay for the item and wait to receive it. Once he does, he will claim it isn't working and request a refund. A refund requires them to ship back the item in the same package, which is what they do. But instead of putting your item back in the package, they'll put scraps worth nothing, but weighting the same your item. This is often enough to trick the automated process used by escrow agents and receive their refund. 

The results in you getting your item stolen and not getting any money for it. The scammer gets to get your item and keep all of his money. This happens every day, all day, to thousands of honest people around the world. 


Intrusive data requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To make a decision and resolve a dispute, an escrow agent needs to know as much as possible about you and the party you're transacting with. It also needs to know all of the details of the transaction under dispute. All of this information is stored on a central database for further reference by the escrow agent and its partners.

This is an obvious case of storing too much data which can easily lead to damaging data breaches. The more data a company collects about its users, the bigger the target becomes on their database.

No privacy at all
^^^^^^^^^^^^^^^^^

When using an escrow service, you and the other party you're transacting with both need to put your full trust into the escrow agent choosen to secure the transaction. That's because you are granting that party full access to a lot of sensitive information about you.

Not only do you need to trust that it will secure your data the right way, you also need to trust its integrity. The amount of data provided to escrow agents gives them a full overview of all your personal, professional, and financial activities on the platform you're transacting on. Not only do they have to be impartial, they also need to respect your privacy to its fullest extent. 

Ultimately, the entire concept of privacy when using an escrow service relies on trust — a fragile concept when dealing, on the internet, with people you've never met.

A Radically Different Approach
------------------------------

Particl adopts a **radically different model that fixes all of these issues**. This system is called a **two-party escrow** because it only involves two party. Instead of requiring a third-party to hold payments between two parties and resolve disputes, it requires both participants to make an equal security deposit into a completely autonomous smart-contract. This security deposit is automatically refunded to both parties, without any fee, once the transaction is completed. 

If any dispute or issue arises from a transaction, a resolution needs to be agreed to by both parties before they can get back their security deposit.

This escrow system **naturally leads both parties to remain honest with each other and reach reasonable resolutions** is a dispute or issues arises. That's because they both have a security deposit on the line which they can't get back unless both parties agree to a resolution. 

Game theory
^^^^^^^^^^^

This two-party escrow system relies heavily on the strong principles of *game theory*. By definition, game theory simply refers to the `study of mathematical models of strategic interaction among rational decision-makers <https://en.wikipedia.org/wiki/Game_theory>`_. In other words, how can Particl **reward rational, honest decisions** and also **punish irrational, dishonest decisions** at the same time.

To accomplish that, Particl takes on a unique approach to the *Mutually Assured Destruction (MAD)* game theory and gives it a financial twist. "MAD" is a military doctrine "based on the theory of deterrence, which holds that the **threat of using strong weapons against the enemy prevents the enemy's use of those same weapons**. The strategy is a form of *Nash equilibrium* in which, once armed, neither side has any incentive to initiate a conflict or to disarm" (`Wikipedia <https://en.wikipedia.org/wiki/Mutual_assured_destruction>`_). Simply put, when two countries are armed with nuclear weapons, there is no incentive for any of them to attack each other as that would inevitably result in an equally destructive retaliation. This would, ultimately, leave both countries in rumbles and make no winner.

Particl takes that same military doctrine and substitutes weapons of war for financial stakes. When you buy or sell something on the marketplace, you and the other party you're transacting with are required to lock an equal security deposit paid in PART coins in a smart-contract. If one of the two parties tries to scam the other or doesn't act in full honesty, the "victim" can **retaliate by not authorizing the release of the bad actor's security deposit**.

Even just trying to cheat can lead you to lose your security deposit unless you can find a reasonable resolution with the other party. That's because you need the other party you're transacting with to authorize the release of your security deposit.

And so, just like the military superpowers of this world, Particl uses the proven mathematical model behind the MAD game theory to enforce honesty and accountability among all of its participants.

Smart-contracts and automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A *smart-contract* is a special type of blockchain script that can accomplish tasks and execute transactions autonously just by following an immutable set of rules. This is how Particl is able to automate its two-party escrow system. Smart-contracts are programmed with a set of rules, pre-defined by the mathematical model of the MAD game theory, and they automatically tell the network when to execute payments and coordinate the security deposit refunds.

Smart-contracts are how Particl's two-party escrow system is able to run on its own without requiring any human intervention or maintenance. 

Benefits
--------

Particl's two-party escrow system is a novel way to secure online transactions and has only recently been made possible thanks to the rise of blockchain technology and cryptocurrencies. It unlocks several benefits and gives Particl's escrow system a few unique advantages over the more traditional escrow systems.

No fee, 100% free to use
^^^^^^^^^^^^^^^^^^^^^^^^

Escrow transactions on Particl are **completely free and do not cost any commission**. The only small fee you need to pay is the typical transaction fee attached to any cryptocurrency transaction. But don't worry, that fee is usually just a few cents or sometimes even less than that.

You're in control
^^^^^^^^^^^^^^^^^

You and the other party you're transacting with are in full control of your destiny. There is no third-party involved in the transaction, so you know that **bad decisions can't be forced on you** without you having any say at all.

Your data is safe
^^^^^^^^^^^^^^^^^

Particl's two-party escrow system has **no data requirement**. It works entirely autonomously using the simple but strong mathematical principles of MAD game-theory. If you're not honest or if you misbehave, the other party can block the release of your security deposit. There's **no need to know anything about you, actions speak louder than words**!

Much better privacy
^^^^^^^^^^^^^^^^^^^

Since there isn't any third-party sitting in the middle of all your transactions, **every single bit of detail about their nature remain confidential** between you and the parties you're transacting with. There's simply nobody in the world that can know anything about it. It's the **digital equivalent of making an in-person cash purchase or sale**.