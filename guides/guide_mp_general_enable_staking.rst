===============
Staking Rewards
===============

In exchange for the work provided by your staking :term:`node <Node>`, the :term:`Particl Network` pays you an interest in dividend-like payments proportional to the number of PART coins you own on that node. This amounts to a minimum of 2% yearly interest, but in reality, it fluctuates between 2% and 5% depending on how many more people are staking on the network as well.

When you're staking on Particl, it means your computer (referred to as a "staking :term:`node <Node>`") is helping the network by validating transactions. This task is fully automated and doesn't require you to do any manual work.

.. seealso::

 To learn more about the concept of staking, read the
 :doc:`Staking Explained <../in-depth/indepth_staking>` in-depth guide.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Enabling staking is generally straight-forward, but some of the staking solutions available on Particl may require more work to setup. This user guide will walk you through the process of enabling any of these solutions without too much hassle.

**Requirements**

- A :term:`Particl Desktop` wallet with any number of PART coins greater than 0.
- PART coins in your :guilabel:`public` balance.
- An active internet connection.
- A separate device to convert into a staking :term:`node <Node>` (required for cold staking only).

There are multiple ways you can stake your PART coins. Each of these solutions have pros and cons as well as their own method of activation. 

Enable Regular Staking
----------------------

Activating regular staking is the fastest method to get started. All it requires you to do is to open up the :term:`Particl Desktop` client and "unlock your wallet for staking only". Regular staking, however, requires your computer to be open and connected to the internet 24/7. 

**Non password protected client**

.. rst-class:: bignums

	#. Launch your :term:`Particl Desktop` client and make sure you have PART coins in your :guilabel:`public` balance.

That's all. Staking is working as long as your :term:`node <Node>` is online.

**Password protected client**

.. rst-class:: bignums

	#. Launch your :term:`Particl Desktop` client and make sure you have PART coins in your :guilabel:`public` balance.
	#. Click the :guilabel:`padlock` icon at the top right corner of your client.
	#. Click on the downward facing arrow next to :guilabel:`Additional unlock options` in the overlay window.
	#. Check the :guilabel:`Unlock for staking only` box.
	#. Enter your password and click the :guilabel:`Unlock wallet` button. 

Enable cold staking
-------------------

Cold staking is a more advanced, secure, and flexible staking option. It requires you to have a separate device that can remain connected to the internet at all times. This can be a hardware device like a `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`_, but it can also be `VPS or cloud server <https://en.wikipedia.org/wiki/Virtual_private_server>`_ (i.e. DigitalOcean, AWS, Google Cloud, etc). 

**On your staking device...**

Choose what device you want to use as a staking :term:`node <Node>` (i.e. `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`_) and install a Linux (i.e. `Raspbian <https://www.raspberrypi.org/downloads/>`_) distribution on it.

.. rst-class:: bignums

	#. Choose what device you want to use as a staking :term:`node <Node>` (i.e. `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`_) and install a Linux (i.e. `Raspbian <https://www.raspberrypi.org/downloads/>`_) distribution on it.

	#. Install dependencies and download Particl's cold staking app; Partyman.

		.. code-block:: bash

			sudo apt-get install python git unzip pv jq dnsutilscd 

		.. code-block:: bash

			cd ~ && git clone https://github.com/dasource/partyman

	#. Install :term:`Particl Core` on your staking device.

	 	.. code-block:: bash

		 partyman/partyman install

	 	If you already have :term:`Particl Core` installed, update it. 

	 	.. code-block:: bash

		 partyman/partyman update

	#. Once Particl Core is installed, restart Partyman.

		.. code-block:: bash

			partyman/partyman restart

	#. Create a new Particl wallet on your staking :term:`node <Node>`.

		.. code-block:: bash

			partyman/partyman stakingnode init

	#. Create a new staking public key. It will let you connect your PART coins to the staking :term:`node <Node>`.

		.. code-block:: bash

			partyman/partyman stakingnode new

		Note or copy this staking public key. You will need it for the next steps.

**On Particl Desktop...**

.. rst-class:: bignums

	#. Make sure you have PART coins in your :guilabel:`public` balance.
	#. In the Wallet module of :term:`Particl Desktop`, navigate to the :guilabel:`Overview` page.
	#. Click on the downward facing arrow in the :guilabel:`cold staking` widget on the right of your screen.
	#. Click on the blue :guilabel:`Set up cold staking` button to enter your staking public key in the designated space and confirm with a click on the :guilabel:`Enable cold staking` button.
	
			- Enter your password when prompted to.
	#. To fully activate cold staking, click on the :guilabel:`Zap` button to instantly bring the progress bar to 100%.

**A few cold staking settings...**

There are a few cold staking settings that you can set up. To do so, go back to your staking :term:`node <Node>` and enter the following commands.

.. code-block:: bash

	## View your staking statistics.
	partyman/partyman stakingnode stats

	## Send your staking rewards to any PART address (public balance) of your choice.
	partyman/partyman stakingnode rewardaddress

	## Configure your marketplace fee preference (more about this setting `here <https://particl.news/adjusting-listing-fees-4b676e230601>`_).
	partyman/partyman stakingnode smsgfeeratetarget

	##Create secure firewall rules that only allow the required ports to connect to the internet.
	partyman/partyman firewall

Connect to a staking pool
-------------------------

Another way to stake your PART coins is to team with other stakers and combine your staking power together. This will give you more frequent, but smaller, staking rewards. To do so, you need to connect your Particl wallet to a staking pool. 

+--------------------------+------------------------------------------+-----------+
| Pool Name                | URL/IP                                   | Pool Fees |
+==========================+==========================================+===========+
| **ColdStakingPool**      | https://coldstakingpool.com/             | 2.5%      |
+--------------------------+------------------------------------------+-----------+
| **Particl.Page**         | https://pool.particl.page/               | 2.5%      |
+--------------------------+------------------------------------------+-----------+
| **Crymel's Pool**        | https://particl.crymel.icu/              | 2.5%      |
+--------------------------+------------------------------------------+-----------+
| **CoinRollin**           | https://coinroll.in/                     | 1%        |
+--------------------------+------------------------------------------+-----------+

.. rst-class:: bignums

	#. Choose the staking pool you want to use from the list above, open the its website, and copy the pool's staking address. (looks like ``pcs19453kf98kz47yktqv7x36j39xa07mtvqx8evse``).
	#. Open up your :term:`Particl Desktop` client and make sure you have PART coins in your :guilabel:`public` balance.
	#. In the Wallet module of :term:`Particl Desktop`, navigate to the :guilabel:`Overview` page.
	#. Click on the downward facing arrow in the :guilabel:`cold staking` widget on the right of your screen.
	#. Click on the blue :guilabel:`Set up cold staking` button to enter your staking public key in the designated space and confirm with a click on the :guilabel:`Enable cold staking` button.
	
			- Enter your password when prompted to.
	#. To fully activate cold staking, click on the :guilabel:`Zap` button to instantly bring the progress bar to 100%.
			
			- Enter your password when prompted to.

.. Enable hardware staking
.. -----------------------

.. "Hardware staking" refers to the act of staking funds stored on a hardware device like a `Ledger Nano S <https://shop.ledger.com/products/ledger-nano-s>`_ or a `Trezor <https://trezor.io/>`_. The activation process is more technically advanced and requires you to use a different Particl client (Particl-Qt). This step-by-step guide assumes you already know how to use Particl on your hardware device and how to deposit funds on it.

.. On a Ledger Nano S device...
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

.. 	#. Set up your `Ledger Nano device <https://support.ledger.com/hc/en-us/articles/360007687153-Particl-PART->`_ and store funds into it.
	#. Set up a :ref:`Cold staking` :term:`node <Node>` and copy its public key or copy the public key of a staking pool :ref:`Staking Pools` into your clipboard.
	#. Download and install the latest **Particl-Qt** client `here <https://particl.io/downloads>`_.
	#. Open and unlock Particl-Qt, plug your Ledger Nano device into your computer and make sure it is ready to transact.
	#. Open the Staking setup window by going in :guilabel:`Window` > :guilabel:`Staking Setup`.
	#. Enter your staking :term:`node <Node>`'s public key in the :guilabel:`Cold staking change address` field and enable staking by clicking on the :guilabel:`Apply` button.

.. **To fully activate hardware staking, you need to "zap" your coins.**

.. rst-class:: bignums

.. 	#. Close Particl-Qt and open :term:`Particl Desktop`.
	#. Navigate to the wallet's :guilabel:`Overview` page located at the top of the left sidebar.
	#. Click on the :guilabel:`Zap` button to instantly bring the progress bar to 100%.

Enable mobile staking
---------------------

It's also possible to stake PART coins stored on a mobile wallet such as `Particl Copay <https://particl.io/downloads/>`_. Staking on your phone is completely secure and requires you to delegate the staking power of your coins to a staking :term:`node <Node>`. 

.. rst-class:: bignums

	#. Set up a :ref:`cold staking` :term:`node <Node>` and copy its public key or copy the public key of a :ref:`Staking Pools` key into your clipboard.
	#. Download and install the `Particl Copay <https://particl.io/downloads/>`_ mobile application, open it, create a new Particl wallet, and send PART coins to it.
	#. After your coins are deposited into this wallet, tap on the :guilabel:`Staking` icon at the bottom right corner of the screen followed by a tap on the :guilabel:`Setup Cold Staking` green button.
	#. Enter the staking public key in the designated space and give it a label.
	#. Tap on the :guilabel:`Enable Cold Staking` green button, then tap on the :guilabel:`Zap` button to finalize the staking setup process.

Adjust Your Staking Privacy
---------------------------

If you operate your own staking :term:`node <Node>`, you can adjust your level of staking privacy. By default, the network sends your staking rewards in your :guilabel:`public` balance, meaning all your staking rewards are publicly displayed publicly on the blockchain. Particl allows you to change that for better privacy.

- :guilabel:`Public` balance: Staking rewards are fully transparent and public on the blockchain.
- :guilabel:`Blind` balance: The number of PART coins contained in each reward remains confidential.
- :guilabel:`Anon` balance: The number of PART coins AND your deposit address remains entirely anonymous. This is the highest level of staking privacy possible on Particl.

.. rst-class:: bignums

	#. Access your staking :term:`node <Node>` and install the Private Staking script.

		.. code-block:: bash

			cd ~ && git clone https://github.com/GBen1/Private-Coldstaking.git

	#. Open the script's directory and launch the script and go through the setup process.

		.. code-block:: bash

			cd ~/Private-Coldstaking && ./privatecoldstaking.sh

	#. Choose the type of balance you'd like to receive your staking rewards to and copy the new staking public key provided by the script.
	
	#. Verify that the script has been activated and properly setup.

		.. code-block:: bash

			./update.sh

	#. In your :term:`Particl Desktop` client, navigate to the Wallet module's :guilabel:`Overview` page and enter the public key in the cold staking widget. If you already have cold staking enabled, you will need to disable cold staking first.

If you want to uninstall the script, enter this command.

		.. code-block:: bash

			cd ~/Private-Colstaking && ./uninstall.sh

.. seealso::

 Other sources for useful or more in-depth information:

 - Particl Academy - :doc:`Staking Explained <../in-depth/indepth_staking>`
 - Particl Wiki - `Learn staking <https://particl.wiki/learn/staking/>`_
 - Particl Wiki - `Tutorials <https://particl.wiki/tutorial/staking/>`_

