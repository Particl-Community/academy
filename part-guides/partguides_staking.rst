=============
Staking Guide
=============

.. title::
   Particl Staking Guide

.. meta::
   :description lang=en: Learn how to enable staking for Particl’s native privacy coin. Proof-of-Stake and cold staking the easy way.

Simply by keeping an open connection to the :term:`Particl Blockchain`, you automatically earn a yearly staking interest rate of at least 4% on the total number of PART coins you hold in your public balance.

Staking also grants you the ability to vote on various community proposals, using your staking power as voting power.


----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Enabling staking is typically straightforward, though some staking solutions on Particl may necessitate additional setup effort. This guide aims to simplify the process of activating any of these solutions.

.. note::

    **Prerequisites**

    - A :term:`Particl Desktop` wallet with at least 1 PART.
    - PART coins in your :guilabel:`Public` balance.
    - An uninterrupted internet connection.
    - For cold staking, a secondary device to serve as a staking :term:`node <Node>`.

Staking your PART coins can be achieved through various methods, each with its own set of advantages, disadvantages, and activation procedures.

Enable Staking
~~~~~~~~~~~~~~

Regular staking
---------------

The quickest way to start staking is through the regular method. This simply involves opening the :term:`Particl Desktop` client and enabling the "unlock your wallet for staking only" option. Note that regular staking necessitates your computer to remain open and online at all times.

**Non-password protected client**

.. rst-class:: bignums

    #. Open your :term:`Particl Desktop` client and ensure that your :guilabel:`Public` balance contains PART coins.

That's all! As long as your :term:`node <Node>` remains connected to the internet, staking will stay active.

**Password protected client**

.. rst-class:: bignums

    #. Open your :term:`Particl Desktop` client and ensure that your :guilabel:`Public` balance contains PART coins.
    #. Click the :guilabel:`Padlock` icon in the top right corner.
    #. Select the downward arrow next to :guilabel:`Additional unlock options` in the overlay.
    #. Select the :guilabel:`Unlock for staking only` option.
    #. Input your password and click :guilabel:`Unlock wallet`.

That's all! As long as your :term:`node <Node>` remains connected to the internet and unlocked, staking will stay active.

Cold staking
------------

Cold staking, a more secure and flexible option, involves using a dedicated device that contains no coin, but can stake using delegated staking weight. This could be a hardware device, like a `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`, a `VPS/cloud server <https://en.wikipedia.org/wiki/Virtual_private_server>` (e.g., DigitalOcean, AWS, Google Cloud), or any sort of internet-connected device.

**On your staking device...**

Select a device for staking, such as a `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`, and install a Linux distribution (e.g., `Raspbian <https://www.raspberrypi.org/downloads/>`).

.. rst-class:: bignums

    #. Install Linux on your staking :term:`node <Node>`.
    #. Install the required dependencies and download the Particl cold staking app (Partyman).

    .. code-block:: bash

        sudo apt-get install python git unzip pv jq dnsutils netcat-openbsd curl net-tools
        cd ~ && git clone https://github.com/dasource/partyman

    #. Install or update :term:`Particl Core` on your staking device.

    .. code-block:: bash

        partyman/partyman install
        # Or, if updating,
        partyman/partyman update

    #. Restart Partyman to apply changes.

    .. code-block:: bash

        partyman/partyman restart now

    #. Initialize a new Particl wallet on your staking :term:`node <Node>`.

    .. code-block:: bash

        partyman/partyman stakingnode init

    #. Generate a new staking public key to link your PART coins to the staking :term:`node <Node>`.

    .. code-block:: bash

        partyman/partyman stakingnode new

Copy this staking public key, it will be needed in subsequent steps.

**On Particl Desktop...**

.. rst-class:: bignums

    #. Ensure that your :guilabel:`Public` balance contains PART coins.
    #. Within :term:`Particl Desktop`'s Wallet module, navigate to the :guilabel:`Overview`.
    #. Access the :guilabel:`Cold staking` widget and click the :guilabel:`Set up cold staking` button to input your staking public key, then enable cold staking.
    #. To immediately activate cold staking in full, use the :guilabel:`Zap` button to fast-track the progress to 100%.

**Cold staking configurations**

Adjust cold staking settings on your staking :term:`node <Node>` with these commands.

.. code-block:: bash

    # View staking statistics.
    partyman/partyman stakingnode stats

    # Redirect staking rewards to a PART address of your choosing.
    partyman/partyman stakingnode rewardaddress

    # Set marketplace fee preferences (more about this setting `here <https://particl.news/adjusting-listing-fees-4b676e230601>`_).
    partyman/partyman stakingnode smsgfeeratetarget

    # Implement firewall rules (required for port access).
    partyman/partyman firewall


Connect to a staking pool
-------------------------

Another way to stake your PART coins is to combine your staking power with other stakers. This approach allows for more frequent, albeit smaller, staking rewards. To participate, link your Particl wallet to a staking pool. 

+--------------------------+------------------------------------------+-----------+
| Pool Name                | URL/IP                                   | Pool Fees |
+==========================+==========================================+===========+
| **ColdStakingPool**      | https://coldstakingpool.com/             | 2.5%      |
+--------------------------+------------------------------------------+-----------+
| **Crymel's Pool**        | https://particl.crymel.icu/              | 2.50%     |
+--------------------------+------------------------------------------+-----------+
| **Particl Page**         | http://161.35.82.61:900/                 | 2.5%      |
+--------------------------+------------------------------------------+-----------+
| **CoinRollin**           | https://coinroll.in/                     | 1%        |
+--------------------------+------------------------------------------+-----------+

.. rst-class:: bignums

    #. Select a staking pool from the list above, visit its website, and copy the pool's staking address (e.g., ``pcs1vzuadmp42slqapdm8eevm6g8ntm3hlvgptmyjy``).
    #. Ensure that your :guilabel:`Public` balance contains PART coins.
    #. Within :term:`Particl Desktop`'s Wallet module, navigate to the :guilabel:`Overview`.
    #. Access the :guilabel:`Cold staking` widget and click the :guilabel:`Set up cold staking` button to input the pool's staking public key in the designated area, then enable cold staking.
    #. To immediately activate cold staking in full, use the :guilabel:`Zap` button to fast-track the progress to 100%.

.. Enable hardware staking
.. -----------------------

.. "Hardware staking" refers to the act of staking funds stored on a hardware device like a `Ledger Nano S <https://shop.ledger.com/products/ledger-nano-s>`_ or a `Trezor <https://trezor.io/>`_. The activation process is more technically advanced and requires you to use a different Particl client (Particl-Qt). This step-by-step guide assumes you already know how to use Particl on your hardware device and how to deposit funds on it.

.. On a Ledger Nano S device...
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

..     #. Set up your `Ledger Nano device <https://support.ledger.com/hc/en-us/articles/360007687153-Particl-PART->`_ and store funds into it.
    #. Set up a :ref:`Cold staking` :term:`node <Node>` and copy its public key or copy the public key of a staking pool :ref:`Staking Pools` into your clipboard.
    #. Download and install the latest **Particl-Qt** client `here <https://particl.io/downloads>`_.
    #. Open and unlock Particl-Qt, plug your Ledger Nano device into your computer and make sure it is ready to transact.
    #. Open the Staking setup window by going in :guilabel:`Window` > :guilabel:`Staking Setup`.
    #. Enter your staking :term:`node <Node>`'s public key in the :guilabel:`Cold staking change address` field and enable staking by clicking on the :guilabel:`Apply` button.

.. **To fully activate hardware staking, you need to "zap" your coins.**

.. rst-class:: bignums

..     #. Close Particl-Qt and open :term:`Particl Desktop`.
    #. Navigate to the wallet's :guilabel:`Overview` page located at the top of the left sidebar.
    #. Click on the :guilabel:`Zap` button to instantly bring the progress bar to 100%.

Mobile staking
--------------

Staking PART coins through a mobile wallet, such as `Particl Copay <https://particl.io/downloads/>`_, is also feasible. Staking via your phone is secure and involves delegating your coins' staking power to a staking :term:`node <Node>`.

.. rst-class:: bignums

    #. Setup a :ref:`cold staking` :term:`node <Node>` and copy its public key or the public key of a staking pool into your clipboard.
    #. Download and install the `Particl Copay <https://particl.io/downloads/>`_ mobile app. Then, open it, create a new Particl wallet, and transfer PART coins to it.
    #. Once your coins are in the wallet, tap the :guilabel:`Staking` icon at the bottom right of the screen, and then tap the :guilabel:`Setup Cold Staking` green button.
    #. Input the staking public key in the provided field and assign a label to it.
    #. Tap the :guilabel:`Enable Cold Staking` green button, then tap the :guilabel:`Zap` button to complete the staking setup.


Adjust Staking Privacy
~~~~~~~~~~~~~~~~~~~~~~

For those operating their own staking :term:`node <Node>`, you can improve your staking privacy by leveraging PART's various privacy protocols. By default, staking rewards are sent to your :guilabel:`Public` balance, making all staking rewards visible on the blockchain. Particl offers options to modify this for increased financial privacy.

- :guilabel:`Public` balance: Rewards are transparent and public on the blockchain.
- :guilabel:`Blind` balance: The amount of PART coins in each reward is confidential.
- :guilabel:`Anon` balance: Both the number of PART coins and your deposit address remain completely anonymous, offering the highest level of staking privacy available on the Particl network.

.. rst-class:: bignums

    #. Access your staking :term:`node <Node>` and install the Private Staking script.

        .. code-block:: bash

            cd ~ && git clone https://github.com/GBen1/Private-Coldstaking.git

    #. Navigate to the script's folder, launch it, and follow the setup instructions.
        .. code-block:: bash

            cd ~/Private-Coldstaking && ./privatecoldstaking.sh

    #. Select your desired balance type for receiving staking rewards, and copy the new staking public key provided by the script.

    #. Confirm that the script is active and properly configured.

        .. code-block:: bash

            ./update.sh

    #. In :term:`Particl Desktop`, go to the Wallet module's :guilabel:`Overview` page and input the public key in the cold staking widget. If cold staking is already enabled, you must disable it first.

To disable the script, use this command:

        .. code-block:: bash

            cd ~/Private-Colstaking && ./uninstall.sh

----

.. seealso::

 * Particl Explained - :doc:`Staking <../particl-blockchain/blockchain_staking>` 
 * Particl Explained - :doc:`Blockchain Overview <../particl-blockchain/blockchain_part_overview>` 
 * Particl Explained - :doc:`Privacy Specifications <../particl-blockchain/blockchain_privacy>`
 * PART Guides - :doc:`Particl Desktop Wallet <../part-guides/partguides_desktop>`
 * PART Guides - :doc:`How to Stake <../part-guides/partguides_sendreceiveconvert>`
 * PART Guides - :doc:`Buy and Sell PART <../particl-blockchain/blockchain_buysell>`
