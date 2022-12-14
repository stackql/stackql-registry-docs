---
title: watchlists
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlists
  - security_insights
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchlists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.watchlists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Describes watchlist properties |
| `etag` | `string` | Etag of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Watchlists_Get` | `SELECT` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Gets a watchlist, without its watchlist items. |
| `Watchlists_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all watchlists, without watchlist items. |
| `Watchlists_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with either rawContent or a valid SAR URI and contentType properties. The rawContent is mainly used for small watchlist (content size below 3.8 MB). The SAS URI enables the creation of large watchlist, where the content size can go up to 500 MB. The status of processing such large file can be polled through the URL returned in Azure-AsyncOperation header. |
| `Watchlists_Delete` | `DELETE` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Delete a watchlist. |
