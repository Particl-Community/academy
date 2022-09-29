====================
Community Governance
====================

.. title::
   Community Governance Explained

.. meta::
      :description lang=en: Get familiar with the community governance of the Particl DAO. Decentralized, private, and autonomous decision-making.

Particl has a :term:`decentralized <Decentralization>` community governance mechanism that gives you a voice in the ecosystem's most critical decisions. The model uses the Particl Proof-of-Stake (:term:`PPoS`) staking protocol to let you cast votes on community proposals.

Particl's :term:`decentralized <Decentralization>` community governance model puts you in control and gives you the tools you need to make almost anything happen. 

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Decentralized Governance
------------------------

In the :term:`cryptocurrency` industry, :term:`decentralized <Decentralization>` governance refers to the ability of a community to publish, debate, and vote on various proposals and issues using distributed tools. It seeks to balance control over a particular project from a small group of individuals to a broader community. Depending on the project being governed, the level of decentralization can vary, giving more or less power to its community and greater resilience against attacks.

Ideally, :term:`decentralized <Decentralization>` governance mechanisms strive to use properly distributed tools to run voting rounds in a provably fair manner. This eliminates third-party risks associated with voting manipulation and unfair influence over the outcome of a vote.

Particl's model in a nutshell
=============================

The Particl project is all about decentralization, security, privacy, and personal freedom. That's why its governance model follows a :term:`decentralized <Decentralization>`, fair, and transparent process.

Anyone from the Particl community can publish proposals on the CCS platform. Each proposal has to first go through a discussion phase, after which it gets moved to a voting phase. That's when the rest of the community can vote to either approve or reject the proposal using their staking power.

To support community initiatives and provide the initial capital they require, Particl has a :term:`decentralized <Decentralization>` treasury fund that is automatically funded by the :term:`blockchain`. Proposals can request funds from it to help bootstrap initiatives as long as they directly benefit the Particl ecosystem.

Community Proposals
-------------------

When it comes to Particl's :term:`decentralized <Decentralization>` governance model, proposals refer to any proposed initiative, project, protocol change, or request of funds from any individual or group.

For proposals to be considered “valid” within Particl’s model, they are required to benefit and bring value to the ecosystem directly. There is no other hard requirement other than to follow the general CCS rules and guidelines.

CCS Platform
============

Proposals are published on the Community Crowdfunding System (CCS) platform. Forked from Firo’s adaptation of Monero’s CCS system, this platform is hosted on GitHub and tracks the lifecycle of a proposal, from edits to comments and voting results. This guarantees the maximum level of transparency.

When published, a proposal initially goes through a discussion phase (:guilabel:`Ideas`) where others can add comments to what's being proposed. During that phase, the proposal's owner(s) can modify its proposition based on the feedback received. Any change made at this stage is transparent and clearly displayed on the proposal's page.

Then, the proposal moves to the :guilabel:`Funding Required` phase to collect the capital it needs for the proposed initiative to get started. A proposal can either request donations from the community or request funds from the :term:`decentralized <Decentralization>` treasury.

Once a proposal is fully funded, it moves to the :guilabel:`Work in Progress` phase, where its owner(s) will get to work. Funds are disbursed to the appropriate party based on pre-defined milestones in the proposal. Milestone-based fund payouts ensure that funds are only used for their promised purpose.

Finally, a proposal is moved to the :guilabel:`Completed Tasks` phase after every milestone has been completed and the project delivered in full.

Decentralized Treasury
======================

Proposal owners can request funds from Particl's :term:`decentralized <Decentralization>` treasury fund to get the startup capital required to kickstart their initiatives. For a claim to be accepted and for funds to be attributed (on a milestone basis) to the owner, it needs to be approved by the community through a community vote.

Particl's :term:`decentralized <Decentralization>` treasury fund is powered by Particl's staking protocol and self-funded using a portion of the network's block rewards. Every time a block is found and validated by a staker, 50% of the staking rewards it contains is automatically deposited into the treasury fund by the protocol.

No coin from the treasury fund can be used or transacted without the community's consensus, which is determined by an on-chain vote.

On-Chain Voting
---------------

Voting rounds on Particl are conducted in a :term:`decentralized <Decentralization>` and provably fair manner. Only active stakers, referred to as "stakeholders" in the specific context of an on-chain vote, can cast votes on proposals. This ensures only individuals with a vested interest in the project can govern its most important decisions.

The process of voting and counting votes leverages the Particl Proof-of-Stake (:term:`PPoS`) staking protocol, and every round's results are publicly inscribed on the :term:`blockchain` permanently. This provides the maximum level of transparency and security possible, making it impossible to modify past results or misreport voting outcomes.

To determine each individual’s voting power, the voting preference of a staker is only counted when they find a block. Then, at the end of a voting round, all the blocks within the voting round’s timeframe are scanned, and each block with a vote inscribed in it is counted towards the final tally. In other words, the more a single staker finds blocks, the more voting power they hold.

Voting rules and parameters depend on the type of proposals being voted on.

Non-Protocol Consensus-Changing Proposals
=========================================

+---------------+----------------------------------------------+
|     Quorum    | 20% of all the blocks during a voting period |
+---------------+----------------------------------------------+
| Approval Rate |                >= 60% in favor               |
+---------------+----------------------------------------------+
|    Duration   |             5,040 blocks minimum             |
+---------------+----------------------------------------------+

The first type of proposal, non-protocol consensus-changing proposals, does not require significant changes to the protocol. Typically, they would be proposals requesting funds from the treasury fund to kickstart a specific project, for example.

For a non-protocol consensus vote to be considered "valid", its voting period must be a minimum of 5,040 blocks (roughly one week). Within that period, 20% of the blocks staked are required to have a vote inscribed in them. That means the quorum, or participation rate, has to be at least 20%.

Finally, to be considered "approved" by the community, it needs to reach an approval rate of at least 60%, meaning at least 60% of all the votes cast for the proposal approve the proposed idea.

Protocol Consensus Changing Proposals
=====================================

+---------------+----------------------------------------------+
|     Quorum    | 20% of all the blocks during a voting period |
+---------------+----------------------------------------------+
| Approval Rate |                >= 75% in favor               |
+---------------+----------------------------------------------+
|    Duration   |             10,080 blocks minimum            |
+---------------+----------------------------------------------+

The other type of proposals, protocol consensus-changing proposals, are typically more critical in scope and can significantly impact the ecosystem. Consensus-changing proposals are proposals that require a specific change in the protocol, such as, for example, modifying the inflation rate of the :term:`blockchain` or introducing a new privacy technology.

Just like non-protocol consensus-changing proposals, their quorum requirement stands at 20%. But because of their increased level of importance and ramifications, they require a higher level of approval from the community. In fact, the required approval rate has to be at least 75%. Finally, the duration of any protocol consensus vote has to be a minimum of 10,080 blocks (roughly two weeks) to give ample time to anyone to be able to cast their vote.

----

.. seealso::

 * Particl Explained - :doc:`DAO and Network Treasury <../particl-blockchain/blockchain_dao>`
 * Particl Explained - :doc:`Staking Guide <../particl-blockchain/blockchain_staking>`
 * PART Guide - :doc:`Buy and Sell PART <../particl-blockchain/blockchain_buysell>`
 * PART Guides - :doc:`Staking Guide <../part-guides/partguides_staking>`
 * PART Guides - :doc:`Send, Receive, and Convert PART <../part-guides/partguides_sendreceiveconvert>`
 * PART Guides - :doc:`Particl Desktop Wallet <../part-guides/partguides_desktop>`
 * Particl Wiki - `How to Vote on Proposals <https://particl.wiki/tutorial/staking/how-to-vote/>`_