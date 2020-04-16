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

Download 
~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~

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

	 	#. Open :guilabel:`Explorer`
	 	#. Press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the **Download folder** and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
	 	#. Type the following command into the terminal while changing :file:`filename` for the real and complete filename of the downloaded file and hit :kbd:`ENTER ↵`.

	 	.. code-block:: bash

	 		CertUtil -hashfile filename SHA256

	 .. group-tab:: Mac

	 	**Checksum verification command with terminal**

	 	.. tip::
	 		**Prerequisite**: Head into :guilabel:`System Preferences` and select :guilabel:`Keyboard` > :guilabel:`Shortcuts` > :guilabel:`Services`. Find :guilabel:`New Terminal at Folder` in the settings and click the box.

	 	#. Open :guilabel:`Finder`
	 	#. Press :kbd:`MOUSE-RIGHT ◳` on the **Download folder** of the file and you're shown the :guilabel:`services` > :guilabel:`open terminal` command to open the terminal. 
		#. Type the following command into the terminal while changing :file:`filename` for the real filename of the downloaded file.

		.. code-block:: bash

			shasum -a 256 filename

	 .. group-tab:: Linux

	 	**Checksum verification command with terminal**

	 	#.  Open a terminal in the **Download-folder** of the file and type the following command by changing :file:`filename` for the real filename of the downloaded file. 
	 	
	 	.. code-block:: bash

	 		sha256sum filename

Once that is done, compare the output you've received in the step above with the checksum of the downloaded file from the release notes :guilabel:`Verification` from your download source. 


**Troubleshooting checksum mismatch**

If the output does not match, try to download the file again. Verify that you did not unzip or rename the file. In some cases it might be possible that antivirus software may alter files, be sure to have a solution on your own for that case.

.. attention::
	
	If all attempts fail to have a **matching number** do not install Particl Desktop unless you know what you are doing and try to reach out for :doc:`Particl Support <../faq/get_support>` for assistance. 

Installation Process
~~~~~~~~~~~~~~~~~~~~

.. tabs::
	 .. group-tab:: Windows

 		**Windows installation**

	 	#. :ref:`Verify the checksum <Checksum verification>` of the file.
	 	#. Open the downloaded :guilabel:`particl-desktop-X.X.X-win.exe` installer file.
	 	#. Follow the installation instructions
	 	#. A launcher is put on to your desktop and into the application launcher menu. Use this to start :guilabel:`Particl Desktop`.
	 	#. Assign rules to your computer`s **firewall** to allow communications. On a standard Windows installation :guilabel:`Microsoft Defender` pops up. You must grant access.


	 .. group-tab:: Mac

	 	**MacOS installation**

	 	#. :ref:`Verify the checksum <Checksum verification>` of the file.
	 	#. Open the downloaded :guilabel:`particl-desktop-X.X.X-mac.dmg` installer image with :kbd:`CTRL` + :kbd:`MOUSE-RIGHT ◳` and click :guilabel:`Open` from the shortcut menu. *Do not just double click the icon.*
	 	#. Drag the :guilabel:`Particl Desktop.app` file into the :guilabel:`Applications` folder. 
	 	#. Open the :guilabel:`Applications` folder and locate the :guilabel:`Particl Desktop.app` file. 
	 	#. Press :kbd:`CTRL` + :kbd:`MOUSE-RIGHT ◳` on the :guilabel:`Particl Desktop.app` file and click :guilabel:`Open`.
	 	#. On the first launch the firewall of your computer must get a rule to allow *Particl Desktop* to communicate with the blockchain. 

	 	From now on you will be able to start :guilabel:`Particl Desktop` from the **Launchpad** or **Spotlight** search.

	 .. group-tab:: Linux

	 	**Linux installation**

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



File locations
~~~~~~~~~~~~~~

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

	