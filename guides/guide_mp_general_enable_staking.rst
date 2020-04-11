Earn Staking Rewards
====================

.. note::
	To learn more about what is staking and how you can earn interest on your PART coins paid in dividend-like payments, check out the :doc:`Staking in-depth guide <in-depth/indepth_staking>`.

When you're *staking* on Particl, it means your computer (referred to as a "staking node") is helping the network by validating transactions. This task is fully automated and doesn't require you to do any manual work. In exchange for the help provided by your staking node, **the Particl network pays you an interest in dividend-like payments** proportional to the number of PART coins you own.

Enabling staking is pretty straight-forward, but some of the staking solutions can be a bit more complicated to set up. Rest assured, this user guide will make sure you can enable any of the staking options available to you without too much hassle. Just carefully follow the steps below and start earning staking rewards in just a few minutes.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Requirements
------------

- Particl Desktop downloaded and installed (check out the :doc:`Installation Guide <guides/guide_mp_setup_installation>`).
- Any number of PART coins greater than 0.
- Hold the PART coins you want to earn a staking interest on in your public balance.
- An active internet connection.
- A separate device that will be converted into a staking node (cold staking only).

Enable Staking
--------------

On Particl, there are multiple ways that you can stake. Each of these solutions have pros and cons as well as their own method of activation. To learn more about each of these staking options, check out the :doc:`Staking in-depth guide <in-depth/indepth_staking>`.

Regular staking
^^^^^^^^^^^^^^^

Activating staking the regular way is the fastest method to get started. All it requires you to do is to open up Particl, but it isn't very convenient as you'll need to keep your computer online 24/7. 

If your client is not password protected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Launch your Particl Desktop client and keep it open at all times.
#. Make sure you have PART coins in your **public PART balance**.
#. That's all you need to do to start staking!

If your client is password protected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Launch your Particl Desktop client and keep it open at all times.
#. Make sure you have PART coins in your **public PART balance**.
#. Click on the padlock icon at the top right corner of your client.
#. In the window that pops up, click on the downward facing arrow next to ``Additional unlock options``.
#. Check the ``Unlock for staking only`` box.
#. Enter your password in the designated space at the top of the staking window. 
#. Click on ``Unlock wallet`` button.
#. You're now staking!

Cold staking
^^^^^^^^^^^^

Cold staking is a more advanced, secure, and flexible staking option. It requires you to have a separate device that can remain connected to the internet at all times. This can be a hardware device like a `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`_ or a `VPS server <https://en.wikipedia.org/wiki/Virtual_private_server>`_ (i.e. DigitalOcean, AWS, Google Cloud, etc). 

The staking node's sole purpose is to stake PART coins held on external addresses. It doesn't store any coin at all. For this reason, hosting a staking node on any VPS server provider is entirely secure and will not put your PART coins at risk of being stolen.

**On your staking device...**

#. Choose what device you want to use as a staking node (i.e. `Raspberry Pi <https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/>`_).
#. Install a Linux (i.e. `Raspbian <https://www.raspberrypi.org/downloads/>`_) distribution on it.
#. Update your system.
	``sudo apt-get update && sudo apt-get upgrade``
#. Install the required dependencies to run the cold staking app.
	``sudo apt-get install python git unzip pv jq dnsutils``
#. Download Partyman, Particl's cold staking app.
	``cd ~ && git clone https://github.com/dasource/partyman``
#. Install Particl on your staking device.
	``partyman/partyman install``
#. If you already have Particl installed, update it. 
	``partyman/partyman update``
#. If you encounter any issue with Particl on your staking node, reinstall it.
	``partyman/partyman reinstall``
#. Once Particl is ready, restart Partyman.
	``partyman/partyman restart``
#. Create a new Particl wallet on your staking node.
	``partyman/partyman stakingnode init``
#. Create a new **staking public key** (lets you connect your PART coins to the staking node).
	``partyman/partyman stakingnode new``
#. Note or copy this **staking public key** somewhere.

**On Particl Desktop...**

#. Make sure you have PART coins in your **public PART balance**.
#. Navigate to the ``Overview`` page located at the top of the menu on the left.
#. Click on the downward facing arrow in the **cold staking widget** on the right of your screen.
#. Click on the blue ``Set up cold staking`` button.
#. Enter your **staking public key** in the designated space.
#. Click on the ``Enable cold staking`` button.
#. Enter your password when prompted to.
#. To fully activate cold staking, click on the Zap button to instantly bring the progress bar to 100%.
#. Your now cold staking!

**A few cold staking settings...**

There are a few cold staking settings that you can set up. To do so, go back to your staking node and enter the following commands.

- View your staking statistics.
	``partyman/partyman stakingnode stats``
- Send your staking rewards to any PART address (public balance) of your choice.
	``partyman/partyman stakingnode rewardaddress``
- :doc:`Adjust your level of staking privacy <guides/guide_mp_enable_staking#adjust-your-staking-privacy>`.
- Configure your marketplace fee preference (more about this setting `here <https://particl.news/adjusting-listing-fees-4b676e230601>`_).
	``partyman/partyman stakingnode smsgfeeratetarget``
- Create secure firewall rules that only allow the required ports to connect to the internet.
	``partyman/partyman firewall``

Staking pools
^^^^^^^^^^^^^

Another way to stake your PART coins is to team up with other stakers by combining your staking rewards. This will give you more frequent but smaller staking rewards. To do so, you need to connect your Particl wallet to a staking pool. 

Don't worry, just like with cold staking, the pool won't have direct access to your coins. Staking on a staking pool is perfectly safe. 

+--------------------------+------------------------------------------+-----------+
| Pool Name                | URL/IP                                   | Pool Fees |
+==========================+==========================================+===========+
| **Tecnovert's Pool**     | http://66.172.10.231:903/                | 3%        |
+--------------------------+------------------------------------------+-----------+
| **Particl.Page**         | https://pool.particl.page/               | 2.5%      |
+--------------------------+------------------------------------------+-----------+
| **Crymel's Pool**        | https://particl.crymel.icu/              | 2.5%      |
+--------------------------+------------------------------------------+-----------+
| **CoinRollin**           | https://coinroll.in/                     | 1%        |
+--------------------------+------------------------------------------+-----------+

#. Choose which staking pool you want to use from the list above.
#. Open up the pool's website.
#. Copy the pool's staking address (looks like ``pcs14ch7w7ue2q8kadljsl42wehfw8tm99yxsez4kz``).
#. Open up your Particl Desktop client.
#. Make sure you have PART coins in your **public PART balance**.
#. Navigate to the ``Overview`` page located at the top of the menu on the left.
#. Click on the downward facing arrow in the **cold staking widget** on the right of your screen.
#. Click on the blue ``Set up cold staking`` button.
#. Enter your staking public key in the designated space.
#. Click on the ``Enable cold staking`` button.
#. Enter your password when prompted to.
#. Click on the Zap button to instantly bring the progress bar to 100%.
#. You're now staking on a pool!

Hardware staking
^^^^^^^^^^^^^^^^

"Hardware staking" refers to the act of staking funds stored on a hardware device like a `Ledger Nano S <https://shop.ledger.com/products/ledger-nano-s>`_ or a `Trezor <https://trezor.io/>`_. The activation process is more technically advanced and requires you to use a different Particl client (Particl-Qt). This step-by-step guide assumes you already know how to use Particl on a your hardware device and how to deposit funds on it.

On a Ledger Nano S device...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Set up your Ledger Nano device and store funds into it.
#. :doc:`Set up a cold staking node <guides/guide_mp_enable_staking#cold-staking>` and copy its public key or copy the :doc:`public key of a staking pool <guides/guide_mp_enable_staking#staking-pools>`.
#. Download and install the latest Particl-Qt client here.
#. Open and unlock Particl-Qt.
#. Plug your Ledger Nano device into your computer and make sure it is ready to transact.
#. Open the Staking setup window by going in ``Window`` → ``Staking Setup``.
#. Enter your staking node's public key in the ``Cold staking change address`` field.
#. Enable staking by clicking on the ``Apply`` button.

**To fully activate hardware staking, you need to "zap" your coins.**

#. Close Particl-Qt and open Particl Desktop.
#. Navigate to the ``Overview`` page located at the top of the left sidebar.
#. Click on the Zap button to instantly bring the progress bar to 100%.

Mobile staking
^^^^^^^^^^^^^^

It's also possible to stake your PART coins when they are stored on a mobile wallet such as `Particl Copay <https://particl.io/downloads/>`_. Staking on your phone is completely secure and requires you to delegate the staking power of your coins to a staking node. 

#. :doc:`Set up a cold staking node <guides/guide_mp_enable_staking#cold-staking>` and copy its public key or copy the :doc:`public key of a staking pool <guides/guide_mp_enable_staking#staking-pools>`.
#. Download and install `Particl Copay <https://particl.io/downloads/>`_.
#. Open Particl Copay, create a new Particl wallet, and send PART coins to it.
#. On Particl Copay's main screen, open up the wallet you want to stake by tapping on its tile.
#. Tap on the ``Staking`` icon at the bottom right corner of the app. 
#. Tap on the ``Setup Cold Staking`` green button.
#. Enter the staking node's public key in the designated space and give it a label.
#. Tap on the ``Enable Cold Staking`` green button.
#. Tap on the ``Zap`` button to finalize the staking setup process.
#. Tap on the ``ZAP`` button in the new window that appears on your app.
#. Tap on the ``PROCEED`` button to fully activate staking on your phone.
#. You're now staking the coins on your phone!

Adjust Your Staking Privacy
---------------------------

If you operate your own staking node, you can adjust your level of staking privacy. By default, the network pays staking interest in public balances. That means all staking rewards are publicly auditable and fully transparent. It is the same as if everyone in the world could see the value of all of your pay checks whenever they get deposited into your bank account. 

Luckily, Particl allows you control your level of staking privacy. To do so, you need to indicate to the network that you'd like to receive your staking rewards in another type of balance other than your public balance.

- **Public balance:** Staking rewards are publicly auditable and fully transparent.
- **Blind balance:** The number of PART coins each staking reward contains remains confidential.
- **Anon balance:** The number of PART coins each staking reward contains and who this reward goes to remains confidential. This is the highest level of staking privacy possible on Particl.

#. Access your :doc:`staking node <guides/guide_mp_enable_staking#cold-staking>` to type a few commands.
#. Update your system.
	``sudo apt update && sudo apt upgrade``
#. Download the Private Staking script on your staking node.
	``cd ~ && git clone https://github.com/GBen1/Private-Coldstaking.git``
#. Open the script's directory.
	``cd Private-Coldstaking/``
#. Launch the script and go through the setup process.
	``bash privatecoldstaking.sh``
#. Choose which type of balance you'd like to receive your staking rewards in.
#. Copy the new staking public key provided by the script.
#. Activate cold staking in your Particl Desktop client using the new staking public key.

	- If you already have cold staking enabled, disable it in the cold staking widget first.
#. Verify the script has been activated and properly setup.
	``bash update.sh``
#. If you want to uninstall the script, enter this command.
	``cd ~./Private-Colstaking && bash uninstall.sh``