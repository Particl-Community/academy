Enable Tor (Network Privacy)
============================

.. danger::
	
	**Always make sure your Tor is up-to-date with the latest version. This is a critical requirement that, if not followed, can heavily compromise your online privacy and potentially let other people spy on your online activity.**

The only privacy setting not turned on by default is the ability to keep your IP address anonymous when using Particl. This is done by routing your client's connection through Tor, a networking protocol designed to anonymize your IP address. 

Install and Run Tor
-------------------

The Tor network can be installed using three different methods. Always make sure that, regardless of the installation method you choose, Tor is running the latest version before using it.

Using the Tor Browser
^^^^^^^^^^^^^^^^^^^^^

#. Download the `Tor Browser <https://www.torproject.org/download/>`_.
#. Install the Tor Browser on your computer.
#. Launch the Tor Browser.
#. Connect to the Tor network by clicking on ``Connect`` or configure your connection parameters by clicking on ``Configure``.
#. Once connected, leave the Tor Browser running in the background of your computer.


Using the Tor daemon
^^^^^^^^^^^^^^^^^^^^

.. tabs::
	 .. group-tab:: Windows

	 	**Run Tor daemon**

	 	#. Download the `Tor Browser <https://www.torproject.org/download/>`_.
		#. Install the Tor Browser on your computer.
	 	#. Open the Windows File Explorer and navigate to the directory in which you’ve installed the Tor Browser (i.e. ``C:\Tor Browser\``).
		#. Go into the ``Browser\TorBrowser\Tor`` directory.
		#. Hold down the ``[SHIFT]`` key and right-click on the Tor folder.
		#. Click on ``Open command window here``.
		#. In the terminal that pops up, type ``tor.exe –service install``.
		#. Verify that Tor is running by holding down the Windows and ``r`` keys to open up the ``Run`` window. 
		#. Then, type ``services.msc``, press ``OK``, and make sure that you see Tor running as a service.

	 .. group-tab:: MacOS

	 	**Using the Tor daemon**

	 	#. Go in your Applications list and open a terminal.
		#. Install ``Brew`` by typing ``/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``.
		#. Go through the installation process.
		#. Install the Tor daemon by typing ``brew install tor``.
		#. Enable Tor as a Brew service by typing ``brew services start tor``

	.. group-tab:: Linux

	 	**Using the Tor daemon**

	 	#. Open a terminal
		#. Install the Tor daemon by typing ``sudo apt install tor``
		#. Make sure Tor launches on startup by typing ``sudo systemctl enable tor``


Using Tor as a Hidden Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On linux, you can also run Tor as a hidden service and connect your Particl Desktop to it. This allows other people to use your node as an entry or exit point, making the Tor network more decentralized and private.

#. Open a terminal.
#. Install the Tor network by typing ``sudo apt-get install tor``.
#. Define that you want to use Tor as a hidden service by modifying the Tor config file. To do so, type ``sudo nano /etc/tor/torrc``.
#. In the config file, add these two lines:
    - ``HiddenServiceDir /var/lib/tor/particl-service/``
    - ``HiddenServicePort 51738 127.0.0.1:51738``
#. Save and exit the file editor by pressing ``[CTRL]`` + ``[X]``, then type ``[Y]`` followed by ``[ENTER]``.
#. Restart Tor by typing ``sudo service tor restart``.
#. Find your hidden service’s IP address (.onion) by typing ``sudo cat /var/lib/tor/particl-service/hostname``. For the purpose of this tutorial, we'll refer to this address as ``[yourexternalip].onion``.
#. Modify your Particl config file to route its connection through your hidden service by typing ``nano ~/.particl/particl.conf``.
#. If that file doesn’t exist, create it by typing ``mkdir ~/.particl then nano ~/.particl/particl.conf``.
#. Your particl.conf file will need to contain at least the following. Replace [yourexternalip].onion with the onion domain of your hidden service.

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

All you need to do to enable Tor on Particl is to launch Particl Desktop with the proper instructions. It just requires you to add a special argument to the command you use to launch Particl.

.. tabs::
	 .. group-tab:: Windows

	 	**Launching Particl With Tor**

	 	#. Hit ``[SHIFT]`` + ``[MOUSE-RIGHT-CLICK]`` on the folder where you've installed Particl Desktop and choose "*Open command window here*" or "*Open power shell here*".
	 	#. Type the following command into the command-window and hit ``[ENTER]``.

	 	.. code-block:: bash

	 		“Particl Desktop.exe” -proxy=127.0.0.1:9150

	 .. group-tab:: MacOS

	 	**Launching Particl With Tor**

	 	#. Head into *System Preferences* and select "*Keyboard*" > "*Shortcuts*" > "*Services*". Find "*New Terminal at Folder*" in the settings and click the box.
	 	#. Open *Finder*, ``[MOUSE-RIGHT-CLICK]`` on the folder where you've installed Particl Desktop and click on "*services*" > "*open terminal*" command to open the terminal. 
		#. Type the following command into the command-window.

		.. code-block:: bash

			./Particl\ Desktop.app/Contents/MacOS/Particl\ Desktop -proxy=127.0.0.1:9150

	.. group-tab:: Linux

	 	**Launching Particl With Tor**

	 	
	 	#. Open a terminal in the folder where you've installed Particl Desktop and type the following command.
		
		.. code-block:: bash

			./Particl\ Desktop -proxy=127.0.0.1:9150

	.. group-tab:: Linux (.deb)

	 	**Launching Particl With Tor**

	 	
	 	#. Open a terminal in the folder where you've installed Particl Desktop and type the following command.
		
		.. code-block:: bash

			particl-desktop -proxy=127.0.0.1:9150

Important Considerations
------------------------

Tor isn't enabled by default on Particl because it requires extra care from you to be truly safe. It's a network that runs independently from Particl on your computer and needs you to keep two important security considerations in mind.

Keep Tor up-to-date
^^^^^^^^^^^^^^^^^^^

Tor needs to always be updated to the latest version. This is a critical requirement that, if not followed, can heavily compromise your online privacy. Tor updates contain very important security fixes to keep your identity confidential. 

As the network itself is widely targeted by hackers due to the privacy it provides, unpatched versions of Tor are considered unsafe to use. If exploited, a compromised version of Tor may leak your true identity and even let others spy on your online activity.

.. tabs::
	 .. group-tab:: Windows

	 	**Updating Tor**

	 	#. Open the Tor Browser
	 	#. Check if the browser prompts you to update the a newer version.

	 .. group-tab:: MacOS

	 	**Updating Tor**

	 	#. Go in your Applications list and open a terminal.
	 	#. Type ``brew update``.
	 	#. Type ``brew upgrade``.

	 .. group-tab:: Linux

	 	**Updating Tor**

	 	#. Open a terminal.
	 	#. Type ``sudo apt update && sudo apt-upgrade``.

Update Tor the right way
^^^^^^^^^^^^^^^^^^^^^^^^

Updating Tor is one thing, safely updating it is another. To make sure you don't download a compromised version of Tor, always make sure to download it from their official website. What good would updating Tor do to you if it lets the door wide open to hackers? 

To avoid any `man-in-the-middle-attack <https://en.wikipedia.org/wiki/Man-in-the-middle_attack>`_, always verify the cryptographic signature of the Tor files you download, even if it's from Tor's official website.

To do so, follow `this tutorial on how to verify Tor signatures <https://support.torproject.org/tbb/how-to-verify-signature/>`_ written by the Tor team itself.