===============
Staking Rewards
===============

.. note::
	To learn more about staking, different options, and how you can earn dividend-like payments, check out the :ref:`Staking Explained` in-depth guide.

When you're staking your Particl coins, it means your computer (referred to as a "staking :term:`node`") is helping the network by validating transactions. This task is fully automated and doesn't require you to do any manual work. In exchange for the help provided by your staking :term:`node`, the :term:`Particl Network` pays you an interest in dividend-like payments proportional to the number of PART coins you own. The minimum yearly interest you can earn on your PART coins is 2%, although that typically fluctuates between 2% and 5% depending on how many people are staking on the network.

Enabling staking is pretty straight-forward, but some of the staking solutions can be a bit more complicated to set up. Rest assured, this user guide will make sure you can enable any of the staking options available to you without too much hassle. Just carefully follow the steps below and start earning staking rewards in just a few minutes.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

**Requirements**

- A :term:`Particl Desktop` wallet with any number of PART coins greater than 0.
- Hold the PART coins you want to earn a staking interest on in your :guilabel:`public` balance.
- An active internet connection.
- A separate device that will be converted into a staking :term:`node` (required for cold staking only).

**Enable Staking**


There are multiple ways you can stake your PART coins. Each of these solutions have pros and cons as well as their own method of activation. 

**Regular staking**

Activating staking the regular way is the fastest method to get started. All it requires you to do is to open up :term:`Particl Client` and unlock your wallet for staking. Regular staking is, however, needs you to keep your computer online 24/7. 

**Non password protected client**

.. rst-class:: bignums

	#. Launch your :term:`Particl Desktop` client and make sure you have PART coins in your :guilabel:`public` balance.

That's all. Staking is working as long as your :term:`node` is online.

**Password protected client**

.. rst-class:: bignums

	#. Launch your :term:`Particl Desktop` client and make sure you have PART coins in your :guilabel:`public` balance.
	#. Click the :guilabel:`padlock` icon at the top right corner of your client.
	#. Click on the downward facing arrow next to :guilabel:`Additional unlock options` in the overlay window.
	#. Check the :guilabel:`Unlock for staking only` box.
	#. Enter your password and click the :guilabel:`Unlock wallet` button. 

That's it. Staking is working as long as your :term:`node` is online.

Enable cold staking
-------------------

Cold staking is a more advanced, secure, and flexible staking option. It requires you to have a separate device that can remain connected to the internet at all times. This can be a hardware device like a `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`_, but it can also be `VPS or cloud server <https://en.wikipedia.org/wiki/Virtual_private_server>`_ (i.e. DigitalOcean, AWS, Google Cloud, etc). 

The staking :term:`node`'s sole purpose is to stake PART coins held on external addresses. The staking :term:`node` itself doesn't contain any coin, it only tells the network that it's staking on behalf of another address. For this reason, hosting a staking :term:`node` on any VPS server provider is entirely secure and will not put your PART coins at risk of being stolen. If a hacker or malicious gets access to your staking :term:`node`, there is no coin to steal.

**On your staking device...**

Prerequisite: Choose what device you want to use as a staking :term:`node` (i.e. `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`_) and install a Linux (i.e. `Raspbian <https://www.raspberrypi.org/downloads/>`_) distribution on it.

.. rst-class:: bignums

	#. Install dependencies and Download Partyman, Particl's cold staking app.

		.. code-block:: bash

			sudo apt-get install python git unzip pv jq dnsutilscd 
			cd ~ && git clone https://github.com/dasource/partyman

	#. Install :term:`Particl Core` on your staking device.

	 	.. code-block:: bash

		 partyman/partyman install

	 	If you already have :term:`Particl Core` installed, update it. 

	 	.. code-block:: bash

		 partyman/partyman update

	#. Once Particl is ready, restart Partyman.

		.. code-block:: bash

			partyman/partyman restart

	#. Create a new Particl wallet on your staking :term:`node`.

		.. code-block:: bash

			partyman/partyman stakingnode init

	#. Create a new staking public key. It lets you connect your PART coins to the staking :term:`node`.

		.. code-block:: bash

			partyman/partyman stakingnode new

		Note or copy this staking public key. You will need this public key during the setup phase within :term:`Particl Desktop`.

**On Particl Desktop...**

.. rst-class:: bignums

	#. Make sure you have PART coins in your :guilabel:`public` balance.
	#. In the Wallet module of :term:`Particl Desktop`, navigate to the :guilabel:`Overview` page located at the top of the menu on the left.
	#. Click on the downward facing arrow in the :guilabel:`cold staking` widget on the right of your screen.
	#. Click on the blue :guilabel:`Set up cold staking` button and enter your staking public key in the designated space and confirm with a click on the :guilabel:`Enable cold staking` button.
	
			- Enter your password when prompted to.
	#. To fully activate cold staking, click on the :guilabel:`Zap` button to instantly bring the progress bar to 100%.

Congratulations! You are now now cold staking.

**A few cold staking settings...**

There are a few cold staking settings that you can set up. To do so, go back to your staking :term:`node` and enter the following commands.

.. code-block:: bash

	## View your staking statistics.
	partyman/partyman stakingnode stats

	## Send your staking rewards to any PART address (public balance) of your choice.
	partyman/partyman stakingnode rewardaddress

	## Configure your marketplace fee preference (more about this setting `here <https://particl.news/adjusting-listing-fees-4b676e230601>`_).
	partyman/partyman stakingnode smsgfeeratetarget

	##Create secure firewall rules that only allow the required ports to connect to the internet.
	partyman/partyman firewall

Connect to staking pools
------------------------

Another way to stake your PART coins is to team with other stakers and combine your staking power together. This will give you more frequent, but smaller, staking rewards. To do so, you need to connect your Particl wallet to a staking pool. 

Don't worry, just like with cold staking, the staking pool doesn't have any control over your coins. It's only staking on the network on your behalf and using the combined staking power of all the stakers connected to the pool. Staking on a staking pool is perfectly safe. 

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

	#. Choose a staking pool you want to use from the list above, open the pool's website and copy the pool's staking address. (looks like ``pcs19453kf98kz47yktqv7x36j39xa07mtvqx8evse``).
	#. Open up your :term:`Particl Desktop` client and make sure you have PART coins in your :guilabel:`public` balance.
	#. Navigate to the wallet's :guilabel:`Overview` page located at the top of the menu on the left and click on the downward facing arrow in the :guilabel:`cold staking` widget on the right of your screen.
	#. Click on the blue :guilabel:`Set up cold staking` button and enter a pool's staking address key in the designated space and confirm with a click on the :guilabel:`Enable cold staking` button.
			
			- Enter your password when prompted to.
	#. Click on the :guilabel:`Zap` button to instantly bring the progress bar to 100%.

Congratulations! You are now staking on a pool!

Enable hardware staking
-----------------------

"Hardware staking" refers to the act of staking funds stored on a hardware device like a `Ledger Nano S <https://shop.ledger.com/products/ledger-nano-s>`_ or a `Trezor <https://trezor.io/>`_. The activation process is more technically advanced and requires you to use a different Particl client (Particl-Qt). This step-by-step guide assumes you already know how to use Particl on your hardware device and how to deposit funds on it.

On a Ledger Nano S device...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

	#. Set up your `Ledger Nano device <https://support.ledger.com/hc/en-us/articles/360007687153-Particl-PART->`_ and store funds into it.
	#. Set up a :ref:`Cold staking` :term:`node` and copy its public key or copy the public key of a staking pool :ref:`Staking Pools` into your clipboard.
	#. Download and install the latest **Particl-Qt** client `here <https://particl.io/downloads>`_.
	#. Open and unlock Particl-Qt, plug your Ledger Nano device into your computer and make sure it is ready to transact.
	#. Open the Staking setup window by going in :guilabel:`Window` > :guilabel:`Staking Setup`.
	#. Enter your staking :term:`node`'s public key in the :guilabel:`Cold staking change address` field and enable staking by clicking on the :guilabel:`Apply` button.

**To fully activate hardware staking, you need to "zap" your coins.**

.. rst-class:: bignums

	#. Close Particl-Qt and open :term:`Particl Desktop`.
	#. Navigate to the wallet's :guilabel:`Overview` page located at the top of the left sidebar.
	#. Click on the :guilabel:`Zap` button to instantly bring the progress bar to 100%.

Enable mobile staking
---------------------

It's also possible to stake your PART coins stored on a mobile wallet such as `Particl Copay <https://particl.io/downloads/>`_. Staking on your phone is completely secure and requires you to delegate the staking power of your coins to a staking :term:`node`. 

.. rst-class:: bignums

	#. Set up a :ref:`cold staking` :term:`node` and copy its public key or copy the :ref:`Staking Pools` key into your clipboard.
	#. Download and install `Particl Copay <https://particl.io/downloads/>`_, open Particl Copay app, create a new Particl coin wallet, and send PART coins to it.
	#. On Particl Copay's main screen, open up the wallet you want to stake by tapping on its tile.
	#. Tap on the :guilabel:`Staking` icon at the bottom right corner, followed by a tap on the :guilabel:`Setup Cold Staking` green button.
	#. Enter the staking :term:`node`'s public key in the designated space and give it a label.
	#. Tap on the :guilabel:`Enable Cold Staking` green button, then tap on the :guilabel:`Zap` button to finalize the staking setup process.
	#. Tap on the :guilabel:`Zap` button in the new window that appears on your app, followed by a tap on the :guilabel:`PROCEED` button to fully activate staking on your phone.

Congratulations! You are now staking the coins on your phone!

Adjust Your Staking Privacy
---------------------------

If you operate your own staking :term:`node`, you can adjust your level of staking privacy. By default, the network sends your staking rewards in your :guilabel:`public` balance. That means all staking rewards are fully transparent and displayed publicly on the blockchain.

Luckily, Particl allows you to easily control your level of staking privacy. To do so, you need to indicate to the network that you'd like to receive your staking rewards in another type of balance other than your :guilabel:`public` balance.

- :guilabel:`Public` balance: Staking rewards are fully transparent and public on the blockchain.
- :guilabel:`Blind` balance: The number of PART coins contained in each reward remains confidential.
- :guilabel:`Anon` balance: The number of PART coins AND to who the address is going to is entirely anonymous. This is the highest level of staking privacy possible on Particl.

.. rst-class:: bignums

	#. Access your :ref:`Cold Staking` :term:`node` to type a few commands. Additionally, be sure to have the latest updates to your system.

		.. code-block:: bash

			sudo apt update && sudo apt upgrade

	#. Download the Private Staking script on your staking :term:`node`.

		.. code-block:: bash

			cd ~ && git clone https://github.com/GBen1/Private-Coldstaking.git

	#. Open the script's directory and launch the script and go through the setup process.

		.. code-block:: bash

			cd Private-Coldstaking
			./privatecoldstaking.sh

	#. Choose which type of balance you'd like to receive your staking rewards in and copy the new staking public key provided by the script.
	#. Activate cold staking in your :term:`Particl Desktop` client using the new staking public key. If you already have cold staking enabled, disable it in the :guilabel:`Cold Staking` widget first.
	#. Verify the script has been activated and properly setup.

		.. code-block:: bash

			./update.sh

If you want to uninstall the script, enter this command.

		.. code-block:: bash

			cd ~/Private-Colstaking && ./uninstall.sh