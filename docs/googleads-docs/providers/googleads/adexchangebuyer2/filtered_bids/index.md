---
title: filtered_bids
hide_title: false
hide_table_of_contents: false
keywords:
  - filtered_bids
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
<tr><td><b>Name</b></td><td><code>filtered_bids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.filtered_bids</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `creativeStatusRows` | `array` | List of rows, with counts of filtered bids aggregated by filtering reason (for example, creative status). |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListFilteredBidsRequest.pageToken field in the subsequent call to the filteredBids.list method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `bidders_accounts_filterSets_filteredBids_list` | `SELECT` | `accountsId, biddersId, filterSetsId` |
| `bidders_filterSets_filteredBids_list` | `SELECT` | `biddersId, filterSetsId` |
