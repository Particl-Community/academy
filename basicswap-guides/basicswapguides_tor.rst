==========
Enable Tor
==========

.. title::
   BasicSwap DEX Tor Usage Guide
   
.. meta::
   :description lang=en: Learn how to enable Tor on BasicSwap.
   :keywords lang=en: Particl, DEX, Trading, Exchange, Buy Crypto, Sell Crypto, Installation, Quickstart, Blockchain, Privacy, E-Commerce, multi-vendor marketplace, online marketplace

By default, connections to the :term:`BasicSwap <BasicSwap>` network are public, much like connecting to other P2P networks (i.e., torrents). However, you can easily anonymize your network information (i.e., IP address, location) by routing your BasicSwap connection through the privacy-preserving `Tor network <https://www.torproject.org/>`_.


This guide will show you how to protect your network information by routing BasicSwap's connection through the Tor network.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

.. attention::

    Tor integration into BasicSwap is experimental and only officially supported for Docker installations. 

    **Always keep Tor up-to-date with the latest version.** Failure to do so may incur more risks than benefits.

Create Initial Files
====================

If you're about to connect BasicSwap to Tor for the first time, you first need to create Tor configuration files.

.. rst-class:: bignums

#. Create the initial files BasicSwap needs to connect to the Tor network. Docker will create directories instead of files if these don't exist.

    .. code-block:: bash
    
       touch $COINDATA_PATH/tor/torrc

Enable Tor on First Startup
===========================

If you are doing a fresh installation of BasicSwap and want to route it through the Tor network, the :guilabel:`torrc` configuration file won't exist yet. Follow these instructions to create it.

.. rst-class:: bignums

    #. Install BasicSwap through the installation process detailed :doc:`here <../basicswap-guides/basicswapguides_installation>`.  

    #. Create the :guilabel:`torrc` configuration file by typing these two commands **one by one**.

       .. code-block:: bash

          docker compose -f docker-compose_with_tor.yml run --name tor --rm tor \
                tor --allow-missing-torrc --SocksPort 0.0.0.0:9050

          docker compose -f docker-compose_with_tor.yml run -e TOR_PROXY_HOST=172.16.238.200 --rm swapclient \
                basicswap-prepare --usetorproxy --datadir=/coindata --withcoins=monero,particl

    #. Start BasicSwap with the following command.
    
       .. code-block:: bash          

          docker compose -f docker-compose_with_tor.yml up   

Enable Tor
==========

If you have been using BasicSwap previously and want to enable Tor now, you can easily activate it with a single command.

.. rst-class:: bignums

    #. Shutdown BasicSwap entirely.

    #. Enable Tor and make the required modifications to your data directory.

       .. code-block:: bash

          docker compose -f docker-compose_with_tor.yml run -e TOR_PROXY_HOST=172.16.238.200 --rm swapclient \
                basicswap-prepare --datadir=/coindata --enabletor

    #. Start BasicSwap along with Tor.

       .. code-block:: bash

          export COINDATA_PATH=/var/data/coinswaps && docker compose -f docker-compose_with_tor.yml up

Update Coins Through Tor
========================

.. rst-class:: bignums

    #. Shutdown BasicSwap entirely.

    #. Start a Tor-connected BasicSwap instance in the background.

       .. code-block:: bash

          docker compose -f docker-compose_with_tor.yml up -d tor

    #. Update the coin you want by typing this command and modifying the :guilabel:`withcoins` argument.

       .. code-block:: bash

          docker compose -f docker-compose_with_tor.yml run -e TOR_PROXY_HOST=172.16.238.200 --rm swapclient \
                basicswap-prepare --usetorproxy --datadir=/coindata --preparebinonly --withcoins=bitcoin

    #. Once the process from the last step completes, shutdown BasicSwap instance running in the background. 

       .. code-block:: bash

          docker compose -f docker-compose_with_tor.yml stop

Disable Tor
===========

.. rst-class:: bignums

    #. Shutdown BasicSwap entirely.

    #. Enable Tor and make the required modifications to your data directory.

       .. code-block:: bash

          docker compose -f docker-compose_with_tor.yml run --rm swapclient \
                basicswap-prepare --datadir=/coindata --disabletor

    #. Start Tor normally.

       .. code-block:: bash

          export COINDATA_PATH=/var/data/coinswaps && docker-compose up

----

.. seealso::

 - BasicSwap Explained - :doc:`BasicSwap Explained <../basicswap-dex/basicswap_explained>`
 - BasicSwap Guides - :doc:`Install BasicSwap <../basicswap-guides/basicswapguides_installation>`
 - BasicSwap Guides - :doc:`Update BasicSwap <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Make an Offer <../basicswap-guides/basicswapguides_make>`
 - BasicSwap Guides - :doc:`Take an Offer <../basicswap-guides/basicswapguides_take>`
