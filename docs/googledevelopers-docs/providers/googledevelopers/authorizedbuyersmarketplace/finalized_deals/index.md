---
title: finalized_deals
hide_title: false
hide_table_of_contents: false
keywords:
  - finalized_deals
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
<tr><td><b>Name</b></td><td><code>finalized_deals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.authorizedbuyersmarketplace.finalized_deals</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the finalized deal. Format: `buyers/&#123;accountId&#125;/finalizeddeals/&#123;finalizedDealId&#125;` |
| `dealPausingInfo` | `object` | Information related to deal pausing. |
| `dealServingStatus` | `string` | Serving status of the deal. |
| `readyToServe` | `boolean` | Whether the Programmatic Guaranteed deal is ready for serving. |
| `rtbMetrics` | `object` | Real-time bidding metrics. For what each metric means refer to [Report metrics](https://support.google.com/adxbuyer/answer/6115195#report-metrics) |
| `deal` | `object` | A deal represents a segment of inventory for displaying ads that contains the terms and targeting information that is used for serving as well as the deal stats and status. Note: A proposal may contain multiple deals. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bidders_finalizedDeals_list` | `SELECT` | `biddersId` | Lists finalized deals. Use the URL path "/v1/buyers/&#123;accountId&#125;/finalizedDeals" to list finalized deals for the current buyer and its clients. Bidders can use the URL path "/v1/bidders/&#123;accountId&#125;/finalizedDeals" to list finalized deals for the bidder, its buyers and all their clients. |
| `buyers_finalizedDeals_get` | `SELECT` | `buyersId, finalizedDealsId` | Gets a finalized deal given its name. |
| `buyers_finalizedDeals_list` | `SELECT` | `buyersId` | Lists finalized deals. Use the URL path "/v1/buyers/&#123;accountId&#125;/finalizedDeals" to list finalized deals for the current buyer and its clients. Bidders can use the URL path "/v1/bidders/&#123;accountId&#125;/finalizedDeals" to list finalized deals for the bidder, its buyers and all their clients. |
| `buyers_finalizedDeals_pause` | `EXEC` | `buyersId, finalizedDealsId` | Pauses serving of the given finalized deal. This call only pauses the serving status, and does not affect other fields of the finalized deal. Calling this method for an already paused deal has no effect. This method only applies to programmatic guaranteed deals. |
| `buyers_finalizedDeals_resume` | `EXEC` | `buyersId, finalizedDealsId` | Resumes serving of the given finalized deal. Calling this method for an running deal has no effect. If a deal is initially paused by the seller, calling this method will not resume serving of the deal until the seller also resumes the deal. This method only applies to programmatic guaranteed deals. |
| `buyers_finalizedDeals_setReadyToServe` | `EXEC` | `buyersId, finalizedDealsId` | Sets the given finalized deal as ready to serve. By default, deals are set as ready to serve as soon as they're finalized. If you want to opt out of the default behavior, and manually indicate that deals are ready to serve, ask your Technical Account Manager to add you to the allowlist. If you choose to use this method, finalized deals belonging to the bidder and its child seats don't start serving until after you call `setReadyToServe`, and after the deals become active. For example, you can use this method to delay receiving bid requests until your creative is ready. This method only applies to programmatic guaranteed deals. |
