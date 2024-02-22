===================
BasicSwap Explained
===================
 
.. title::
     BasicSwap DEX Explained

.. meta::
      
      :description lang=en: Overview of the BasicSwap DEX protocol and its local desktop client.
 
:term:`BasicSwap <BasicSwap>` is a cross-chain and privacy-centric :term:`DEX <DEX>` (decentralized exchange) that lets you trade cryptocurrencies without middleman interference. Its distributed ledger technology enables users to place or accept orders without fees, promoting a free and open trading environment devoid of central points of failure.

Developed as a countermeasure to the intrusive data collection and demands prevalent in modern :term:`cryptocurrency` exchanges and third-party services, BasicSwap aims to restore sovereignty and privacy to cryptocurrency trading for users worldwide.

----
 
.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2
 
----

What is it?
^^^^^^^^^^^

.. figure:: ../_static/media/images/basicswap_orders.png
    :align: center
    :alt: BasicSwap's order book — WIP, design subject to change
    :target: ../_static/media/images/basicswap_orders.png

    BasicSwap's order book — WIP/Beta, UI/UX subject to change

The :term:`BasicSwap` decentralized exchange (DEX) is designed for ease of use and clarity in operation, but its underlying protocol is rather intricate and sophisticated.

It incorporates several distributed and open-source technologies, including atomic swaps, scriptless scripts, adaptor signatures, and the SMSG network to function independently without the need for centralized servers, databases, or administrative staff. Instead, it is developed, upheld, and operated by an extensive, decentralized community of open-source contributors and participants.

Benefits
---------

:term:`BasicSwap` distinguishes itself from conventional exchanges, often known as “centralized exchanges” or “CEX,” through its decentralized framework which offers several key advantages:

* **No trading fees** — Trading fees are a thing of the past.
* **Total privacy** — Your data and personal information remain confidential.
* **Secure** — A non-custodial model ensures unparalleled security for your assets.
* **No KYC or account** — Account creation or KYC documentation is not required.
* **Complete freedom** — No bans, geographical restrictions, or asset confiscations.
* **Unstoppable** — It is immune to censorship or shutdown.
* **Autonomous** — Operates independently without human intervention.

These benefits stem directly from the inherently :term:`decentralized <Decentralization>` nature of the BasicSwap protocol and aren't possible on centralized infrastructure.

Features
--------

Currently in beta, BasicSwap already supports essential trading functionalities typical of centralized exchanges, with ongoing developments to introduce additional features.

* **True cross-chain support** — Swap cryptocurrencies across different blockchains, like Bitcoin and Monero.
* **Distributed order book** — Place or accept limit orders through a fully distributed order book.
* **No third-party or middleman** — Offers direct crypto trades without intermediaries.
* **No trading fees** — You are only subject to standard :term:`cryptocurrency` network fees, eliminating any other additional trading costs.
* **Privacy from the ground up** — Designed with a privacy-first approach in all components.
* **Full Monero support** — Provides direct swaps between Monero and other cryptocurrencies, such as Bitcoin, Litecoin, or Particl, without relying on wrapped assets or convoluted L2 layers.
* **User-friendly interface** — Features a straightforward and intuitive interface, simplifying complex processes for the user.

Compatible Coins
^^^^^^^^^^^^^^^^

.. figure:: ../_static/media/images/basicswap_wallets.png
    :align: center
    :alt: BasicSwap's wallets page — WIP, design subject to change
    :target: ../_static/media/images/basicswap_wallets.png

    BasicSwap's wallets page — WIP/Beta, UI/UX subject to change

:term:`BasicSwap` provides decentralized trading services for a selection of cryptocurrencies. (`check out the full list on BasicSwap website <https://basicswapdex.com/markets>`_).

+----------------------------------+---------------------------------------------+
| **Coin Name**                    | **Ticker**                                  |
+----------------------------------+---------------------------------------------+
| Bitcoin                          | BTC                                         |
+----------------------------------+---------------------------------------------+
| Monero                           | XMR                                         |
+----------------------------------+---------------------------------------------+
| Dash                             | DASH                                        |
+----------------------------------+---------------------------------------------+
| Litecoin                         | LTC                                         |
+----------------------------------+---------------------------------------------+
| Firo                             | FIRO                                        |
+----------------------------------+---------------------------------------------+
| PIVX                             | PIVX                                        |
+----------------------------------+---------------------------------------------+
| Particl                          | PART                                        |
+----------------------------------+---------------------------------------------+

Plans are underway to expand the list of available assets such as ETH and its ERC-20 tokens. Cryptocurrencies based on Bitcoin and enabled for Segwit can be seamlessly integrated with minimal effort, and token-issuing blockchains like Fantom, Solana, Avalanche, Polygon, or BSC might be incorporated into BasicSwap during later phases of our integration roadmap.

Access Gateways
^^^^^^^^^^^^^^^

Access gateways are the platforms through which end-users access and interact with BasicSwap, essentially serving as the application's graphical interface.

Given that BasicSwap is fundamentally an open DEX protocol, it can support access and usability across a diverse array of gateways.

These gateways, each with its unique advantages and limitations, may vary in presentation or feature set. However, since all gateways connect to the same underlying protocol, they are interoperable, sharing identical order books and liquidity pools. This ensures that traders can transact with each other regardless of the specific gateway they choose to use.

.. container:: toggle

    .. container:: header

        **BasicSwap Desktop**

    BasicSwap Desktop is the primary access point for the BasicSwap open beta, with plans to introduce additional gateways. It facilitates management of multiple non-custodial :term:`cryptocurrency` wallets and enables direct trading without third-party involvement. 

    **Pros:**

    * **No compromise** — Operate on BasicSwap devoid of any centralized service.
    * **Desktop access** — Directly engage with the DEX from your personal computer.
    * **Maximum privacy** — Easily achieve complete privacy during trades.

    **Cons:**

    * **Slower setup** — Manual compilation is required for the local client, making the initial setup potentially complex.
    * **No web access** — Trades must be conducted via a local client, lacking the convenience of web browser access.    
    * **Continuous online presence** — To maintain your offers on the order book and fulfill trades, your BasicSwap :term:`node <node>` must stay connected.
    * **Storage demands** — Enabling certain coins requires downloading and storing their full blockchain nodes, which can consume significant disk space.

.. container:: toggle

    .. container:: header

        **Web Gateway**

    A web gateway, which is not yet available, is planned to be released to allow DEX access via web browsers. This initiative aims to leverage the ubiquity of web applications in our digital routines and the commonality of web-based exchange platforms, positioning BasicSwap’s web gateway as a highly convenient but still secure option for trading.

    **Pros:**

    * **Universal access** — Engage with BasicSwap on any device with internet access.
    * **Quick setup** — Begin trading in moments, thanks to a streamlined setup process that eliminates the need to maintain full blockchain :term:`nodes <node>` on your device.
    * **User-friendly** — The web offers the most straightforward trading experience.

    **Cons:**

    * **Dependence on third-party nodes** — Utilizing third-party nodes slightly diminishes decentralization but maintains privacy and security through end-to-end encryption and non-custodial practices.
    * **Increased phishing risk** — Web platforms are inherently more susceptible to phishing, cloning, and social engineering schemes.

.. container:: toggle

    .. container:: header

        **Third-Party Integrations**

    BasicSwap is planned to support integrations with external applications, such as :term:`cryptocurrency` wallets, payment services, and web plugins, in a bid to broaden the ecosystem and bring its benefits to as many people as possible. Further development of a comprehensive SDK and user-friendly modules is still required to allow for this.

    **Pros:**

    * **Enhanced functionality** — Add coin swapping functionality to your products by incorporating BasicSwap DEX capabilities.
    * **Diverse access points** — Utilize BasicSwap through familiar third-party applications, like a cryptocurrency wallet for example.
    * **Web and mobile gateways** — Third-party app integration can offer the conveniences of web or mobile gateways.

    **Cons:**

    * **Reduced decentralization** — Reliance on third-party nodes can slightly impact the network's decentralized nature.
    * **Potential privacy concerns** — Third-party applications may not adhere strictly to Particl's privacy principles, posing risks of data collection or user tracking.
    * **Dependence on third-party integrity** — Trust in the third-party's implementation is essential, introducing potential risks.
    * **Introduction of custodianship** — Some third-parties may offer a custodial solution, meaning that you may not fully own your privacy keys.

----

.. seealso::
 
 - Blog Post - `BasicSwap The Fully Private Cross Chain DEX <https://particl.news/basicswap-the-fully-private-cross-chain-dex/>`_  
 - Github - `BasicSwap <https://github.com/tecnovert/basicswap>`_
 - BasicSwap Explained - :doc:`DEX Comparison <../basicswap-dex/basicswap_compared>`
 - BasicSwap Explained - :doc:`Under the Hood <../basicswap-dex/basicswap_technicals>`
 - BasicSwap Guides - :doc:`Install and Get Started <../basicswap-guides/basicswapguides_installation>`
 - BasicSwap Guides - :doc:`How to Use <../basicswap-guides/basicswapguides_usage>` 
 - BasicSwap Guides - :doc:`Add or Remove a Coin <../basicswap-guides/basicswapguides_installation>`
 - BasicSwap Guides - :doc:`Apply for Coin Listing <../basicswap-guides/basicswapguides_apply>`  
