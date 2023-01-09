---
title: bid_responses_without_bids
hide_title: false
hide_table_of_contents: false
keywords:
  - bid_responses_without_bids
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
<tr><td><b>Name</b></td><td><code>bid_responses_without_bids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.bid_responses_without_bids</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `bidResponseWithoutBidsStatusRows` | `array` | List of rows, with counts of bid responses without bids aggregated by status. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListBidResponsesWithoutBidsRequest.pageToken field in the subsequent call to the bidResponsesWithoutBids.list method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `bidders_accounts_filterSets_bidResponsesWithoutBids_list` | `SELECT` | `accountsId, biddersId, filterSetsId` |
| `bidders_filterSets_bidResponsesWithoutBids_list` | `SELECT` | `biddersId, filterSetsId` |
