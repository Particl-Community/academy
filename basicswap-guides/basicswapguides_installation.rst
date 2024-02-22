=====================
Get Started (Install)
=====================

.. title::
   BasicSwap DEX Installation Guide
   
.. meta::
   :description lang=en: Learn how to install BasicSwap DEX on your desktop computer.
   :keywords lang=en: Particl, DEX, Trading, Exchange, Buy Crypto, Sell Crypto, Installation, Quickstart, Blockchain, Privacy, E-Commerce, multi-vendor marketplace, online marketplace

:term:`BasicSwap DEX <BasicSwap>` is a cross-chain and privacy-first decentralized exchange (DEX) enabling direct cryptocurrency trades without intermediaries, restrictions, or fees. This guide provides comprehensive instructions for installing and configuring it according to your needs.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

.. tip::

	 To significantly improve your network privacy (e.g., masking your IP address and location), consider running :term:`BasicSwap` via the :term:`Tor` network. For step-by-step guidance, refer to the :doc:`BasicSwap Tor Guide <../basicswap-guides/basicswapguides_tor>`.

.. attention::

     During the installation of a full BasicSwap node, closely monitor the terminal's output. It's crucial to ensure there are no error messages at any step. Errors must be addressed immediately; failure to do so may prevent BasicSwap from launching successfully.

Automated Installation Methods
==============================

Windows Installation Wizard (.exe)
----------------------------------

Install :term:`BasicSwap` on Windows effortlessly with a graphical installation wizard by downloading the .exe installer from `this Github link <https://github.com/gerlofvanek/basicswap-installation-GUI/releases>`_. This intuitive installer streamlines the setup process via an easy-to-navigate menu. Note that **you must run it as an administrator** for it to work properly.

Linux Installation Scripts Suite
-------------------------------

For Linux users, the simplest installation method is through the use of community-developed scripts, available `here on Github <https://github.com/nahuhh/basicswap-bash/releases>`_. This collection of scripts automates common setup tasks, including installing, adding/removing/updating coin cores, updating :term:`BasicSwap`, and enabling :term:`Tor`.


Install Using Docker
====================

As :term:`BasicSwap` is currently in early beta, it lacks ready-made executables or in-app integrations (such as Particl Desktop, web gateways, or third-party services). Thus, the initial step involves compiling and running a full BasicSwap node on your device.

Install Docker
--------------

Docker offers a straightforward method for setting up :term:`BasicSwap` without one of the automated solutions. Please note, this installation method does not support OSX. If you are using a Mac, refer to the subsequent section for alternative setup instructions.

.. tabs::

     .. group-tab:: Windows
     
        **Install the Docker engine on your device**

         .. rst-class:: bignums

             #. Begin by completing the prerequisites listed on the `Docker Desktop WSL 2 backend page <https://docs.docker.com/desktop/windows/wsl/>`_. This involves activating the WSL2 feature on Windows.

             #. Proceed to download `Docker Desktop for Windows <https://docs.docker.com/desktop/windows/wsl/>`_.

             #. Follow the detailed installation guide for Docker with WSL 2 on the Docker Desktop WSL 2 backend page.

         .. note:: 
             Be aware that certain versions of Docker might not be fully compatible with Windows 11. Should issues arise, trying an earlier version of Docker could be beneficial.  

         .. note::
             You may need to adjust BIOS settings, such as enabling hardware-assisted virtualization, to ensure Docker runs smoothly. Please adhere to any guidance provided during the setup process if that's the case.

     .. group-tab:: Linux

         **Install the Docker engine on your device**

         .. rst-class:: bignums

             #. Install the required dependencies.

                 .. code-block:: bash

                     apt-get install curl jq git

             #. Check if Docker is already installed on your system.

             	 .. code-block:: bash
             	 	 
             	 	 docker -v

             	 If you see a message indicating :guilabel:`Docker version (...)`, Docker is already installed and you can move on to the next steps without reinstalling it.

             #. Install Docker by following `the instructions on their website <https://docs.docker.com/engine/install/#server>`_.

             #. Configuring Docker to run without sudo is recommended, as outlined in `this guide <https://docs.docker.com/engine/install/linux-postinstall/>`_. Without this setup, you'll need to include :guilabel:`sudo` before every :guilabel:`docker-compose` command.

Create the Docker Image
-----------------------

Create BasicSwap's docker image, which you'll need to run whenever you want to launch the DEX.

.. tabs::

     .. group-tab:: Windows

     	 .. rst-class:: bignums

             #. Open a WSL (Linux) terminal.

                 :kbd:`Windows` + :kbd:`R` > "wsl" -> :kbd:`ENTER`.

             #. Install Git.

             	 .. code-block:: bash
             	 	 
             	 	 sudo apt update
             	 	 sudo apt install git jq curl

             #. Download the BasicSwap code.

             	 .. code-block:: bash

             	 	 git clone https://github.com/tecnovert/basicswap.git

             #. Navigate to BasicSwap's Docker folder.

                 .. code-block:: bash

             	 	 cd basicswap/docker/

             #. Copy the default environment file.

                 .. code-block:: bash

             	 	 cp example.env .env

             #. **(Optional)** Set a custom coin data path by modifying the target path in your :guilabel:`.env` file.

                 .. code-block:: bash

                     nano .env

             #. Create the BasicSwap Docker image (make sure you are in :guilabel:`basicswap/docker`.

                     .. code-block:: bash
				 
             	 	 docker-compose build


     .. group-tab:: Linux

         .. rst-class:: bignums

                 #. Open a terminal.
		
		 #. Install Git.

             	    .. code-block:: bash
             	 	 
             	 	 sudo apt update
             	 	 sudo apt install git jq curl

                 #. Download the BasicSwap code.

                     .. code-block:: bash

	             	 	 git clone https://github.com/tecnovert/basicswap.git

                 #. Navigate to BasicSwap's Docker folder.

                     .. code-block:: bash

	             	 	 cd basicswap/docker/

            	 #. Copy the default environment file.

                     .. code-block:: bash

             	 	 	cp example.env .env

             	#. **(Optional)** Set a custom coin data path by modifying the target path in your :guilabel:`.env` file.

                     .. code-block:: bash

    	                 	nano .env

                 #. Create the BasicSwap Docker image (make sure you are in :guilabel:`basicswap/docker`.

                     .. code-block:: bash
					 
	             	 	 docker-compose build        	 	 


Configure the Docker Image
--------------------------

After creating BasicSwap's Docker image, it's time to configure it to your preferences.

.. tabs::

     .. group-tab:: Windows

     	 .. rst-class:: bignums

             #. Open a WSL (Linux) terminal.

                 :kbd:`Windows` + :kbd:`R` > "wsl" -> :kbd:`ENTER`.

             #. Navigate to BasicSwap's Docker folder.

                 .. code-block:: bash

             	 	 cd basicswap/docker/

             #. Set :guilabel:`xmrrestoreheight` to Monero's current chain height.

             	 .. code-block:: bash

             	 	 CURRENT_XMR_HEIGHT=$(curl https://localmonero.co/blocks/api/get_stats | jq .height)

             #. Select the cryptocurrencies you want to activate (Particl is activated by default). You must specify your choices in the configuration command. :ref:`See here <compatible coins>` for a complete list of compatible currencies on BasicSwap.

             #. Decide on whether to perform a fast sync of the Bitcoin blockchain using a checkpoint or to synchronize from the beginning. This choice affects whether you include the :guilabel:`--usebtcfastsync` parameter in your configuration command.

             #. Execute the following command to configure your BasicSwap Docker image, adjusting it according to your preferences as described above.

             	 .. code-block:: bash

             	 	 export COINDATA_PATH=/var/data/coinswaps
			 docker run --rm -t --name swap_prepare -v $COINDATA_PATH:/coindata i_swapclient basicswap-prepare --datadir=/coindata --withcoins=monero,bitcoin --htmlhost="0.0.0.0" --wshost="0.0.0.0" --xmrrestoreheight=$CURRENT_XMR_HEIGHT --usebtcfastsync

             #. Securely record and store the mnemonic provided by the above command. It serves as your wallet's backup key.

             #. Safely note the result of the following command, it is useful if you need to recover your Monero wallet.

                 .. code-block:: bash

             	 	 echo $CURRENT_XMR_HEIGHT

             #. **(Optional)** Adjust your timezone by specifying the appropriate :guilabel:`TZ` value in your :guilabel:`.env` file, located within the BasicSwap Docker directory. Use the :guilabel:`timedatectl list-timezones` command to view valid timezone options.

             	 .. code-block:: bash
             	 
             	 	 nano .env

             	 To save changes, press :kbd:`CTRL` + :kbd:`X`, then :kbd:`Y` + :kbd:`ENTER`.


     .. group-tab:: Linux

     	 .. rst-class:: bignums

             #. Open a terminal.

             #. Navigate to BasicSwap's Docker folder.

                 .. code-block:: bash

             	 	 cd basicswap/docker/

             #. Set :guilabel:`xmrrestoreheight` to Monero's current chain height.

             	 .. code-block:: bash

             	 	 CURRENT_XMR_HEIGHT=$(curl https://localmonero.co/blocks/api/get_stats | jq .height)

             #. Select the cryptocurrencies you want to activate (Particl is activated by default). You must specify your choices in the configuration command. :ref:`See here <compatible coins>` for a complete list of compatible currencies on BasicSwap.

             #. Decide on whether to perform a fast sync of the Bitcoin blockchain using a checkpoint or to synchronize from the beginning. This choice affects whether you include the :guilabel:`--usebtcfastsync` parameter in your configuration command.

             #. Execute the following command to configure your BasicSwap Docker image, adjusting it according to your preferences as described above.

             	 .. code-block:: bash

             	 	 export COINDATA_PATH=/var/data/coinswaps
			 docker run --rm -t --name swap_prepare -v $COINDATA_PATH:/coindata i_swapclient basicswap-prepare --datadir=/coindata --withcoins=monero,bitcoin --htmlhost="0.0.0.0" --wshost="0.0.0.0" --xmrrestoreheight=$CURRENT_XMR_HEIGHT --usebtcfastsync

             #. Securely record and store the mnemonic provided by the above command. It serves as your wallet's backup key.

             #. Safely note the result of the following command, it is useful if you need to recover your Monero wallet.

                 .. code-block:: bash

             	 	 echo $CURRENT_XMR_HEIGHT

             #. **(Optional)** Adjust your timezone by specifying the appropriate :guilabel:`TZ` value in your :guilabel:`.env` file, located within the BasicSwap Docker directory. Use the :guilabel:`timedatectl list-timezones` command to view valid timezone options.

             	 .. code-block:: bash

             	 	 nano .env

             	 To save changes, press :kbd:`CTRL` + :kbd:`X`, then :kbd:`Y` + :kbd:`ENTER`.

Start BasicSwap
---------------

After configuring your Docker image, the next step is to run it. Doing so will launch BasicSwap, making it accessible through web browsers.

.. tabs::

     .. group-tab:: Windows

     	 .. rst-class:: bignums

             #. Open a WSL (Linux) terminal.

                 :kbd:`Windows` + :kbd:`R` > "wsl" -> :kbd:`ENTER`.

             #. Navigate to BasicSwap's Docker folder.

                 .. code-block:: bash

             	 	 cd basicswap/docker/

             #. Start the Docker image. This will launch BasicSwap's startup process.

             	 .. code-block:: bash

             	 	 export COINDATA_PATH=/var/data/coinswaps
			 docker-compose up

             #. Wait for BasicSwap to start fully, then open it up in your favorite web browser by navigating to the following address.

                 .. code-block:: bash

             	 	 http://localhost:12700

     .. group-tab:: Linux
 
             .. rst-class:: bignums
 
                 #. Open a terminal.
 
                 #. Navigate to BasicSwap's Docker folder.
 
                     .. code-block:: bash
 
                         cd basicswap/docker/
 
                 #. Start the Docker image. This will launch BasicSwap's startup process.

                     .. code-block:: bash

                         export COINDATA_PATH=/var/data/coinswaps
			 docker-compose up

                 #. Wait for BasicSwap to start fully, then open it up in your favorite web browser by navigating to the following address.

                     .. code-block:: bash

                         http://localhost:12700

Install Without Docker
======================

Build BasicSwap
---------------

The first step to running BasicSwap without docker is to build it locally on your device.

.. tabs::

     .. group-tab:: Mac OS
 
             .. rst-class:: bignums
 
                 #. Open :guilabel:`Terminal` (i.e., :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`).

                 #. Install Homebrew by executing the following command in the Terminal. Homebrew extends MacOS with a wealth of Linux-style package management capabilities.

                     .. code-block::

                         /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

                 #. Install the required dependencies

                     .. code-block::

                         brew install wget unzip python git protobuf gnupg automake libtool pkg-config curl jq

                 #. Close the terminal and open a new one. This will update the python symlinks and allow you to progress through the next steps.

                 #. Execute the commands below sequentially to setup the environment. **Each line must be run one-by-one** to prevent errors and ensure successful execution.

                     .. code-block::

                         export SWAP_DATADIR=/Users/$USER/coinswaps
                         mkdir -p "$SWAP_DATADIR/venv"
                         python3 -m venv "$SWAP_DATADIR/venv"
                         . $SWAP_DATADIR/venv/bin/activate && python -V
                         cd $SWAP_DATADIR
                         wget -O coincurve-anonswap.zip https://github.com/tecnovert/coincurve/archive/refs/tags/anonswap_v0.1.zip
                         unzip -d coincurve-anonswap coincurve-anonswap.zip
                         mv ./coincurve-anonswap/*/{.,}* ./coincurve-anonswap || true
                         cd $SWAP_DATADIR/coincurve-anonswap
                         pip3 install .
                         cd $SWAP_DATADIR
                         git clone https://github.com/tecnovert/basicswap.git 
                         cd $SWAP_DATADIR/basicswap

                 #. Install root SSL certificates for the SSL module (more information `here <https://pypi.org/project/certifi/>`_).

                         .. code-block::

                             sudo python3 bin/install_certifi.py

                 #. Continue with the BasicSwap installation, executing the following two commands **one by one**.
                         
                         .. code-block::

                             protoc -I=basicswap --python_out=basicswap basicswap/messages.proto
                             pip3 install .

     .. group-tab:: Linux
 
             .. rst-class:: bignums
 
                 #. Install the required dependencies

                     .. code-block::

                         apt-get install -y wget python3-pip gnupg unzip protobuf-compiler automake libtool pkg-config curl jq

                 #. Execute the commands below sequentially to setup the environment. **Each line must be run one-by-one** to prevent errors and ensure successful execution.

                     .. code-block::

                         export SWAP_DATADIR=/Users/$USER/coinswaps
                         mkdir -p "$SWAP_DATADIR/venv"
                         python3 -m venv "$SWAP_DATADIR/venv"
                         . $SWAP_DATADIR/venv/bin/activate && python -V
                         cd $SWAP_DATADIR
                         wget -O coincurve-anonswap.zip https://github.com/tecnovert/coincurve/archive/refs/tags/anonswap_v0.1.zip
                         unzip -d coincurve-anonswap coincurve-anonswap.zip
                         mv ./coincurve-anonswap/*/{.,}* ./coincurve-anonswap || true
                         cd $SWAP_DATADIR/coincurve-anonswap
                         pip3 install .
                         cd $SWAP_DATADIR
                         git clone https://github.com/tecnovert/basicswap.git 
                         cd $SWAP_DATADIR/basicswap
                         protoc -I=basicswap --python_out=basicswap basicswap/messages.proto
                         pip3 install .

Configure BasicSwap
-------------------

After the installation, configure BasicSwap according to your requirements.

.. tabs::

     .. group-tab:: Mac OS
 
             .. rst-class:: bignums

                 #. Open :guilabel:`Terminal` (i.e., :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`).

                 #. Navigate to your BasicSwap folder.

                     .. code-block:: bash

                         cd /Users/$USER/coinswaps

                 #. Set :guilabel:`xmrrestoreheight` to Monero's current chain height.

                     .. code-block:: bash

                         CURRENT_XMR_HEIGHT=$(curl https://localmonero.co/blocks/api/get_stats | jq .height)

             	#. Select the cryptocurrencies you want to activate (Particl is activated by default). You must specify your choices in the configuration command. :ref:`See here <compatible coins>` for a complete list of compatible currencies on BasicSwap.

             	#. Decide on whether to perform a fast sync of the Bitcoin blockchain using a checkpoint or to synchronize from the beginning. This choice affects whether you include the :guilabel:`--usebtcfastsync` parameter in your configuration command.

             	#. Execute the following command to configure your BasicSwap Docker image, adjusting it according to your preferences as described above.

                     .. code-block:: bash

                         basicswap-prepare --datadir=$SWAP_DATADIR --withcoins=monero,bitcoin --xmrrestoreheight=$CURRENT_XMR_HEIGHT --usebtcfastsync

     .. group-tab:: Linux
 
             .. rst-class:: bignums
 
                 #. Open a terminal.

                 #. Navigate to your BasicSwap folder.

                     .. code-block:: bash

                         cd /Users/$USER/coinswaps

                 #. Set :guilabel:`xmrrestoreheight` to Monero's current chain height.

                     .. code-block:: bash

                         CURRENT_XMR_HEIGHT=$(curl https://localmonero.co/blocks/api/get_stats | jq .height)

            	 #. Select the cryptocurrencies you want to activate (Particl is activated by default). You must specify your choices in the configuration command. :ref:`See here <compatible coins>` for a complete list of compatible currencies on BasicSwap.

             	 #. Decide on whether to perform a fast sync of the Bitcoin blockchain using a checkpoint or to synchronize from the beginning. This choice affects whether you include the :guilabel:`--usebtcfastsync` parameter in your configuration command.

             	 #. Execute the following command to configure your BasicSwap Docker image, adjusting it according to your preferences as described above.

                     .. code-block:: bash

                         basicswap-prepare --datadir=$SWAP_DATADIR --withcoins=monero,bitcoin --xmrrestoreheight=$CURRENT_XMR_HEIGHT --usebtcfastsync

Start BasicSwap
---------------

After configuring your Docker image, the next step is to run it. Doing so will launch BasicSwap, making it accessible through web browsers.

.. tabs::

     .. group-tab:: Mac OS
 
             .. rst-class:: bignums

                 #. Open :guilabel:`Terminal` (i.e., :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`).

                 #. Navigate to your BasicSwap folder.

                     .. code-block:: bash

                         cd /Users/$USER/coinswaps

                 #. Launch BasicSwap.

                     .. code-block:: bash

                         basicswap-run --datadir=$SWAP_DATADIR

                 #. Open BasicSwap's user interface in your favorite web browser by navigating to the following address.

                     .. code-block:: bash

                         http://localhost:12700

     .. group-tab:: Linux
 
             .. rst-class:: bignums
 
                 #. Open a terminal.

                 #. Navigate to your BasicSwap folder.

                     .. code-block:: bash

                         cd /Users/$USER/coinswaps

                 #. Launch BasicSwap.

                     .. code-block:: bash

                         basicswap-run --datadir=$SWAP_DATADIR

                 #. Open BasicSwap's user interface in your favorite web browser by navigating to the following address.

                     .. code-block:: bash

                         http://localhost:12700

----

.. seealso::

 - BasicSwap Explained - :doc:`BasicSwap Explained <../basicswap-dex/basicswap_explained>`
 - BasicSwap Guides - :doc:`Update BasicSwap <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Route BasicSwap Through Tor <../basicswap-guides/basicswapguides_update>`
 - BasicSwap Guides - :doc:`Make an Offer <../basicswap-guides/basicswapguides_make>`
 - BasicSwap Guides - :doc:`Take an Offer <../basicswap-guides/basicswapguides_take>`
