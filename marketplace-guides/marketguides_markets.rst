=======================
Create and Join Markets
=======================

.. title::
   Particl Marketplace - Markets & Storefronts

.. meta::
      
      :description lang=en: Join or launch your own marketplace or online shops on Particl’s e-commerce platform. No fees, total privacy, and complete freedom for all.

On Particl Marketplace, you can create your own markets and storefronts or join a wide variety of user-generated ones. 

The only difference between a market and a storefront is user permissions. On a market, anyone with access to it can buy or sell anything. On a storefront, only those in possession of a publish key can sell. Others with access to the storefront but not its publish key can only purchase items.

.. note::

   To simplify the terminology, "markets" and "storefronts" may both be referred to as “markets”.

There’s no limit to how many markets you can join or create, and each of them can host an equally-unlimited number of listings. 

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

.. container:: toggle

    .. container:: header

        **Create a Market**

    You can easily create a new market by following these simple instructions.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`MANAGE MARKETS` -> :guilabel:`Your Markets` and click on the :guilabel:`Create new Market` button to start the market creation process.
      #. Enter a title, a short description, and an image representing your market, and then choose the region it targets (can be worldwide). 
      #. Select the :guilabel:`Community Market` or :guilabel:`Storefront` option depending on your permission preferences.
      #. Click on :guilabel:`Confirm & Create Market` to review the information about your market.

    Your market is now created. You can promote it to the Market Browser to enable public access or keep its Access Key private. In the latter case, only those in possession of the market’s Access Key will have access to it or even know the market exists in the first place. Its content will be encrypted and indecipherable to everyone else. 

    .. attention::

       Anyone in possession of the Access Key of your market will be able to join and sell. If you've created a storefront instead, they will require an additional publish key to sell, which you may or may not want to share with others.

    **Publish Listings**

    To publish listings to your new community market, go through the normal :doc:`product listing process <../guides/guide_mp_vendor_understanding_sellflow>` and choose your community market when ready to publish your item(s). 

.. container:: toggle

    .. container:: header

        **Promote a Market**

    By default, a community market isn’t publicly visible and is only known to its creator and those in possession of its Access Key. However, a market can be published publicly within Particl Desktop’s :term:`Market Browser`.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`MANAGE MARKETS` -> :guilabel:`Your Markets`.
      #. Click on the tile of the market you want to promote and open the market promotion window by clicking on the :guilabel:`Promote in Market Browser` icon at the bottom of the expanded tile.
      #. Select the number of days you want to promote your market on the :term:`Market Browser` and confirm with a click on :guilabel:`Promote Market`.

.. container:: toggle

    .. container:: header

        **Browse Markets**

    You can browse through all the markets promoted by the community and join those that interest you by navigating the :term:`Market Browser`.

    .. rst-class:: bignums

      #.  Open :guilabel:`Market` -> :guilabel:`MANAGE MARKETS` -> :guilabel:`Browser`.
      #. Browse the publicly listed markets and find one that interests you.
      #. Click on its tile to expand its options, and click on :guilabel:`Join this Market` to connect to it.

    .. hint::

     #. Open :guilabel:`Market` -> :guilabel:`MANAGE MARKETS` -> :guilabel:`Your Markets` to see all the markets you have joined.
     #. You can browse the market's listings by going to :guilabel:`Market` -> :guilabel:`BROWSE` and selecting the community market in the :guilabel:`FILTER` section.

.. container:: toggle

    .. container:: header

        **Manually Join a Market**

    If you are in possession of the Market ID and Access/Publish keys of a particular market, you can directly join it even if it's not promoted in the Market Browser. If you only possess the Access Key of a storefront, you will only be able to buy items. If you also possess its Publish Key, then you'll be able to sell items as well. 

    .. rst-class:: bignums

      #. First, make sure you possess the Market ID and Access Key of the market/storefront you want to join. You may need to collect this information from private sources if its creator or users do not publicly broadcast them.
      #. Open :guilabel:`Market` -> :guilabel:`MANAGE MARKETS` -> :guilabel:`Browser` and click on the :guilabel:`Join via Market ID` button to expand the window to join a new market.
      #. Fill in the community market's information. You can decide to enter the information that feels the most helpful and relevant to you.
      #. Enter the community market's Market ID and Access/Publish Key, and then click on the :guilabel:`Join this Market` button to join the community market.

    .. hint::

     #. Open :guilabel:`Market` -> :guilabel:`MANAGE MARKETS` -> :guilabel:`Your Markets` to see all the markets you have joined.
     #. You can browse the market's listings by :guilabel:`Market` -> :guilabel:`BROWSE` and select the community market in the :guilabel:`FILTER` section.

.. container:: toggle

    .. container:: header

        **Flag Markets**

    Just like with undesirable listings, you can flag an entire market if you see  content that you deem appropriate. If enough people downvote the market with you, it will be filtered off by Particl Marketplace’s moderation system. To learn more about the :term:`Particl Marketplace` moderation mechanism, read :doc:`Market Moderation Explained <../in-depth/indepth_mp_moderation>`.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`MANAGE MARKETS` -> :guilabel:`Your Markets`.
      #. Click on the tile of the community market you want to flag to expand its options.
      #. Click on :guilabel:`Report Inappropriate Market` to open the Flagging window and click on the :guilabel:`Flag this market` button to flag it.

    .. hint::

      The total number of coins you hold in your :guilabel:`Public` balance will now be used as downvotes for this community market. If the market's moderation score goes below the remove threshold of |Threshold|, it will be taken off the :term:`Particl Network`.

.. container:: toggle

    .. container:: header

        **Vote to Keep a Market**

    Sometimes, other users may flag markets that you believe should remain on Particl. In those cases, you need to make your voice heard by upvoting the market, essentially countering the downvotes. To learn more about the :term:`Particl Marketplace` moderation mechanism, read :doc:`Market Moderation Explained <../in-depth/indepth_mp_moderation>`.

    .. rst-class:: bignums

      #. Open :guilabel:`Market` -> :guilabel:`MANAGE MARKETS` -> :guilabel:`Your Markets`.
      #. Click on the tile of the flagged market you believe should remain on Particl. Flagged markets will have their flag icon highlighted in red instead of black.
      #. In the window that appears, click on the :guilabel:`Keep Market` green button to confirm that you believe this market shouldn't be moderated out.

    .. hint::

      The number of coins you hold in your :guilabel:`Public` balance will now be used as upvotes for this community market. As long as the market's overall moderation score doesn't go below the removal threshold of |Threshold|, the market will remain on the :term:`Particl Network`.

----

.. seealso::

 - Marketplace Guides - :doc:`Sell Stuff <../marketplace-guides/marketguides_sell>`
 - Marketplace Guides - :doc:`Buy Stuff <../marketplace-guides/marketguides_buy>`
 - Marketplace Explained - :doc:`Markets and Storefronts <../particl-marketplace/marketplace_markets>`
 - Marketplace Explained - :doc:`Content Moderation <../particl-marketplace/marketplace_moderation>`
 - Marketplace Explained - :doc:`Two Party Escrow System <../particl-marketplace/marketplace_escrow>`