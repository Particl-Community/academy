Installation Guide
==================

To get started with Particl Marketplace, you need to download and install the Particl Desktop client software. Its installation is very easy and won't take you more than a few minutes! 

The entire process of setting up Particl Marketplace, from A to Z, can be seen in this walkthrough tutorial video.

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="390" src="https://www.youtube.com/embed/IC9yY3MThoo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Automatic installation  
~~~~~~~~~~~~~~~~~~~~~~

To make the installation process as easy and safe as possible we provide you skripts for your operating systems that do all in one. Downloading the latest client, verifying the checksum and starting the installation process.

.. tabs::
	 .. group-tab:: Windows

	 	**Windows procedure**

	 	Open Powershell and run these commands

	 	.. code-block:: bash

			user@windows:~> curl -s "https://api.github.com/repos/particl/particl-desktop/releases/latest" | select-string "TODO"| cut -d : -f 2,3 | tr -d \"


	 .. group-tab:: Mac

	 	**MacOS procedure**

	 	Open terminal and run these commands

	 	.. code-block:: bash

			user@mac:~> curl -s "https://api.github.com/repos/particl/particl-desktop/releases/latest" | grep -o browser_download_url.*${3:-dmg} | cut -d : -f 2,3 | tr -d \"

	 .. group-tab:: Linux

	 	**Linux procedure**

		Open terminal and run these commands
	 	
	 	.. code-block:: bash

			user@linux:~> curl -s "https://api.github.com/repos/particl/particl-desktop/releases/latest" | grep -o browser_download_url.*${3:-rpm} | cut -d : -f 2,3 | tr -d \"

When everything is done here head over to the :ref:`Installation Process`

Download 
~~~~~~~~

.. danger::

   **NEVER download Particl clients from 3rd party websites**! Hackers and bad actors are constantly trying to distribute malware-infected versions of popular cryptocurrency wallets with the goal of stealing your funds! Always download from official sources only. 

.. attention::
	
	Being your own bank with blockchain related products shifts some responsibilities to you. One of them is to take security seriously. Please make sure that the file you've downloaded isn't compromised in any way by **verifying its checksum**.

**Download sources**

Download the latest version of Particl Desktop by visiting the `Downloads page of the official Particl website <https://particl.io/downloads/>`_ or the official Particl GitHub repository.

**Download from GitHub**

- `Particl Desktop (with Open Marketplace) <https://github.com/particl/particl-desktop/releases/latest>`_

**Choose the right version to download**

.. tabs::
	 .. group-tab:: Windows

	 	**Windows file version**

	 	In 95% of all cases you will be fine by downloading the ``particl-desktop-X.X.X-win.exe`` installer file. It supports any version of Windows except 32-bit only environments.

	 .. group-tab:: Mac

	 	**MacOS file version**

	 	In 95% of all cases you will be fine by downloading the ``particl-desktop-X.X.X-mac.dmg`` installer image. It supports any version, including 10.15 (Catalina) or greater.

	 .. group-tab:: Linux

	 	**Linux file version**

	 	Depending on your Linux distribution you have the choice between different packages including Debian based **.deb** and Rpm based **.rpm** packages as well as a distribution independent **.zip** version. 

	 	We assume that you know what you are doing here and what you need.


Checksum verification
~~~~~~~~~~~~~~~~~~~~~

Obtain the checksum code from the release notes verification section on the `Particl Github releases page <https://github.com/particl/particl-desktop/releases/latest>`_ for your downloaded file. Each file has its own checksum. The screenshot below shows you an example of this checksum highlighted.

.. figure:: ../_static/media/images/mp_installation_github_checksum_verification.png
    :align: center
    :alt: Particl Marketplace installation checksum highlighted image
    :target: ../_static/media/images/mp_installation_github_checksum_verification.png

    Particl Marketplace installation checksum highlighted image

**Commands for each OS**

.. tabs::
	 .. group-tab:: Windows

	 	**Checksum verification command with terminal**

	 	#. Hit ``[SHIFT]`` + ``[MOUSE-RIGHT-CLICK]`` on the *Download-folder* and choose "*Open command window here*" or "*Open power shell here*".
	 	#. Type the following command into the command-window while changing *"filename"* for the real and complete filename of the downloaded file and hit ``[ENTER]``.

	 	.. code-block:: bash

	 		CertUtil -hashfile filename SHA256

	 .. group-tab:: Mac

	 	**Checksum verification command with terminal**

	 	.. tip::
	 		**Prerequisite**: Head into *System Preferences* and select "*Keyboard*" > "*Shortcuts*" > "*Services*". Find "*New Terminal at Folder*" in the settings and click the box.

	 	#. Open *Finder*, ``[MOUSE-RIGHT-CLICK]`` on the *Download-folder* of the file and you're shown the "*services*" > "*open terminal*" command to open the terminal. 
		#. Type the following command into the command-window while changing *"filename"* for the real filename of the downloaded file.

		.. code-block:: bash

			shasum -a 256 filename

	 .. group-tab:: Linux

	 	**Checksum verification command with terminal**

	 	#.  Open a terminal in the *Download-folder* of the file and type the following command by changing *"filename"* for the real filename of the downloaded file. 
	 	
	 	.. code-block:: bash

	 		sha256sum filename

Once that is done, compare the output you've received in the step above with the checksum of the downloaded file from the release notes *Verification* section on the `Particl Github releases page <https://github.com/particl/particl-desktop/releases/latest>`_. If all attempts fail to have a **matching number** do not install Particl Desktop unless you know what you are doing and try to reach out for :doc:`Particl Support <../faq/get_support>`. 

**Troubleshooting checksum mismatch**

If the output does not match, try to download the file again. Verify that you did not unzip or rename the file. In some cases it might be possible that antivirus software may alter files, be sure to have a solution on your own for that case.

Installation Process
~~~~~~~~~~~~~~~~~~~~

.. tabs::
	 .. group-tab:: Windows

 		**Windows installation**

	 	#. Verify the checksum of the downloaded installer file as stated above for your own safetey.
	 	#. Open the downloaded ``particl-desktop-X.X.X-win.exe`` installer file.
	 	#. Follow the installation instructions
	 	#. A launcher is put on to your desktop and into the application launcher menu. Use this to start *Particl Desktop*.
	 	#. On the first launch the firewall of your computer must get a rule to allow *Particl Desktop* to communicate with the blockchain. On a standard Windows installation Microsoft Defender pops up. You must grant access.


	 .. group-tab:: Mac

	 	**MacOS installation**

	 	#. Verify the checksum of the downloaded installer file as stated above for your own safetey.
	 	#. Open the downloaded ``particl-desktop-X.X.X-mac.dmg`` installer image with ``[CTRL]`` + ``[MOUSE-RIGHT-CLICK]`` and click "*Open*" from the shortcut menu. Do not just double click the icon.
	 	#. Drag the ``Particl Desktop.app`` file into the "*Applications*" folder. 
	 	#. Open the "*Applications*" folder and locate the ``Particl Desktop.app`` file. 
	 	#. Press ``[CTRL]`` + ``[MOUSE-RIGHT-CLICK]`` on the ``Particl Desktop.app`` file and click "*Open*".
	 	#. On the first launch the firewall of your computer must get a rule to allow *Particl Desktop* to communicate with the blockchain. 

	 	From now on you will be able to start *Particl Desktop* from the Launchpad or Spotlight search.

	 .. group-tab:: Linux

	 	**Linux installation**

	 	#. Verify the checksum of the downloaded installer file as stated above for your own safetey.
	 	#. Navigate to where you've downloaded your installer file in the terminal.

	 	Depending on your package manager this command will vary. Using your standard package manager is recommended.

	 	**Debian based installation**

	 	.. code-block:: bash

	 		sudo apt install particl-desktop-x.x.x-linux.deb

		**RPM based installation** 

	 	.. code-block:: bash

	 		sudo dnf -i particl-desktop-x.x.x-linux.rpm

	 	An application launcher is put to your applications menu. Click this to start *Particl Desktop* client.

	 	**Terminal speciality**

	 	If you want to launch it from the terminal: At the time of writing the executable is named "Particl Desktop" which makes it neccessary to open the file with qutation marks or escaping the string.

		.. code-block:: bash

			user@linux:~> which "Particl Desktop"
			/usr/bin/Particl Desktop

			user@linux:~> "/usr/bin/Particl Desktop"
			(Particl Desktop:16887)



File locations
~~~~~~~~~~~~~~

After a successful installation of *Particl Desktop* the main application has been installed into the standard location of your operating system. Once the *Particl Desktop* is run the first time it will create user specific data within your user account. These include settings, logfiles, wallets and the blockchain itself.

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


Firewall settings & Ports
~~~~~~~~~~~~~~~~~~~~~~~~~

	
.. tip::

	Wait for Particl Desktop to load and download the latest Particl Core version. This happens automatically on launch each time a newer version of Particl Core is available.
	

