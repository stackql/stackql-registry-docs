---
title: details
hide_title: false
hide_table_of_contents: false
keywords:
  - details
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
<tr><td><b>Name</b></td><td><code>details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `detailType` | `string` | The type of detail that the detail IDs represent. |
| `filteredBidDetailRows` | `array` | List of rows, with counts of bids with a given creative status aggregated by detail. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListCreativeStatusBreakdownByDetailRequest.pageToken field in the subsequent call to the filteredBids.details.list method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `bidders_accounts_filterSets_filteredBids_details_list` | `SELECT` | `accountsId, biddersId, creativeStatusId, filterSetsId` |
| `bidders_filterSets_filteredBids_details_list` | `SELECT` | `biddersId, creativeStatusId, filterSetsId` |
