===================
Installation Guides
===================

In this section you learn how to install Particl Marketplace, additional software and how-to backup your data.

.. meta::
      
      :description lang=en: Particl Marketplace installation guides.

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Particl Marketplace
===================

To get started with Particl Marketplace, you need to download and install the Particl Desktop client software. Its installation is very easy and won't take you more than a few minutes! 

The entire process of setting up Particl Marketplace, from A to Z, can be seen in this walkthrough tutorial video.

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="390" src="https://www.youtube.com/embed/IC9yY3MThoo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

Download 
--------

.. danger::

   **NEVER download Particl clients from 3rd party websites**! Bad actors are constantly trying to distribute malware-infected versions of popular cryptocurrency wallets with the goal of stealing your funds! Always download from official sources only. 

.. attention::
	
	Being your own bank with blockchain related products shifts some responsibilities to you. One of them is to take security seriously. Please make sure that the file you've downloaded isn't compromised in any way by **verifying its checksum**.

**Download sources**

- Particl Homepage: https://particl.io/downloads/
- Particl Github: https://github.com/particl/particl-desktop/releases/latest

**Choose the right version to download**

.. tabs::
	 .. group-tab:: Windows

	 	**Windows file version**

	 	In 95% of all cases you will be fine by downloading the :file:`particl-desktop-X.X.X-win.exe` installer file. It supports any version of Windows except 32-bit only environments.

	 .. group-tab:: Mac

	 	**MacOS file version**

	 	In 95% of all cases you will be fine by downloading the :file:`particl-desktop-X.X.X-mac.dmg` installer image. It supports any version, including 10.15 (Catalina) or greater.

	 .. group-tab:: Linux

	 	**Linux file version**

	 	Depending on your Linux distribution you have the choice between different packages including Debian based :file:`.deb` and Rpm based :file:`.rpm` packages as well as a distribution independent :file:`.zip` version. 

	 	We assume that you know what you are doing here and what you need.


Checksum verification
---------------------

Obtain the checksum code from your download source for the downloaded file. Each file has its own checksum. The screenshot below shows you an example of this checksum highlighted from the GitHub releasenotes :guilabel:`Verification` section.

.. figure:: ../_static/media/images/mp_installation_github_checksum_verification.png
    :align: center
    :alt: Particl Marketplace installation checksum highlighted image
    :target: ../_static/media/images/mp_installation_github_checksum_verification.png

    Particl Marketplace installation checksum highlighted image

**Commands for each OS**

.. tabs::
	 .. group-tab:: Windows

	 	**Checksum verification command with terminal**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Explorer`
	 		#. Press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the **Download folder** and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
	 		#. Type the following command into the terminal while changing :file:`filename` for the real and complete filename of the downloaded file and hit :kbd:`ENTER ↵`.

	 			.. code-block:: bash

	 				CertUtil -hashfile filename SHA256

	 .. group-tab:: Mac

	 	**Checksum verification command with terminal**

	 	.. tip::
	 		**Prerequisite**: Head into :guilabel:`System Preferences` and select :guilabel:`Keyboard` > :guilabel:`Shortcuts` > :guilabel:`Services`. Find :guilabel:`New Terminal at Folder` in the settings and click the box.

		.. rst-class:: bignums

	 		#. Open :guilabel:`Finder`
	 		#. Press :kbd:`MOUSE-RIGHT ◳` on the **Download folder** of the file and you're shown the :guilabel:`services` > :guilabel:`open terminal` command to open the terminal. 
			#. Type the following command into the terminal while changing :file:`filename` for the real filename of the downloaded file.

				.. code-block:: bash

					shasum -a 256 filename

	 .. group-tab:: Linux

	 	**Checksum verification command with terminal**

	 	.. rst-class:: bignums

	 		#.  Open a terminal in the **Download-folder** of the file and type the following command by changing :file:`filename` for the real filename of the downloaded file. 
	 	
	 			.. code-block:: bash

	 				sha256sum filename

Once that is done, compare the output you've received in the step above with the checksum of the downloaded file from the release notes :guilabel:`Verification` from your download source. 


**Troubleshooting checksum mismatch**

If the output does not match, try to download the file again. Verify that you did not unzip or rename the file. In some cases it might be possible that antivirus software may alter files, be sure to have a solution on your own for that case.

.. attention::
	
	If all attempts fail to have a **matching number** do not install Particl Desktop unless you know what you are doing and try to reach out for :doc:`Particl Support <../faq/get_support>` for assistance. 

Installation process
--------------------

.. tabs::
	 .. group-tab:: Windows

 		**Windows installation**

 		.. rst-class:: bignums

	 		#. :ref:`Verify the checksum <Checksum verification>` of the file.
	 		#. Open the downloaded :guilabel:`particl-desktop-X.X.X-win.exe` installer file.
	 		#. Follow the installation instructions
	 		#. A launcher is put on to your desktop and into the application launcher menu. Use this to start :guilabel:`Particl Desktop`.
	 		#. Assign rules to your computer`s **firewall** to allow communications. On a standard Windows installation :guilabel:`Microsoft Defender` pops up. You must grant access.


	 .. group-tab:: Mac

	 	**MacOS installation**

	 	.. rst-class:: bignums

	 		#. :ref:`Verify the checksum <Checksum verification>` of the file.
	 		#. Open the downloaded :guilabel:`particl-desktop-X.X.X-mac.dmg` installer image with :kbd:`CTRL` + :kbd:`MOUSE-RIGHT ◳` and click :guilabel:`Open` from the shortcut menu. *Do not just double click the icon.*
	 		#. Drag the :guilabel:`Particl Desktop.app` file into the :guilabel:`Applications` folder. 
	 		#. Open the :guilabel:`Applications` folder and locate the :guilabel:`Particl Desktop.app` file. 
	 		#. Press :kbd:`CTRL` + :kbd:`MOUSE-RIGHT ◳` on the :guilabel:`Particl Desktop.app` file and click :guilabel:`Open`.
	 		#. On the first launch the firewall of your computer must get a rule to allow *Particl Desktop* to communicate with the blockchain. 

	 	From now on you will be able to start :guilabel:`Particl Desktop` from the **Launchpad** or **Spotlight** (e.g. :kbd:`COMMAND` + :kbd:`SPACE` and type "Particl" > hit :kbd:`ENTER ↵`) search.

	 .. group-tab:: Linux

	 	**Linux installation**

	 	.. rst-class:: bignums

	 		#. :ref:`Verify the checksum <Checksum verification>` of the file.
	 		#. Navigate to where you've downloaded your installer file in the terminal.

	 	*Depending on your package manager this command will vary. Using your standard package manager is recommended.*

	 	**Debian based installation**

	 	.. code-block:: bash

	 		sudo apt install particl-desktop-x.x.x-linux.deb

		**RPM based installation** 

	 	.. code-block:: bash

	 		sudo dnf -i particl-desktop-x.x.x-linux.rpm

	 	An application launcher is put to your applications menu. Click this to start *Particl Desktop* client.

	 	.. tip::

	 		If you want to launch it from the terminal: At the time of writing the executable is named :code:`Particl Desktop` which makes it neccessary to open the file with quotation marks or escaping the string.

			.. code-block:: bash
	
				user@linux:~> which "Particl Desktop"
				/usr/bin/Particl Desktop
	
				user@linux:~> "/usr/bin/Particl Desktop"
				(Particl Desktop:16887)

**Congratulations! You have installed Particl Marketplace.**

------

Backup Account and Data
=======================

File locations
--------------

After a successful installation of :guilabel:`Particl Desktop` the main application has been installed into the standard location of your operating system. Once the :guilabel:`Particl Desktop` is run the first time it will create user specific data within your user account. These include settings, logfiles, wallets and the blockchain-data itself.

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

------

Install Tor (Network Privacy)
=============================

.. danger::
	
	Always make sure your Tor is up-to-date with the latest version. This is a critical requirement that, if not followed, can heavily compromise your online privacy and potentially let other people spy on your online activity.

The *only* privacy setting not turned on by default is the ability to keep your IP address anonymous when using Particl. This is done by routing your client's connection through Tor, a networking protocol designed to anonymize your IP address.

.. attention::
	
	Tor isn't enabled by default on Particl because it requires extra care from you to be truly safe. It's a network that runs independently from Particl on your computer and needs you to keep two important security considerations in mind. 

Install and Run Tor
-------------------

The Tor network can be installed using three different methods. Always make sure that, regardless of the installation method you choose, Tor is running the latest version before using it.

Using the Tor Browser
~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

	#. Download the `Tor Browser <https://www.torproject.org/download/>`_.
	#. Install the Tor Browser on your computer.
	#. Launch the Tor Browser.
	#. Connect to the Tor network by clicking on :guilabel:`Connect` or configure your connection parameters by clicking on :guilabel:`Configure`.
	#. Once connected, **leave the Tor Browser running in the background** of your computer.


Using the Tor daemon
~~~~~~~~~~~~~~~~~~~~

.. tabs::

	.. group-tab:: Windows

		**Run Tor daemon**

		.. rst-class:: bignums

	 		#. Download the `Tor Browser <https://www.torproject.org/download/>`_.
			#. Install the Tor Browser on your computer.
	 		#. Open :guilabel:`Explorer` 
	 		#. Navigate to the Tor installation directory (e.g. :file:`C:\/Program Files\/Tor Browser`).
			#. Go into the :file:`Tor` directory, hold down :kbd:`SHIFT ⇧` and click with :kbd:`MOUSE-RIGHT ◳`.
			#. Open :guilabel:`Open command window here` from the menu.
			#. In the terminal that pops up, type:

				.. code-block:: bash

					tor.exe –service install

			#. Verify that Tor service is running, type: 
			
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

			#. Install the Tor daemon with homebrew by typing:

				.. code-block:: bash

					brew install tor

			#. Enable Tor as a Brew service by typing:

				.. code-block:: bash

					brew services start tor

	.. group-tab:: Linux

	 	**Using the Tor daemon**

	 	.. rst-class:: bignums

	 		#. Open a :guilabel:`terminal`
			#. Install the Tor daemon by typing:

				.. code-block:: bash 

					sudo apt install tor

			#. Make sure Tor launches on startup by typing: 

				.. code-block:: bash

					sudo systemctl enable tor

Using Tor as a Hidden Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On linux, you can also run Tor as a hidden service and connect your :guilabel:`Particl Desktop` to it. This allows other people to use your node as an entry or exit point, making the Tor network more decentralized and private.

.. rst-class:: bignums

	#. Open a :guilabel:`terminal`.
	#. Install the Tor network by typing: 
	
		.. code-block:: bash

			sudo apt-get install tor

	#. Define that you want to use Tor as a hidden service by modifying the Tor config file. To do so, type: 

		.. code-block:: bash

			sudo nano /etc/tor/torrc

	#. In the config file, add these two lines:

		.. code-block:: bash

			HiddenServiceDir /var/lib/tor/particl-service/
			HiddenServicePort 51738 127.0.0.1:51738

	#. Save and exit the file editor by pressing :kbd:`CTRL` + :kbd:`c`, then type :kbd:`y` followed by :kbd:`ENTER ↵` to save the changes.
	#. Restart Tor by typing 
	
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

Enable Tor on Particl
---------------------

All you need to do to enable Tor on Particl is to launch Particl Desktop with the proper instructions. Either you to add a special argument to the command you use to launch Particl or you make it a permanent setting.

Enable by default from GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

	#. Open :guilabel:`Particl Desktop`
	#. Click on :guilabel:`Configure settings` in the bottom left corner
	#. Go To :guilabel:`Global` > :guilabel:`Core Network Connection`
	#. Put into the :guilabel:`Connect via Proxy` field :code:`127.0.0.1:9150`
	#. Hit :guilabel:`Save changes` and restart :guilabel:`Particl Desktop`

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

	From now on :guilabel:`Particl Desktop` will try to connect with the settings you made. That means if :guilabel:`Tor` is not running on your machine :guilabel:`Particl Desktop` has no access to the internet.

Enable with terminal startup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

	.. group-tab:: Windows

	 	**Launching Particl With Tor**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Explorer`
	 		#. Press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the **Installation folder** (e.g. :file:`C:\/Program Files\/Particl`) and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
	 		#. Type the following command into the terminal and hit :kbd:`ENTER ↵`.

	 			.. code-block:: bash

	 				“Particl Desktop.exe” -proxy=127.0.0.1:9150

	.. group-tab:: Mac

	 	**Launching Particl With Tor**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Terminal` (e.g. :kbd:`COMMAND` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`)
	 		#. Type in this command:

				.. code-block:: bash

					/Applications/Particl\ Desktop.app/Contents/MacOS/Particl\ Desktop -proxy=127.0.0.1:9150

	.. group-tab:: Linux

	 	**Launching Particl With Tor**

	 	.. rst-class:: bignums
	 	
	 		#. Open a terminal in the folder where you've installed Particl Desktop and type the following command.
		
				.. code-block:: bash

					./Particl\ Desktop -proxy=127.0.0.1:9150


Important Considerations
------------------------

Keep Tor up-to-date
~~~~~~~~~~~~~~~~~~~

Tor needs to always be updated to the latest version. This is a critical requirement that, if not followed, can heavily compromise your online privacy. Tor updates contain very important security fixes to keep your identity confidential. 

As the network itself is widely targeted by hackers due to the privacy it provides, unpatched versions of Tor are considered unsafe to use. If exploited, a compromised version of Tor may leak your true identity and even let others spy on your online activity.

.. tabs::
	 .. group-tab:: Windows

	 	**Updating Tor**

	 	.. rst-class:: bignums

	 		#. Open the Tor Browser
	 		#. Check if the browser prompts you to update the a newer version.

	 .. group-tab:: Mac

	 	**Updating Tor**

	 	.. rst-class:: bignums

	 		#. Open :guilabel:`Terminal` (e.g. :kbd:`COMMAND` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`)
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


Update Tor Safely
~~~~~~~~~~~~~~~~~

Updating Tor is one thing, safely updating it is another. To make sure you don't download a compromised version of Tor, always make sure to download it from their official website. What good would updating Tor do to you if it lets the door wide open to hackers? 

To avoid any `man-in-the-middle-attack <https://en.wikipedia.org/wiki/Man-in-the-middle_attack>`_, always verify the cryptographic signature of the Tor files you download, even if it's from Tor's official website.

To do so, follow `this tutorial on how to verify Tor signatures <https://support.torproject.org/tbb/how-to-verify-signature/>`_ written by the Tor team itself.	
