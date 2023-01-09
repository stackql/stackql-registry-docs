---
title: non_billable_winning_bids
hide_title: false
hide_table_of_contents: false
keywords:
  - non_billable_winning_bids
  - adexchangebuyer2
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>non_billable_winning_bids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.non_billable_winning_bids</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListNonBillableWinningBidsRequest.pageToken field in the subsequent call to the nonBillableWinningBids.list method to retrieve the next page of results. |
| `nonBillableWinningBidStatusRows` | `array` | List of rows, with counts of bids not billed aggregated by reason. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `bidders_accounts_filterSets_nonBillableWinningBids_list` | `SELECT` | `accountsId, biddersId, filterSetsId` |
| `bidders_filterSets_nonBillableWinningBids_list` | `SELECT` | `biddersId, filterSetsId` |
