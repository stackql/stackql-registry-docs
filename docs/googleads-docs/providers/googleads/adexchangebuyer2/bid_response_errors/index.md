---
title: bid_response_errors
hide_title: false
hide_table_of_contents: false
keywords:
  - bid_response_errors
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
<tr><td><b>Name</b></td><td><code>bid_response_errors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.bid_response_errors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `calloutStatusRows` | `array` | List of rows, with counts of bid responses aggregated by callout status. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListBidResponseErrorsRequest.pageToken field in the subsequent call to the bidResponseErrors.list method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `bidders_accounts_filterSets_bidResponseErrors_list` | `SELECT` | `accountsId, biddersId, filterSetsId` |
| `bidders_filterSets_bidResponseErrors_list` | `SELECT` | `biddersId, filterSetsId` |
