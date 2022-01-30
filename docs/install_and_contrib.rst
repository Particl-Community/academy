==================================
Contribution Tutorial and Workflow
==================================

The best installation tutorial, best practices, and the complete workflow from A-Z for all OS's. 

If you want to contribute to the Academy as a power contributor follow this tutorial. It will save you from a lot of headaches and lost time equally. You will learn how to render a local HTML copy of the Academy and how to push your edits into the live version.  

If you are an occasional contributor and you only want to add one or two lines, or fix some typos, hit the :guilabel:`Edit on Github` button in the top right corner on the Academy website, it will serve you well without bloat.

.. note::

   **General Contribution Flow**

   1. Fork the :code:`particl-community/academy` repository as your forked repository and clone the forked repository into your local repository.
   2. Do your changes, review them in a local live version of the Academy, commit them, and push from your local to your forked repository on Github.
   3. Create a pull request as your contribution's integration request on the upstream :code:`particl-community/academy` repository.
   4. After a manual review by the maintainers, your code gets merged.
   5. A new Academy version gets rendered and is instantly available.
   6. Congrats, you've created footsteps and contributed to Particl's history. 


The process of writing documentation and translations is a tedious and time-consuming task, and you will most likely get very little appreciation in doing so. I can assure you, solely the purpose is worth it, against all odds because you are Particl!

.. rst-class:: achievement
   
   Now, let's go dance with it!

Installation of prerequisite tools
----------------------------------

It's time to ensure the installation of some packages like a proper package manager, Git, Python, Sphinx, Sublime Text, and Sublime Merge.

**Package Manager**

It takes the hassle off you searching for installation binaries and makes it a breeze to keep them updated.

.. admonition:: See also

   * Windows: `Chocolatey <https://chocolatey.org>`_ is an installation package manager for Windows.
   * Mac: `Brew <https://brew.sh>`_ is a package manager for Mac and sometimes Linux as well
   * Linux: There are plenty. APT, DNF, YUM, Zypper, Pacman, SNAP ... to name a few. 

**Git**

It's the foundation protocol to handle code versions and collaboration on Github.

.. admonition:: See also

   * Git Docs `What is Git <https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F#what_is_git_section>`_
   * Git Website https://git-scm.com
   * Github Website https://github.com
   * GitDocs https://git-scm.com/docs
   * Cheatsheets https://training.github.com

**Python**

It's the foundational language to run Sphinx.

**Sphinx**

Sphinx is a program that makes it easy to create intelligent documentation in reST. reStructuredText is a file format for textual data used primarily in the Python programming language community for technical documentation. reStructuredText is comparable to Markdown but with added functionality. Technically, Sphinx takes the .rst files and renders different outputs like the HTML or PDF versions of the Academy.

.. admonition:: See also

   * Local Examples :ref:`Test page on the Academy<Testpage>`
   * Sphinx Docs `Sphinx Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
   * Sphinx Docs `TOC <https://www.sphinx-doc.org/en/master/usage/index.html>`_

**Sublime Text**

It's a leightweight and sophisticated text editor with a myriad of extensions available. Technically, you could use any text editor, but this one is described in detail in the follow-up tutorials.

.. admonition:: See also

   * Website https://www.sublimetext.com
   * Docs https://www.sublimetext.com/docs/index.html
   * Extensions https://packagecontrol.io

**Sublime Merge**

It's a sophisticated GUI for managing Git repositories. Technically, you could use any git manager, but this one is described in detail in the follow-up tutorials.

.. admonition:: See also

   * Website https://www.sublimemerge.com
   * Docs https://www.sublimemerge.com/docs/

Download & Install the Package Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. group-tab:: Windows

      .. rst-class:: bignums

         #. Open Windows Powershell (`As Administrator <https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.2#with-administrative-privileges-run-as-administrator>`_)
         #. Paste :code:`Get-ExecutionPolicy` and hit :kbd:`Enter`. If it returns **"Restricted"**, paste :code:`Set-ExecutionPolicy AllSigned` and hit :kbd:`Enter`. Answer with :kbd:`A`.
         #. Paste the code below and hit :kbd:`Enter` 

         .. code-block:: bash

            Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

   .. group-tab:: MacOS

      .. rst-class:: bignums

         #. Open Terminal

         #. Paste the code below and hit :kbd:`Enter`

         .. code-block:: bash

            xcode-select --install
            ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
            echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.profile

   .. group-tab:: Linux

      Linux has everything on board!


Download & Install Additional Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. group-tab:: Windows

      .. rst-class:: bignums

         #. Open Windows Powershell (`As Administrator <https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.2#with-administrative-privileges-run-as-administrator>`_)
         #. Paste the code below and hit :kbd:`Enter` 

         .. code-block:: bash

            choco install git git-lfx gh sublimetext4 sublimemerge -y
            choco install python -y
            # close the powershell and open a new one; then proceed
            pip install sphinx sphinx-rtd-theme sphinx-copybutton sphinx-tabs rst2pdf


   .. group-tab:: MacOS

      .. rst-class:: bignums

         #. Open Terminal
         #. Paste the code below and hit :kbd:`Enter` 

         .. code-block:: bash

            brew install git git-lfs gh sublime-text sublime-merge
            brew install python
            brew link python
            pip install sphinx sphinx-rtd-theme sphinx-copybutton sphinx-tabs rst2pdf

         **Check Python Versions**

         For Python it should be 3.x and for Pip 21.x pointing to the same Python version. 

         .. code-block:: bash
            
            python --version
            pip -V

         If this is not the case set an alias.

         .. code-block:: bash

            echo 'alias python=python3' >> ~/.bash_aliases
            echo 'alias pip=pip3' >> ~/.bash_aliases
            source ~/.bash_aliases
   

   .. group-tab:: Linux

      .. rst-class:: bignums

         #. Get inspiration from the MacOS documentation and adapt it to your package manager. Unless, you're a die hard Gentoo guy.

         #. Python installation can be tricky if you are in the need to maintain multiple versions. Even in this case, feel free to get some inspirations from the MacOS documentation.

.. rst-class:: achievement

  Congratulations! You have installed everything you need.

Get the Process Flying
----------------------

Create a Github account, grab data from Github into your fork and local destinations, learn a bit about branches and strategies, and follow the first configuration steps to make your workflow as easy and fast as possible.

Create a Github Account
~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

   #. Go to https://github.com/login
   #. Click on :guilabel:`Create an account` and follow through
   #. Confirm the account according to the TOS
   #. Store your Github Credentials locally

      By leaving out to store the Github login data, you’ll get prompted to enter a password every time you push something to Github. So, you want to store them –really.

      .. tabs::

         .. group-tab:: Windows

            Please follow the `official guides <https://github.com/GitCredentialManager/git-credential-manager#standalone-installation>`_. 
            And `download <https://github.com/GitCredentialManager/git-credential-manager/releases/latest>`_ here.

         .. group-tab:: MacOS

            Open Terminal and paste the code below and hit :kbd:`Enter` 

            .. code-block:: bash

               brew tap microsoft/git
               brew install --cask git-credential-manager-core

         .. group-tab:: Linux

            Please follow the `official guides <https://github.com/GitCredentialManager/git-credential-manager#linux>`_ and `download <https://github.com/GitCredentialManager/git-credential-manager/releases/latest>`_ here. Please don't miss the additional credstore configuration tutorial for `linux <https://aka.ms/gcm/credstores>`_.

   .. admonition:: see also

         * Github `About Authentication on Github <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github>`_
         * Github `Configuration Options Tutorial <https://github.com/GitCredentialManager/git-credential-manager/blob/main/docs/configuration.md>`_
         * Github `Cred Store Information <https://github.com/GitCredentialManager/git-credential-manager/blob/main/docs/credstores.md>`_
         * Github `Personal Access Token <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>`_


Fork the Academy Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

   #. Go to https://github.com/Particl-Community/academy
   #. Click on :guilabel:`Fork`

Now you have created a fork repository :code:`[username]/academy` to work on. 

.. hint::

   It's never wrong to know a bit about `Remote repositories <https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories>`_.

Clone your Forked Academy Repository Locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. group-tab:: Windows

      .. rst-class:: bignums

         #. Open Powershell

         #. Paste the code below and hit :kbd:`Enter` (Don't forget to change `YOUR-GH-USERNAME`.)

         .. code-block:: bash

            cd %USERPROFILE%
            git clone https://github.com/YOUR-GH-USERNAME/academy.git


   .. group-tab:: MacOS

      .. rst-class:: bignums

         #. Open Terminal

         #. Paste the code below and hit :kbd:`Enter` (Don't forget to change `YOUR-GH-USERNAME`.)

         .. code-block:: bash

            cd ~
            git clone https://github.com/YOUR-GH-USERNAME/academy.git

   .. group-tab:: Linux

      .. rst-class:: bignums

         #. Open Terminal

         #. Paste the code below and hit :kbd:`Enter` (Don't forget to change `YOUR-GH-USERNAME`.)

         .. code-block:: bash

            cd ~
            git clone https://github.com/YOUR-GH-USERNAME/academy.git

Now you have everything you need to start tackling the Academy. By default, you are on the **master** branch of the Academy's repository. Let's configure Git, Sublime Text, and Sublime Merge.

Configure Sublime Text
~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

   #. Open :guilabel:`Sublime-Text`
   #. Click on :guilabel:`File` > :guilabel:`Open Folder` > Navigate to and select the previously cloned :code:`academy` folder.
   #. Create a new build shortcut

      #. Click on :guilabel:`Tools` > :guilabel:`Build System` > :guilabel:`New Build System`
      #. Copy and paste the code below (don't forget to check if the folder is true in your case)

      .. tabs::

         .. group-tab:: Windows

            .. code-block:: bash

               {
               "shell_cmd": "cd %USERPROFILE%\\academy & rmdir /s /q _build & make html"
               }

         .. group-tab:: MacOS

            .. code-block:: bash

               {
               "shell_cmd": "cd ~/academy && rm -Rf _build && make html"
               }

         .. group-tab:: Linux

            .. code-block:: bash

               {
               "shell_cmd": "cd ~/academy && rm -Rf _build && make html"
               }

      #. Save as :code:`buildAcademy.sublime-build`
      #. Make it the default build system

         Click on :guilabel:`Tools` > :guilabel:`Build System` > :guilabel:`buildAcademy`
   
   #. Render Test

      If you hit :kbd:`CTRL` + :kbd:`B` or :kbd:`CMD` + :kbd:`B` on a Mac the Academy gets rendered locally as HTML within the folder :code:`_build`

      In order to open it in the Internet Browser use the :guilabel:`Folders navigation` in Sublime Text's :guilabel:`Side Bar` and unfold the :guilabel:`_build` folder. Go ahead to :code:`html/index.html`, press the :guilabel:`Right Mouse Button` -> :guilabel:`Reveal in XX` -> press the :kbd:`Right Mouse Button` on the :code:`index.html` file and chose :guilabel:`Open with` or just Drag and Drop the file into your preferred Browser.

      Each time you make a change in your local copy of the Academy press :kbd:`CTRL` + :kbd:`B` or :kbd:`CMD` + :kbd:`B` on a Mac to get it rendered and refresh the page in the Browser to see the changes.

   #. Save the project

      If you save your project into a project file you are able to resume your work where you left it. It's a handy tool.

      #. Click :guilabel:`Project` > :guilabel:`Save project as`

   .. admonition:: see also

         * Sublime Docs `Build System <https://www.sublimetext.com/docs/build_systems.html>`_

Configure Sublime Merge
~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

   #. Open Sublime Merge from Sublime Text on location

      Use the :guilabel:`Folders navigation` in Sublime Text's :guilabel:`Side Bar` and press the :guilabel:`Right Mouse Button` on the :guilabel:`academy` folder and choose :guilabel:`Open Git Repository` -> Sublime Merge opens.

   #. Your forked repository is your origin

      Since you have cloned your forked repository from your account its considered as :code:`origin` repository. 

   #. Add the upstream repository

      Click :kbd:`Right Mouse Button` on :guilabel:`Remotes` > select :guilabel:`Add remote` > set name to :code:`upstream` and paste the URL :code:`https://github.com/Particl-Community/academy.git`.

.. note::

   Adding the upstream repository helps you later on to fetch updates and merge them into your local and origin repositories.

   Sublime Merge is currently not capable to perform pull requests to upstreams. That's why you will need to push your local commits to your fork repository and create a PR from Github's website. There are ways to do this on the CLI but they are not covered in this tutorial.

.. rst-class:: achievement

  Congratulations! You you're almost there. Now let's talk about workflow strategies.


Merging, Branching, and Commits
-------------------------------

Branches in Git are snapshots of your code repository at a given state. You can switch between them and/or merge code back and forth.

With your initial cloning of your Academy as origin repository you're by default on the master branch. As soon as you checkout (switch) into a different branch all your files get modified according to its branch status. If you switch back, you're back on the initial code base.

.. attention::

   Creating commits has the purpose of documentation and identification of your code contributions. So, you're well-advised to be precise with your descriptions, and you are asked to keep related changes across multiple files into one commit but not mix up different topics in one commit. Otherwise, we will not accept your pull request (PR) if we see such a mess.

**Branch: Master**

*Purpose*

The master branch is the one where the live version of the Academy gets rendered from. As soon as changes are pushed to this branch on the upstream repository a new build process is invoked.

*What you can do here*

You can fix typos, add content, and create pull requests to the upstream repository. 


**Branch: Temp**

*Purpose*

The temp branch is the one where you can test things back and forth. As soon as you are happy with your changes you can merge them into your master branch and push it to your origin repository and finally create a pull request from there to get it integrated into the live version aka upstream repository.

*What you can do here*

Anything you want.

**Branch: 3.x**

*Purpose*

It is envisioned to be on par with the advancements of the Particl Desktop software. Currently, a version named repository will be a kind of archive or snapshot for that particular version. Localized versions will emerge and look like :code:`[VersionID]-[LangID]` where langID stands for your international abbreviation like for French its :code:`fr` and would look like this :code:`3.x-FR`, or :code:`3.x-DE` for German.

*What you can do here*

Currently nothing. But in the future it might become handy if we tend to write new documentations prior to a software release.

.. note::

   As soon as you want to change the in-depth structure, add new documents, or collaborate with multiple people at the same time it's due to work temporarily in a different branch and once its finalized it can get merged into the master branch. 

   **Side-note:** If you work with multiple people on a branch you will work with your personal fork of the repository not on the upstream repository. You can individually grant write-access to your origin repository version of the Academy. 


Creating a new branch
~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: bignums

   #. Open :guilabel:`Sublime Merge`
   #. Click :kbd:`Right Mouse Button` on :guilabel:`Branches` (It's automatically under your local repository)
   #. Give it a name depending on the usecase, e.g. :code:`Testground` and hit :kbd:`Enter`.
   #. Make it the activated branch by :kbd:`Right Mouse Button` > :guilabel:`Checkout [Branchname]`.
   #. Push the locally create branch to your origin repository

      #. Be sure the correct branch in selected in the menu.
      #. Click the small dropdown arrow :guilabel:`▼` next to the :guilabel:`↑` arrow. 
      #. Now choose the destination :guilabel:`origin` and click on :guilabel:`push`

   You  will recognize the local branch appears now under your :guilabel:`origin` branch which you can also verify on your Github page.

.. admonition:: see also

   * Library of Congress `Language Code List <https://www.loc.gov/standards/iso639-2/php/code_list.php>`_
   * Github Docs `Remote Repositories <https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories>`_
   * Github Docs `RR and PR <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-for-a-fork>`_
   * Git SCM `Branches in a Nutshell <https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>`_

A commit with PR by example
---------------------------

.. rst-class:: bignums

   #. Open :guilabel:`Sublime Text` and change your desired file

      As soon as you create a preview render with e.g. :kbd:`CTRL/CMD` + :kbd:`b` or you save the file, Git recognizes this change. 

   #. Open :guilabel:`Sublime Merge` 

      You'll find a new :guilabel:`unstaged` file in the list of :guilabel:`Commits`.

   #. Click on :guilabel:`Stage` to qualify this particular file (and more, if there are more to stage) for the desired commit.
   #. Enter a meaningful :guilabel:`Commit Message` e.g. :code:`Changed because; Or Typo fixed; Regression fixed;`.
   #. Click on :guilabel:`Stage X files` to confirm -> Your commit is written.
   #. Push this commit to your origin repository

      #. Be sure the correct branch in selected in the menu.
      #. Click the small dropdown arrow :guilabel:`▼` next to the :guilabel:`↑` arrow. 
      #. Now choose the destination :guilabel:`origin` and click on :guilabel:`push` ->Your commit is pushed to Github.

   #. Create the PR

      #. Open your origin academy repository on the Github website :code:`https://github.com/[USERNAME]/academy`
      #. You should see a yellow notification banner which invites you to create a PR towards the upstream repository.
      #. Leave an additional comment if you think it's due or leave the commit message as is. It's depending on the depth of your changes.
      #. Click on :guilabel:`Create pull request`


.. rst-class:: achievement

  Congratulations! That was a wild ride. Now you have gained a lot of knowledge nobody can take away from you. May your contribution be a blessing!


FAQ
---

.. container:: toggle

    .. container:: header

        **Where do I put images and videos?**

    Technically, they belong into the :code:`_/static/media/xxx` folders. Yet, we have not started to implement supportive graphics. When the right time has come we will let you know. Then you'll be able to add language based overlays or audio tracks.
   
.. container:: toggle

    .. container:: header

        **Can I start creating new pages in my native language?**

    We are aiming for a cohesive file and communications structure across all languages. So, we really, really want to have the english representation as the origin of all other translated contents and not vice versa. So, if you want to create content in your language, find out if there's already a branch named :code:`master-[LangID]` where langID stands for your international abbreviation like for French its :code:`fr` and would look like this :code:`master-FR`, or :code:`master-DE` for German. If not, create it and make a PR so that we know it has been claimed.

.. container:: toggle

    .. container:: header

        **What do I need to consider when translating content?**

    Try to find out if there’s already a language branch. You can find the branches on the upstream repository. The person who created it has a fork himself and is then a maintainer if no other person may have been denominated. Try to contact them to tackle your tasks as a team.

    It’s of utmost importance you have people at hand able to proofread your writings in any case. Ideally, a Particl unaware person can understand what you have written.

.. container:: toggle

    .. container:: header

        **Where do I find information how reStructuredText markup works?**

    It has been mentioned above. But here again: :ref:`Open Testpage <testpage>`.

.. container:: toggle

    .. container:: header

        **How can I discuss a certain topic regarding the Academy?**

    Open an :guilabel:`issue` on the `Upstream Academy Repository <https://github.com/particl-community/academy/issues>`_.

.. container:: toggle

    .. container:: header

        **Can I create some PR's for testing purposes?**

    You can create them, but they won't get merged. So, behave.

.. container:: toggle

    .. container:: header

        **Can I use a different software for editing?**

    Yes you can. Examples are `Atom <https://atom.io>`_ or `Visual Code <https://code.visualstudio.com>`_ or really any other text editor. But you'll need to adapt the processes yourself. So, everything in this tutorial is done the way to take you up to light-speed.
