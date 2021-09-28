===================
Installation Guides
===================

.. title::
   Particl Desktop & Marketplace Installation Guide

.. meta::
   :description lang=en: step by step learn every aspect of the installation of Particl Destop & Marketplace.
   :keywords lang=en: Particl, Marketplace, Installation, Blockchain, Privacy, E-Commerce

In this section you learn how to install :term:`Particl Marketplace`, additional software and how-to backup your data.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Particl Marketplace
===================

To get started with :term:`Particl Marketplace`, you need to download and install the :guilabel:`Particl Desktop` client software. Its installation is very easy and won't take you more than a few minutes!

Download 
--------

Choose the right version to download.

.. tabs::
	 .. group-tab:: Windows

	 	**Windows file version**

	 	Mostly you will be fine by downloading the :file:`particl-desktop-X.X.X-win.exe` installer file. It supports any version of Windows. Currently, 32-bit environments are an exception but this will change.

	 	**Download sources**

		- Particl Homepage: https://particl.io/downloads/
		- Particl Github: https://github.com/particl/particl-desktop/releases/latest

		.. attention::

   		 NEVER download Particl clients from 3rd party websites! Bad actors are constantly trying to distribute malware-infected versions of popular :term:`cryptocurrency <Cryptocurrency>` wallets with the goal of stealing your funds! Always download from official sources only. 

	 .. group-tab:: Mac

	 	**MacOS file version**

	 	Mostly you will be fine by downloading the :file:`particl-desktop-X.X.X-mac.dmg` installer image. It supports any version of MacOS including 10.15 (Catalina) or greater.

	 	**Download sources**

		- Particl Homepage: https://particl.io/downloads/
		- Particl Github: https://github.com/particl/particl-desktop/releases/latest

		.. attention::

   		 NEVER download Particl clients from 3rd party websites! Bad actors are constantly trying to distribute malware-infected versions of popular :term:`cryptocurrency <Cryptocurrency>` wallets with the goal of stealing your funds! Always download from official sources only. 

	 .. group-tab:: Linux

	 	**Linux file version**

	 	Depending on your Linux distribution you have the choice between different packages including Debian based :file:`.deb`, :file:`.rpm` packages as well as a distribution independent :file:`.zip` version. 

	 	Once you know which Linux distribution you are running, it's straight forward to find out which package manager you have and which package will suit you.

	 	**Download sources**

		- Particl Homepage: https://particl.io/downloads/
		- Particl Github: https://github.com/particl/particl-desktop/releases/latest

		.. attention::

   		 NEVER download Particl clients from 3rd party websites! Bad actors are constantly trying to distribute malware-infected versions of popular :term:`cryptocurrency <Cryptocurrency>` wallets with the goal of stealing your funds! Always download from official sources only. 

Installation process
--------------------

.. tabs::
	 .. group-tab:: Windows

 		**Windows installation**

 		.. rst-class:: bignums

	 		#. :ref:`Verify the checksum <Checksum verification>` of the file.
	 		#. Open the downloaded :guilabel:`particl-desktop-X.X.X-win.exe` installer file.
	 		#. Follow the installation instructions
	 		#. A launcher is put on to your desktop and into the application launcher menu. Use this to start :term:`Particl Desktop`.
	 		#. Assign rules to your computer`s firewall to allow communications. On a standard Windows installation :guilabel:`Microsoft Defender` pops up. You must grant access.

	 .. group-tab:: Mac

	 	**MacOS installation**

	 	.. rst-class:: bignums

	 		#. :ref:`Verify the checksum <Checksum verification>` of the file.
	 		#. Open the downloaded :guilabel:`particl-desktop-X.X.X-mac.dmg` installer image by pressing :kbd:`CONTROL` + :kbd:`MOUSE-RIGHT ◳` and click :guilabel:`Open` from the appearing shortcut menu. *Do not just double click the icon.*
	 		#. Drag and drop the :term:`Particl Desktop.app <Particl Desktop>` file into the :guilabel:`Applications` folder. 
	 		#. Open the :guilabel:`Applications` folder and locate the :term:`Particl Desktop.app <Particl Desktop>` file. 
	 		#. Press :kbd:`CONTROL` + :kbd:`MOUSE-RIGHT ◳` on the :term:`Particl Desktop.app <Particl Desktop>` file and click :guilabel:`Open`.
	 		#. On the first launch the firewall of your computer must get a rule to allow :term:`Particl Desktop` to communicate with the blockchain. 

	 	From now on you will be able to start :term:`Particl Desktop` from the Launchpad or Spotlight (e.g. :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "Particl" > hit :kbd:`ENTER ↵`) search.

	 .. group-tab:: Linux

	 	**Linux installation**

	 	.. rst-class:: bignums

	 		#. :ref:`Verify the checksum <Checksum verification>` of the file.
	 		#. Navigate to where you've downloaded your installer file in the terminal.

	 		#. *Depending on your package manager this command will vary. Using your standard package manager is recommended.*

	 			**Debian based installation**

	 			.. code-block:: bash

	 				sudo apt install particl-desktop-x.x.x-linux.deb

				**RPM based installation** 

	 			.. code-block:: bash

	 				sudo dnf -i particl-desktop-x.x.x-linux.rpm

	 		#. An application launcher is put to your applications menu. Click this to start :term:`Particl Desktop` client.

	 	.. tip::

	 		If you want to launch it from the terminal: At the time of writing the executable is named :code:`Particl Desktop` which makes it neccessary to open the file with quotation marks or escaping the string.

			.. code-block:: bash
	
				user@linux:~> which "Particl Desktop"
				/usr/bin/Particl Desktop
	
				user@linux:~> "/usr/bin/Particl Desktop"
				(Particl Desktop:16887)

.. rst-class:: achievement

	Congratulations! You have installed :term:`Particl Marketplace`.

.. hint::

	**Loading and Syncing Times**

	Because the :term:`Particl Marketplace`'s content is hosted on distributed Networks for payments and data-exchange, the marketplace may take a few minutes to sync. It may take even a few more minutes to fully load all marketplace's listings. This is to be normally expected and will get much faster as the Particl team improves the marketplace.

Checksum verification
---------------------

Obtain the checksum code from the official download sources for the downloaded file. Each file has its own checksum. 

Being your own bank with blockchain related products shifts some responsibilities to you. One of them is to take security seriously. Please make sure that the file you've downloaded isn't compromised in any way by verifying its checksum.

.. tabs::
	 .. group-tab:: Windows

	 	**Checksum verification command with terminal**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Windows Explorer`
	 		#. Press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the Download folder and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
	 		#. Type the following command into the terminal while changing :file:`filename` for the real and complete filename of the downloaded file and hit :kbd:`ENTER ↵`.

	 			.. code-block:: bash

	 				CertUtil -hashfile filename SHA256

	 .. group-tab:: Mac

	 	**Checksum verification command with terminal**

	 	.. tip::
	 		**Prerequisite**: Head into :guilabel:`System Preferences` and select :guilabel:`Keyboard` > :guilabel:`Shortcuts` > :guilabel:`Services`. Find :guilabel:`New Terminal at Folder` in the settings and enable the checkbox.

		.. rst-class:: bignums

	 		#. Open :guilabel:`Finder`
	 		#. Press :kbd:`MOUSE-RIGHT ◳` on the Download folder of the file and you're shown the :guilabel:`services` > :guilabel:`open terminal` command to open the terminal at this location. 
			#. Type the following command into the terminal while changing :file:`filename` for the real filename of the downloaded file.

				.. code-block:: bash

					shasum -a 256 filename

	 .. group-tab:: Linux

	 	**Checksum verification command with terminal**

	 	.. rst-class:: bignums

	 		#.  Open a terminal in the Download-folder of the file and type the following command by changing :file:`filename` for the real filename of the downloaded file. 
	 	
	 			.. code-block:: bash

	 				sha256sum filename

Once that is done, compare the checksum output you've received in the step above with the checksum stated in the official download sources. The screenshot below shows you an example of this checksum highlighted from the GitHub releasenotes :guilabel:`Verification` section.

.. figure:: ../_static/media/images/mp_installation_github_checksum_verification.png
    :align: center
    :alt: Particl Marketplace installation checksum highlighted image
    :target: ../_static/media/images/mp_installation_github_checksum_verification.png

    Particl Marketplace installation checksum highlighted image

**Troubleshooting checksum mismatch**

If the output does not match, try to download the file again. Verify that you did not unzip or rename the file. In some cases it might be possible that antivirus software may alter files, be sure to have a solution on your own in that case.

.. attention::
	
	If all attempts fail to have a matching number do not install :term:`Particl Desktop` unless you know what you are doing and try to reach out for :doc:`Particl Support <../faq/get_support>` for assistance. 

Starting Particl Desktop
------------------------

You have two options. Either startup with the launcher icon (recommended) or with a terminal command.

Startup with Launcher
~~~~~~~~~~~~~~~~~~~~~

.. tabs::

	.. group-tab:: Windows

	 	**Launching Particl Desktop with Launcher**

	 	.. rst-class:: bignums

	 		#. Open your :guilabel:`Start Menu` by pressing :kbd:`WIN ⊞` Key
	 		#. Start typing :code:`Particl`
	 		#. Click on the :term:`Particl Desktop` launcher icon.

	.. group-tab:: Mac

	 	**Launching Particl Desktop with Launcher**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Spotlight` (e.g. :kbd:`COMMAND ⌘` + :kbd:`SPACE`) 
	 		#. Type :code:`Particl`
	 		#. Click on the :term:`Particl Desktop` launcher icon.

	.. group-tab:: Linux

	 	**Launching Particl Desktop with Launcher**

	 	.. rst-class:: bignums
	 	
	 		#. Open your applications menu
	 		#. Click on :term:`Particl Desktop` launcher icon

Startup from Terminal
~~~~~~~~~~~~~~~~~~~~~

Sometimes it is handy to start :term:`Particl Marketplace` from the terminal aka commandline. It gives you plenty of output and information what is happening in the background.

.. tabs::

	.. group-tab:: Windows

	 	**Launching Particl Desktop from terminal**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Windows Explorer`
	 		#. Press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the Installation folder (e.g. :file:`C:\/Program Files\/Particl`) and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
	 		#. Type the following command into the terminal and hit :kbd:`ENTER ↵`.

	 			.. code-block:: bash

	 				“Particl Desktop.exe”

	.. group-tab:: Mac

	 	**Launching Particl Desktop from terminal**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Terminal` (e.g. :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`)
	 		#. Type in this command:

				.. code-block:: bash

					/Applications/Particl\ Desktop.app/Contents/MacOS/Particl\ Desktop

	.. group-tab:: Linux

	 	**Launching Particl Desktop from terminal**

	 	.. rst-class:: bignums
	 	
	 		#. Open a terminal in the folder where you've installed :term:`Particl Desktop` and type the following command.
		
				.. code-block:: bash

					./Particl\ Desktop

Backup Account and Data
=======================

File locations
--------------

After a successful installation of :term:`Particl Desktop` the main application has been installed into the standard location of your operating system. Once the :term:`Particl Desktop` is run the first time it will create user specific data within your user account. These include settings, logfiles, wallets and the blockchain-data itself. From time to time it is a reasonable measure to backup these data to an encrypted external resource.

.. tabs::
	 .. group-tab:: Windows

	 	.. code-block:: bash

	 		## Windows paths

	 		"%UserProfile%\AppData\Roaming\Particl"
			"%userprofile%\AppData\Roaming\particl-bot"
			"%userprofile%\AppData\Roaming\particl-market"
			"%userprofile%\AppData\Roaming\Particl Desktop"


	 .. group-tab:: Mac

	 	.. code-block:: bash

	 		## MacOS paths

	 		"~/Library/Application Support/Particl"
			"~/Library/Application Support/particl-bot"
			"~/Library/Application Support/particl-market"
			"~/Library/Application Support/Particl Desktop"

	 .. group-tab:: Linux

	 	.. code-block:: bash

	 		## Linux paths

	 		"~/.particl"
			"~/.particl-bot"
			"~/.particl-market"
			"~/.config/particl-desktop"

			## Launcher path

			"/opt/Particl Desktop/Particl Desktop"

.. seealso::

 Other sources for useful or more in-depth information:

 - Particl Wiki - `Backup & Restore wallet <https://particl.wiki/tutorial/security/backup-restore-wallet/>`_

Install Tor (Network Privacy)
=============================

.. danger::
	
	Always make sure your :term:`Tor` is up-to-date with the latest version. This is a critical requirement that, if not followed, can heavily compromise your online privacy and potentially let other people spy on your online activity.

The *only* privacy setting not turned on by default is the ability to keep your IP address anonymous when using Particl. This is done by routing your client's connection through Tor, a networking protocol designed to anonymize your IP address.

.. attention::
	
	:term:`Tor` isn't enabled by default on Particl because it requires extra care from you to be truly safe. It's a network that runs independently from Particl on your computer and needs you to keep important security considerations in mind. 

Install and Run Tor
-------------------

To make sure you don't download a compromised version of Tor, always make sure to download it from their official website. What good would updating :term:`Tor` do to you if it lets the door wide open to hackers? 

To avoid any `man-in-the-middle-attack <https://en.wikipedia.org/wiki/Man-in-the-middle_attack>`_, always verify the cryptographic signature of the :term:`Tor` files you download, even if it's from Tor's official website.

To do so, follow this tutorial on `how to verify Tor signatures <https://support.torproject.org/tbb/how-to-verify-signature/>`_ written by the :term:`Tor` team itself.	

The :term:`Tor` network can be installed using three different methods. Always make sure that, regardless of the installation method you choose, :term:`Tor` is running the latest version before using it.

Using the Tor Browser
~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

	#. Download the `Tor Browser <https://www.torproject.org/download/>`_ and install it on your computer.
	#. Launch the :term:`Tor` Browser.
	#. Connect to the :term:`Tor` network by clicking on :guilabel:`Connect` or configure your connection parameters by clicking on :guilabel:`Configure`.
	#. Once connected, leave the :term:`Tor` Browser running in the background of your computer.


Using the Tor daemon
~~~~~~~~~~~~~~~~~~~~

.. tabs::

	.. group-tab:: Windows

		**Run Tor daemon**

		.. rst-class:: bignums

	 		#. Download the `Tor Browser <https://www.torproject.org/download/>`_ and install it on your computer.
	 		#. Open :guilabel:`Windows Explorer` and navigate to the :term:`Tor` installation directory (e.g. :file:`C:\/Program Files\/Tor Browser`).
			#. Go into the :file:`Tor` directory, hold down :kbd:`SHIFT ⇧` and click with :kbd:`MOUSE-RIGHT ◳`.
			#. Open :guilabel:`Open command window here` from the menu.
			#. In the terminal that pops up, type:

				.. code-block:: bash

					tor.exe –service install

			#. Verify that :term:`Tor` service is running, type: 
			
				.. code-block:: bash

					sc query "Tor" | find "RUNNING"

	.. group-tab:: Mac

	 	**Using the Tor daemon**

	 	.. tip:: 

	 		If not already in place install homebrew. Put this code into the terminal.

	 		.. code-block:: bash 

	 				xcode-select --install
					ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
					echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.profile

		.. rst-class:: bignums

			#. Install the :term:`Tor` daemon with homebrew by typing:

				.. code-block:: bash

					brew install tor

			#. Enable :term:`Tor` as a Brew service by typing:

				.. code-block:: bash

					brew services start tor

	.. group-tab:: Linux

	 	**Using the Tor daemon**

	 	.. rst-class:: bignums

	 		#. Open a :guilabel:`Terminal`
			#. Install the :term:`Tor` daemon by typing:

				.. code-block:: bash 

					sudo apt install tor

			#. Make sure :term:`Tor` launches on startup by typing: 

				.. code-block:: bash

					sudo systemctl enable tor

Using Tor as a Hidden Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On linux, you can also run :term:`Tor` as a hidden service and connect your :term:`Particl Desktop` to it. This allows other people to use your :term:`node <Node>` as an entry or exit point, making the :term:`Tor` network more :term:`decentralized <Decentralization>` and private.

.. rst-class:: bignums

	#. Open a :guilabel:`Terminal` and install the :term:`Tor` network by typing: 
	
		.. code-block:: bash

			sudo apt-get install tor

	#. Define that you want to use :term:`Tor` as a hidden service by modifying the :term:`Tor` config file. To do so, type: 

		.. code-block:: bash

			sudo nano /etc/tor/torrc

		In the config file, add these two lines:

		.. code-block:: bash

			HiddenServiceDir /var/lib/tor/particl-service/
			HiddenServicePort 51738 127.0.0.1:51738

		Save and exit the nano file editor by pressing :kbd:`CTRL+c`, then type :kbd:`y` followed by :kbd:`ENTER ↵` to save the changes.

	#. Restart :term:`Tor` by typing into the terminal 
	
		.. code-block:: bash
		
			sudo service tor restart

	#. Find your hidden service’s IP address (.onion) by typing (For the purpose of this tutorial, we'll refer to this address as :code:`[yourexternalip].onion`):
	
		.. code-block:: bash

			sudo cat /var/lib/tor/particl-service/hostname

	#. Modify your Particl config file to route its connection through your hidden service by typing: 

		.. code-block:: bash

			touch ~/.particl/particl.conf && nano ~/.particl/particl.conf

		Then add these lines to the file and don`t forget to set :code:`yourexternalip.onion` 

		.. code-block:: bash
	
			externalip=[yourexternalip].onion
			onion=127.0.0.1:9050
			addnode=7vusex6gv5eerqi2.onion
			addnode=quf7tm4gk3xn3aee.onion
			addnode=46fvsrrq75dx5vq4.onion
			addnode=ciikdjtoop7l6p6h.onion
			addnode=frlfghlielxq2ncy.onion
			addnode=partusq5qad6jd2c.onion
			addnode=x6fxdwpq2krxzmr3.onion
			addnode=amu2ck7lyw26fiqs.onion
			addnode=kfyopkn3shigcneh.onion
			onlynet=tor
			listen=1
			bind=127.0.0.1:51738
			maxconnections=30

		Save and exit the nano file editor by pressing :kbd:`CTRL` + :kbd:`c`, then type :kbd:`y` followed by :kbd:`ENTER ↵` to save the changes.

Enable Tor on Particl
---------------------

All you need to do to enable :term:`Tor` on Particl is to launch :term:`Particl Desktop` with the proper instructions. Either you to add a special argument to the command you use to launch Particl or you make it a permanent setting.

Enable by default from GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

	#. Open :term:`Particl Desktop` and click on :guilabel:`Particl Desktop Settings` in the bottom left corner
	#. Go to :guilabel:`Core network connection` and put into the :guilabel:`Connect via Proxy` field :code:`127.0.0.1:9150`
	#. Hit :guilabel:`Save changes` and restart :term:`Particl Desktop`

Enable by default from commandline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

	#. Open the configuration file: 

		.. code-block:: bash

			nano ~/.particl/particl.conf

	#. Add this line to the configuration file:

		.. code-block:: bash

			proxy=127.0.0.1:9150

.. note::

	From now on :term:`Particl Desktop` will try to connect with the settings you made. That means if :guilabel:`Tor` is not running on your machine, then :term:`Particl Desktop` has no access to the internet.

Enable with terminal startup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

	.. group-tab:: Windows

	 	**Launching Particl With Tor**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Windows Explorer` and press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the Installation folder (e.g. :file:`C:\/Program Files\/Particl`) and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
	 		#. Type the following command into the terminal and hit :kbd:`ENTER ↵`.

	 			.. code-block:: bash

	 				“Particl Desktop.exe” -proxy=127.0.0.1:9150

	.. group-tab:: Mac

	 	**Launching Particl With Tor**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Terminal` (e.g. :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`)
	 		#. Type in this command:

				.. code-block:: bash

					/Applications/Particl\ Desktop.app/Contents/MacOS/Particl\ Desktop -proxy=127.0.0.1:9150

	.. group-tab:: Linux

	 	**Launching Particl With Tor**

	 	.. rst-class:: bignums
	 	
	 		#. Open a terminal in the folder where you've installed :term:`Particl Desktop` and type the following command.
		
				.. code-block:: bash

					./Particl\ Desktop -proxy=127.0.0.1:9150


Important Considerations
------------------------

Keep Tor up-to-date
~~~~~~~~~~~~~~~~~~~

:term:`Tor` needs to always be updated to the latest version. This is a critical requirement that, if not followed, can heavily compromise your online privacy. :term:`Tor` updates contain very important security fixes to keep your identity confidential. 

As the network itself is widely targeted by hackers due to the privacy it provides, unpatched versions of :term:`Tor` are considered unsafe to use. If exploited, a compromised version of :term:`Tor` may leak your true identity and even let others spy on your online activity.

.. tabs::
	 .. group-tab:: Windows

	 	**Updating Tor**

	 	.. rst-class:: bignums

	 		#. Open the :term:`Tor` Browser
	 		#. Check if the browser prompts you to update the a newer version.

	 .. group-tab:: Mac

	 	**Updating Tor**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Terminal` (e.g. :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`)
	 		#. Type this line of code and  hit :kbd:`ENTER ↵`

	 			.. code-block:: bash
	
	 				brew update && brew upgrade

	 .. group-tab:: Linux

	 	**Updating Tor**

	 	.. rst-class:: bignums

	 		#. Open a :guilabel:`Terminal` and run the upgrade procedure depending on your package manager.

	 			**Example**

	 			.. code-block:: bash

	 				sudo apt update && sudo apt-upgrade

	 	Depending on your linux flavor this command may vary. There are multiple package-managers out there, but their usage is quite the same.


