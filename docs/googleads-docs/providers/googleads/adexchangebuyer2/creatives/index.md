---
title: creatives
hide_title: false
hide_table_of_contents: false
keywords:
  - creatives
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
<tr><td><b>Name</b></td><td><code>creatives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.creatives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `filteredBidCreativeRows` | `array` | List of rows, with counts of bids with a given creative status aggregated by creative. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListCreativeStatusBreakdownByCreativeRequest.pageToken field in the subsequent call to the filteredBids.creatives.list method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_creatives_get` | `SELECT` | `accountId, creativeId` | Gets a creative. |
| `accounts_creatives_list` | `SELECT` | `accountId` | Lists creatives. |
| `bidders_accounts_filterSets_filteredBids_creatives_list` | `SELECT` | `accountsId, biddersId, creativeStatusId, filterSetsId` | List all creatives associated with a specific reason for which bids were filtered, with the number of bids filtered for each creative. |
| `bidders_filterSets_filteredBids_creatives_list` | `SELECT` | `biddersId, creativeStatusId, filterSetsId` | List all creatives associated with a specific reason for which bids were filtered, with the number of bids filtered for each creative. |
| `accounts_creatives_create` | `INSERT` | `accountId` | Creates a creative. |
| `accounts_creatives_stopWatching` | `EXEC` | `accountId, creativeId` | Stops watching a creative. Will stop push notifications being sent to the topics when the creative changes status. |
| `accounts_creatives_update` | `EXEC` | `accountId, creativeId` | Updates a creative. |
| `accounts_creatives_watch` | `EXEC` | `accountId, creativeId` | Watches a creative. Will result in push notifications being sent to the topic when the creative changes status. |
