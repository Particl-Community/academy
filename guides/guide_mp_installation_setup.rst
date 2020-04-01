Installing Particl's Marketplace
================================

To get started with Particl's marketplace, you need to download and install the Particl Desktop client. Its installation is very easy and won't take you more than a few minutes! 

The entire process of setting up Particl's marketplace, from A to Z, can be seen in this walkthrough tutorial video.

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="390" src="https://www.youtube.com/watch?v=IC9yY3MThoo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

Download Particl Desktop
---------------------------

.. danger::

   **NEVER download Particl clients from 3rd party websites**! Hackers and bad actors are constantly trying to distribute malware-infected versions of popular cryptocurrency wallets with the goal of stealing your funds! Always download from official sources only. 

#. Download the latest version of Particl Desktop by visiting the `Downloads page of the official Particl website <https://particl.io/downloads/>`_.

Verify the File
^^^^^^^^^^^^^^

Being your own bank with blockchain related products shifts some responsibilities to you. One of them is to take security seriously. Please make sure that the file you've downloaded isn't compromised in any way by verifying its checksum.

.. tabs::
	 .. tab:: Windows

	 	- [Shift] + [right-click] on the Download folder and choose **Open command window here** or **Open power shell here**.
	 	- Type the following command by changing **filename** for the real filename of the downloaded file. 
	 	- ``CertUtil -hashfile filename SHA256``

	 .. tab:: Mac

	 	- Head into **System Preferences** and select Keyboard > Shortcuts > Services. Find "**New Terminal at Folder**" in the settings and click the box. 
	 	- In **Finder**, right-click the folder where you've downloaded the file and open a Terminal. 
		- Type the following command by changing **filename** for the real filename of the downloaded file.
		- ``shasum -a 256 filename``

	 .. tab:: Linux

	 	- Open a terminal and type the following command by changing **filename** for the real filename of the downloaded file. 
	 	- ``sha256sum filename``

Once that is done, compare the output you've received in the step above with the hash of the downloaded file from GitHub in the verification section of the release note.

**Latest releases**

- `Particl Desktop (with Open Marketplace) <https://github.com/particl/particl-desktop/releases/latest>`_

- `Particl Core (Qt) (with Ledger wallet support) <https://github.com/particl/particl-core/releases/latest>`_

Install Particl Desktop
--------------------------

#. Extract the content of the ZIP file to any location on your computer.
#. Launch Particl Desktop:

.. tabs::
	 .. tab:: Windows

	     Launch Particl Desktop by clicking on the ``Particl Desktop.exe`` file. 

	 .. tab:: Mac

	    Launch Particl Desktop by clicking on the ``Particl Desktop`` executable file. 

	 .. tab:: Linux (tar.gz)

	    From a terminal, launch Particl Desktop by executing ``./"Particl Desktop"`` in app's folder.

	 .. tab:: Linux (deb)	 

	 	#. Navigate to where you've downloaded the ``.deb`` installer.
	 	#. From a terminal, depackage the file by typing ``sudo dpkg -i particl-desktop-x.x.x-linux-amd65.deb``. Make sure to write the exact name of the downloaded file as each new Particl Desktop update results in a new file name.
	 	#. Launch Particl Desktop by executing ``Particl\ Desktop``.

Prepare Particl Desktop
-------------------------

#. Wait for Particl Desktop to load and download the latest Particl Core version. This happens automatically on launch each time a newer version of Particl Core is available.
#. Read and accept the terms and conditions, if you agree with them.

Create Your First Wallet
--------------------------

TBD by the new version

Enable the Marketplace
------------------------

TBD by the new version