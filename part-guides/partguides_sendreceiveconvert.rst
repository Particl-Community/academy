==========================
Send, Receive, and Convert
==========================

.. title::
   Send and Receive PART

.. meta::
   :description lang=en: Learn how to send, receive, and convert the PART privacy coin.

Although sending and receiving PART is a straightforward process, Particl’s native privacy coin also offers a variety of different options from which you can choose from. This guide will teach you everything you need to know about them and walk you through all the steps. 

----

.. contents:: Table of Contents
   :local:
   :backlinks: none
   :depth: 2

----

Send PART
---------

You can send PART to anyone without restrictions using any of the available wallets. Depending on the context, you may want to send funds with a varying level of privacy, which PART easily allows you to do.

Public Transactions
*******************

You can send PART using public transactions. This makes the transaction entirely public by permanently inscribing the information of both participants, as well as the transacted amounts, on the blockchain. Public transactions are pseudonymous, akin to regular Bitcoin transactions. 

.. tabs::
     .. group-tab:: Particl Desktop

       - Open Particl Desktop and navigate to the :guilabel:`Wallet` section.
       - Make sure that you have coins in your public balance.    
       - Click on the :guilabel:`SEND / CONVERT` button to open the :guilabel:`Send` page.
       - Select your public balance and enter the information of the intended recipient of the payment.
       - (Optional) Select the outputs you want to use for that transaction by clicking on the :guilabel:`Coin control` button. 
       - Enter the amount you wish to send, and click on the :guilabel:`Make payment` button.
       - Verify the payment information in the confirmation pop-up window that appears, and click on the :guilabel:`Confirm & Send` button to send the payment. 

     .. group-tab:: Particl Qt

       - Open Particl Qt.
       - Make sure that you have coins in your public balance.
       - Click on the :guilabel:`Send` tab.
       - Enter the information of the intended recipient of the payment as well as the amount you wish to send.
       - Make sure that the two dropdown menus (just above where the fee estimate is displayed) are set as :guilabel:`“PART”` and :guilabel:`“PART”`.
       - (Optional) Select the outputs you want to use for that transaction with Coin Control by clicking on the :guilabel:`Inputs…` button. 
       - Click on the :guilabel:`Send` button to prepare your transaction.
       - Verify the payment information in the confirmation pop-up window that appears, and click on the :guilabel:`Sign & Send` button to send the payment. 

     .. group-tab:: Particl Electrum

       - Open a wallet on Particl Electrum.
       - Make sure that you have coins in your public balance
       - Click on the :guilabel:`Send` tab.
       - Enter the information of the intended recipient of the payment as well as the amount you wish to send.
       - Verify the payment information in the confirmation pop-up window that appears, and click on the :guilabel:`Send` button to send the payment. 

----

Blind Transactions
******************

.. tabs::
     .. group-tab:: Particl Desktop

       - Open Particl Desktop and navigate to the :guilabel:`Wallet` section.
       - Make sure that you have coins in your blind balance.
       - Click on the :guilabel:`SEND / CONVERT` button to open the :guilabel:`Send` page.
       - Select your blind balance and enter the information of the intended recipient of the payment.
       - (Optional) Select the outputs you want to use for that transaction by clicking on the :guilabel:`Coin control` button.
       - Enter the amount you wish to send, and click on the :guilabel:`Make payment` button.
       - Verify the payment information in the confirmation pop-up window that appears, and click on the Confirm & Send button to send the payment. 

     .. group-tab:: Particl Qt

       - Open Particl Qt.
       - Make sure that you have coins in your blind balance.
       - Click on the :guilabel:`Send` tab.
       - Enter the information of the intended recipient of the payment as well as the amount you wish to send.
       - Make sure that the first of the two dropdown menus just above where the fee estimate is displayed is set as :guilabel:`“Blind”`. This indicates that you wish to send coins from your blind balance.
       - Select what type of balance you want to send your payment to by selecting it in the second dropdown menu. If, for example, you select :guilabel:`Anon`, your blind transaction will be sent to an anon balance.
       - (Optional) Select the outputs you want to use for that transaction with Coin Control by clicking on the :guilabel:`Inputs…` button. 
       - Click on the :guilabel:`Send` button to prepare your transaction.
       - Verify the payment information in the confirmation pop-up window. that appears, and click on the :guilabel:`Sign & Send` button to send the payment. 

----

Anonymous Transactions
**********************

.. tabs::
     .. group-tab:: Particl Desktop

       - Open Particl Desktop and navigate to the :guilabel:`Wallet` section.
       - Make sure that you have coins in your anon balance.
       - Click on the :guilabel:`SEND / CONVERT` button to open the :guilabel:`Send` page.
       - Select your anon balance and enter the information of the intended recipient of the payment.
       - (Optional) Select the outputs you want to use for that transaction by clicking on the :guilabel:`Coin control` button. 
       - (Optional) Select the desired level of transactional privacy by clicking on the :guilabel:`Advanced options` button. Move the slider according to your preferences.
       - Enter the amount you wish to send, and click on the :guilabel:`Make payment` button.
       - Verify the payment information in the confirmation pop-up window that appears, and click on the :guilabel:`Confirm & Send` button to send the payment. 

     .. group-tab:: Particl Qt

       - Open Particl Qt
       - Make sure that you have coins in your anon balance.
       - Click on the :guilabel:`Send` tab.
       - Enter the information of the intended recipient of the payment as well as the amount you wish to send.
       - Make sure that the first of the two dropdown menus (just above where the fee estimate is displayed) is set as :guilabel:`“Anon”`. This indicates that you wish to send coins from your anon balance.
       - Select what type of balance you want to send your payment to by selecting it in the second dropdown menu. If, for example, you select :guilabel:`Blind`, your anon transaction will be sent to a blind balance.
       - (Optional) Select the outputs you want to use for that transaction with Coin Control by clicking on the :guilabel:`Inputs…` button. 
       - (Optional) Select the desired level of transactional privacy by clicking on the Advanced options button.
       - Click on the :guilabel:`Send` button to prepare your transaction.
       - Verify the payment information in the confirmation pop-up window that appears, and click on the :guilabel:`Sign & Send` button to send the payment.  

----

Receive Coins
-------------

.. tabs::
     .. group-tab:: Particl Desktop

       - Open Particl Desktop and navigate to the :guilabel:`Wallet` section.
       - Click on the :guilabel:`RECEIVE` button to open the :guilabel:`Receive` page.
       - If you are receiving a blind or anon transaction, click on the :guilabel:`Private address` tab. If you are receiving a public transaction, click on the :guilabel:`Public address` tab.
       - (Optional) Generate a new deposit address by clicking on the :guilabel:`New public/private address` button.
       - Copy the displayed deposit address by clicking on the :guilabel:`Copy address` button.
       - Send the copied address to the entity sending you the payment.


     .. group-tab:: Particl Qt

       - Open Particl Qt.
       - Click on the :guilabel:`Receive` tab.
       - Select the type of deposit address you want to create. Choose :guilabel:`Standard` if receiving a public transaction or :guilabel:`Stealth` if receiving a blind or anon transaction.
       - Generate the desired type of deposit address by clicking on the :guilabel:`Create new receiving address` button.
       - Copy the displayed deposit address by clicking on the :guilabel:`Copy Address` button.
       - Send the copied address to the entity sending you the payment.

     .. group-tab:: Particl Electrum

       - Open a wallet on Particl Electrum.
       - Click on the :guilabel:`Receive` tab.
       - Generate a deposit address by clicking on the :guilabel:`New Address` button.
       - Copy the address in your clipboard and send it to the entity sending you the payment.

----

Convert Balances
----------------

You can also move your coins between the three different types of balance available. Refer to the :doc:`Privacy Guide <../in-depth/indepth_part_coin>` for more details on transaction types and balances.

.. tabs::
     .. group-tab:: Particl Desktop

       - Open Particl Desktop and navigate to the :guilabel:`Wallet` section.
       - Click on the :guilabel:`SEND / CONVERT` button to open the Send page.
       - Click on the :guilabel:`Convert Public / Private` tab.
       - Select the type of balance you're sending your coins from on the left and the type of balance you’re sending them to on the right.
       - (Optional) Select the outputs you wish to use by clicking on :guilabel:`Coin control` and the desired level of privacy (if sending from an anon balance) by clicking on :guilabel:`Advanced options`.
       - Enter the amount you wish to send, and click on the :guilabel:`Make payment` button.
       - Verify the balance transfer information in the confirmation pop-up window that appears, and click on the Confirm & Send button to send the payment. 


     .. group-tab:: Particl Qt

       - Open Particl Qt.
       - Click on the :guilabel:`Receive` tab.
       - Select the type of deposit address matching the balance you want to convert your coins into. Choose :guilabel:`Standard` if you want to send coins to your public balance or :guilabel:`Stealth` if you want to send it to either your blind or anon balance.
       - Generate the desired type of deposit address by clicking on the :guilabel:`Create new receiving address:guilabel:` button.
       - Copy the displayed deposit address by clicking on the :guilabel:`Copy Address:guilabel:` button.
       - Click on the :guilabel:`Send` tab.
       - Enter the number of coins you want to transfer into another balance and paste the address you’ve just copied in the :guilabel:`Pay To` text field.
       - Make sure that the first of the two dropdown menus (just above where the fee estimate is displayed) is set as the balance type you want to send your coins from. Set the second dropdown menu to the type of balance you want to send your coins into. For example, if you want to send coins from your public balance into your blind balance, the first menu would be set as :guilabel:`Part` and the second as :guilabel:`Blind`.      
       - Click on the :guilabel:`Send` button to prepare your transaction.
       - Verify the balance transfer information in the confirmation pop-up window that appears, and click on the :guilabel:`Sign & Send` button to send the payment. 

        
.. tip::

    #. You must wait for twelve (12) confirmations (approximately 24 minutes) before funds transferred in and out of an anon balance can be moved again.
    #. You can track the status of transactions on the :guilabel:`Overview` page under :guilabel:`Recent Transactions`.

----

.. seealso::

 * Particl Explained - :doc:`Privacy Specifications <../particl-blockchain/blockchain_privacy>`
 * PART Guides - :doc:`Particl Desktop Wallet <../part-guides/partguides_desktop>`
 * PART Guides - :doc:`How to Stake <../part-guides/partguides_sendreceiveconvert>`
 * PART Guides - :doc:`Buy and Sell PART <../particl-blockchain/blockchain_buysell>`