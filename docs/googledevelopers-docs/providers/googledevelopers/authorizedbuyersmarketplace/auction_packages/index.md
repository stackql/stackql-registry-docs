---
title: auction_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - auction_packages
  - authorizedbuyersmarketplace
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auction_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.authorizedbuyersmarketplace.auction_packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The unique identifier for the auction package. Format: `buyers/&#123;accountId&#125;/auctionPackages/&#123;auctionPackageId&#125;` The auction_package_id part of name is sent in the BidRequest to all RTB bidders and is returned as deal_id by the bidder in the BidResponse. |
| `description` | `string` | Output only. A description of the auction package. |
| `subscribedClients` | `array` | Output only. The list of clients of the current buyer that are subscribed to the AuctionPackage. Format: `buyers/&#123;buyerAccountId&#125;/clients/&#123;clientAccountId&#125;` |
| `updateTime` | `string` | Output only. Time the auction package was last updated. This value is only increased when this auction package is updated but never when a buyer subscribed. |
| `createTime` | `string` | Output only. Time the auction package was created. |
| `creator` | `string` | Output only. The buyer that created this auction package. Format: `buyers/&#123;buyerAccountId&#125;` |
| `displayName` | `string` | The display_name assigned to the auction package. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `buyers_auctionPackages_get` | `SELECT` | `auctionPackagesId, buyersId` | Gets an auction package given its name. |
| `buyers_auctionPackages_list` | `SELECT` | `buyersId` | List the auction packages subscribed by a buyer and its clients. |
| `buyers_auctionPackages_subscribe` | `EXEC` | `auctionPackagesId, buyersId` | Subscribe to the auction package for the specified buyer. Once subscribed, the bidder will receive a call out for inventory matching the auction package targeting criteria with the auction package deal ID and the specified buyer. |
| `buyers_auctionPackages_subscribeClients` | `EXEC` | `auctionPackagesId, buyersId` | Subscribe the specified clients of the buyer to the auction package. If a client in the list does not belong to the buyer, an error response will be returned, and all of the following clients in the list will not be subscribed. Subscribing an already subscribed client will have no effect. |
| `buyers_auctionPackages_unsubscribe` | `EXEC` | `auctionPackagesId, buyersId` | Unsubscribe from the auction package for the specified buyer. Once unsubscribed, the bidder will no longer receive a call out for the auction package deal ID and the specified buyer. |
| `buyers_auctionPackages_unsubscribeClients` | `EXEC` | `auctionPackagesId, buyersId` | Unsubscribe from the auction package for the specified clients of the buyer. Unsubscribing a client that is not subscribed will have no effect. |
