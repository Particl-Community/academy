===========
Get Started 
===========

.. title::
   Particl Marketplace Installation Guide
   
.. meta::
   :description lang=en: Learn how to install Particl Marketplace on your desktop computer 
   :keywords lang=en: Particl, Marketplace, Installation, Quickstart, Blockchain, Privacy, E-Commerce, multi-vendor marketplace, online marketplace

:term:`Particl Marketplace` provides you with the most secure, private, and unrestricted e-commerce experience on the web. This section will teach you how to install and configure it to your liking, as well as how to back up your Marketplace data.

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Install Particl Marketplace
===========================

To get started with :term:`Particl Marketplace`, you need to first download and install the Particl Desktop client.

Download
--------

Choose the correct version to download.

.. tabs::
     .. group-tab:: Windows

         **Windows file version**

         Download the :file:`particl-desktop-X.X.X-win.exe` installer file. It supports any version of Windows.

         **Download sources**

         - Particl Homepage: https://particl.io/downloads
         - Particl Github: https://github.com/particl/particl-desktop/releases/latest

        .. attention::

            NEVER download Particl clients from third-party websites! Bad actors are constantly trying to distribute malware-infected versions of popular :term:`cryptocurrency <Cryptocurrency>` wallets to steal your funds! Always download directly from official sources.

     .. group-tab:: Mac

         **MacOS file version**

         Download the :file:`particl-desktop-X.X.X-mac.dmg` installer image. It supports any version of MacOS.

         **Download sources**

         - Particl Homepage: https://particl.io/downloads
         - Particl Github: https://github.com/particl/particl-desktop/releases/latest

        .. attention::

            NEVER download Particl clients from third-party websites! Bad actors are constantly trying to distribute malware-infected versions of popular :term:`cryptocurrency <Cryptocurrency>` wallets to steal your funds! Always download directly from official sources.

     .. group-tab:: Linux

         **Linux file version**

         Depending on your Linux distribution, you can choose between different packages, including Debian-based :file:`.deb`, :file:`.rpm` packages, or a distribution-independent :file:`.AppImage` version.

         Once you know which Linux distribution you are running, it is easy to find out which package manager you have,  and which package will suit you. The distribution independent :file:`.AppImage` will also be of great help.

         **Download sources**

        - Particl Homepage: https://particl.io/downloads
        - Particl Github: https://github.com/particl/particl-desktop/releases/latest

        .. attention::

            NEVER download Particl clients from third-party websites! Bad actors are constantly trying to distribute malware-infected versions of popular :term:`cryptocurrency <Cryptocurrency>` wallets to steal your funds! Always download directly from official sources.

Installation process
--------------------

.. tabs::
     .. group-tab:: Windows

         **Windows installation**

         .. rst-class:: bignums

             #. :ref:`Verify the checksum <Checksum verification>` of the file.
             #. Open the downloaded :guilabel:`particl-desktop-X.X.X-win.exe` installer file.
             #. Follow the installation instructions.
             #. An executable file will be added to your desktop and into the application launcher menu. Use this to start :term:`Particl Desktop`.
             #. Assign allow-rules to your computer's firewall and antivirus software. On a standard Windows installation, :guilabel:`Microsoft Defender` pops up.

             .. note:: Ignoring step 5 may cause a degraded blockchain sync or communications problems with other peers. If you are unsure how to apply rules to your firewall and anti-virus software, please review the vendor's documentation of your installed programs.

     .. group-tab:: Mac

         **MacOS installation**

         .. rst-class:: bignums

             #. :ref:`Verify the checksum <Checksum verification>` of the file.
             #. Open the downloaded :guilabel:`particl-desktop-X.X.X-mac.dmg` installer image by pressing :kbd:`CONTROL` + :kbd:`MOUSE-RIGHT ◳` and clicking on :guilabel:`Open` from the appearing shortcut menu. *Do not just double-click the icon.*
             #. Drag and drop the :term:`Particl Desktop.app <Particl Desktop>` file into the :guilabel:`Applications` folder.
             #. Open the :guilabel:`Applications` folder and locate the :term:`Particl Desktop.app <Particl Desktop>` file.
             #. Press :kbd:`CONTROL` + :kbd:`MOUSE-RIGHT ◳` on the :term:`Particl Desktop.app <Particl Desktop>` file and click :guilabel:`Open`.
             #. On the first launch, your computer's firewall must get a rule to allow Particl Desktop to communicate with the blockchain.

         From now on, you will be able to start :term:`Particl Desktop` from the Launchpad or Spotlight (e.g., :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "Particl" > hit :kbd:`ENTER ↵`) search.

         .. note:: Ignoring step 6 may cause a degraded blockchain sync or communications problems with other peers. If you are unsure how to apply rules to your firewall and antivirus software, please review the vendor's documentation of your installed programs.

     .. group-tab:: Linux

         **Linux installation**

         .. rst-class:: bignums

             #. :ref:`Verify the checksum <Checksum verification>` of the file.
             #. Navigate to where you've downloaded your installer file in the terminal.

             #. *Depending on your package manager, this command will vary.*

                 **Debian-based installation**

                 .. code-block:: bash

                     sudo apt install particl-desktop-x.x.x-linux.deb

                **RPM-based installation**

                 .. code-block:: bash

                     sudo dnf -i particl-desktop-x.x.x-linux.rpm

                 **AppImage**

                 .. code-block:: bash

                     chmod a+x particl-desktop-x.x.x-linux.AppImage
                     ./particl-desktop-x.x.x-linux.AppImage

             #. On the first launch, your computer’s firewall must get a rule to allow Particl Desktop to communicate with the blockchain.

             An application launcher will be added to your applications menu when using :file:`.deb` or :file:`.rpm` installations. Click it to start the :term:`Particl Desktop` client.

             .. note:: Ignoring step 4 may cause a degraded blockchain sync or communications problems with other peers. If you are unsure how to apply rules to your firewall and antivirus software, please review the vendor's documentation of your installed programs.

         .. tip::

             If you want to launch it from the terminal, quotation marks may be required because there is a space in the name (Particl Desktop).


            .. code-block:: bash
    
                user@linux:~> which "Particl Desktop"
                /usr/bin/Particl Desktop
    
                user@linux:~> "/usr/bin/Particl Desktop"
                (Particl Desktop:16887)

.. rst-class:: achievement

    Congratulations! You have installed :term:`Particl Marketplace`.

.. hint::

    **Loading and Syncing Times**

     Because the :term:`Particl Marketplace`'s content is hosted on a distributed network for payments and exchange of data, the marketplace may take a few minutes to sync. It may also take a few more minutes to load all marketplace listings fully. Those short wait times are normal in the current state of the marketplace and will get much faster in future updates.

     If you open the :guilabel:`Market` > :guilabel:`Browse` module, keep an eye on the :guilabel:`Refresh` button. As soon as a count appears, new listings have arrived. Click on it to refresh the listings display. With very slow connections, the entire syncing process can sometimes take up to an hour.

Checksum verification
---------------------

Obtain the checksum code from the official download sources for the downloaded file. Each file has its own checksum.

From the official download source, obtain the checksum of the file you’ve just downloaded. Each file has its own checksum, so make sure you select the release you’ve downloaded.

To verify the integrity of the downloaded file — ensuring that it hasn’t been tampered with in any way — validate your file’s hash against the checksum provided in the official download source.

.. tabs::
     .. group-tab:: Windows

         **Checksum verification command with terminal**

         .. rst-class:: bignums

             #. Open :guilabel:`Windows Explorer`.
             #. Press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the Download folder and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
             #. Type the following command into the terminal while changing :file:`filename` for the real and complete filename of the downloaded file and hit :kbd:`ENTER ↵`.

                 .. code-block:: bash

                     CertUtil -hashfile filename SHA256

     .. group-tab:: Mac

         **Checksum verification command with terminal**

         .. tip::
             **Prerequisite**: Head into :guilabel:`System Preferences` and select :guilabel:`Keyboard` > :guilabel:`Shortcuts` > :guilabel:`Services`. Find :guilabel:`New Terminal at Folder` in the settings and enable the checkbox.

        .. rst-class:: bignums

             #. Open :guilabel:`Finder`.
             #. Press :kbd:`MOUSE-RIGHT ◳` on the Download folder of the file and you're shown the :guilabel:`services` > :guilabel:`open terminal` command to open the terminal at this location.
             #. Type the following command into the terminal while changing :file:`filename` for the real filename of the downloaded file.

                .. code-block:: bash

                    shasum -a 256 filename

     .. group-tab:: Linux

         **Checksum verification command with terminal**

         .. rst-class:: bignums

             #.  Open a terminal where you downloaded the file and type the following command by changing :file:`filename` for the real filename of the downloaded file.
         
                 .. code-block:: bash

                     sha256sum filename

Once that is done, compare the checksum output you've received in the step above with the checksum provided in the official download sources. The screenshot below shows an example of this checksum highlighted from the GitHub release notes :guilabel:`Verification` section.

.. figure:: ../_static/media/images/mp_installation_github_checksum_verification.png
    :align: center
    :alt: Particl Marketplace installation checksum highlighted image
    :target: ../_static/media/images/mp_installation_github_checksum_verification.png

    Particl Marketplace installation checksum highlighted image

**Troubleshooting checksum mismatch**

If the output does not match, try downloading the file again. Verify that you did not unzip or rename the file. In some cases, it might be possible that antivirus software may alter files; be sure to have a solution on your own in that case.

.. attention::
    
    If all attempts fail to have a matching number, do not install :term:`Particl Desktop` unless you know what you are doing, and reach out to :doc:`Particl Support <../faq/get_support>` for assistance.

Starting Particl Desktop
------------------------

You have two options: startup with the launcher icon (recommended) or a terminal command.

Startup with Launcher
~~~~~~~~~~~~~~~~~~~~~

.. tabs::

    .. group-tab:: Windows

         **Launching Particl Desktop with Launcher**

         .. rst-class:: bignums

             #. Open your :guilabel:`Start Menu` by pressing the :kbd:`WIN ⊞` key.
             #. Start typing :code:`Particl`.
             #. Click on the :term:`Particl Desktop` launcher icon.

    .. group-tab:: Mac

         **Launching Particl Desktop with Launcher**

         .. rst-class:: bignums

             #. Open :guilabel:`Spotlight` (e.g., :kbd:`COMMAND ⌘` + :kbd:`SPACE`).
             #. Type :code:`Particl`.
             #. Click on the :term:`Particl Desktop` launcher icon.

    .. group-tab:: Linux

         **Launching Particl Desktop with Launcher**

         .. rst-class:: bignums
         
             #. Open your applications menu.
             #. Click on :term:`Particl Desktop` launcher icon.

Startup from Terminal
~~~~~~~~~~~~~~~~~~~~~

Sometimes it is handy to start :term:`Particl Marketplace` from the terminal, aka command line. It gives you plenty of output and information about what is happening in the background.

.. tabs::

    .. group-tab:: Windows

         **Launching Particl Desktop from terminal**

         .. rst-class:: bignums

             #. Open :guilabel:`Windows Explorer`.
             #. Press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the Installation folder (e.g., :file:`C:\/Program Files\/Particl`) and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
             #. Type the following command into the terminal and hit :kbd:`ENTER ↵`.

                 .. code-block:: bash

                     “Particl Desktop.exe”

    .. group-tab:: Mac

         **Launching Particl Desktop from terminal**

         .. rst-class:: bignums

             #. Open :guilabel:`Terminal` (i.e., :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`).
             #. Type in this command:

                .. code-block:: bash

                    /Applications/Particl\ Desktop.app/Contents/MacOS/Particl\ Desktop

    .. group-tab:: Linux

         **Launching Particl Desktop from terminal**

         .. rst-class:: bignums
         
             #. Open a terminal in the folder where you've installed :term:`Particl Desktop` and type the following command.
        
                .. code-block:: bash

                    ./Particl\ Desktop


.. include:: /faq/common_issues_desktop_installation.rst.txt


Backup Account and Data
=======================

File locations
--------------

After a successful installation of :term:`Particl Desktop`, the main application has been installed into the standard location of your operating system. When running Particl Desktopfor the first time, it will create user-specific data within your user account. These files include settings, log files, wallets, and the blockchain data itself. We recommend manually backing up that data on a secure device from time to time as a good practice to follow.

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

.. attention::

    For security reasons, Tor is the *only* privacy setting not enabled by default. You can easily enable it by routing your client's connection through its network.

.. danger::
    
    Always make sure your :term:`Tor` :term:`node <node>` is up-to-date with the latest version. This is a critical requirement that, if not followed, can heavily compromise your online privacy and potentially let other people spy on your online activity.

To make sure you don't download a compromised version of Tor, always download it from their official website. Additionally, avoid any `man-in-the-middle attack <https://en.wikipedia.org/wiki/Man-in-the-middle_attack>`_ by always verifying the encrypted signature attached to the Tor files you download. To do so, follow this tutorial on `how to verify Tor signatures <https://support.torproject.org/tbb/how-to-verify-signature/>`_ written by the :term:`Tor` team itself.    

You can run the :term:`Tor` network using two different methods, after which you can route Particl Desktop through it. Always make sure that, regardless of the installation method you choose, :term:`Tor` is running the latest version before using it.

Using the Tor browser
---------------------

.. rst-class:: bignums

    #. Download the `Tor Browser <https://www.torproject.org/download/>`_ and install it on your computer.
    #. Launch the :term:`Tor` browser.
    #. Connect to the :term:`Tor` network by clicking on :guilabel:`Connect` or configure your connection parameters by clicking on :guilabel:`Configure`.
    #. Once connected, leave the :term:`Tor` Browser running in the background of your computer.


Using the Tor daemon
--------------------

.. tabs::

    .. group-tab:: Windows

        .. rst-class:: bignums

            #. Download the `Tor Browser <https://www.torproject.org/download/>`_ and install it on your computer.
            #. Open :guilabel:`Windows Explorer` and navigate to the :term:`Tor` installation directory (e.g., :file:`C:\/Program Files\/Tor Browser`).
            #. Go into the :file:`Tor` directory, hold down :kbd:`SHIFT ⇧` and click with :kbd:`MOUSE-RIGHT ◳`.
            #. Open the :guilabel:`Open command window here` from the menu.
            #. In the terminal that pops up, type:

                .. code-block:: bash

                    tor.exe –service install

            #. Verify that the :term:`Tor` service is running, type:
            
                .. code-block:: bash

                    sc query "Tor" | find "RUNNING"

    .. group-tab:: Mac

         .. tip::

             If you haven’t got Homebrew yet, install it using this terminal command.

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

         .. rst-class:: bignums

            #. Open a :guilabel:`Terminal`
            #. Install the :term:`Tor` daemon by typing:

                .. code-block:: bash

                    sudo apt install tor

            #. Make sure :term:`Tor` launches on startup by typing:

                .. code-block:: bash

                    sudo systemctl enable tor


Enable Tor on Particl Desktop
-----------------------------

After starting Tor on your computer using either the Tor Browser or a daemon, route your :term:`Particl Desktop` connection through it. You can do this by either adding a proxy argument to the desktop’s launch command or by changing its settings after launching the application. 

Enable Tor by Default From GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

    #. Open :term:`Particl Desktop` and click on :guilabel:`Particl Desktop Settings` in the bottom left corner.
    #. Go to :guilabel:`Core network connection` and enter :code:`127.0.0.1:9150` into the :guilabel:`Connect via Proxy` field if you are using the Tor Browser OR :code:`127.0.0.1:9050` if you are using the Tor daemon.
    #. Hit :guilabel:`Save changes` and restart :term:`Particl Desktop`.

Enable by Tor Default From Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

    #. Open the configuration file:

        .. code-block:: bash

            nano ~/.particl/particl.conf

    #. If you are using Tor Browser, add this line to the configuration file:

        .. code-block:: bash

            proxy=127.0.0.1:9150
        
        If you are using Tor daemon, add this line to the configuration file:

        .. code-block:: bash

            proxy=127.0.0.1:9050    

.. note::

    From now on, :term:`Particl Desktop` will always connect to the internet using Tor. If :guilabel:`Tor` is not running on your machine, then :term:`Particl Desktop` will not be able to connect to other peers. You can always revert back to the default setting to disable Tor.

Enable Tor Once From Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

    .. group-tab:: Windows

         **Launching Particl With Tor**

         .. rst-class:: bignums

             #. Open :guilabel:`Windows Explorer`, press :kbd:`SHIFT ⇧` + :kbd:`MOUSE-RIGHT ◳` on the installation folder (e.g., :file:`C:\/Program Files\/Particl`), and choose :guilabel:`Open command window here` or :guilabel:`Open power shell here`.
             #. If you are using Tor Browser, type the following commands into the terminal and hit :kbd:`ENTER ↵`.
                 
                 .. code-block:: bash

                     “Particl Desktop.exe” -proxy=127.0.0.1:9150
                 
                 If you are using Tor daemon, type the following commands into the terminal and hit :kbd:`ENTER ↵`.

                 .. code-block:: bash

                     “Particl Desktop.exe” -proxy=127.0.0.1:9050        

    .. group-tab:: Mac

         **Launching Particl With Tor**

         .. rst-class:: bignums

             #. Open :guilabel:`Terminal` (e.g., :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal", then hit :kbd:`ENTER ↵`).
             #. Type in this command if you are using Tor Browser:

                .. code-block:: bash

                    /Applications/Particl\ Desktop.app/Contents/MacOS/Particl\ Desktop -proxy=127.0.0.1:9150

                Type in this command if you are using Tor daemon:

                .. code-block:: bash

                    /Applications/Particl\ Desktop.app/Contents/MacOS/Particl\ Desktop -proxy=127.0.0.1:9050    

    .. group-tab:: Linux

         **Launching Particl With Tor**

         .. rst-class:: bignums
         
             #. Open a terminal in the folder where you've installed :term:`Particl Desktop` and type the following command if you are using Tor Browser.
        
                .. code-block:: bash

                    ./Particl\ Desktop -proxy=127.0.0.1:9150

                Type the following command if you are using Tor daemon.
        
                .. code-block:: bash

                    ./Particl\ Desktop -proxy=127.0.0.1:9050        


Using Tor as a Hidden Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Linux, you can also run :term:`Tor` as a hidden service and connect your :term:`Particl Desktop` to it. This allows other people to use your :term:`node <Node>` as an entry or exit point, making the :term:`Tor` network more :term:`decentralized <Decentralization>` and private for all.

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

    #. Restart :term:`Tor` by typing into the terminal:
    
        .. code-block:: bash
        
            sudo service tor restart

    #. Find your hidden service’s IP address (.onion) by typing:
    
        .. code-block:: bash

            sudo cat /var/lib/tor/particl-service/hostname

    #. Modify your Particl config file to route its connection through your hidden service by typing:

        .. code-block:: bash

            touch ~/.particl/particl.conf && nano ~/.particl/particl.conf

        Then add these lines to the file, and don't forget to set :code:`yourexternalip.onion`

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

Important Considerations
------------------------

Keep Tor up-to-date
~~~~~~~~~~~~~~~~~~~

It is critical to manually maintain your :term:`Tor` node to the latest version. Otherwise, you can heavily compromise your online privacy and security by remaining vulnerable to a wide range of potential attacks on the network. 

As the network itself is widely targeted by hackers due to the privacy it provides, unpatched versions of :term:`Tor` are considered unsafe to use. If exploited, a compromised version of :term:`Tor` may leak your true identity and even let others spy on your online activity.

:term:`Tor` constantly pushes important security updates, so make sure to always be on the lookout for them.

.. tabs::
     .. group-tab:: Windows

         **Updating Tor**

         .. rst-class:: bignums

             #. Open the :term:`Tor` Browser.
             #. Check if the browser prompts you to update to a newer version.

     .. group-tab:: Mac

         **Updating Tor**

         .. rst-class:: bignums

             #. Open :guilabel:`Terminal` (e.g., :kbd:`COMMAND ⌘` + :kbd:`SPACE` and type "terminal" > hit :kbd:`ENTER ↵`).
             #. Type this line of code and  hit :kbd:`ENTER ↵`.

                 .. code-block:: bash
    
                     brew update && brew upgrade

     .. group-tab:: Linux

         **Updating Tor**

         .. rst-class:: bignums

             #. Open a :guilabel:`Terminal` and run the upgrade procedure depending on your package manager.

                 **Example**

                 .. code-block:: bash

                     sudo apt update && sudo apt-upgrade

         Depending on your Linux distribution, this command may vary. There are multiple package managers out there, but they all have the same role in this case.

----

.. seealso::

 - Marketplace Guides - :doc:`Install and Get Started <../marketplace-guides/marketguides_installation>`
 - Marketplace Guides - :doc:`Sell Stuff <../marketplace-guides/marketguides_sell>`
 - Marketplace Guides - :doc:`Buy Stuff <../marketplace-guides/marketguides_buy>`
 - Particl Wiki - `Open Market Protocol <https://particl.wiki/learn/marketplace/open-market-protocol/>`_
 - Particl Wiki - `SecureMessaging <https://particl.wiki/learn/marketplace/smsg/>`_
 - Github - `Particl Desktop <https://github.com/particl/particl-desktop>`_
 - Github - `Particl Core <https://github.com/particl/particl-core>`_
 - Unofficial Gateway - `Particl Store <https://particl.store/>`_
 - Unofficial Gateway - `Particl Marketplace Shop <http://particlmarketplace.shop/>`_
 - Particl Explained - :doc:`Privacy Specifications <../particl-blockchain/blockchain_privacy>`
 - Particl Explained - :doc:`Two-Party Escrow System <../particl-marketplace/marketplace-escrow>`
