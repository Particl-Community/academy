Vendor Questions
====================================

.. note::

   The content contained in this page is constantly updated to match the latest features and functions of the Particl Marketplace (version 2.4.0).

.. contents:: Table of contents
   :local:
   :backlinks: none
   :depth: 1

   
What are PART balances (public, blind, anon) and how to manage/convert them?
---------------------------

Balance types are an important concept to understand to properly use Particl. Each balance type has its own level of transactional privacy and serves a different function within the Particl platform.

- **Public**
	- **What is it?** Public balances are the default balance type used by exchanges and other third-party services. It is also the only balance type that allows staking (earning a passive income on your funds through Proof-of-Stake) 
	- **What's its level of privacy?** When sending coins from a public balance, the transaction's data (the sender, receiver, and number of coins transfered) is publicly auditable on any Particl blockchain explorer, just like a Bitcoin transaction. It is the balance type with the lowest level of privacy.
	- **What is it used for?**
		- Receiving and sending public PART transactions .
		- Staking PART coins (earn a passive income on your funds through Proof-of-Stake).
		- Paying for listing fees.
		- Flagging inappropriate listings (one(1) coin equals one (1) vote).
		- Casting votes using Particl Desktop's prososal system ("PROPOSALS").
- **Blind (Private)**
	- **What is it** Blind balances are private balances that can interact with decentralized applications such as Particl's marketplace. Because they have "programmable outputs", they can be used by smart-contract to make decentralized applications more private than with public balances. They also enable anon balances, which do not have programmable outputs, to be used in decentralized applications by linking their outputs to blind balances. 
	- **What's its level of privacy?** When sending coins from a blind balance, the number of coins sent is anonymized on any Particl blockchain explorer. Only the sender and receiver's PART addresses are made publicly available. This type of balance uses the Confidential Transactions privacy protocol.
	- **What is it used for?**
		- Receiving and sending transactions without publicly disclosing the number of coins sent between two parties.
		- Using decentralized applications and smart-contracts without publicly disclosing the number of coins transacted.
		- Enabling anon balances to be used by decentralized applications and smart-contracts so that they can benefit from the highest level of privacy possible.
- **Anon (Private)**
	- **What is it** Anon balances are the most private type of balances on Particl and are used by those looking for the ultimate privacy package.
	- **What's its level of privacy?** When sending coins from an anon balance, both the number of coins sent and the transaction's participants (sender, receiver) are anonymized on any Particl blockchain explorer. An anon transaction is an entirely anonymous cryptocurrency transaction. This type of balance uses the RingCT + Bulletproofs privacy protocol.
	- **What is it used for?** 
		- Receiving and sending entirely anonymous transactions where both the number of coins sent and the transaction's participants are kept hidden.
		- Paying for products and services on Particl's marketplace.
		- Escrowing transactions anonymously.

**You can easily send coins to and from different balance types to use the various functionalities of Particl Desktop. To do so, simply follow these steps:**

#. Navigate to the send and convert page ("SEND / CONVERT") of the wallet menu on the left of your Particl Desktop client.
#. Click on the convert tab ("Convert Public <-> Private").
#. In the "PAY FROM" section on the left of the page, select the type of balance you want to send coins from.
#. In the "CONVERT TO" section on the right of the page, select the type of balance you want to send coins to. 
	- For example, if you wanted to convert coins from a public balance to an anon balance, you would select Public on the left and Anon on the right. 
#. Enter the amount of coins you want to convert. 
#. Click on the "Make payment" button and unlock your wallet when prompted to.
#. Review the transaction details and click on the "Confirm & Send" button to execute the transaction.
#. Wait at least one (1) confirmation (approximately 2 minutes) for the converted coins to be available unless you have converted them into an anon balance, which will need twelve (12) confirmations (approximately 24 minutes) before becoming available again.

How do I put an item for sale?
---------------------------

.. note::

   To put an item for sale, you need to have PART coins in your public balance to pay for the listing fees.

#. Navigate to the sell page ("SELL") of the market menu on the left of your Particl Desktop client.
#. Click on the listings tab ("Listings"), and then on the "Add new listing" button.
#. Fill up all the text boxes with the information on your listing and upload a (or multiple) pictures of your product or service.
#. Review all of the information and when ready to publish your listing, click on the "Save and Publish" button. 
	- Alternatively, you can click on the "Save" button to save your listing information and publish it later.
	- To publish your listing later, you will have to navigate to the listing tab of the sell page.
	- Locate your saved listing (it will be marked as "UNPUBLISHED").
	- Click on its tile, and either edit it by clicking on the "Edit listing" button, or publish it by clicking the "Publish" button.
	- You can also delete the template if you do not have any use for it anymore by clicking on the red X icon ("Delete listing").
#. Unlock your wallet when prompted to.
#. Set the expiry time (the number of days your listings will be available) in the dropdown menu and click on "Confirm & Publish".
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listing will be live on the Particl marketplace.

How to add multiple listings at the same time?
---------------------------

.. note::

   Adding multiple listings at once requires that you set up a .csv file compatible with the Particl marketplace. You can download a .csv template directly from Particl Desktop by following the steps below.

.. note::

   To put an item for sale, you need to have PART coins in your public balance to pay for the listing fees.

#. Navigate to the sell page ("SELL") of the market menu on the left of your Particl Desktop client.
#. Click on the listings tab ("Listings"), and then on the "Import listings" button.
#. In the "SELECT IMPORT SOURCE" section, select CSV file. 
	- If you don't already have a .csv file with your listings, download the template by clicking on the "Download example CSV" hyperlink located in the "IMPORT SETTINGS" section.
	- Save the file on your computer.
	- Open it with a spreadsheet editor (i.e. Excel, LibreOffice, etc).
	- Add as many listings as you want with all of the information required
#. Click on the "CSV file to import" line.
#. Browse your computer files and choose the .csv file that contains the listings you want to list on Particl.
#. Click on the "Load" button to upload the file. Wait for Particl Desktop to load your listings.
#. Review your import data and edit any listing, as needed, by clicking on its tile and then by clicking on the "Edit listing" button.
	- If there is an error in your .csv file or if there is missing information, the client will let you know about it and allow you to edit listings manually.
	- You can also opt to not publish certain listings by unchecking their "Publish" checkboxes.
#. When you have reviewed your listings and are satisfied with the information provided, click on the "Continue" button.
#. Set your shipping and expiration parameters. 
	- The shipping location is important so that the client can pick the correct shipping fees to charge your customers.
	- The expiry time will determine how long your listings will stay on the marketplace and how much you are going to pay in listing fees.
#. When you have put all the information, click on the "Continue" button and let the client estimate the total listing fees.
#. Review the quoted fees and click on the "Publish imported listings" button. Careful, this is the final step, and you will be charged listing fees when clicking on that button.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listings will be live on the Particl marketplace.
	- For large amount of listings, the network may require more than one (1) confirmation so that all of your listings are published. You can check the "OVERVIEW" or "HISTORY" pages in the market menu on the left of your Particl Desktop client to track the publishing status.

How to add listings from a .csv file?
---------------------------

.. note::

   Adding multiple listings at once requires that you set up a .csv file compatible with the Particl marketplace. You can download a .csv template directly from Particl Desktop by following the steps below.

.. note::

   To put an item for sale, you need to have PART coins in your public balance to pay for the listing fees.

#. Navigate to the sell page ("SELL") of the market menu on the left of your Particl Desktop client.
#. Click on the listings tab ("Listings"), and then on the "Import listings" button.
#. In the "SELECT IMPORT SOURCE" section, select CSV file. 
	- If you don't already have a .csv file with your listings, download the template by clicking on the "Download example CSV" hyperlink located in the "IMPORT SETTINGS" section.
	- Save the file on your computer.
	- Open it with a spreadsheet editor (i.e. Excel, LibreOffice, etc).
	- Add as many listings as you want with all of the information required
#. Click on the "CSV file to import" line.
#. Browse your computer files and choose the .csv file that contains the listings you want to list on Particl.
#. Click on the "Load" button to upload the file. Wait for Particl Desktop to load your listings.
#. Review your import data and edit any listing, as needed, by clicking on its tile and then by clicking on the "Edit listing" button.
	- If there is an error in your .csv file or if there is missing information, the client will let you know about it and allow you to edit listings manually.
	- You can also opt to not publish certain listings by unchecking their "Publish" checkboxes.
#. When you have reviewed your listings and are satisfied with the information provided, click on the "Continue" button.
#. Set your shipping and expiration parameters. 
	- The shipping location is important so that the client can pick the correct shipping fees to charge your customers.
	- The expiry time will determine how long your listings will stay on the marketplace and how much you are going to pay in listing fees.
#. When you have put all the information, click on the "Continue" button and let the client estimate the total listing fees.
#. Unlock your wallet when prompted to. Make sure to unlock it for long enough for the full listing fee estimation to complete.
#. Review the quoted fees and click on the "Publish imported listings" button. Careful, this is the final step, and you will be charged listing fees when clicking on that button.
#. Unlock your wallet when prompted to. Make sure to unlock it for long enough so that the full publishing process can be completed.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listings will be live on the Particl marketplace.
	- For large amount of listings, the network may require more than one (1) confirmation so that all of your listings are published. You can check the "OVERVIEW" or "HISTORY" pages in the market menu on the left of your Particl Desktop client to track the publishing status.

How to import listings from your WooCommerce?
---------------------------

.. note::

   To put an item for sale, you need to have PART coins in your public balance to pay for the listing fees.

#. Export your WooCommerce products into a .csv file by following **[WooCommerce's own documentation](https://docs.woocommerce.com/document/product-csv-importer-exporter/)**.
#. Navigate to the sell page ("SELL") of the market menu on the left of your Particl Desktop client.
#. Click on the listings tab ("Listings"), and then on the "Import listings" button.
#. In the "SELECT IMPORT SOURCE" section, select WooCommerce. 
#. Click on the "Woocommerce export file" line.
#. Browse your computer files and choose the WooCommerce export file that contains the listings you want to list on Particl.
#. On the "Fiat per PART rate", enter the value of 1 PART that you want to sell your products.
	- This step is required to convert the quoted prices of your WooCommerce products into PART prices.
	- Calculate the fiat valuation of PART based on the same national currency (USD, EUR, CAD, etc) used on your WooCommerce export file.
	- Until automatic fiat rates are supported on Particl Desktop, you'll need to set a conversion rate manually. If you're selling for USD on your shop and the USD/PART price is $5, enter "5". Keep in mind that the price of your products won't reflect future PART price changes.
#. Click on the "Load" button to upload the file. Wait for Particl Desktop to load your listings.
#. Review your import data and edit any listing, as needed, by clicking on its tile and then by clicking on the "Edit listing" button.
	- If there is an error in your .csv file or if there is missing information, the client will let you know about it and allow you to edit listings manually.
	- You can also opt to not publish certain listings by unchecking their "Publish" checkboxes.
#. When you have reviewed your listings and are satisfied with the information provided, click on the "Continue" button.
#. Set your shipping and expiration parameters. 
	- The shipping location is important so that the client can pick the correct shipping fees to charge your customers. 
	- The expiry time will determine how long your listings will stay on the marketplace and how much you are going to pay in listing fees.
#. When you have put all the information, click on the "Continue" button and let the client estimate the total listing fees.
#. Unlock your wallet when prompted to. Make sure to unlock it for long enough for the full listing fee estimation to complete.
#. Review the quoted fees and click on the "Publish imported listings" button. Careful, this is the final step, and you will be charged listing fees when clicking on that button.
#. Unlock your wallet when prompted to. Make sure to unlock it for long enough so that the full publishing process can be completed.
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listings will be live on the Particl marketplace.
	- For large amount of listings, the network may require more than one (1) confirmation so that all of your listings are published. You can check the "OVERVIEW" or "HISTORY" pages of the market menu on the left of your Particl Desktop client to track the publishing status.


Why am I not receiving any order? 
---------------------------

If you have encrypted your Particl Desktop client, **you need to unlock it with your password** so that it can pick up new orders from the Particl network. If you keep your client locked at all time, then it won't be able to receive any order. 

The reason for this is that, due to the private-by-default and decentralized nature of the Particl marketplace, your client cannot tell if an order is addressed to you or to another seller. The only way for it to pick up your orders is by attempting to decrypt the entirety of the orders broadcast on the network by buyers using your client’s password. If an order cannot be decrypted, it means it is not addressed to you. If it can be, then that means that’s an order for one of your listings.

How can I edit or delete a listing after it has been published?
---------------------------

Due to the current stage of development of the Particl marketplace (Beta), it is currently not possible. Listings on Particl are broadcast using P2P messages relayed by other peers on the Particl network. Once a message is broadcast, it cannot be modified due to the decentralized nature of the network and to maintain the network's integrity. It is the same reason why you cannot modify past Bitcoin transactions. While there are workarounds to circumvent the issue of editing or deleting already published listings, they haven't yet been integrated into the marketplace. This functionality will be added at a later stage during the Beta phase of development. To know what next features are planned for the marketplace, refer to **[Particl's development roadmap](https://particl.io/roadmap)**.

However, take note that every listings require you to enter an expiry date during the publishing process. Once this expiry date has passed, the listing is removed from the marketplace and won't be visible to buyers anymore. A listing can then be modified before re-uploading.

How can I manage quantities for my products?

---------------------------
Due to the current stage of development of the Particl marketplace (Beta), it is currently not possible. This is, however, one of the next functionality that is going to be added to the marketplace. The feature, called Inventory Management, will allow you to manage quantities for your products as well as various other attributes such as sizes, colors, fabrics, and etc. To know what next features are planned for the marketplace, refer to **[Particl's development roadmap](https://particl.io/roadmap)**.

How to list an item with multiple sizes, colors, and other attributes?
---------------------------

Due to the current stage of development of the Particl marketplace (Beta), it is currently not possible. This is, however, one of the next functionality that is going to be added to the marketplace. The feature, called Inventory Management, will allow you to manage quantities for your products as well as various other attributes such as sizes, colors, fabrics, and etc. To know what next features are planned for the marketplace, refer to **[Particl's development roadmap](https://particl.io/roadmap)**.

How long do listings stay on the marketplace? 
---------------------------

The expiry time for listings on the Particl marketplace depends on the listing fee you pay when publishing your listings. When publishing one or multiple listings, the Particl Desktop client will prompt you to select the number of days you want your listings to stay live. Simply choose the number of days from the dropdown menu.

How do I re-publish a listing?
---------------------------

Due to the current stage of development of the Particl marketplace (Beta), listings cannot be automatically re-published. To publish a listing once again, you need to clone it first, then publish the clone. To do so, follow these steps.

#. Navigate to the sell page ("SELL") in the market menu on the left of your Particl Desktop client.
#. Click on the listings tab ("Listings") to see all previously published listings.
#. Find the listing you want to re-publish in the list of previously published listings. It should be marked as "EXPIRED".
#. Click its tile to expand it, and click the "Clone listing" icon to clone it. This will bring you to its publishing page. 
#. Update its information and price, if needed, and click on the "Save & Publish" button.
#. Unlock your wallet when prompted to.
#. Set the expiry time (the number of days your listings will be available) in the dropdown menu and click on "Confirm & Publish".
#. Wait until the network goes through one (1) blockchain confirmation (approximately 2 minutes), and then your listing will be live on the Particl marketplace.

What do each order status mean?
---------------------------

- BIDDING: A buyer has made a bid on an item and is now waiting for you to accept the bid.
- PAYMENT: You have accepted a bid on an item and are now waiting for the buyer to confirm payment and lock his/her funds (payment + security deposit) into escrow.
- ESCROW: The buyer has locked his/her funds into escrow and is now waiting for you to lock your security deposit into escrow.
- PACKAGING: The buyer of the item is now waiting for you to package the order and ship it.
- SHIPPING: You have marked the item as shipped and are now waiting for the buyer to confirm the delivery.
- COMPLETE: The item has been confirmed to be received by the buyer. There are no more open actions in this transaction and you've received both the payment for the order and your security deposit back.

How to sell an item on Particl from start to finish?
---------------------------

#. Publish your listing(s).
#. Wait for a customer to place a bid on an item.
#. Once a bid is placed, accept the bid by going to the "Orders" tab of the sell page ("SELL") and by clicking on the "Accept bid" button.
#. Wait for the customer to lock his funds (payment + security deposit) into escrow.
#. Once the customer has locked his funds into escrow, lock your security deposit by going to the "Orders" tab of the sell page ("SELL") and by clicking on the "Complete escrow" button.
#. Package the ordered item and ship it through the post.
#. Once that is done, go to the "Orders" tab of the sell page ("SELL") and click the "Mark as shipped" button.
#. At this stage, you can optionally add a tracking number or note to the customer. Enter the information, if any, and click on the "Order shipper" button.
#. Wait for your customer to confirm he has received the item after which he will confirm the order as completed.
#. Once the order is completed, you will receive your payment as well as your security deposit back. The transaction history will show up in the "OVERVIEW" or "HISTORY" pages of the market menu on the left of your Particl Desktop client to track the publishing status.


How to create your own market?
---------------------------

How to create your own storefront?
---------------------------

How to manage your seller profiles?
---------------------------

How to promote your market or storefront on Particl’s Market Browser?
---------------------------

How to send a tracking number or note to a customer?
---------------------------

Due to the current stage of development of the Particl marketplace (Beta), directly messaging a customer is not yet supported. You can, however, send a tracking number or note to your customer as part of the order processing flow. In fact, once you mark an order as shipped, the Particl Desktop client will prompt you to enter a tracking number or note to your customer before going to the next step. Doing so is entirely optional but helps your customers keep track of their order(s). 

An integrated messaging system will be added at a later time during the Beta phase of development. To know what next features are planned for the marketplace, refer to **[Particl's development roadmap](https://particl.io/roadmap)**.

How to respond to a question, comment, review, or feedback left on one of your listings?
---------------------------

How to manage refunds and returns through the marketplace?
---------------------------

Due to the current stage of development of the Particl marketplace (Beta), this feature is currently not supported. Direct messaging and escrow management/negociations will be added at a later time during the Beta phase of development. To know what next features are planned for the marketplace, refer to **[Particl's development roadmap](https://particl.io/roadmap)**.

Why does my product shows up in "reported listings" and what does this mean?
---------------------------

If one of your listing shows up in the reported listings section, it means at least one user has flagged it as inappropriate. If enough users flag a listing as inappropriate, it will be taken off the marketplace. If your listing shows up in the reported listings section but still shows up on the marketplace, it means that not enough users have flagged the listing.

The Particl marketplace has a self-moderation system where any user can flag products as inappropriate. The system works similarly to the Reddit upvote and downvote system where any user can upvote or downvote a thread or reply. However, Particl's self-moderation mechanism is based on one (1) coin equals one (1) vote instead of Reddit's (1) user equals one (1) vote system. The reason for the difference is that, because of Particl's decentralized nature and focus on user privacy, it is impossible for the network to know if a single user creates multiple accounts and downvotes the same listing until it gets delisted. By instead giving each coin one (1) voting right, it becomes impossible to game the network as you need, in all cases, to get more PART coins to get more voting power. If a user downvotes a listing and then moves his coins to another wallet, the downvote will not be effective and counted anymore. 

To learn more about Particl's self-moderation mechanism, **[read this blog post](https://particl.news/particl-explained-decentralized-marketplace-moderation-7daa3c75d5b2)**.

How to contact and send a message to a customer?
---------------------------

Due to the current stage of development of the Particl marketplace (Beta), directly messaging a customer is not yet supported. You can, however, send a tracking number or note to your customer as part of the order processing flow. In fact, once you mark an order as shipped, the Particl Desktop client will prompt you to enter a tracking number or note to your customer before going to the next step. Doing so is entirely optional but helps your customers keep track of their order(s). 

An integrated messaging system will be added at a later time during the Beta phase of development. To know what next features are planned for the marketplace, refer to **[Particl's development roadmap](https://particl.io/roadmap)**.

How can I get an order/sales/shipment report for tax purposes?
---------------------------

Due to the current stage of development of the Particl marketplace (Beta), an integrated tax reporting system isn't included yet but is planned to be added at a later time during the Beta phase of development. You can, however, manually inspect your transaction history to get the data you need to report your taxes.

#. Navigate to the sell page ("SELL") of the market menu on the left of your Particl Desktop client.
#. Click on the orders tab ("Orders").
	- On that page, you can manually search for a specific order by typing its title in the search bar or filter all of your orders by their statuses.
#. Find the orders you need and click on their tiles to get more details and data.
	- Doing so will show you the customer's address, when the order was created and completed, as well as all price-related information.
	- To calculate the price of an order in your national currency, take note of the number of PART you received as payment as well as the date and time the order was completed. 
	- Go on a website that keeps track of PART's historical price data and get the proper national currency valuation of your payment at the time you received it. CoinMarketCap is a good website where you can find that information, just **[click on this link](https://coinmarketcap.com/currencies/particl/historical-data/)** to be taken directly to the historical data page for the PART coin.

Functionalities that will make tax reporting, order data exporting, and national currency calculations will be added at a later time during the Beta phase of development. To know what next features are planned for the marketplace, refer to **[Particl's development roadmap](https://particl.io/roadmap)**.

How can I get further technical support?
---------------------------

You can find a ton of information by consulting **[this pinned thread](https://www.reddit.com/r/Particl/comments/erews3/useful_links_to_start_with_particl_project_2020/)** on Particl's Reddit page. It contains a wide array of useful links that will most likely answer most of your questions.

Additionally, Particl is an open-source project, meaning you can get a lot of technical support from Particl's own online community. Simply join one of these social platforms and look for their help channels. Don't be shy, there is a whole online community waiting to be help you out!

- **`Discord server <https://discord.me/particl>`_** (more specifically, the **#support** channel)
- **[Telegram group](https://t.me/particlproject)** (more specifically, the **[help channel](https://t.me/particlhelp)**)
- **[Riot server](https://matrix.to/#/+particl:matrix.org)** (more specifically, the **[Particl Help channel](https://riot.im/app/#/room/#particlhelp:matrix.org)**)

Finally, you can get direct support from the Particl team itself by signing up to the Vendor Onboarding Program. This will give you access to VIP vendor-specific channels on Discord and will also give you a direct line of contact with team members who'll be able to assist you with any issue you encounter. 

To learn more about the Vendor Onboarding Program and its benefits, **[follow this link](https://particl.io)**.