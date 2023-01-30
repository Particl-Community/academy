=======================
Enable or Disable Coins
=======================

.. title::
   BasicSwap DEX Coin Usage Guide
   
.. meta::
   :description lang=en: Learn how to enable or disable coins on your BasicSwap instance.
   :keywords lang=en: Particl, DEX, Trading, Exchange, Buy Crypto, Sell Crypto, Installation, Quickstart, Blockchain, Privacy, E-Commerce, multi-vendor marketplace, online marketplace

By default, :term:`BasicSwap <BasicSwap>` only comes with Particl enabled, but you can easily enable other coins that you want to trade.

This guide will show you how to enable or disable coins on BasicSwap.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

.. attention::

     Currently, each coin you add has to be added **one by one**. Repeat the following step for each coin you want to enable.

.. attention::

     Currently, adding a new coin to BasicSwap requires you to download its blockchain locally. We are working on adding more options, such as using light services and access gateways (i.e., web), which will be available at a later beta stage. 

BasicSwap on Docker
===================

If you've built :term:`BasicSwap` using the Docker method, follow these steps to enable or disable coins your instance to the most up-to-date version.

.. tabs::

     .. group-tab:: Enable Coins 

         .. rst-class:: bignums

             #. Stop the docker image (this will shut down all BasicSwap processes).

                 .. code-block:: bash

                     docker-compose stop
                     
             #. If you haven’t set your COINDATA_PATH variable permanently in your :guilabel:`.env` file, you’ll need to export the variable first. 
             
                .. code-block:: bash

                   export COINDATA_PATH=/var/data/coinswaps        

             #. Enable coins by typing the following commands accompanied by the coin you want to enable after the :guilabel:`--addcoin`.

                 .. code-block:: bash

                     docker run --rm -t --name swap_prepare -v $COINDATA_PATH:/coindata i_swapclient basicswap-prepare --datadir=/coindata --addcoin=bitcoin

         .. note::

             You can copy an existing pruned datadir (excluding :guilabel:`bitcoin.conf` and any wallets) over to :guilabel:`$COINDATA_PATH/bitcoin`. Remove any existing wallets after copying over a pruned chain, or the Bitcoin daemon won't start.

     .. group-tab:: Disable Coins

         .. rst-class:: bignums

         .. rst-class:: bignums

             #. Stop BasicSwap completely.

                 .. code-block:: bash

                     docker-compose stop

             #. Remove the coin's record in the :guilabel:`basicswap.json` config file.

                 .. code-block:: bash

                     sudo nano /var/data/coinswaps/basicswap.json

                 In this example, here is the excerpt you would remove from :guilabel:`basicswap.json` if you wanted to remove Monero.

                 .. code-block:: bash

                         "monero": {
                                 "connection_type": "rpc",
                                 "manage_daemon": true,
                                 "manage_wallet_daemon": true,
                                 "rpcport": 29798,
                                 "zmqport": 30898,
                                 "walletrpcport": 29998,
                                 "rpchost": "127.0.0.1",
                                 "walletrpchost": "127.0.0.1",
                                 "walletrpcuser": "xmr_wallet_user",
                                 "walletrpcpassword": "xmr_wallet_pwd",
                                 "walletfile": "swap_wallet",
                                 "datadir": "/coindata/monero",
                                 "bindir": "/coindata/bin/monero",
                                 "restore_height": 2731435,
                                 "blocks_confirmed": 7,
                                 "walletsdir": "/coindata/monero"
                         },

             #. Launch BasicSwap normally.

                 .. code-block:: bash

                     COINDATA_PATH=/var/data/coinswaps && docker-compose up 

BasicSwap Without Docker
========================

If you've built :term:`BasicSwap` without using the Docker method, follow these steps to add or remove coins to your BasicSwap instance.

.. tabs::

     .. group-tab:: Enable Coins

         .. rst-class:: bignums

             #. Stop BasicSwap completely.

                 .. code-block:: bash

                     docker-compose stop

             #. Enable coins by typing the following commands accompanied by the coin you want to enable after the :guilabel:`--addcoin`.

                 .. code-block:: bash

                     export SWAP_DATADIR=/Users/$USER/coinswaps
                     basicswap-prepare --usebtcfastsync --datadir=/$SWAP_DATADIR --addcoin=bitcoin

             #. Activate the change to your BasicSwap instance.

                 .. code-block::

                     export SWAP_DATADIR=/Users/$USER/coinswaps
                     . $SWAP_DATADIR/venv/bin/activate && python -V

         .. note::

             You can copy an existing pruned datadir (excluding :guilabel:`bitcoin.conf` and any wallets) over to :guilabel:`$COINDATA_PATH/bitcoin`. Remove any existing wallets after copying over a pruned chain, or the Bitcoin daemon won't start.

     .. group-tab:: Disable Coins

         .. rst-class:: bignums

             #. Stop BasicSwap completely.

             #. Remove the coin's record in the :guilabel:`basicswap.json` config file.

                 .. code-block:: bash

                     sudo nano /Users/$USER/coinswaps/basicswap.json

                 In this example, here is the excerpt you would remove from :guilabel:`basicswap.json` if you wanted to remove Monero.

                 .. code-block:: bash

                         "monero": {
                                 "connection_type": "rpc",
                                 "manage_daemon": true,
                                 "manage_wallet_daemon": true,
                                 "rpcport": 29798,
                                 "zmqport": 30898,
                                 "walletrpcport": 29998,
                                 "rpchost": "127.0.0.1",
                                 "walletrpchost": "127.0.0.1",
                                 "walletrpcuser": "xmr_wallet_user",
                                 "walletrpcpassword": "xmr_wallet_pwd",
                                 "walletfile": "swap_wallet",
                                 "datadir": "/coindata/monero",
                                 "bindir": "/coindata/bin/monero",
                                 "restore_height": 2731435,
                                 "blocks_confirmed": 7,
                                 "walletsdir": "/coindata/monero"
                         },

             #. Once that is done, save the changes with :kbd:`CTRL` + :kbd:`X`, following by an :kbd:`ENTER`.

             #. Launch BasicSwap normally.

----

.. seealso::

 - BasicSwap Explained - :doc:`BasicSwap Explained <../basicswap-dex/basicswap_explained>`
 - BasicSwap Guides - :doc:`Install BasicSwap <../basicswap-guides/basicswapguides_installation>`
 - BasicSwap Guides - :doc:`Update BasicSwap <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Route BasicSwap Through Tor <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Make an Offer <../basicswap-guides/basicswapguides_make>`
 - BasicSwap Guides - :doc:`Take an Offer <../basicswap-guides/basicswapguides_take>`
